# Generates the archetypes, translations and project archetypes of the PM2 profile.
# Usage: python tools/gen.py [<profile folder>] (default: the folder above tools/),
# with the Python environment of PROTEUS (it needs lxml).
import re, sys, shutil
from pathlib import Path
from lxml import etree

sys.path.insert(0, str(Path(__file__).parent))
from model import *          # noqa: F401,F403
import content

PROFILE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# XML of properties and objects
# ---------------------------------------------------------------------------

def txt(v, lang):
    return v[lang] if isinstance(v, dict) else v

def prop_xml(spec, lang, value=None):
    kind, name, cat, attrs, default = spec
    v = txt(default if value is None else value, lang)
    a = f'name="{name}" category="{cat}"'
    if "tooltip" in attrs: a += f' tooltip="{attrs["tooltip"]}"'
    if kind == "code":
        return (f'<codeProperty {a} inmutable="true"><prefix><![CDATA[{txt(attrs["prefix"], lang)}]]></prefix>'
                f'<number>{v}</number><suffix><![CDATA[]]></suffix></codeProperty>')
    if kind in ("string", "markdown", "url", "file"):
        return f'<{kind}Property {a}><![CDATA[{v}]]></{kind}Property>'
    if kind == "enum":
        return f'<enumProperty {a} choices="{" ".join(ENUMS[attrs["choices"]])}">{v}</enumProperty>'
    if kind in ("date", "boolean", "integer", "float"):
        return f'<{kind}Property {a}>{v}</{kind}Property>'
    if kind == "unit":
        return (f'<unitProperty {a} units="{attrs["units"]}"><value>{v}</value>'
                f'<unit>{attrs["units"].split()[0]}</unit></unitProperty>')
    if kind == "trace":
        a += f' acceptedTargets="{attrs["acceptedTargets"]}" traceType="{attrs["traceType"]}"'
        if "maxTargetsNumber" in attrs: a += f' maxTargetsNumber="{attrs["maxTargetsNumber"]}"'
        if not v: return f'<traceProperty {a}/>'
        traces = "".join(f'\n      <trace target="{t_}" traceType="{attrs["traceType"]}"/>' for t_ in v)
        return f'<traceProperty {a}>{traces}\n    </traceProperty>'
    raise ValueError(kind)

def object_xml(id_, classes, accepted_children, accepted_parents, props, children=()):
    head = f'<object id="{id_}" classes="{classes}" acceptedChildren="{accepted_children}"'
    if accepted_parents: head += f' acceptedParents="{accepted_parents}"'
    body = "".join(f"\n    {p}" for p in props)
    kids = "".join(f'\n    <child id="{c}"/>' for c in children)
    kids_xml = f"<children>{kids}\n  </children>" if children else "<children/>"
    return (f"<?xml version='1.0' encoding='UTF-8'?>\n{head}>\n  <properties>{body}\n  </properties>\n"
            f"  {kids_xml}\n</object>\n")

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")

# ---------------------------------------------------------------------------
# Object archetypes
# ---------------------------------------------------------------------------

def archetype_xml(id_, lang):
    a = ARCHETYPES[id_]
    return object_xml(id_, a["classes"], a["children"], a["parents"],
                      [prop_xml(p, lang) for p in a["props"]])

def place_archetypes(root):
    """Moves the archetypes copied from basic (and the assets their file properties
    point to) to the tab TABS gives them, and removes the generated archetypes and
    the tab folders that are no longer used."""
    existing = {f.stem: f for f in root.glob("*/objects/*.xml")}
    for tab, ids in TABS.items():
        for id_ in ids:
            src, dst = existing.get(id_), root / tab / "objects" / f"{id_}.xml"
            if id_ in ARCHETYPES or src is None or src == dst:
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            for asset in etree.parse(str(src)).getroot().iterfind("properties/fileProperty"):
                f = src.parent.parent / "assets" / (asset.text or "").strip()
                if asset.text and f.is_file():
                    (root / tab / "assets").mkdir(exist_ok=True)
                    shutil.move(str(f), str(root / tab / "assets" / f.name))
            shutil.move(str(src), str(dst))
    listed = {(tab, id_) for tab, ids in TABS.items() for id_ in ids}
    for f in root.glob("*/objects/*.xml"):
        if (f.parent.parent.name, f.stem) not in listed:
            assert f.stem in ARCHETYPES, f"{f} is not in TABS: add it or remove it by hand"
            f.unlink()
    for d in root.iterdir():
        if d.is_dir() and d.name not in TABS:
            (d / "objects.xml").unlink(missing_ok=True)
            for sub in ("objects", "assets"):
                if (d / sub).is_dir(): (d / sub).rmdir()   # fails if not empty: on purpose
            d.rmdir()

def write_archetypes(lang):
    root = PROFILE / "archetypes" / lang / "objects"
    place_archetypes(root)
    for id_, a in ARCHETYPES.items():
        assert id_ in TABS[a["category"]], f"{id_} is not in the tab {a['category']}"
        write(root / a["category"] / "objects" / f"{id_}.xml", archetype_xml(id_, lang))
    for tab, ids in TABS.items():
        for id_ in ids:
            assert (root / tab / "objects" / f"{id_}.xml").is_file(), f"{tab}/{id_} not found"
        lines = "".join(f'\n  <object id="{i}" />' for i in ids)
        write(root / tab / "objects.xml",
              f'<?xml version="1.0" encoding="UTF-8"?>\n<objects>{lines}\n</objects>\n')

# ---------------------------------------------------------------------------
# Instances: copies of an archetype (pm2 or basic) with other values
# ---------------------------------------------------------------------------

def basic_archetype_file(lang, id_):
    for f in (PROFILE / "archetypes" / lang / "objects").glob(f"*/objects/{id_}.xml"):
        return f
    raise FileNotFoundError(id_)

def instance(lang, archetype_id, id_, values=None, children=()):
    """XML of a new object cloned from an archetype file, with some property values."""
    root = etree.parse(str(basic_archetype_file(lang, archetype_id))).getroot()
    root.set("id", id_)
    for name, value in (values or {}).items():
        value = txt(value, lang)
        prop = root.find(f"properties/*[@name='{name}']")
        if prop is None:
            raise KeyError(f"{archetype_id} has no property {name}")
        tag = prop.tag
        if tag == "traceProperty":
            for tr in list(prop): prop.remove(tr)
            for target in value:
                tr = etree.SubElement(prop, "trace", target=target, traceType=prop.get("traceType"))
        elif tag == "codeProperty":
            prop.find("number").text = value
        elif tag == "unitProperty":
            prop.find("value").text = value
        elif tag in ("stringProperty", "markdownProperty", "urlProperty", "fileProperty"):
            prop.text = etree.CDATA(value)
        else:
            prop.text = value
    old = root.find("children")
    if old is not None: root.remove(old)
    kids = etree.SubElement(root, "children")
    for c in children:
        etree.SubElement(kids, "child", id=c)
    etree.indent(root, space="  ")
    xml = etree.tostring(root, encoding="unicode")
    # lxml drops empty CDATA sections, and PROTEUS reads an empty text property as "None"
    xml = re.sub(r'<((?:string|markdown|url|file)Property)([^>]*?)(?:/>|></\1>)',
                 r'<\1\2><![CDATA[]]></\1>', xml)
    return "<?xml version='1.0' encoding='UTF-8'?>\n" + xml + "\n"

class Project:
    def __init__(self, lang, folder, project_id, name_, description):
        self.lang, self.folder, self.objects, self.documents = lang, folder, {}, []
        self.project_id, self.name, self.description = project_id, name_, description

    def add(self, archetype_id, id_, values=None, children=()):
        assert id_ not in self.objects, f"duplicated id {id_} in {self.folder}"
        self.objects[id_] = instance(self.lang, archetype_id, id_, values, children)
        return id_

    def document(self, id_, props, children):
        assert id_ not in self.objects, f"duplicated id {id_} in {self.folder}"
        self.objects[id_] = object_xml(id_, ":Proteus-document", ":Proteus-any", None, props, children)
        self.documents.append(id_)

    def save(self, assets=()):
        lang = self.lang
        d = PROFILE / "archetypes" / lang / "projects" / self.folder
        props = [prop_xml(name(self.name), lang),
                 prop_xml(("string", "version", "general", {}, "1.0"), lang),
                 prop_xml(date(), lang),
                 prop_xml(md("description", self.description), lang),
                 prop_xml(md("comments", "", "comments"), lang)]
        docs = "".join(f'\n    <document id="{x}"/>' for x in self.documents)
        body = "".join(f"\n    {p}" for p in props)
        write(d / "project.xml",
              f"<?xml version='1.0' encoding='UTF-8'?>\n<project id=\"{self.project_id}-{lang[:2]}\">\n"
              f"  <properties>{body}\n  </properties>\n  <documents>{docs}\n  </documents>\n</project>\n")
        for id_, xml in self.objects.items():
            write(d / "objects" / f"{id_}.xml", xml)
        for stale in (d / "objects").glob("*.xml"):     # objects of a previous generation
            if stale.stem not in self.objects:
                stale.unlink()
        write(d / ".gitignore", "state.yaml\nstate.yml\n")
        (d / "assets").mkdir(exist_ok=True)
        for src in assets:
            shutil.copy(src, d / "assets" / Path(src).name)

def document_values(lang, values):
    """Document object properties (document_props spec) with some values replaced."""
    props = []
    for spec in document_props(*values.pop("_args")):
        props.append(prop_xml(spec, lang, values.get(spec[1])))
    return props

# ---------------------------------------------------------------------------
# Translations
# ---------------------------------------------------------------------------

def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\\\\n", "\\n") + '"'

def write_i18n(lang):
    lines = ["# PM2 archetypes: classes, toolbar tabs, properties, choices, units and tooltips", ""]
    for k, v in CLASSES.items():    lines.append(f"archetype.class.{k}: {q(v[lang])}")
    lines.append("")
    for k, v in CATEGORIES.items(): lines.append(f"archetype.category.{k}: {q(v[lang])}")
    lines.append("")
    for k, v in PROP_NAMES.items(): lines.append(f"archetype.prop_name.{k.lower()}: {q(v[lang])}")
    lines.append("")
    for k, v in CHOICE_LABELS.items(): lines.append(f"archetype.enum_choices.{k}: {q(v[lang])}")
    lines.append("")
    for k, v in UNITS.items():      lines.append(f"archetype.enum_units.{k}: {q(v[lang])}")
    lines.append("")
    for k, v in TOOLTIPS.items():   lines.append(f"archetype.tooltip.{k}: {q(v[lang])}")
    lines.append("")
    for k, v in PROP_CATEGORIES.items(): lines.append(f"archetype.prop_category.{k}: {q(v[lang])}")
    write(PROFILE / "i18n" / lang / "pm2_archetypes.yaml", "\n".join(lines) + "\n")
    lines = ["# Texts of the PM2 XSLT modules", ""]
    for k, v in XSLT_LABELS.items(): lines.append(f"{k}: {q(v[lang])}")
    write(PROFILE / "i18n" / lang / "pm2_xslt_labels.yaml", "\n".join(lines) + "\n")

# ---------------------------------------------------------------------------

if __name__ == "__main__":
    for lang in LANGS:
        write_archetypes(lang)
        write_i18n(lang)
    for lang in LANGS:
        content.build(lang, Project, document_values)
    print("done")

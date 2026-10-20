# Guidance comments of the sections of the project archetypes: what the section
# contains and which objects should be used in it (class label and toolbar tab).
from pathlib import Path
import yaml
from model import t, LANGS, CLASSES, CATEGORIES, TABS

PROFILE = Path(__file__).resolve().parent.parent

# Second-level archetypes: no toolbar button, created from the context menu of
# their parent
CONTEXT_MENU = {"cost-item": "cost-plan", "approval": "document-control",
                "revision": "document-control"}

def _basic_labels(lang):
    """Class labels of the archetypes copied from basic (basic_archetypes.yaml)."""
    data = yaml.safe_load((PROFILE / "i18n" / lang / "basic_archetypes.yaml").read_text(encoding="utf-8"))
    return {k[len("archetype.class."):]: v for k, v in data.items() if k.startswith("archetype.class.")}

_BASIC = {lang: _basic_labels(lang) for lang in LANGS}

# Archetypes of basic whose main class is not their id
MAIN_CLASS = {"local-figure": "figure", "remote-figure": "figure"}

def class_label(cls, lang):
    cls = MAIN_CLASS.get(cls, cls)
    label = CLASSES[cls][lang] if cls in CLASSES else _BASIC[lang][cls]
    return label.replace("\\n", " ").replace("\n", " ")

def tab_label(cls, lang):
    for folder, ids in TABS.items():
        if cls in ids:
            return CATEGORIES[folder[3:]][lang]
    raise KeyError(cls)

def object_text(cls, lang):
    if cls in CONTEXT_MENU:
        parent = class_label(CONTEXT_MENU[cls], lang)
        return {"en_us": f"**{class_label(cls, lang)}** (context menu of the {parent.lower()})",
                "es_es": f"**{class_label(cls, lang)}** (menú contextual del {parent.lower()})"}[lang]
    return {"en_us": f"**{class_label(cls, lang)}** (*{tab_label(cls, lang)}* tab)",
            "es_es": f"**{class_label(cls, lang)}** (pestaña *{tab_label(cls, lang)}*)"}[lang]

def guidance(help_, objects):
    """Text of the guidance comment: the help of the section and the objects to use."""
    text = {}
    for lang in LANGS:
        parts = [help_[lang]] if help_ else []
        if objects:
            head = {"en_us": "*Objects to use:* ", "es_es": "*Objetos que se usan:* "}[lang]
            parts.append(head + ", ".join(object_text(c, lang) for c in objects) + ".")
        text[lang] = "\n\n".join(parts)
    return text

GUIDANCE_NAME = t("Guidance", "Orientaciones")

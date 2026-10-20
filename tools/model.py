# PM2 profile model: archetype definitions and their labels in English and Spanish.
# Everything that must be identical in both languages (ids, classes, properties,
# choices) is defined once; only the texts are given per language.

DATE = "2026-10-19"
LANGS = ("en_us", "es_es")

def t(en, es):
    return {"en_us": en, "es_es": es}

# ---------------------------------------------------------------------------
# Enumerations: property choices (first one is the default) and choice labels
# ---------------------------------------------------------------------------

ENUMS = {
    "sensitivity": ["public", "sensitive-basic", "sensitive-high"],
    "delivery-type": ["tbd", "in-house", "outsourced", "mixed", "not-known"],
    "situation-kind": ["tbd", "need", "problem", "opportunity"],
    "legal-kind": ["tbd", "legislation", "directive", "policy", "other"],
    "perspective": ["tbd", "internal", "external"],
    "impact-area": ["tbd", "processes", "people", "culture", "external-stakeholders"],
    "impact-source": ["tbd", "current-situation", "solution"],
    "dimension": ["tbd", "scope", "schedule", "cost", "quality", "benefits"],
    "assumption-area": ["tbd", "business", "technology", "resources", "organisation",
                        "scope", "expectations", "schedule"],
    "validation": ["not-validated", "validated", "invalidated"],
    "constraint-area": ["tbd", "schedule", "budget", "resources", "products", "decisions",
                        "compliance", "organisation", "external-environment"],
    "risk-category": ["tbd", "business", "staffing", "contractor", "legal", "technical", "other"],
    "risk-status": ["proposed", "assessing", "awaiting-approval", "approved", "rejected", "closed"],
    "level": ["tbd", "very-low", "low", "medium", "high", "very-high"],
    "response-strategy": ["tbd", "avoid", "reduce", "accept", "transfer-share"],
    "approval-action": ["approve", "review", "optional-review"],
}

CHOICE_LABELS = {
    "public": t("Public", "Pública"),
    "sensitive-basic": t("Basic", "Básica"),
    "sensitive-high": t("High", "Alta"),
    "high": t("High (4)", "Alto (4)"),
    "in-house": t("In-house", "Interna"),
    "outsourced": t("Outsourced", "Externalizada"),
    "mixed": t("Mixed", "Mixta"),
    "not-known": t("Not known", "Desconocida"),
    "need": t("Business need", "Necesidad de negocio"),
    "problem": t("Problem", "Problema"),
    "opportunity": t("Opportunity", "Oportunidad"),
    "legislation": t("Legislation", "Legislación"),
    "directive": t("Management directive", "Directriz de la dirección"),
    "policy": t("Internal regulation or policy", "Normativa o política interna"),
    "other": t("Other", "Otro"),
    "internal": t("Internal", "Interna"),
    "external": t("External", "Externa"),
    "processes": t("Processes", "Procesos"),
    "people": t("People", "Personas"),
    "culture": t("Culture", "Cultura"),
    "external-stakeholders": t("External stakeholders", "Partes interesadas externas"),
    "current-situation": t("Current situation", "Situación actual"),
    "solution": t("Desired solution", "Solución deseada"),
    "scope": t("Scope", "Alcance"),
    "schedule": t("Schedule", "Plazo"),
    "cost": t("Cost", "Coste"),
    "quality": t("Quality", "Calidad"),
    "benefits": t("Benefits", "Beneficios"),
    "business": t("Business", "Negocio"),
    "technology": t("Technology", "Tecnología"),
    "resources": t("Resources", "Recursos"),
    "organisation": t("Organisation", "Organización"),
    "expectations": t("Expectations", "Expectativas"),
    "not-validated": t("Not validated", "No validada"),
    "validated": t("Validated", "Validada"),
    "invalidated": t("Invalidated", "Invalidada"),
    "budget": t("Budget", "Presupuesto"),
    "products": t("Products", "Productos"),
    "decisions": t("Decisions", "Decisiones"),
    "compliance": t("Compliance", "Cumplimiento normativo"),
    "external-environment": t("External environment", "Entorno externo"),
    "staffing": t("Staffing", "Personal"),
    "contractor": t("Contractor", "Contratista"),
    "legal": t("Legal", "Legal"),
    "technical": t("Technical", "Técnico"),
    "proposed": t("Proposed", "Propuesto"),
    "assessing": t("Assessing", "En evaluación"),
    "awaiting-approval": t("Awaiting approval", "Pendiente de aprobación"),
    "approved": t("Approved", "Aprobado"),
    "rejected": t("Rejected", "Rechazado"),
    "closed": t("Closed", "Cerrado"),
    "very-low": t("Very low (1)", "Muy bajo (1)"),
    "low": t("Low (2)", "Bajo (2)"),
    "medium": t("Medium (3)", "Medio (3)"),
    "very-high": t("Very high (5)", "Muy alto (5)"),
    "avoid": t("Avoid", "Evitar"),
    "reduce": t("Reduce", "Reducir"),
    "accept": t("Accept", "Aceptar"),
    "transfer-share": t("Transfer / share", "Transferir / compartir"),
    "approve": t("Approve", "Aprobar"),
    "review": t("Review", "Revisar"),
    "optional-review": t("Review (optional)", "Revisar (opcional)"),
}

# ---------------------------------------------------------------------------
# Property names, tooltips, classes and toolbar tabs
# ---------------------------------------------------------------------------

PROP_NAMES = {
    "sensitivity": t("Sensitivity", "Sensibilidad"),
    "document-author": t("Document author", "Autor del documento"),
    "project-manager": t("Project Manager (PM)", "Jefe de proyecto (PM)"),
    "document-location": t("Document location", "Ubicación del documento"),
    "initiator": t("Initiator", "Iniciador"),
    "requesting-unit": t("Organisation / unit", "Organización / unidad"),
    "project-owner": t("Project Owner (PO)", "Propietario del proyecto (PO)"),
    "solution-provider": t("Solution Provider (SP)", "Proveedor de la solución (SP)"),
    "approving-authority": t("Approving authority", "Autoridad aprobadora"),
    "request-date": t("Date of request", "Fecha de la solicitud"),
    "estimated-effort": t("Estimated effort", "Esfuerzo estimado"),
    "other-costs": t("Other costs", "Otros costes"),
    "target-delivery-date": t("Target delivery date", "Fecha objetivo de entrega"),
    "delivery-type": t("Type of delivery", "Tipo de entrega"),
    "kind": t("Kind", "Tipo"),
    "owner": t("Owner", "Propietario"),
    "reference": t("Reference", "Referencia"),
    "supports": t("Supports", "Respalda"),
    "addresses": t("Addresses", "Responde a"),
    "contributes-to": t("Contributes to", "Contribuye a"),
    "perspective": t("Perspective", "Perspectiva"),
    "area": t("Area", "Área"),
    "source": t("Caused by", "Causado por"),
    "affects": t("Affects", "Afecta a"),
    "dimension": t("Dimension", "Dimensión"),
    "target": t("Target", "Objetivo"),
    "evaluates": t("Evaluates", "Evalúa"),
    "validation": t("Validation", "Validación"),
    "may-become": t("May become", "Puede convertirse en"),
    "status": t("Status", "Estado"),
    "identified-by": t("Identified by", "Identificado por"),
    "likelihood": t("Likelihood", "Probabilidad"),
    "impact": t("Impact", "Impacto"),
    "risk-owner": t("Risk owner", "Propietario del riesgo"),
    "response-strategy": t("Response strategy", "Estrategia de respuesta"),
    "actions": t("Response actions", "Acciones de respuesta"),
    "escalation": t("Escalation", "Escalado"),
    "related": t("Related to", "Relacionado con"),
    "approver": t("Approver / reviewer", "Aprobador / revisor"),
    "action": t("Action", "Acción"),
    "revision": t("Revision", "Revisión"),
    "created-by": t("Created by", "Creada por"),
    "changes": t("Changes", "Cambios"),
}

TOOLTIPS = {
    "pattern": t("Replace the texts in italics between brackets.",
                 "Sustituya los textos en cursiva entre corchetes."),
    "risk-pattern": t("Because of (condition), it might be that (event), which will lead to (impact). Replace the texts in italics.",
                      "Debido a (condición), podría ocurrir que (evento), lo que provocaría (impacto). Sustituya los textos en cursiva."),
    "estimated-effort": t("High level estimate in person-days.",
                          "Estimación de alto nivel en días-persona."),
    "approving-authority": t("Decision maker according to the governance structure of the organisation.",
                             "Responsable de la decisión según la estructura de gobierno de la organización."),
    "validation": t("Assumptions are taken as facts but must be validated; unvalidated assumptions may become risks.",
                    "Los supuestos se toman como hechos pero deben validarse; si no se validan, pueden convertirse en riesgos."),
    "document-location": t("Where the latest version of this controlled document is stored.",
                           "Dónde se guarda la última versión de este documento controlado."),
}

CLASSES = {
    "initiation-request": t("Project initiation\\nrequest", "Solicitud de\\ninicio"),
    "business-situation": t("Business\\nsituation", "Situación\\nNegocio"),
    "strategic-goal": t("Strategic\\ngoal", "Objetivo\\nestratégico"),
    "legal-basis": t("Legal\\nbasis", "Base\\nlegal"),
    "outcome": t("Outcome", "Resultado"),
    "impact": t("Impact", "Impacto"),
    "success-criterion": t("Success\\ncriterion", "Criterio\\nde éxito"),
    "assumption": t("Assumption", "Supuesto"),
    "constraint": t("Constraint", "Restricción"),
    "risk": t("Risk", "Riesgo"),
    "document-control": t("Document\\ncontrol", "Control del\\ndocumento"),
    "approval": t("Approval", "Aprobación"),
    "revision": t("Revision", "Revisión"),
}

CATEGORIES = {
    "document": t("Document", "Documento"),
    "organisation": t("Organisation", "Organización"),
    "rationale": t("Rationale", "Justificación"),
    "conditions": t("Conditions", "Condiciones"),
    "references": t("References", "Referencias"),
}

# Toolbar tabs (category folders) and their archetypes, in order. The archetypes of
# basic are copied into this profile; the PM2 ones are generated (ARCHETYPES below).
# Second-level archetypes (approval, revision) have no button but must be listed.
TABS = {
    "00_document": ["section", "appendix", "paragraph", "comment", "local-figure",
                    "remote-figure", "symbolic-link"],
    "01_organisation": ["organization", "stakeholder", "meeting", "document-control",
                        "approval", "revision"],
    "02_rationale": ["initiation-request", "business-situation", "strategic-goal",
                     "legal-basis", "outcome", "impact"],
    "03_conditions": ["success-criterion", "assumption", "constraint", "risk"],
    "04_references": ["glossary-item", "bibliography-item", "traceability-matrix"],
}

UNITS = {"person-day": t("person-days", "días-persona")}

# Texts of the templates (xslt.* keys)
XSLT_LABELS = {
    "xslt.document_control_info": t("Document control information", "Información de control del documento"),
    "xslt.document_title": t("Document title", "Título del documento"),
    "xslt.project_title": t("Project title", "Título del proyecto"),
    "xslt.approvers_reviewers": t("Document approvers and reviewers", "Aprobadores y revisores del documento"),
    "xslt.document_history": t("Document history", "Historial del documento"),
    "xslt.name": t("Name", "Nombre"),
    "xslt.role": t("Role", "Rol"),
    "xslt.date": t("Date", "Fecha"),
    "xslt.document_location": t("The latest version of this controlled document is stored in {0}.",
                                "La última versión de este documento controlado se guarda en {0}."),
    "xslt.risk_level": t(" (risk level {0})", " (nivel de riesgo {0})"),
    "xslt.escalate": t("To be escalated to the directing or steering layer",
                       "Debe escalarse al nivel de dirección o de gestión"),
    "xslt.yes": t("Yes", "Sí"),
}

# ---------------------------------------------------------------------------
# Property specs: (type, name, category, attributes, default)
# A default is a string, a t(...) dict or a list of trace targets.
# ---------------------------------------------------------------------------

def code(prefix):  return ("code", ":Proteus-code", "general", {"prefix": prefix}, "001")
def name(text):    return ("string", ":Proteus-name", "general", {}, text)
def string(n, v="", cat="detail", **a): return ("string", n, cat, a, v)
def md(n, v="", cat="detail", **a):     return ("markdown", n, cat, a, v)
def enum(n, e, cat="detail", **a):      return ("enum", n, cat, dict(a, choices=e), ENUMS[e][0])
def date(n=":Proteus-date", cat="general"): return ("date", n, cat, {}, DATE)
def trace(n, targets, cat="dependencies", ttype=":Proteus-dependency", max_=None):
    a = {"acceptedTargets": targets, "traceType": ttype}
    if max_: a["maxTargetsNumber"] = str(max_)
    return ("trace", n, cat, a, [])
def unit(n, units, v="0", cat="detail", **a): return ("unit", n, cat, dict(a, units=units), v)
def boolean(n, v="false", cat="detail"): return ("boolean", n, cat, {}, v)
def url(n, cat="detail"): return ("url", n, cat, {}, "")

def header(name_text):
    return [name(name_text), date(), ("string", "version", "general", {}, "1.0"),
            trace("authors", "stakeholder", "general", ":Proteus-author"),
            trace("sources", "stakeholder", "general", ":Proteus-information-source")]

def item(prefix, name_text, pattern, tooltip="pattern"):
    return [code(prefix)] + header(name_text) + [md("description", pattern, tooltip=tooltip)]

COMMENTS = md("comments", "", "comments")

ARCHETYPES = {}   # id -> dict(category, classes, children, parents, props, numbered)

def archetype(id_, category, classes, props, children=":Proteus-none",
              parents=":Proteus-document section"):
    ARCHETYPES[id_] = dict(category=category, classes=classes, children=children,
                           parents=parents, props=props + [COMMENTS])

archetype("initiation-request", "02_rationale", "initiation-request",
    header(t("Project initiation request", "Solicitud de inicio del proyecto")) + [
        trace("initiator", "stakeholder", "detail", max_=1),
        trace("requesting-unit", "organization", "detail", max_=1),
        trace("project-owner", "stakeholder", "detail", max_=1),
        trace("solution-provider", "stakeholder", "detail", max_=1),
        trace("approving-authority", "stakeholder organization", "detail", max_=1),
        date("request-date", "detail"),
        unit("estimated-effort", "person-day", tooltip="estimated-effort"),
        md("other-costs"),
        date("target-delivery-date", "detail"),
        enum("delivery-type", "delivery-type"),
    ], parents=":Proteus-document")

archetype("business-situation", "02_rationale", "traceable-object business-situation",
    item("SIT-", t("Business situation", "Situación de negocio"),
         t("Currently, _[current situation]_, which causes _[consequence for the business]_.",
           "Actualmente, _[situación actual]_, lo que provoca _[consecuencia para el negocio]_.")) +
    [enum("kind", "situation-kind")])

archetype("strategic-goal", "02_rationale", "traceable-object strategic-goal",
    item("SG-", t("Strategic goal", "Objetivo estratégico"),
         t("_[Strategic goal of the organisation the project contributes to]_.",
           "_[Objetivo estratégico de la organización al que contribuye el proyecto]_.")) +
    [trace("owner", "organization", "detail", max_=1)])

archetype("legal-basis", "02_rationale", "traceable-object legal-basis",
    item("LB-", t("Legal basis", "Base legal"),
         t("_[Act, directive or agreement]_ establishes that _[obligation or mandate]_.",
           "_[Norma, directriz o acuerdo]_ establece que _[obligación o mandato]_.")) +
    [enum("kind", "legal-kind"), url("reference"),
     trace("supports", "strategic-goal")])

archetype("outcome", "02_rationale", "traceable-object outcome",
    item("OUT-", t("Outcome", "Resultado"),
         t("After the project, _[desired future state]_.",
           "Tras el proyecto, _[situación futura deseada]_.")) +
    [trace("addresses", "business-situation"), trace("contributes-to", "strategic-goal")])

archetype("impact", "02_rationale", "traceable-object impact",
    item("IMP-", t("Impact", "Impacto"),
         t("_[The current situation / the solution]_ affects _[processes, people or stakeholders]_ because _[reason]_.",
           "_[La situación actual / la solución]_ afecta a _[procesos, personas o partes interesadas]_ porque _[motivo]_.")) +
    [enum("perspective", "perspective"), enum("area", "impact-area"),
     enum("source", "impact-source"), trace("affects", "stakeholder organization")])

archetype("success-criterion", "03_conditions", "traceable-object success-criterion",
    item("SC-", t("Success criterion", "Criterio de éxito"),
         t("The project will be considered a success if _[measurable criterion]_.",
           "El proyecto se considerará un éxito si _[criterio medible]_.")) +
    [enum("dimension", "dimension"), string("target"), trace("evaluates", "outcome")])

archetype("assumption", "03_conditions", "traceable-object assumption",
    item("ASM-", t("Assumption", "Supuesto"),
         t("It is assumed that _[fact taken as true]_.",
           "Se asume que _[hecho que se da por cierto]_.")) +
    [enum("area", "assumption-area"), enum("validation", "validation", tooltip="validation"),
     trace("may-become", "risk")])

archetype("constraint", "03_conditions", "traceable-object constraint",
    item("CON-", t("Constraint", "Restricción"),
         t("The project must _[limit on schedule, budget, resources, products or compliance]_.",
           "El proyecto debe _[límite de plazo, presupuesto, recursos, productos o cumplimiento]_.")) +
    [enum("area", "constraint-area")])

archetype("risk", "03_conditions", "traceable-object risk",
    item("RSK-", t("Risk", "Riesgo"),
         t("Because of _[condition]_, it might be that _[event]_, which will lead to _[impact]_.",
           "Debido a _[condición]_, podría ocurrir que _[evento]_, lo que provocaría _[impacto]_."),
         tooltip="risk-pattern") +
    [enum("category", "risk-category"), enum("status", "risk-status"),
     trace("identified-by", "stakeholder", "detail", max_=1),
     enum("likelihood", "level"), enum("impact", "level"),
     trace("risk-owner", "stakeholder", "detail", max_=1),
     enum("response-strategy", "response-strategy"), md("actions"), boolean("escalation"),
     trace("related", "assumption constraint")])

archetype("document-control", "01_organisation", "document-control",
    [name(t("Document control", "Control del documento"))],
    children="approval revision")

archetype("approval", "01_organisation", "approval",
    [name(t("Approval", "Aprobación")), date(),
     trace("approver", "stakeholder", "general", max_=1),
     enum("action", "approval-action", "general")],
    parents="document-control")

archetype("revision", "01_organisation", "revision",
    [name(t("Revision", "Revisión")), date(),
     string("revision", "0.1", "general"),
     trace("created-by", "stakeholder", "general", max_=1),
     md("changes", "", "general")],
    parents="document-control")

# Document objects (not object archetypes): PIR and stakeholders documents
def document_props(acronym, name_text, description):
    return [("string", ":Proteus-acronym", "general", {}, acronym), name(name_text),
            ("string", "version", "general", {}, "0.1"), date(),
            enum("sensitivity", "sensitivity", "general"),
            trace("document-author", "stakeholder", "general", max_=1),
            trace("project-manager", "stakeholder", "general", max_=1),
            string("document-location", "", "general", tooltip="document-location"),
            md("description", description),
            trace("prepared-for", "organization", "dependencies"),
            trace("prepared-by", "organization", "dependencies", ":Proteus-author"),
            COMMENTS]

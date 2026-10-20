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
    "impact-area": ["tbd", "strategy", "processes", "people", "culture", "it-landscape",
                    "external-stakeholders"],
    "severity": ["tbd", "minor", "moderate", "significant"],
    "applies-to": ["tbd", "project", "product"],
    "process-category": ["tbd", "policy-lifecycle", "legislation-lifecycle", "coordination",
                         "programme-management", "grant-management", "external-communication",
                         "internal-communication", "strategic-management", "financial-management",
                         "procurement", "document-management", "asset-management", "audit",
                         "human-resources", "it", "other"],
    "alternative-kind": ["tbd", "do-nothing", "reuse", "simple", "sophisticated", "other"],
    "inclusion": ["in", "out"],
    "scope-kind": ["tbd", "output", "process", "organisation", "location", "other"],
    "deliverable-kind": ["tbd", "process", "information-system", "policy", "service", "platform",
                         "plan", "event", "training", "other"],
    "milestone-kind": ["milestone", "start", "delivery"],
    "dependency-kind": ["tbd", "interrelation", "dependency", "synergy", "it-reuse", "it-request",
                        "it-sharing"],
    "dependency-scope": ["tbd", "internal", "external"],
    "cost-group": ["solution-implementation", "business-implementation"],
    "cost-category": ["tbd", "development", "maintenance", "support", "training", "infrastructure",
                      "change-management", "start-up", "coordination", "other"],
    "cost-nature": ["other-costs", "staff"],
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
    # Business Case
    "strategy": t("Strategy", "Estrategia"),
    "it-landscape": t("IT landscape", "Panorama TI"),
    "minor": t("Minor", "Menor"),
    "moderate": t("Moderate", "Moderado"),
    "significant": t("Significant", "Significativo"),
    "project": t("Project", "Proyecto"),
    "product": t("Product", "Producto"),
    "policy-lifecycle": t("Policy lifecycle", "Ciclo de vida de políticas"),
    "legislation-lifecycle": t("Legislation lifecycle", "Ciclo de vida legislativo"),
    "coordination": t("Coordination", "Coordinación"),
    "programme-management": t("Programme management", "Gestión de programas"),
    "grant-management": t("Grant management", "Gestión de subvenciones"),
    "external-communication": t("Communication and dissemination (external)", "Comunicación y difusión (externa)"),
    "internal-communication": t("Communication and dissemination (internal)", "Comunicación y difusión (interna)"),
    "strategic-management": t("Strategic management", "Gestión estratégica"),
    "financial-management": t("Financial management", "Gestión financiera"),
    "procurement": t("Procurement", "Contratación"),
    "document-management": t("Document management", "Gestión documental"),
    "asset-management": t("Asset management", "Gestión de activos"),
    "audit": t("Audit", "Auditoría"),
    "human-resources": t("Human resources", "Recursos humanos"),
    "it": t("IT", "TI"),
    "do-nothing": t("Do nothing", "No hacer nada"),
    "reuse": t("Reuse an existing solution", "Reutilizar una solución existente"),
    "simple": t("Simple solution (develop or buy and customise)", "Solución sencilla (desarrollar o comprar y adaptar)"),
    "sophisticated": t("Sophisticated solution (develop or buy and customise)", "Solución sofisticada (desarrollar o comprar y adaptar)"),
    "in": t("In scope", "Dentro del alcance"),
    "out": t("Out of scope", "Fuera del alcance"),
    "output": t("Output", "Producto o resultado"),
    "process": t("Process", "Proceso"),
    "location": t("Location", "Ubicación"),
    "information-system": t("Information system", "Sistema de información"),
    "service": t("Service", "Servicio"),
    "platform": t("Platform", "Plataforma"),
    "plan": t("Plan or strategy", "Plan o estrategia"),
    "event": t("Event", "Evento"),
    "training": t("Training", "Formación"),
    "milestone": t("Milestone", "Hito"),
    "start": t("Project start", "Inicio del proyecto"),
    "delivery": t("Project delivery", "Entrega del proyecto"),
    "interrelation": t("Interrelation", "Interrelación"),
    "dependency": t("Interdependency", "Interdependencia"),
    "synergy": t("Synergy", "Sinergia"),
    "it-reuse": t("Reused IT service or component", "Servicio o componente TI reutilizado"),
    "it-request": t("Requested common IT service or component", "Servicio o componente TI común solicitado"),
    "it-sharing": t("IT service or component made reusable", "Servicio o componente TI que se hará reutilizable"),
    "solution-implementation": t("Solution implementation", "Implantación de la solución"),
    "business-implementation": t("Business implementation", "Implantación en el negocio"),
    "development": t("Solution development", "Desarrollo de la solución"),
    "maintenance": t("Solution maintenance", "Mantenimiento de la solución"),
    "support": t("Support", "Soporte"),
    "infrastructure": t("Infrastructure", "Infraestructura"),
    "change-management": t("Change management", "Gestión del cambio"),
    "start-up": t("Start-up costs", "Costes de puesta en marcha"),
    "other-costs": t("Other costs (k€)", "Otros costes (k€)"),
    "staff": t("Staff (FTE)", "Personal (ETC)"),
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
    # Business Case
    "refines": t("Refines", "Refina"),
    "urgency": t("Urgency", "Urgencia"),
    "severity": t("Impact on owners and users", "Impacto en responsables y usuarios"),
    "affected-processes": t("Affected processes", "Procesos afectados"),
    "critical": t("Critical", "Crítico"),
    "applies-to": t("Applies to", "Se aplica a"),
    "process-category": t("Process category", "Categoría de proceso"),
    "domain": t("Domain", "Dominio"),
    "sub-domain": t("Sub-domain", "Subdominio"),
    "macro-process": t("Macro process", "Macroproceso"),
    "strengths": t("Strengths", "Fortalezas"),
    "weaknesses": t("Weaknesses", "Debilidades"),
    "opportunities": t("Opportunities", "Oportunidades"),
    "threats": t("Threats", "Amenazas"),
    "assessment": t("Qualitative assessment", "Valoración cualitativa"),
    "chosen": t("Chosen alternative", "Alternativa elegida"),
    "selection-rationale": t("Reasons for the choice", "Motivos de la elección"),
    "indicator": t("Indicator", "Indicador"),
    "baseline": t("Baseline", "Valor de partida"),
    "derives-from": t("Derives from", "Procede de"),
    "perceived-by": t("Perceived by", "Percibido por"),
    "inclusion": t("Inclusion", "Inclusión"),
    "realises": t("Realises", "Materializa"),
    "within": t("Within the scope item", "Dentro del elemento de alcance"),
    "planned-date": t("Planned date", "Fecha prevista"),
    "delivers": t("Delivers", "Entrega"),
    "scope": t("Scope", "Ámbito"),
    "first-year": t("First year", "Primer año"),
    "funding-source": t("Funding source", "Fuente de financiación"),
    "group": t("Group", "Grupo"),
    "nature": t("Nature", "Naturaleza"),
    "year-1": t("Year 1", "Año 1"),
    "year-2": t("Year 2", "Año 2"),
    "year-3": t("Year 3", "Año 3"),
    "year-4": t("Year 4", "Año 4"),
    "year-5": t("Year 5", "Año 5"),
}

PROP_CATEGORIES = {
    "swot": t("SWOT", "DAFO"),
    "costs": t("Costs", "Costes"),
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
    "refines": t("Object of a previous artefact that this one refines (e.g. a success criterion of the Project Initiation Request refined in the Business Case).",
                 "Objeto de un artefacto anterior que este refina (p. ej., un criterio de éxito de la solicitud de inicio refinado en el caso de negocio)."),
    "critical": t("Without it, the project cannot be considered a success.",
                  "Sin él, el proyecto no puede considerarse un éxito."),
    "chosen": t("The alternative recommended and described in the solution.",
                "La alternativa recomendada, que se describe en la solución."),
    "first-year": t("Year of the first column of the cost tables; costs are given for 5 years.",
                    "Año de la primera columna de las tablas de costes; los costes se dan para 5 años."),
    "cost-nature": t("Staff costs are given in full-time equivalents (FTE), other costs in thousands of euros (k€).",
                     "Los costes de personal se dan en equivalentes a tiempo completo (ETC) y el resto en miles de euros (k€)."),
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
    "business-process": t("Business\\nprocess", "Proceso de\\nnegocio"),
    "alternative": t("Alternative", "Alternativa"),
    "benefit": t("Benefit", "Beneficio"),
    "scope-item": t("Scope\\nitem", "Elemento\\nalcance"),
    "deliverable": t("Deliverable", "Entregable"),
    "milestone": t("Milestone", "Hito"),
    "interdependency": t("Interdependency", "Interdependencia"),
    "cost-plan": t("Cost\\nplan", "Plan de\\ncostes"),
    "cost-item": t("Cost", "Coste"),
}

CATEGORIES = {
    "document": t("Document", "Documento"),
    "organisation": t("Organisation", "Organización"),
    "rationale": t("Rationale", "Justificación"),
    "solution": t("Solution", "Solución"),
    "conditions": t("Conditions", "Condiciones"),
    "references": t("References", "Referencias"),
}

# Toolbar tabs (category folders) and their archetypes, in order. The archetypes of
# basic are copied into this profile; the PM2 ones are generated (ARCHETYPES below).
# Second-level archetypes (approval, revision) have no button but must be listed.
TABS = {
    "00_document": ["section", "appendix", "paragraph", "comment", "local-figure",
                    "remote-figure", "symbolic-link"],
    "01_organisation": ["organization", "stakeholder", "meeting", "business-process",
                        "initiation-request", "document-control", "approval", "revision"],
    "02_rationale": ["business-situation", "strategic-goal", "legal-basis", "outcome",
                     "impact", "benefit"],
    "03_solution": ["alternative", "scope-item", "deliverable", "milestone", "cost-plan",
                    "cost-item"],
    "04_conditions": ["success-criterion", "assumption", "constraint", "risk",
                      "interdependency"],
    "05_references": ["glossary-item", "bibliography-item", "traceability-matrix"],
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
    "xslt.chosen": t(" (chosen)", " (elegida)"),
    "xslt.swot": t("SWOT analysis", "Análisis DAFO"),
    "xslt.total_staff": t("Total staff (FTE)", "Total personal (ETC)"),
    "xslt.total_other": t("Total other costs (k€)", "Total otros costes (k€)"),
    "xslt.cost_concept": t("Cost", "Coste"),
    "xslt.unit_fte": t(" (FTE)", " (ETC)"),
    "xslt.unit_keur": t(" (k€)", " (k€)"),
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
def trace(n, targets, cat="dependencies", ttype=":Proteus-dependency", max_=None, tooltip_=None):
    a = {"acceptedTargets": targets, "traceType": ttype}
    if max_: a["maxTargetsNumber"] = str(max_)
    if tooltip_: a["tooltip"] = tooltip_
    return ("trace", n, cat, a, [])
def unit(n, units, v="0", cat="detail", **a): return ("unit", n, cat, dict(a, units=units), v)
def boolean(n, v="false", cat="detail", **a): return ("boolean", n, cat, a, v)
def url(n, cat="detail"): return ("url", n, cat, {}, "")
def number(n, v="0", cat="detail", **a): return ("float", n, cat, a, v)
def integer(n, v="0", cat="detail", **a): return ("integer", n, cat, a, v)

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
    # Every traceable PM2 object may refine an object of the same class of a
    # previous artefact (e.g. a success criterion of the PIR in the Business Case)
    if classes.startswith("traceable-object "):
        props = props + [trace("refines", classes.split()[-1], tooltip_="refines")]
    ARCHETYPES[id_] = dict(category=category, classes=classes, children=children,
                           parents=parents, props=props + [COMMENTS])

archetype("initiation-request", "01_organisation", "initiation-request",
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
    [enum("kind", "situation-kind"), md("urgency")])

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
     enum("source", "impact-source"), enum("severity", "severity"),
     trace("affects", "stakeholder organization"), trace("affected-processes", "business-process")])

archetype("benefit", "02_rationale", "traceable-object benefit",
    item("BEN-", t("Benefit", "Beneficio"),
         t("_[Measurable improvement]_ for _[beneficiary]_.",
           "_[Mejora medible]_ para _[beneficiario]_.")) +
    [string("indicator"), string("baseline"), string("target"),
     trace("derives-from", "outcome"), trace("perceived-by", "stakeholder organization")])

archetype("success-criterion", "04_conditions", "traceable-object success-criterion",
    item("SC-", t("Success criterion", "Criterio de éxito"),
         t("The project will be considered a success if _[measurable criterion]_.",
           "El proyecto se considerará un éxito si _[criterio medible]_.")) +
    [enum("dimension", "dimension"), string("target"),
     boolean("critical", tooltip="critical"), enum("applies-to", "applies-to"),
     trace("evaluates", "outcome")])

archetype("assumption", "04_conditions", "traceable-object assumption",
    item("ASM-", t("Assumption", "Supuesto"),
         t("It is assumed that _[fact taken as true]_.",
           "Se asume que _[hecho que se da por cierto]_.")) +
    [enum("area", "assumption-area"), enum("validation", "validation", tooltip="validation"),
     trace("may-become", "risk")])

archetype("constraint", "04_conditions", "traceable-object constraint",
    item("CON-", t("Constraint", "Restricción"),
         t("The project must _[limit on schedule, budget, resources, products or compliance]_.",
           "El proyecto debe _[límite de plazo, presupuesto, recursos, productos o cumplimiento]_.")) +
    [enum("area", "constraint-area")])

archetype("risk", "04_conditions", "traceable-object risk",
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

archetype("interdependency", "04_conditions", "traceable-object interdependency",
    item("DEP-", t("Interdependency", "Interdependencia"),
         t("_[The situation / the solution]_ _[is related to / depends on / can reuse]_ _[other need, initiative, system or service]_.",
           "_[La situación / la solución]_ _[está relacionada con / depende de / puede reutilizar]_ _[otra necesidad, iniciativa, sistema o servicio]_.")) +
    [enum("kind", "dependency-kind"), enum("scope", "dependency-scope"),
     trace("related", "business-situation alternative deliverable")])

# --- Business Case: organisation and solution ---------------------------------

archetype("business-process", "01_organisation", "traceable-object business-process",
    item("BP-", t("Business process", "Proceso de negocio"),
         t("_[What the process does and who takes part in it]_.",
           "_[Qué hace el proceso y quién interviene en él]_.")) +
    [enum("process-category", "process-category"), string("domain"), string("sub-domain"),
     string("macro-process"), trace("owner", "organization stakeholder", "detail", max_=1)])

archetype("alternative", "03_solution", "traceable-object alternative",
    item("ALT-", t("Alternative", "Alternativa"),
         t("_[What the alternative consists of]_.",
           "_[En qué consiste la alternativa]_.")) +
    [enum("kind", "alternative-kind"),
     md("strengths", "", "swot"), md("weaknesses", "", "swot"),
     md("opportunities", "", "swot"), md("threats", "", "swot"),
     md("assessment"), boolean("chosen", tooltip="chosen"), md("selection-rationale"),
     trace("addresses", "business-situation")])

archetype("scope-item", "03_solution", "traceable-object scope-item",
    item("SCP-", t("Scope item", "Elemento de alcance"),
         t("The project _[includes / excludes]_ _[output, process, organisation or location]_.",
           "El proyecto _[incluye / excluye]_ _[producto, proceso, organización o ubicación]_.")) +
    [enum("inclusion", "inclusion"), enum("kind", "scope-kind"),
     trace("realises", "alternative")])

archetype("deliverable", "03_solution", "traceable-object deliverable",
    item("DLV-", t("Deliverable", "Entregable"),
         t("_[Deliverable]_, which _[purpose]_.",
           "_[Entregable]_, que _[finalidad]_.")) +
    [enum("kind", "deliverable-kind"),
     trace("within", "scope-item"), trace("contributes-to", "outcome")])

archetype("milestone", "03_solution", "traceable-object milestone",
    item("MS-", t("Milestone", "Hito"),
         t("_[Event that marks the milestone]_.",
           "_[Acontecimiento que marca el hito]_.")) +
    [enum("kind", "milestone-kind"), date("planned-date", "detail"),
     trace("delivers", "deliverable")])

archetype("cost-plan", "03_solution", "cost-plan",
    [name(t("Costs, effort and funding source", "Costes, esfuerzo y fuente de financiación")),
     integer("first-year", DATE[:4], tooltip="first-year"), md("funding-source")],
    children="cost-item")

archetype("cost-item", "03_solution", "cost-item",
    [name(t("Cost", "Coste")),
     enum("group", "cost-group", "general"), enum("category", "cost-category", "general"),
     enum("nature", "cost-nature", "general", tooltip="cost-nature")] +
    [number(f"year-{i}", "0", "costs") for i in range(1, 6)],
    parents="cost-plan")

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

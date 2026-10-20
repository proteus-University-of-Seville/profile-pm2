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
    "milestone-kind": ["milestone", "start", "phase-end", "delivery"],
    "phase": ["tbd", "initiating", "planning", "executing", "closing"],
    "need-priority": ["tbd", "essential", "desirable", "optional"],
    "resource-kind": ["tbd", "staff", "equipment", "facilities", "tools", "other"],
    "pm2-role": ["tbd", "agb", "psc", "po", "bm", "sp", "pm", "big", "ur", "pct", "pso"],
    "stakeholder-category": ["tbd", "customer", "developer", "user"],
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
    "constraint-area": ["tbd", "schedule", "budget", "resources", "people", "products",
                        "technology", "interfaces", "decisions", "compliance", "security",
                        "data-protection", "document-management", "organisation",
                        "external-environment"],
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
    # Project Charter
    "phase-end": t("End of phase", "Fin de fase"),
    "initiating": t("Initiating", "Inicio"),
    "planning": t("Planning", "Planificación"),
    "executing": t("Executing", "Ejecución"),
    "closing": t("Closing", "Cierre"),
    "essential": t("Essential", "Imprescindible"),
    "desirable": t("Desirable", "Deseable"),
    "optional": t("Optional", "Opcional"),
    "equipment": t("Equipment", "Equipamiento"),
    "facilities": t("Facilities", "Instalaciones"),
    "tools": t("Support tools", "Herramientas de apoyo"),
    "agb": t("Appropriate Governance Body (AGB)", "Órgano de gobierno competente (AGB)"),
    "psc": t("Project Steering Committee (PSC)", "Comité de dirección del proyecto (PSC)"),
    "po": t("Project Owner (PO)", "Propietario del proyecto (PO)"),
    "bm": t("Business Manager (BM)", "Responsable de negocio (BM)"),
    "sp": t("Solution Provider (SP)", "Proveedor de la solución (SP)"),
    "pm": t("Project Manager (PM)", "Jefe de proyecto (PM)"),
    "big": t("Business Implementation Group (BIG)", "Grupo de implantación en el negocio (BIG)"),
    "ur": t("User Representatives (UR)", "Representantes de los usuarios (UR)"),
    "pct": t("Project Core Team (PCT)", "Equipo central del proyecto (PCT)"),
    "pso": t("Project Support Office (PSO)", "Oficina de apoyo al proyecto (PSO)"),
    "interfaces": t("Interfaces", "Interfaces"),
    "security": t("Security", "Seguridad"),
    "data-protection": t("Data protection", "Protección de datos"),
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
    # Project Charter
    "budget-line": t("Budget line", "Partida presupuestaria"),
    "previous-investments": t("Previous investments", "Inversiones previas"),
    "phase": t("Phase", "Fase"),
    "stakeholders": t("Stakeholders", "Partes interesadas"),
    "desired-solution": t("Desired solution", "Solución deseada"),
    "justification": t("Justification", "Justificación"),
    "current-handling": t("How it is addressed today", "Cómo se aborda hoy"),
    "priority": t("Priority", "Prioridad"),
    "satisfies": t("Satisfies", "Satisface"),
    "delivered-in": t("Delivered in", "Se entrega en"),
    "quantity": t("Quantity", "Cantidad"),
    "skills": t("Skills and experience", "Conocimientos y experiencia"),
    "acquisition": t("How it will be obtained", "Cómo se obtendrá"),
    "provided-by": t("Provided by", "Aportado por"),
    "responsible": t("Responsible", "Responsable"),
    "pm2-role": t("PM² role", "Rol PM²"),
    "assignee": t("Assigned to", "Asignado a"),
    "responsibilities": t("Responsibilities", "Responsabilidades"),
    "deviations": t("Deviations from the standard", "Desviaciones respecto al estándar"),
    "profile": t("Profile", "Perfil"),
    "perceived-problems": t("Perceived problems", "Problemas percibidos"),
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
    "need-priority": t("Relative importance of the need from the point of view of the stakeholders: essential needs must be addressed, desirable ones should be.",
                       "Importancia relativa de la necesidad desde el punto de vista de las partes interesadas: las imprescindibles deben abordarse y las deseables, si es posible."),
    "feature": t("High level capability of an output: what is needed and why, not how it will be implemented.",
                 "Capacidad de alto nivel de un producto: qué se necesita y por qué, no cómo se implementará."),
    "perceived-problems": t("Key problems that the stakeholder perceives and that the solution should address.",
                            "Problemas clave que percibe la parte interesada y que debería abordar la solución."),
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
    "business-process": t("Business\\nprocess", "Proceso\\nNegocio"),
    "alternative": t("Alternative", "Alternativa"),
    "benefit": t("Benefit", "Beneficio"),
    "scope-item": t("Scope\\nitem", "Elemento\\nalcance"),
    "deliverable": t("Deliverable", "Entregable"),
    "milestone": t("Milestone", "Hito"),
    "interdependency": t("Interdependency", "Interdependencia"),
    "cost-plan": t("Cost\\nplan", "Plan de\\ncostes"),
    "cost-item": t("Cost", "Coste"),
    "need": t("Need", "Necesidad"),
    "feature": t("Feature", "Funcionalidad"),
    "resource-requirement": t("Resource", "Recurso"),
    "role-assignment": t("Role\\nassignment", "Asignación\\nde rol"),
}

CATEGORIES = {
    "document": t("Document", "Documento"),
    "organisation": t("Organisation", "Organización"),
    "rationale": t("Rationale", "Justificación"),
    "solution": t("Solution", "Solución"),
    "planning": t("Planning", "Planificación"),
    "conditions": t("Conditions", "Condiciones"),
    "references": t("References", "Referencias"),
}

# Toolbar tabs (category folders) and their archetypes, in order. The archetypes of
# basic are copied into this profile; the PM2 ones are generated (ARCHETYPES below).
# Second-level archetypes (approval, revision) have no button but must be listed.
TABS = {
    "00_document": ["section", "appendix", "paragraph", "comment", "local-figure",
                    "remote-figure", "symbolic-link", "document-control", "approval", "revision"],
    "01_organisation": ["organization", "stakeholder", "business-process", "role-assignment",
                        "meeting", "initiation-request"],
    "02_rationale": ["business-situation", "strategic-goal", "legal-basis", "outcome",
                     "impact", "benefit"],
    "03_solution": ["alternative", "scope-item", "need", "feature", "deliverable"],
    "04_planning": ["milestone", "resource-requirement", "cost-plan", "cost-item"],
    "05_conditions": ["success-criterion", "assumption", "constraint", "risk",
                      "interdependency"],
    "06_references": ["glossary-item", "bibliography-item", "traceability-matrix"],
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
    "xslt.cost_total": t("Total", "Total"),
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
    item(t("SIT-", "SIT-"), t("Business situation", "Situación de negocio"),
         t("Currently, _[current situation]_, which causes _[consequence for the business]_.",
           "Actualmente, _[situación actual]_, lo que provoca _[consecuencia para el negocio]_.")) +
    [enum("kind", "situation-kind"), md("urgency")])

archetype("strategic-goal", "02_rationale", "traceable-object strategic-goal",
    item(t("GOAL-", "OBJ-"), t("Strategic goal", "Objetivo estratégico"),
         t("_[Strategic goal of the organisation the project contributes to]_.",
           "_[Objetivo estratégico de la organización al que contribuye el proyecto]_.")) +
    [trace("owner", "organization", "detail", max_=1)])

archetype("legal-basis", "02_rationale", "traceable-object legal-basis",
    item(t("LEG-", "LEG-"), t("Legal basis", "Base legal"),
         t("_[Act, directive or agreement]_ establishes that _[obligation or mandate]_.",
           "_[Norma, directriz o acuerdo]_ establece que _[obligación o mandato]_.")) +
    [enum("kind", "legal-kind"), url("reference"),
     trace("supports", "strategic-goal")])

archetype("outcome", "02_rationale", "traceable-object outcome",
    item(t("OUT-", "RESU-"), t("Outcome", "Resultado"),
         t("After the project, _[desired future state]_.",
           "Tras el proyecto, _[situación futura deseada]_.")) +
    [trace("addresses", "business-situation"), trace("contributes-to", "strategic-goal")])

archetype("impact", "02_rationale", "traceable-object impact",
    item(t("IMP-", "IMP-"), t("Impact", "Impacto"),
         t("_[The current situation / the solution]_ affects _[processes, people or stakeholders]_ because _[reason]_.",
           "_[La situación actual / la solución]_ afecta a _[procesos, personas o partes interesadas]_ porque _[motivo]_.")) +
    [enum("perspective", "perspective"), enum("area", "impact-area"),
     enum("source", "impact-source"), enum("severity", "severity"),
     trace("affects", "stakeholder organization"), trace("affected-processes", "business-process")])

archetype("benefit", "02_rationale", "traceable-object benefit",
    item(t("BEN-", "BEN-"), t("Benefit", "Beneficio"),
         t("_[Measurable improvement]_ for _[beneficiary]_.",
           "_[Mejora medible]_ para _[beneficiario]_.")) +
    [string("indicator"), string("baseline"), string("target"),
     trace("derives-from", "outcome"), trace("perceived-by", "stakeholder organization")])

archetype("success-criterion", "05_conditions", "traceable-object success-criterion",
    item(t("SUCC-", "CEXI-"), t("Success criterion", "Criterio de éxito"),
         t("The project will be considered a success if _[measurable criterion]_.",
           "El proyecto se considerará un éxito si _[criterio medible]_.")) +
    [enum("dimension", "dimension"), string("target"),
     boolean("critical", tooltip="critical"), enum("applies-to", "applies-to"),
     trace("evaluates", "outcome")])

archetype("assumption", "05_conditions", "traceable-object assumption",
    item(t("ASM-", "SUP-"), t("Assumption", "Supuesto"),
         t("It is assumed that _[fact taken as true]_.",
           "Se asume que _[hecho que se da por cierto]_.")) +
    [enum("area", "assumption-area"), enum("validation", "validation", tooltip="validation"),
     trace("may-become", "risk")])

archetype("constraint", "05_conditions", "traceable-object constraint",
    item(t("CON-", "REST-"), t("Constraint", "Restricción"),
         t("The project must _[limit on schedule, budget, resources, products or compliance]_.",
           "El proyecto debe _[límite de plazo, presupuesto, recursos, productos o cumplimiento]_.")) +
    [enum("area", "constraint-area")])

archetype("risk", "05_conditions", "traceable-object risk",
    item(t("RISK-", "RIES-"), t("Risk", "Riesgo"),
         t("Because of _[condition]_, it might be that _[event]_, which will lead to _[impact]_.",
           "Debido a _[condición]_, podría ocurrir que _[evento]_, lo que provocaría _[impacto]_."),
         tooltip="risk-pattern") +
    [enum("category", "risk-category"), enum("status", "risk-status"),
     trace("identified-by", "stakeholder", "detail", max_=1),
     enum("likelihood", "level"), enum("impact", "level"),
     trace("risk-owner", "stakeholder", "detail", max_=1),
     enum("response-strategy", "response-strategy"), md("actions"), boolean("escalation"),
     trace("related", "assumption constraint")])

archetype("interdependency", "05_conditions", "traceable-object interdependency",
    item(t("DEP-", "DEP-"), t("Interdependency", "Interdependencia"),
         t("_[The situation / the solution]_ _[is related to / depends on / can reuse]_ _[other need, initiative, system or service]_.",
           "_[La situación / la solución]_ _[está relacionada con / depende de / puede reutilizar]_ _[otra necesidad, iniciativa, sistema o servicio]_.")) +
    [enum("kind", "dependency-kind"), enum("scope", "dependency-scope"),
     trace("related", "business-situation alternative deliverable")])

# --- Business Case: organisation and solution ---------------------------------

archetype("business-process", "01_organisation", "traceable-object business-process",
    item(t("PROC-", "PROC-"), t("Business process", "Proceso de negocio"),
         t("_[What the process does and who takes part in it]_.",
           "_[Qué hace el proceso y quién interviene en él]_.")) +
    [enum("process-category", "process-category"), string("domain"), string("sub-domain"),
     string("macro-process"), trace("owner", "organization stakeholder", "detail", max_=1)])

archetype("alternative", "03_solution", "traceable-object alternative",
    item(t("ALT-", "ALT-"), t("Alternative", "Alternativa"),
         t("_[What the alternative consists of]_.",
           "_[En qué consiste la alternativa]_.")) +
    [enum("kind", "alternative-kind"),
     md("strengths", "", "swot"), md("weaknesses", "", "swot"),
     md("opportunities", "", "swot"), md("threats", "", "swot"),
     md("assessment"), boolean("chosen", tooltip="chosen"), md("selection-rationale"),
     trace("addresses", "business-situation")])

archetype("scope-item", "03_solution", "traceable-object scope-item",
    item(t("SCP-", "ALC-"), t("Scope item", "Elemento de alcance"),
         t("The project _[includes / excludes]_ _[output, process, organisation or location]_.",
           "El proyecto _[incluye / excluye]_ _[producto, proceso, organización o ubicación]_.")) +
    [enum("inclusion", "inclusion"), enum("kind", "scope-kind"),
     trace("realises", "alternative")])

archetype("deliverable", "03_solution", "traceable-object deliverable",
    item(t("DLV-", "ENTR-"), t("Deliverable", "Entregable"),
         t("_[Deliverable]_, which _[purpose]_.",
           "_[Entregable]_, que _[finalidad]_.")) +
    [enum("kind", "deliverable-kind"),
     trace("within", "scope-item"), trace("contributes-to", "outcome")],
    # a deliverable may be composed of sub-deliverables
    children="deliverable", parents=":Proteus-document section deliverable")

archetype("need", "03_solution", "traceable-object need",
    item(t("NEED-", "NEC-"), t("Need", "Necesidad"),
         t("_[Stakeholder or user group]_ needs _[need]_ in order to _[reason]_.",
           "_[Parte interesada o grupo de usuarios]_ necesita _[necesidad]_ para _[motivo]_.")) +
    [enum("priority", "need-priority", tooltip="need-priority"), md("desired-solution"),
     md("justification"), md("current-handling"),
     trace("stakeholders", "stakeholder organization"), trace("addresses", "business-situation")])

archetype("feature", "03_solution", "traceable-object feature",
    item(t("FEAT-", "FUN-"), t("Feature", "Funcionalidad"),
         t("_[The output]_ shall allow _[capability]_ so that _[benefit for the users]_.",
           "_[El producto]_ permitirá _[capacidad]_ para que _[beneficio para los usuarios]_."),
         tooltip="feature") +
    [trace("satisfies", "need"), trace("delivered-in", "deliverable")])

archetype("milestone", "04_planning", "traceable-object milestone",
    item(t("MILE-", "HITO-"), t("Milestone", "Hito"),
         t("_[Event that marks the milestone]_.",
           "_[Acontecimiento que marca el hito]_.")) +
    [enum("kind", "milestone-kind"), enum("phase", "phase"), date("planned-date", "detail"),
     trace("delivers", "deliverable")])

archetype("cost-plan", "04_planning", "cost-plan",
    [name(t("Costs, effort and funding source", "Costes, esfuerzo y fuente de financiación")),
     integer("first-year", DATE[:4], tooltip="first-year"), md("funding-source"),
     md("previous-investments")],
    children="cost-item")

archetype("cost-item", "04_planning", "cost-item",
    [name(t("Cost", "Coste")),
     enum("group", "cost-group", "general"), enum("category", "cost-category", "general"),
     enum("nature", "cost-nature", "general", tooltip="cost-nature"),
     string("budget-line", "", "general")] +
    [number(f"year-{i}", "0", "costs") for i in range(1, 6)],
    parents="cost-plan")

archetype("resource-requirement", "04_planning", "traceable-object resource-requirement",
    item(t("RSRC-", "RECU-"), t("Resource", "Recurso"),
         t("The project requires _[resource]_ for _[purpose]_.",
           "El proyecto requiere _[recurso]_ para _[finalidad]_.")) +
    [enum("kind", "resource-kind"), string("quantity"), md("skills"),
     enum("phase", "phase"), md("acquisition"),
     trace("provided-by", "organization", "detail", max_=1),
     trace("responsible", "stakeholder", "detail", max_=1)])

# --- Project Charter: governance and stakeholders ---------------------------

archetype("role-assignment", "01_organisation", "traceable-object role-assignment",
    [code(t("ROLE-", "ROL-"))] + header(t("Role assignment", "Asignación de rol")) +
    [enum("pm2-role", "pm2-role", "detail"),
     trace("assignee", "stakeholder organization", "detail"),
     md("responsibilities"), md("deviations")])

# The stakeholder of basic, generated here to add the profile and the
# perceived problems that the Project Charter asks for
archetype("stakeholder", "01_organisation", "traceable-object stakeholder",
    header(t("Surname, Name", "Apellidos, Nombre")) +
    [string("role"), enum("category", "stakeholder-category"),
     string("phone-number"), string("email"),
     trace("works-for", "organization", "detail", ":Proteus-works-for"),
     ("file", "photo", "detail", {"tooltip": "file-info"}, "stakeholder_photo.png"),
     md("profile"), md("perceived-problems", tooltip="perceived-problems")])

archetype("document-control", "00_document", "document-control",
    [name(t("Document control", "Control del documento"))],
    children="approval revision")

archetype("approval", "00_document", "approval",
    [name(t("Approval", "Aprobación")), date(),
     trace("approver", "stakeholder", "general", max_=1),
     enum("action", "approval-action", "general")],
    parents="document-control")

archetype("revision", "00_document", "revision",
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

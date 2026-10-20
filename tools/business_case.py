# Business Case document of the project archetypes of the PM2 profile.
from model import t, DATE
from guidance import guidance as guidance_text, GUIDANCE_NAME

# ---------------------------------------------------------------------------
# Structure of the Business Case: (key, title, guidance, subsections).
# The guidance is shown as a comment in the empty project.
# ---------------------------------------------------------------------------

BC_SECTIONS = [
    ("request", t("Project Initiation Request information", "Información de la solicitud de inicio"),
     t("Link to the **project initiation request** of the Project Initiation Request (a symbolic "
       "link shows it here without copying it).",
       "Enlace a la **solicitud de inicio** de la Solicitud de inicio del proyecto (un enlace "
       "simbólico la muestra aquí sin copiarla)."), []),
    ("context", t("Context", "Contexto"), None, [
        ("situation", t("Current situation description and urgency", "Descripción de la situación actual y urgencia"),
         t("Detail the **business situations** described in the Project Initiation Request (link them) and "
           "add the considerations on the **urgency** of addressing them.",
           "Detalle las **situaciones de negocio** descritas en la solicitud de inicio (enlácelas) y añada "
           "las consideraciones sobre la **urgencia** de abordarlas."), []),
        ("current-impact", t("Current situation impact", "Impacto de la situación actual"), None, [
            ("impact-processes", t("Current impact on processes and the organisation", "Impacto actual en los procesos y la organización"),
             t("Describe the **impact** of the current situation on the strategy, the **business processes** "
               "(trace the affected processes and rate the impact on their owners and users), the people "
               "and the IT landscape of the organisation.",
               "Describa el **impacto** de la situación actual en la estrategia, los **procesos de negocio** "
               "(trace los procesos afectados y valore el impacto en sus responsables y usuarios), las personas "
               "y el panorama TI de la organización."), []),
            ("impact-stakeholders", t("Impact on stakeholders and users", "Impacto en las partes interesadas y los usuarios"),
             t("Describe the **impact** of the current situation on the stakeholders and users. If the project "
               "includes an information system, describe the current working environment of the users from a "
               "non-technical point of view.",
               "Describa el **impacto** de la situación actual en las partes interesadas y los usuarios. Si el "
               "proyecto incluye un sistema de información, describa el entorno de trabajo actual de los usuarios "
               "desde un punto de vista no técnico."), []),
        ]),
        ("interrelations", t("Interrelations and interdependencies", "Interrelaciones e interdependencias"),
         t("Describe the **interrelations and interdependencies** of the current situation with other "
           "problems, opportunities or needs, inside and outside the organisation.",
           "Describa las **interrelaciones e interdependencias** de la situación actual con otros problemas, "
           "oportunidades o necesidades, dentro y fuera de la organización."), []),
    ]),
    ("outcomes", t("Expected outcomes", "Resultados esperados"),
     t("Explain the desired **outcomes** from the business point of view. Start from the outcomes of the "
       "Project Initiation Request (link them).",
       "Explique los **resultados** deseados desde el punto de vista del negocio. Parta de los resultados de "
       "la solicitud de inicio (enlácelos)."), []),
    ("alternatives", t("Possible alternatives", "Alternativas posibles"),
     t("Describe at least two **alternatives**, the first one always *do nothing*, with a SWOT analysis and "
       "a qualitative assessment. Mark the chosen one and give the reasons for the choice.",
       "Describa al menos dos **alternativas**, la primera siempre *no hacer nada*, con un análisis DAFO y una "
       "valoración cualitativa. Marque la elegida y dé los motivos de la elección."), []),
    ("solution", t("Solution description", "Descripción de la solución"),
     t("Elaborate on the chosen alternative.", "Desarrolle la alternativa elegida."), [
        ("legal", t("Legal basis", "Base legal"),
         t("Legal basis and **strategic goals** of the solution (link those of the Project Initiation Request).",
           "Base legal y **objetivos estratégicos** de la solución (enlace los de la solicitud de inicio)."), []),
        ("benefits", t("Benefits", "Beneficios"),
         t("Describe the **benefits**: the measurable improvements resulting from the outcomes, as perceived "
           "by the stakeholders.",
           "Describa los **beneficios**: las mejoras medibles que se derivan de los resultados, tal como las "
           "perciben las partes interesadas."), []),
        ("success", t("Success criteria", "Criterios de éxito"),
         t("Measurable **success criteria** of the project. Mark the critical ones and distinguish project "
           "criteria from product criteria. A criterion of the Project Initiation Request can be linked or "
           "refined (trace *refines*).",
           "**Criterios de éxito** medibles del proyecto. Marque los críticos y distinga los del proyecto de "
           "los del producto. Un criterio de la solicitud de inicio puede enlazarse o refinarse (traza *refina*)."), []),
        ("scope", t("Scope", "Alcance"),
         t("**Scope items** that set the boundaries of the project: outputs, processes, organisations or "
           "locations included in and excluded from it.",
           "**Elementos de alcance** que fijan los límites del proyecto: productos, procesos, organizaciones o "
           "ubicaciones que incluye y que excluye."), []),
        ("solution-impact", t("Solution impact", "Impacto de la solución"),
         t("How the solution addresses the **impact** on each affected business process (impacts caused by the "
           "solution, traced to the processes).",
           "Cómo aborda la solución el **impacto** en cada proceso de negocio afectado (impactos causados por la "
           "solución, trazados a los procesos)."), []),
        ("deliverables", t("Deliverables", "Entregables"),
         t("Most important **deliverables**: a process, an information system, a policy, a service, staff "
           "trained...",
           "**Entregables** más importantes: un proceso, un sistema de información, una normativa, un servicio, "
           "personal formado..."), []),
        ("assumptions", t("Assumptions", "Supuestos"),
         t("Key **assumptions** of the solution (link or refine those of the Project Initiation Request).",
           "**Supuestos** clave de la solución (enlace o refine los de la solicitud de inicio)."), []),
        ("constraints", t("Constraints", "Restricciones"),
         t("Key **constraints** of the solution (link or refine those of the Project Initiation Request).",
           "**Restricciones** clave de la solución (enlace o refine las de la solicitud de inicio)."), []),
        ("risks", t("Risks", "Riesgos"),
         t("Key **risks** of the solution, with a high level response strategy if there is one.",
           "**Riesgos** clave de la solución, con una estrategia de respuesta de alto nivel si la hay."), []),
        ("costs", t("Costs, effort and funding source", "Costes, esfuerzo y fuente de financiación"),
         t("Total cost of ownership for at least 5 years: add a **cost** to the cost plan for each concept, "
           "with staff costs in FTE and other costs in k€, and state the funding source.",
           "Coste total de propiedad durante al menos 5 años: añada un **coste** al plan de costes por cada "
           "concepto, con los de personal en ETC y el resto en k€, e indique la fuente de financiación."), []),
        ("roadmap", t("Roadmap", "Hoja de ruta"),
         t("Expected start and delivery dates and the major **milestones** of the project.",
           "Fechas previstas de inicio y de entrega y los principales **hitos** del proyecto."), []),
        ("synergies", t("Synergies and interdependencies", "Sinergias e interdependencias"),
         t("**Synergies and interdependencies** of the solution with other initiatives, and the IT services "
           "or components reused, requested or made reusable.",
           "**Sinergias e interdependencias** de la solución con otras iniciativas, y los servicios o "
           "componentes TI que se reutilizan, se solicitan o se harán reutilizables."), []),
    ]),
    ("governance", t("Governance", "Gobierno"), None, [
        ("po", t("Project Owner (PO)", "Propietario del proyecto (PO)"),
         t("Person nominated by the organisation that funds the project and is its main beneficiary (link it).",
           "Persona nombrada por la organización que financia el proyecto y es su principal beneficiaria (enlácela)."), []),
        ("sp", t("Solution Provider (SP)", "Proveedor de la solución (SP)"),
         t("Person nominated by the organisation that executes the project and is accountable for its "
           "deliverables (link it).",
           "Persona nombrada por la organización que ejecuta el proyecto y responde de sus entregables (enlácela)."), []),
        ("authority", t("Approving authority", "Autoridad aprobadora"),
         t("Decision maker according to the governance structure of the organisation (link it). Its "
           "approval is recorded in the document control.",
           "Responsable de la decisión según la estructura de gobierno de la organización (enlácelo). Su "
           "aprobación se registra en el control del documento."), []),
    ]),
]

REFERENCES = ("references", t("References and related documents", "Referencias y documentos relacionados"),
              t("Reference the relevant documents with their title, version, date and source or location.",
                "Referencie los documentos relevantes con su título, versión, fecha y fuente o ubicación."))

BC_ACRONYM = t("BC", "CN")
BC_NAME = t("Business Case", "Caso de negocio")
BC_DESCRIPTION = t("Justification of the project: alternatives, chosen solution, benefits and costs "
                   "(PM² artefact of the initiating phase).",
                   "Justificación del proyecto: alternativas, solución elegida, beneficios y costes "
                   "(artefacto PM² de la fase de inicio).")

PROCESSES_SECTION = ("processes", t("Business processes", "Procesos de negocio"),
                     t("Business processes affected by the current situation or by the solution, with "
                       "their category, domain and owner.",
                       "Procesos de negocio afectados por la situación actual o por la solución, con su "
                       "categoría, dominio y responsable."), ["business-process"])


# Objects to use in each section (shown in its guidance comment)
OBJECTS = {
    "request": ["symbolic-link"],
    "situation": ["symbolic-link", "business-situation"],
    "impact-processes": ["impact", "business-process"],
    "impact-stakeholders": ["symbolic-link", "impact"],
    "interrelations": ["interdependency"],
    "outcomes": ["symbolic-link", "outcome"],
    "alternatives": ["alternative"],
    "legal": ["symbolic-link", "legal-basis", "strategic-goal"],
    "benefits": ["benefit"],
    "success": ["symbolic-link", "success-criterion"],
    "scope": ["scope-item"],
    "solution-impact": ["symbolic-link", "impact"],
    "deliverables": ["deliverable"],
    "assumptions": ["symbolic-link", "assumption"],
    "constraints": ["symbolic-link", "constraint"],
    "risks": ["symbolic-link", "risk"],
    "costs": ["cost-plan", "cost-item"],
    "roadmap": ["milestone"],
    "synergies": ["interdependency"],
    "po": ["symbolic-link"], "sp": ["symbolic-link"], "authority": ["symbolic-link"],
    "references": ["bibliography-item"],
    "processes": ["business-process"],
}

# Guidance of the sections that only group subsections
CONTAINER_HELP = {
    "context": t("Current situation that the project addresses: its description and urgency, its impact "
                 "and its relations with other situations. Each subsection says what it contains.",
                 "Situación actual que aborda el proyecto: su descripción y urgencia, su impacto y sus "
                 "relaciones con otras situaciones. Cada subsección indica lo que contiene."),
    "current-impact": t("Impact of the current situation, on the organisation and on the stakeholders.",
                        "Impacto de la situación actual, en la organización y en las partes interesadas."),
    "governance": t("Main roles of the governance of the project, as defined in the PM² roles and "
                    "responsibilities. Each subsection links to the person or body that plays the role.",
                    "Principales roles del gobierno del proyecto, según los roles y responsabilidades de "
                    "PM². Cada subsección enlaza a la persona u órgano que desempeña el rol."),
}


def tree(p, prefix, specs, items, guidance, objects=None, container_help=None):
    """Sections (and subsections) of a document, with their guidance and items.
    objects and container_help default to those of the Business Case."""
    objects = OBJECTS if objects is None else objects
    container_help = CONTAINER_HELP if container_help is None else container_help
    ids = []
    for key, title, help_, subs in specs:
        kids = []
        if guidance:
            kids.append(p.add("comment", f"{prefix}-{key}-help",
                              {":Proteus-name": GUIDANCE_NAME,
                               "text": guidance_text(help_ or container_help[key], objects.get(key))}))
        kids += items.get(key, [])
        kids += tree(p, prefix, subs, items, guidance, objects, container_help)
        ids.append(p.add("section", f"{prefix}-{key}", {":Proteus-name": title}, kids))
    return ids


def link(p, target, prefix="bc"):
    """Symbolic link to an object of another document."""
    return p.add("symbolic-link", f"{prefix}-link-{target}", {"link": [target]})


def references(p, items, guidance, prefix="bc", spec=None, objects=None):
    key, title, help_ = REFERENCES if spec is None else spec
    objects = OBJECTS if objects is None else objects
    kids = []
    if guidance:
        kids.append(p.add("comment", f"{prefix}-{key}-help",
                          {":Proteus-name": GUIDANCE_NAME, "text": guidance_text(help_, objects[key])}))
    return p.add("appendix", f"{prefix}-{key}", {":Proteus-name": title}, kids + items)


def empty(p, lang, document_values):
    """Business Case of the empty project, with the guidance of every section."""
    approval = p.add("approval", "bc-approval-1")
    revision = p.add("revision", "bc-revision-1")
    control = p.add("document-control", "bc-control", {}, [approval, revision])
    costs = p.add("cost-plan", "bc-cost-plan")
    secs = tree(p, "bc", BC_SECTIONS, {"request": [link(p, "pir-request")], "costs": [costs]}, True)
    p.document("bc", document_values(lang, {"_args": (BC_ACRONYM, BC_NAME, BC_DESCRIPTION)}),
               [control] + secs + [references(p, [], True)])


def sample(p, lang, document_values, ids):
    """Business Case of the sample project. ids: objects of the other documents."""
    def item(arch, id_, num, name_, desc, **values):
        v = {":Proteus-code": num, ":Proteus-name": name_, "description": desc}
        v.update({k.replace("_", "-"): x for k, x in values.items()})
        return p.add(arch, id_, v)

    # --- business processes (in the stakeholders document) ---------------------------
    bp1 = item("business-process", "bp-1", "001", t("Final project management", "Gestión de trabajos fin de estudios"),
               t("Proposal, assignment, supervision, filing and defence of the final degree and master projects, "
                 "with students, supervisors, committees and the secretariat.",
                 "Propuesta, asignación, tutela, depósito y defensa de los trabajos fin de grado y fin de máster, "
                 "con estudiantes, tutores, comisiones y secretaría."),
               process_category="document-management", domain=t("Academic management", "Gestión académica"),
               sub_domain=t("Final projects", "Trabajos fin de estudios"),
               macro_process=t("Academic organisation", "Ordenación académica"), owner=[ids["school"]])
    bp2 = item("business-process", "bp-2", "002", t("Registry and filing", "Registro y archivo"),
               t("Registration and filing of the documents of the administrative procedures of the university.",
                 "Registro y archivo de los documentos de los procedimientos administrativos de la universidad."),
               process_category="document-management", domain=t("Administration", "Administración"),
               sub_domain=t("Electronic administration", "Administración electrónica"),
               macro_process=t("Document management", "Gestión documental"), owner=[ids["us"]])
    bp3 = item("business-process", "bp-3", "003", t("Grading", "Calificación"),
               t("Grading of the final projects by the committees and recording of the marks in the transcripts.",
                 "Calificación de los trabajos por las comisiones y registro de las notas en las actas."),
               process_category="coordination", domain=t("Academic management", "Gestión académica"),
               sub_domain=t("Assessment", "Evaluación"), macro_process=t("Academic organisation", "Ordenación académica"),
               owner=[ids["school"]])

    # --- context ---------------------------------------------------------------------
    imp4 = item("impact", "imp-4", "004", t("Manual final project management", "Gestión manual de los trabajos"),
                t("The current situation affects the final project management because every step is done by "
                  "e-mail and spreadsheets, so documents get lost and deadlines are missed.",
                  "La situación actual afecta a la gestión de los trabajos porque cada paso se hace por correo y "
                  "hojas de cálculo, por lo que se pierden documentos y se incumplen plazos."),
                perspective="internal", area="processes", source="current-situation", severity="significant",
                affects=[ids["school"]], affected_processes=[bp1, bp2])
    imp5 = item("impact", "imp-5", "005", t("Systems in use", "Sistemas en uso"),
                t("The current situation affects the IT landscape because students and supervisors use e-mail, "
                  "the virtual campus and shared folders, which are not integrated with the registry.",
                  "La situación actual afecta al panorama TI porque estudiantes y tutores usan el correo, el "
                  "campus virtual y carpetas compartidas, que no están integrados con el registro."),
                perspective="internal", area="it-landscape", source="current-situation", severity="moderate",
                affected_processes=[bp1, bp2])
    imp6 = item("impact", "imp-6", "006", t("Electronic final project management", "Gestión electrónica de los trabajos"),
                t("The solution affects the final project management because the whole procedure is processed in "
                  "a single system integrated with the registry and the transcripts.",
                  "La solución afecta a la gestión de los trabajos porque todo el procedimiento se tramita en un "
                  "único sistema integrado con el registro y las actas."),
                perspective="internal", area="processes", source="solution", severity="moderate",
                affects=[ids["school"]], affected_processes=[bp1, bp2, bp3])
    dep1 = item("interdependency", "dep-1", "001", t("Academic calendar", "Calendario académico"),
                t("The situation is related to the academic calendar of the school: final project calls must be "
                  "coordinated with the closing of the transcripts.",
                  "La situación está relacionada con el calendario académico de la escuela: las convocatorias deben "
                  "coordinarse con el cierre de las actas."),
                kind="interrelation", scope="internal", related=[ids["sit-1"]])

    # --- alternatives --------------------------------------------------------------------
    alt1 = item("alternative", "alt-1", "001", t("Do nothing", "No hacer nada"),
                t("Keep managing the final projects by e-mail and spreadsheets.",
                  "Seguir gestionando los trabajos por correo y hojas de cálculo."),
                kind="do-nothing",
                strengths=t("- No cost.\n- No change for the users.", "- Sin coste.\n- Sin cambios para los usuarios."),
                weaknesses=t("- Errors and delays remain.\n- High workload of the secretariat.",
                             "- Se mantienen los errores y retrasos.\n- Alta carga de trabajo en secretaría."),
                opportunities=t("- None.", "- Ninguna."),
                threats=t("- Non-compliance with the electronic processing obligation.",
                          "- Incumplimiento de la obligación de tramitación electrónica."),
                assessment=t("Not viable: it does not comply with the legal basis.",
                             "No viable: no cumple la base legal."),
                addresses=[ids["sit-1"]])
    alt2 = item("alternative", "alt-2", "002", t("Commercial product", "Producto comercial"),
                t("License and customise a commercial final project management product.",
                  "Licenciar y adaptar un producto comercial de gestión de trabajos fin de estudios."),
                kind="sophisticated",
                strengths=t("- Proven functionality.\n- Vendor support.", "- Funcionalidad probada.\n- Soporte del fabricante."),
                weaknesses=t("- Yearly licences.\n- Costly integration with the registry and the transcripts.",
                             "- Licencias anuales.\n- Integración costosa con el registro y las actas."),
                opportunities=t("- Fast start.", "- Puesta en marcha rápida."),
                threats=t("- Dependency on the vendor.\n- Regulations of the university not supported.",
                          "- Dependencia del fabricante.\n- Normativa de la universidad no contemplada."),
                assessment=t("Viable but expensive, and the integration risk is high.",
                             "Viable pero cara, y con alto riesgo de integración."),
                addresses=[ids["sit-1"], ids["sit-2"]])
    alt3 = item("alternative", "alt-3", "003", t("In-house development on the corporate platform",
                                                  "Desarrollo propio sobre la plataforma corporativa"),
                t("Develop the system with the IT services, reusing the corporate e-administration services.",
                  "Desarrollar el sistema con el SIC, reutilizando los servicios corporativos de administración electrónica."),
                kind="simple",
                strengths=t("- Reuses single sign-on, electronic signature and registry.\n- No licences.",
                            "- Reutiliza la identificación única, la firma electrónica y el registro.\n- Sin licencias."),
                weaknesses=t("- Depends on the availability of the IT staff.", "- Depende de la disponibilidad del personal del SIC."),
                opportunities=t("- Other schools may reuse it.", "- Otras escuelas pueden reutilizarlo."),
                threats=t("- Changes of the regulations during the development.",
                          "- Cambios de la normativa durante el desarrollo."),
                assessment=t("Viable, with the lowest total cost of ownership.",
                             "Viable, con el menor coste total de propiedad."),
                chosen="true",
                selection_rationale=t("It complies with the legal basis, reuses the corporate services and has "
                                      "the lowest cost in 5 years; its main risk (staff availability) is managed.",
                                      "Cumple la base legal, reutiliza los servicios corporativos y tiene el menor "
                                      "coste a 5 años; su principal riesgo (la disponibilidad del personal) se gestiona."),
                addresses=[ids["sit-1"], ids["sit-2"], ids["sit-3"]])

    # --- solution ------------------------------------------------------------------------
    ben1 = item("benefit", "ben-1", "001", t("Faster procedure", "Tramitación más rápida"),
                t("Shorter time from the proposal to the assignment of the final project for students.",
                  "Menor tiempo desde la propuesta hasta la asignación del trabajo para los estudiantes."),
                indicator=t("Days from the proposal to the assignment", "Días desde la propuesta hasta la asignación"),
                baseline="45", target="15", derives_from=[ids["out-1"]], perceived_by=[ids["school"]])
    ben2 = item("benefit", "ben-2", "002", t("Less secretariat work", "Menos trabajo de secretaría"),
                t("Fewer hours of the secretariat devoted to final projects.",
                  "Menos horas de secretaría dedicadas a los trabajos fin de estudios."),
                indicator=t("Hours per month", "Horas al mes"), baseline="120", target="40",
                derives_from=[ids["out-3"]], perceived_by=[ids["secretary"]])
    ben3 = item("benefit", "ben-3", "003", t("Fewer status enquiries", "Menos consultas sobre el estado"),
                t("Fewer e-mails of students and supervisors asking about the status of their final projects.",
                  "Menos correos de estudiantes y tutores preguntando por el estado de sus trabajos."),
                indicator=t("Enquiries per academic year", "Consultas por curso"), baseline="300", target="50",
                derives_from=[ids["out-2"]])
    sc5 = item("success-criterion", "sc-5", "005", t("First call fully electronic", "Primera convocatoria totalmente electrónica"),
               t("The project will be considered a success if the first call of the 2027-28 academic year is "
                 "managed entirely in the system, from the proposals to the grading.",
                 "El proyecto se considerará un éxito si la primera convocatoria del curso 2027-28 se gestiona "
                 "por completo en el sistema, desde las propuestas hasta la calificación."),
               dimension="scope", target="100 %", critical="true", applies_to="project",
               evaluates=[ids["out-1"]], refines=[ids["sc-2"]])
    sc6 = item("success-criterion", "sc-6", "006", t("Response time", "Tiempo de respuesta"),
               t("The project will be considered a success if the system answers in less than 2 seconds in the "
                 "busiest week of the call.",
                 "El proyecto se considerará un éxito si el sistema responde en menos de 2 segundos en la semana "
                 "de más carga de la convocatoria."),
               dimension="quality", target="< 2 s", applies_to="product")
    scp1 = item("scope-item", "scp-1", "001", t("Final project application", "Aplicación de trabajos fin de estudios"),
                t("The project includes a web application for students, supervisors, committees and secretariat.",
                  "El proyecto incluye una aplicación web para estudiantes, tutores, comisiones y secretaría."),
                inclusion="in", kind="output", realises=[alt3])
    scp2 = item("scope-item", "scp-2", "002", t("Final project procedure", "Procedimiento de trabajos fin de estudios"),
                t("The project includes the redesign of the procedure: proposal, assignment, filing and defence.",
                  "El proyecto incluye el rediseño del procedimiento: propuesta, asignación, depósito y defensa."),
                inclusion="in", kind="process", realises=[alt3])
    scp3 = item("scope-item", "scp-3", "003", t("Pilot school", "Escuela piloto"),
                t("The project includes the School of Computer Engineering as the pilot school.",
                  "El proyecto incluye la ETSII como escuela piloto."),
                inclusion="in", kind="organisation")
    scp4 = item("scope-item", "scp-4", "004", t("Internships", "Prácticas en empresa"),
                t("The project excludes the management of internships, which has its own system.",
                  "El proyecto excluye la gestión de las prácticas en empresa, que tiene su propio sistema."),
                inclusion="out", kind="process")
    scp5 = item("scope-item", "scp-5", "005", t("Other schools", "Resto de centros"),
                t("The project excludes the other schools of the university, which may join in a later phase.",
                  "El proyecto excluye el resto de centros de la universidad, que podrán incorporarse más adelante."),
                inclusion="out", kind="organisation")
    dlv1 = item("deliverable", "dlv-1", "001", t("Final project management system", "Sistema de gestión de trabajos"),
                t("Web application integrated with the corporate services, which supports the whole procedure.",
                  "Aplicación web integrada con los servicios corporativos, que da soporte a todo el procedimiento."),
                kind="information-system", within=[scp1], contributes_to=[ids["out-1"], ids["out-2"]])
    dlv2 = item("deliverable", "dlv-2", "002", t("Redesigned procedure", "Procedimiento rediseñado"),
                t("Electronic procedure approved by the School Board, which replaces the current one.",
                  "Procedimiento electrónico aprobado por la Junta de Escuela, que sustituye al actual."),
                kind="process", within=[scp2], contributes_to=[ids["out-1"]])
    dlv3 = item("deliverable", "dlv-3", "003", t("Trained staff and supervisors", "Personal y tutores formados"),
                t("Training sessions for the secretariat staff and the supervisors.",
                  "Sesiones de formación para el personal de secretaría y los tutores."),
                kind="training", contributes_to=[ids["out-3"]])
    ms1 = item("milestone", "ms-1", "001", t("Project start", "Inicio del proyecto"),
               t("Kick-off meeting with the school and the IT services.", "Reunión de lanzamiento con la escuela y el SIC."),
               kind="start", phase="initiating", planned_date="2027-01-11")
    ms2 = item("milestone", "ms-2", "002", t("Procedure approved", "Procedimiento aprobado"),
               t("The School Board approves the redesigned procedure.", "La Junta de Escuela aprueba el procedimiento rediseñado."),
               phase="executing", planned_date="2027-04-30", delivers=[dlv2])
    ms3 = item("milestone", "ms-3", "003", t("Pilot version", "Versión piloto"),
               t("The pilot version is tested with a group of supervisors.", "La versión piloto se prueba con un grupo de tutores."),
               phase="executing", planned_date="2027-07-15")
    ms4 = item("milestone", "ms-4", "004", t("Go live", "Puesta en producción"),
               t("The system is in production for the first call of the 2027-28 academic year.",
                 "El sistema está en producción para la primera convocatoria del curso 2027-28."),
               kind="delivery", phase="executing", planned_date="2027-09-15", delivers=[dlv1, dlv3])
    rsk4 = item("risk", "rsk-4", "004", t("Integration with the signature service", "Integración con la firma electrónica"),
                t("Because of the planned upgrade of the electronic signature service, it might be that its "
                  "interface changes during the project, which will lead to delays in the integration.",
                  "Debido a la actualización prevista del servicio de firma electrónica, podría ocurrir que su "
                  "interfaz cambie durante el proyecto, lo que provocaría retrasos en la integración."),
                category="technical", status="assessing", likelihood="low", impact="medium",
                response_strategy="reduce",
                actions=t("Agree the interface version with the e-administration service before the development.",
                          "Acordar la versión de la interfaz con el servicio de administración electrónica antes del desarrollo."),
                related=[ids["asm-2"]])
    dep2 = item("interdependency", "dep-2", "002", t("Corporate e-administration services", "Servicios corporativos de administración electrónica"),
                t("The solution can reuse the single sign-on, the electronic signature and the registry of the university.",
                  "La solución puede reutilizar la identificación única, la firma electrónica y el registro de la universidad."),
                kind="it-reuse", scope="internal", related=[alt3, dlv1])
    dep3 = item("interdependency", "dep-3", "003", t("Other schools", "Otros centros"),
                t("The solution can be made reusable for the other schools of the university.",
                  "La solución puede hacerse reutilizable para el resto de centros de la universidad."),
                kind="it-sharing", scope="internal", related=[dlv1])

    staff_line = t("Chapter 1 (staff)", "Capítulo 1 (personal)")
    goods_line = t("Chapter 2 (goods and services)", "Capítulo 2 (bienes y servicios)")

    def cost(id_, name_, group, category, nature, *years):
        v = {":Proteus-name": name_, "group": group, "category": category, "nature": nature,
             "budget-line": staff_line if nature == "staff" else goods_line}
        v.update({f"year-{i + 1}": str(y) for i, y in enumerate(years)})
        return p.add("cost-item", id_, v)
    costs = [
        cost("cost-1", t("Development (IT staff)", "Desarrollo (personal del SIC)"), "solution-implementation",
             "development", "staff", 0.6, 0, 0, 0, 0),
        cost("cost-2", t("Maintenance (IT staff)", "Mantenimiento (personal del SIC)"), "solution-implementation",
             "maintenance", "staff", 0, 0.2, 0.2, 0.2, 0.2),
        cost("cost-3", t("User support", "Soporte a usuarios"), "solution-implementation",
             "support", "staff", 0.1, 0.1, 0.1, 0.1, 0.1),
        cost("cost-4", t("Servers and storage", "Servidores y almacenamiento"), "solution-implementation",
             "infrastructure", "other-costs", 2, 2, 2, 2, 2),
        cost("cost-5", t("Change management", "Gestión del cambio"), "business-implementation",
             "change-management", "staff", 0.1, 0, 0, 0, 0),
        cost("cost-6", t("Training sessions", "Sesiones de formación"), "business-implementation",
             "training", "other-costs", 1.5, 0.5, 0, 0, 0),
        cost("cost-7", t("Coordination (school)", "Coordinación (escuela)"), "business-implementation",
             "coordination", "staff", 0.05, 0.05, 0, 0, 0),
    ]
    plan = p.add("cost-plan", "bc-cost-plan", {
        "first-year": "2027",
        "previous-investments": t("None: it is the first project of the school in this area.",
                                  "Ninguna: es el primer proyecto de la escuela en este ámbito."),
        "funding-source": t("Staff of the IT services and of the school, funded by their ordinary budgets; other "
                            "costs funded by the digital transformation plan of the university.",
                            "Personal del SIC y de la escuela, con cargo a sus presupuestos ordinarios; el resto de "
                            "costes, con cargo al plan de transformación digital de la universidad.")}, costs)

    # --- references ----------------------------------------------------------------------
    ref1 = p.add("bibliography-item", "ref-1", {
        ":Proteus-name": t("Project Initiation Request, version 1.0", "Solicitud de inicio del proyecto, versión 1.0"),
        "publication_authors": "Herrera Campos, L.",
        "publication_details": t("Document management system of the school, " + DATE + ".",
                                 "Gestor documental de la escuela, " + DATE + ".")})
    ref2 = p.add("bibliography-item", "ref-2", {
        ":Proteus-name": t("PM² Project Management Methodology Guide 3.0", "Guía de la metodología PM² 3.0"),
        "publication_authors": "PM² Alliance",
        "publication_details": "<https://www.pm2alliance.eu/publications>"})

    # --- document --------------------------------------------------------------------------
    a1 = p.add("approval", "bc-approval-1", {":Proteus-name": t("Approval by the School Board", "Aprobación de la Junta de Escuela"),
                                              "approver": [ids["po"]], "action": "approve"})
    a2 = p.add("approval", "bc-approval-2", {":Proteus-name": t("Review by the SP", "Revisión del SP"),
                                              "approver": [ids["sp"]], "action": "review"})
    r1 = p.add("revision", "bc-revision-1", {":Proteus-name": t("First version", "Primera versión"),
                                              "revision": "1.0", "created-by": [ids["pm"]],
                                              "changes": t("First version of the Business Case.", "Primera versión del caso de negocio.")})
    control = p.add("document-control", "bc-control", {}, [a1, a2, r1])
    L = lambda *xs: [link(p, x) for x in xs]
    items = {
        "request": L("pir-request"),
        "situation": L("sit-1", "sit-2", "sit-3"),
        "impact-processes": [imp4, imp5],
        "impact-stakeholders": L("imp-3"),
        "interrelations": [dep1],
        "outcomes": L("out-1", "out-2", "out-3"),
        "alternatives": [alt1, alt2, alt3],
        "legal": L("lb-1", "lb-2", "sg-1"),
        "benefits": [ben1, ben2, ben3],
        "success": L("sc-1", "sc-3", "sc-4") + [sc5, sc6],
        "scope": [scp1, scp2, scp3, scp4, scp5],
        "solution-impact": [imp6] + L("imp-1", "imp-2"),
        "deliverables": [dlv1, dlv2, dlv3],
        "assumptions": L("asm-1", "asm-2", "asm-3"),
        "constraints": L("con-1", "con-2", "con-3"),
        "risks": L("rsk-1", "rsk-2", "rsk-3") + [rsk4],
        "costs": [plan],
        "roadmap": [ms1, ms2, ms3, ms4],
        "synergies": [dep2, dep3],
        "po": L(ids["po"]), "sp": L(ids["sp"]), "authority": L(ids["board"]),
    }
    secs = tree(p, "bc", BC_SECTIONS, items, True)
    p.document("bc", document_values(lang, {
        "_args": (BC_ACRONYM, BC_NAME, BC_DESCRIPTION), "version": "1.0", "sensitivity": "sensitive-basic",
        "document-author": [ids["pm"]], "project-manager": [ids["pm"]],
        "document-location": t("the document management system of the school", "el gestor documental de la escuela"),
        "prepared-for": [ids["us"]], "prepared-by": [ids["sic"]]}),
        [control] + secs + [references(p, [ref1, ref2], True)])
    return [bp1, bp2, bp3]

# Project Charter document of the project archetypes of the PM2 profile.
from model import t, DATE
from business_case import tree, link, references

# ---------------------------------------------------------------------------
# Structure of the Project Charter: (key, title, guidance, subsections)
# ---------------------------------------------------------------------------

PC_SECTIONS = [
    ("summary", t("Executive summary", "Resumen ejecutivo"),
     t("Executive summary of the project, in a few **paragraphs**. Write it last.",
       "Resumen ejecutivo del proyecto, en unos pocos **párrafos**. Escríbalo al final."), []),
    ("considerations", t("Considerations on the Business Case", "Consideraciones sobre el caso de negocio"),
     t("Considerations on the approved Business Case: elaborate on the impact and the **urgency** of the "
       "current situation if needed, and validate the external influences (interfaces, needs, regulations). "
       "Link the objects of the Business Case that are discussed.",
       "Consideraciones sobre el caso de negocio aprobado: desarrolle el impacto y la **urgencia** de la "
       "situación actual si hace falta, y valide las influencias externas (interfaces, necesidades, normativa). "
       "Enlace los objetos del caso de negocio que se comenten."), []),
    ("description", t("Project description", "Descripción del proyecto"), None, [
        ("scope", t("Scope", "Alcance"), None, [
            ("scope-in", t("Includes (IN scope)", "Incluye (dentro del alcance)"),
             t("What the project **will** deliver: the outputs that form the solution, and the organisational "
               "change activities needed to achieve the benefits (scope items *in*).",
               "Lo que el proyecto **sí** entregará: los productos que forman la solución y las actividades de "
               "cambio organizativo necesarias para lograr los beneficios (elementos de alcance *dentro*)."), []),
            ("scope-out", t("Excludes (OUT of scope)", "Excluye (fuera del alcance)"),
             t("What the project will **not** deliver, e.g. deliverables discussed but left out because of "
               "the constraints (scope items *out*).",
               "Lo que el proyecto **no** entregará, p. ej. entregables que se discutieron pero que quedan fuera "
               "por las restricciones (elementos de alcance *fuera*)."), []),
            ("scope-statement", t("Scope statement", "Declaración del alcance"),
             t("Overall scope statement of the project in one or two lines, understandable by the management "
               "and by outsiders.",
               "Declaración general del alcance del proyecto en una o dos líneas, comprensible para la "
               "dirección y para personas ajenas al proyecto."), []),
        ]),
        ("success", t("Success criteria", "Criterios de éxito"),
         t("Measurable **success criteria** of the project, marking the critical ones and distinguishing "
           "project from product criteria (link or refine those of the Business Case).",
           "**Criterios de éxito** medibles del proyecto, marcando los críticos y distinguiendo los del "
           "proyecto de los del producto (enlace o refine los del caso de negocio)."), []),
        ("needs", t("Stakeholder and user needs", "Necesidades de las partes interesadas y los usuarios"),
         t("Key **needs** of the stakeholders and users that the project shall address: who has the need, "
           "what it is, why it should be addressed, how it is addressed today and its priority.",
           "**Necesidades** clave de las partes interesadas y los usuarios que el proyecto debe abordar: quién "
           "la tiene, en qué consiste, por qué debe abordarse, cómo se aborda hoy y su prioridad."), []),
        ("deliverables", t("Deliverables", "Entregables"),
         t("**Deliverables** of the project, tangible or intangible, for the organisation of the Project Owner "
           "(not the project management artefacts). A deliverable may contain sub-deliverables.",
           "**Entregables** del proyecto, tangibles o intangibles, para la organización del propietario del "
           "proyecto (no los artefactos de gestión). Un entregable puede contener subentregables."), []),
        ("features", t("Features", "Funcionalidades"),
         t("High level **features** of the outputs: the capabilities the users need and why, not how they "
           "will be implemented. Trace each feature to the needs it satisfies and to its deliverables; a "
           "traceability matrix of needs and features can summarise them.",
           "**Funcionalidades** de alto nivel de los productos: las capacidades que necesitan los usuarios y "
           "por qué, no cómo se implementarán. Trace cada funcionalidad a las necesidades que satisface y a sus "
           "entregables; una matriz de trazabilidad de necesidades y funcionalidades puede resumirlas."), []),
        ("constraints", t("Constraints", "Restricciones"),
         t("Project **constraints**: people, schedule, budget, resources, products, technology, interfaces, "
           "decisions, compliance, security, data protection... (link or refine those of the Business Case).",
           "**Restricciones** del proyecto: personas, plazo, presupuesto, recursos, productos, tecnología, "
           "interfaces, decisiones, cumplimiento, seguridad, protección de datos... (enlace o refine las del "
           "caso de negocio)."), []),
        ("assumptions", t("Assumptions", "Supuestos"),
         t("Project **assumptions**, still to be validated (link or refine those of the Business Case).",
           "**Supuestos** del proyecto, pendientes de validar (enlace o refine los del caso de negocio)."), []),
        ("risks", t("Risks", "Riesgos"),
         t("Key **risks** identified at this stage, with their assessment and response strategy. The "
           "complete list is kept in the Risk Log.",
           "**Riesgos** clave identificados en esta fase, con su evaluación y estrategia de respuesta. La "
           "lista completa se mantiene en el registro de riesgos."), []),
    ]),
    ("cost-timing", t("Cost, timing and resources", "Coste, plazos y recursos"), None, [
        ("costs", t("Cost", "Coste"),
         t("Financing structure and total cost of ownership: a **cost** per expenditure and budget line, "
           "with staff in FTE and other costs in k€, and the previous investments in this area.",
           "Estructura de financiación y coste total de propiedad: un **coste** por gasto y partida "
           "presupuestaria, con el personal en ETC y el resto en k€, y las inversiones previas en este ámbito."), []),
        ("milestones", t("Timing and milestones", "Plazos e hitos"),
         t("Important points in time of the project: **milestones** of events, deliverables and phases "
           "(initiating, planning, executing, closing), including project management deliverables such as the "
           "Project Work Plan.",
           "Momentos importantes del proyecto: **hitos** de acontecimientos, entregables y fases (inicio, "
           "planificación, ejecución, cierre), incluidos entregables de gestión como el plan de trabajo."), []),
        ("resources", t("Planned resources", "Recursos previstos"),
         t("**Resources** required by the project: staff (number, type, skills, phase) and non-human "
           "resources, who provides them and how they will be obtained.",
           "**Recursos** que requiere el proyecto: personal (número, tipo, conocimientos, fase) y recursos no "
           "humanos, quién los aporta y cómo se obtendrán."), []),
    ]),
    ("approach", t("Approach", "Enfoque"), None, [
        ("methodology", t("Methodology", "Metodología"),
         t("Project management methodology (PM² or the deviations from it) and the methodology of the "
           "domain-specific work, e.g. information systems development.",
           "Metodología de gestión del proyecto (PM² o las desviaciones respecto a ella) y la del trabajo "
           "específico del dominio, p. ej. el desarrollo de sistemas de información."), []),
        ("change-management", t("Change management", "Gestión del cambio"), None, [
            ("project-change", t("Project change", "Cambios del proyecto"),
             t("How changes to the project are requested, assessed and approved (see the Project Handbook).",
               "Cómo se solicitan, evalúan y aprueban los cambios del proyecto (véase el manual del proyecto)."), []),
            ("configuration", t("Configuration management", "Gestión de la configuración"),
             t("Items that can only be modified with authorisation (scope, budget, milestone dates, key "
               "documents) and how their changes are controlled.",
               "Elementos que solo pueden modificarse con autorización (alcance, presupuesto, fechas de los hitos, "
               "documentos clave) y cómo se controlan sus cambios."), []),
            ("organisational-change", t("Organisational change", "Cambio organizativo"),
             t("Organisational change goals and activities, elaborated in the Business Implementation Plan.",
               "Objetivos y actividades de cambio organizativo, que se desarrollan en el plan de implantación en "
               "el negocio."), []),
        ]),
    ]),
    ("governance", t("Governance and stakeholders", "Gobierno y partes interesadas"), None, [
        ("structure", t("Structure", "Estructura"),
         t("Organisational structure of the project team and stakeholders, preferably as a **figure**, "
           "e.g. the Project Steering Committee (PO, BM, SP, PM).",
           "Estructura organizativa del equipo del proyecto y de las partes interesadas, preferiblemente con "
           "una **figura**, p. ej. el comité de dirección (PO, BM, SP, PM)."), []),
        ("roles", t("Roles and responsibilities", "Roles y responsabilidades"),
         t("**Role assignments** of the PM² governance roles, with their responsibilities and any deviation "
           "from the standard.",
           "**Asignaciones de rol** de los roles de gobierno de PM², con sus responsabilidades y cualquier "
           "desviación respecto al estándar."), []),
        ("other-stakeholders", t("Other stakeholders", "Otras partes interesadas"),
         t("All the **stakeholders** of the project (link them), with the profile of the key stakeholders and "
           "user groups and the problems they perceive.",
           "Todas las **partes interesadas** del proyecto (enlácelas), con el perfil de las clave y de los "
           "grupos de usuarios y los problemas que perciben."), []),
    ]),
]

OBJECTS = {
    "summary": ["paragraph"],
    "considerations": ["paragraph", "symbolic-link"],
    "scope-in": ["symbolic-link", "scope-item"],
    "scope-out": ["symbolic-link", "scope-item"],
    "scope-statement": ["paragraph"],
    "success": ["symbolic-link", "success-criterion"],
    "needs": ["need"],
    "deliverables": ["symbolic-link", "deliverable"],
    "features": ["feature", "traceability-matrix"],
    "constraints": ["symbolic-link", "constraint"],
    "assumptions": ["symbolic-link", "assumption"],
    "risks": ["symbolic-link", "risk"],
    "costs": ["symbolic-link", "cost-plan", "cost-item"],
    "milestones": ["symbolic-link", "milestone"],
    "resources": ["resource-requirement"],
    "methodology": ["paragraph"],
    "project-change": ["paragraph"],
    "configuration": ["paragraph"],
    "organisational-change": ["paragraph"],
    "structure": ["local-figure", "paragraph"],
    "roles": ["role-assignment"],
    "other-stakeholders": ["symbolic-link", "stakeholder"],
    "references": ["bibliography-item"],
}

CONTAINER_HELP = {
    "description": t("Description of the project: scope, success criteria, needs, deliverables, features, "
                     "constraints, assumptions and risks. Each subsection says what it contains.",
                     "Descripción del proyecto: alcance, criterios de éxito, necesidades, entregables, "
                     "funcionalidades, restricciones, supuestos y riesgos. Cada subsección indica lo que contiene."),
    "scope": t("Boundaries of the project: what it includes, what it excludes and the scope statement.",
               "Límites del proyecto: lo que incluye, lo que excluye y la declaración del alcance."),
    "cost-timing": t("Cost, milestones and resources of the project.", "Coste, hitos y recursos del proyecto."),
    "approach": t("How the project will be managed: methodology and change management.",
                  "Cómo se gestionará el proyecto: metodología y gestión del cambio."),
    "change-management": t("How changes to the project, to its documents and deliverables, and to the "
                           "organisation will be handled.",
                           "Cómo se gestionarán los cambios del proyecto, de sus documentos y entregables, y de "
                           "la organización."),
    "governance": t("Governance structure, roles and stakeholders of the project.",
                    "Estructura de gobierno, roles y partes interesadas del proyecto."),
}

REFERENCES = ("references", t("References and related documents", "Referencias y documentos relacionados"),
              t("Reference the relevant documents (e.g. the Business Case) with their title, version, date and "
                "source or location.",
                "Referencie los documentos relevantes (p. ej., el caso de negocio) con su título, versión, fecha y "
                "fuente o ubicación."))

PC_ACRONYM = t("PC", "AC")
PC_NAME = t("Project Charter", "Acta de constitución del proyecto")
PC_DESCRIPTION = t("Description of the project approved at the end of the initiating phase: scope, "
                   "deliverables, cost, timing, approach and governance (PM² artefact).",
                   "Descripción del proyecto aprobada al final de la fase de inicio: alcance, entregables, coste, "
                   "plazos, enfoque y gobierno (artefacto PM²).")


def _tree(p, items, guidance):
    return tree(p, "pc", PC_SECTIONS, items, guidance, OBJECTS, CONTAINER_HELP)


def _references(p, items, guidance):
    return references(p, items, guidance, "pc", REFERENCES, OBJECTS)


def empty(p, lang, document_values):
    """Project Charter of the empty project, with the guidance of every section."""
    control = p.add("document-control", "pc-control", {},
                    [p.add("approval", "pc-approval-1"), p.add("revision", "pc-revision-1")])
    secs = _tree(p, {}, True)
    p.document("pc", document_values(lang, {"_args": (PC_ACRONYM, PC_NAME, PC_DESCRIPTION)}),
               [control] + secs + [_references(p, [], True)])


def sample(p, lang, document_values, ids):
    """Project Charter of the sample project. ids: objects of the other documents."""
    def item(arch, id_, num, name_, desc, children=(), **values):
        v = {":Proteus-code": num, ":Proteus-name": name_, "description": desc}
        v.update({k.replace("_", "-"): x for k, x in values.items()})
        return p.add(arch, id_, v, children)

    def para(id_, text):
        return p.add("paragraph", id_, {"text": text})

    L = lambda *xs: [link(p, x, "pc") for x in xs]

    # --- needs and features ---------------------------------------------------------------
    need1 = item("need", "need-1", "001", t("Know the status", "Conocer el estado"),
                 t("Students need to know the status of their final project at any time in order to plan their graduation.",
                   "Los estudiantes necesitan conocer en todo momento el estado de su trabajo para planificar su titulación."),
                 priority="essential",
                 current_handling=t("They ask the secretariat or their supervisor by e-mail.",
                                    "Preguntan a la secretaría o a su tutor por correo."),
                 stakeholders=[ids["students"]], addresses=[ids["sit-1"]])
    need2 = item("need", "need-2", "002", t("Manage proposals online", "Gestionar propuestas en línea"),
                 t("Supervisors need to propose topics and accept students online in order to avoid paperwork.",
                   "Los tutores necesitan proponer temas y aceptar estudiantes en línea para evitar el papeleo."),
                 priority="essential",
                 desired_solution=t("A list of topics where students apply and supervisors accept.",
                                    "Un listado de temas en el que los estudiantes se inscriben y los tutores aceptan."),
                 stakeholders=[ids["initiator"]], addresses=[ids["sit-1"]])
    need3 = item("need", "need-3", "003", t("Organise the defences", "Organizar las defensas"),
                 t("Committees need to schedule the defences and record the grades in order to close the transcripts on time.",
                   "Las comisiones necesitan convocar las defensas y registrar las notas para cerrar las actas a tiempo."),
                 priority="essential", stakeholders=[ids["school"]], addresses=[ids["sit-1"]])
    need4 = item("need", "need-4", "004", t("Control deadlines and filing", "Controlar plazos y depósito"),
                 t("The secretariat needs to control the deadlines and the electronic filing in order to comply with the regulations.",
                   "La secretaría necesita controlar los plazos y el depósito electrónico para cumplir la normativa."),
                 priority="essential", stakeholders=[ids["secretary"]], addresses=[ids["sit-2"]])
    need5 = item("need", "need-5", "005", t("Statistics", "Estadísticas"),
                 t("The school direction needs statistics of the final projects in order to plan the offer of topics.",
                   "La dirección de la escuela necesita estadísticas de los trabajos para planificar la oferta de temas."),
                 priority="desirable", stakeholders=[ids["po"]])

    dlv4a = item("deliverable", "dlv-4a", "005", t("Student and supervisor portal", "Portal de estudiantes y tutores"),
                 t("Web module for proposals, applications, follow-up and filing, which students and supervisors use.",
                   "Módulo web de propuestas, inscripciones, seguimiento y depósito, que usan estudiantes y tutores."),
                 kind="information-system")
    dlv4b = item("deliverable", "dlv-4b", "006", t("Committee module", "Módulo de comisiones"),
                 t("Module for scheduling the defences and recording the grades, which the committees use.",
                   "Módulo de convocatoria de defensas y registro de notas, que usan las comisiones."),
                 kind="information-system")
    dlv4c = item("deliverable", "dlv-4c", "007", t("Integration with the corporate services", "Integración con los servicios corporativos"),
                 t("Connectors with the single sign-on, the electronic signature, the registry and the transcripts.",
                   "Conectores con la identificación única, la firma electrónica, el registro y las actas."),
                 kind="service")
    dlv4 = item("deliverable", "dlv-4", "004", t("Final project management system (modules)", "Sistema de gestión de trabajos (módulos)"),
                t("Web application integrated with the corporate services, made of three sub-deliverables.",
                  "Aplicación web integrada con los servicios corporativos, compuesta por tres subentregables."),
                children=[dlv4a, dlv4b, dlv4c], kind="information-system",
                within=[ids["scp-1"]], contributes_to=[ids["out-1"], ids["out-2"]], refines=[ids["dlv-1"]])

    feats = [
        ("feat-1", "001", t("Online proposals", "Propuestas en línea"),
         t("The portal shall allow supervisors to publish topics and students to apply for them, so that the assignment is done without paperwork.",
           "El portal permitirá a los tutores publicar temas y a los estudiantes inscribirse, para que la asignación se haga sin papeleo."),
         [need2], [dlv4a]),
        ("feat-2", "002", t("Status tracking and notices", "Seguimiento y avisos"),
         t("The portal shall allow students and supervisors to see the status of each final project and receive notices of every change, so that they do not need to ask.",
           "El portal permitirá a estudiantes y tutores ver el estado de cada trabajo y recibir avisos de cada cambio, para que no necesiten preguntar."),
         [need1], [dlv4a]),
        ("feat-3", "003", t("Electronic filing", "Depósito electrónico"),
         t("The system shall allow students to file their final project with an electronic signature and register it, so that the filing complies with the regulations.",
           "El sistema permitirá a los estudiantes depositar su trabajo con firma electrónica y registrarlo, para que el depósito cumpla la normativa."),
         [need1, need4], [dlv4a, dlv4c]),
        ("feat-4", "004", t("Defences and grades", "Defensas y calificaciones"),
         t("The committee module shall allow committees to schedule the defences and record the grades in the transcripts, so that the calls are closed on time.",
           "El módulo de comisiones permitirá convocar las defensas y registrar las notas en las actas, para que las convocatorias se cierren a tiempo."),
         [need3], [dlv4b, dlv4c]),
        ("feat-5", "005", t("Deadline control", "Control de plazos"),
         t("The system shall allow the secretariat to set the deadlines of each call and see the final projects that miss them, so that it can act in time.",
           "El sistema permitirá a la secretaría fijar los plazos de cada convocatoria y ver los trabajos que los incumplen, para que pueda actuar a tiempo."),
         [need4], [dlv4a]),
        ("feat-6", "006", t("Statistics", "Estadísticas"),
         t("The system shall allow the direction to obtain statistics by degree, department and call, so that it can plan the offer of topics.",
           "El sistema permitirá a la dirección obtener estadísticas por titulación, departamento y convocatoria, para que pueda planificar la oferta de temas."),
         [need5], [dlv4b]),
    ]
    features = [item("feature", f_id, num, name_, desc, satisfies=needs, delivered_in=dlvs)
                for f_id, num, name_, desc, needs, dlvs in feats]

    # --- scope, constraints, milestones and resources ------------------------------------------
    scp6 = item("scope-item", "scp-6", "006", t("Organisational change", "Cambio organizativo"),
                t("The project includes the training and communication activities needed to adopt the new procedure.",
                  "El proyecto incluye las actividades de formación y comunicación necesarias para adoptar el nuevo procedimiento."),
                inclusion="in", kind="process")
    con4 = item("constraint", "con-4", "004", t("Corporate interfaces", "Interfaces corporativas"),
                t("The project must integrate with the registry and the electronic signature only through their corporate interfaces.",
                  "El proyecto debe integrarse con el registro y la firma electrónica solo a través de sus interfaces corporativas."),
                area="interfaces")
    ms5 = item("milestone", "ms-5", "005", t("Project Work Plan approved", "Plan de trabajo aprobado"),
               t("The Project Steering Committee approves the Project Work Plan.",
                 "El comité de dirección aprueba el plan de trabajo del proyecto."),
               kind="phase-end", phase="planning", planned_date="2027-02-15")
    ms6 = item("milestone", "ms-6", "006", t("Project closed", "Proyecto cerrado"),
               t("The Project End Report is approved and the project is closed.",
                 "Se aprueba el informe de cierre y se cierra el proyecto."),
               kind="phase-end", phase="closing", planned_date="2027-10-29")
    res1 = item("resource-requirement", "res-1", "001", t("Development team", "Equipo de desarrollo"),
                t("The project requires two developers for the development and the integration of the system.",
                  "El proyecto requiere dos desarrolladores para el desarrollo y la integración del sistema."),
                kind="staff", quantity=t("2 people", "2 personas"),
                skills=t("Web development with the corporate stack; integration with the e-administration services.",
                         "Desarrollo web con las tecnologías corporativas; integración con los servicios de administración electrónica."),
                phase="executing", acquisition=t("Assigned by the IT services.", "Asignados por el SIC."),
                provided_by=[ids["sic"]], responsible=[ids["sp"]])
    res2 = item("resource-requirement", "res-2", "002", t("User representatives", "Representantes de los usuarios"),
                t("The project requires a member of the secretariat and two supervisors for the requirements and the acceptance tests.",
                  "El proyecto requiere una persona de la secretaría y dos tutores para los requisitos y las pruebas de aceptación."),
                kind="staff", quantity=t("3 people, 10 % of their time", "3 personas, al 10 % de su tiempo"),
                phase="executing", provided_by=[ids["school"]], responsible=[ids["secretary"]])
    res3 = item("resource-requirement", "res-3", "003", t("Servers", "Servidores"),
                t("The project requires test and production servers for the system.",
                  "El proyecto requiere servidores de pruebas y de producción para el sistema."),
                kind="equipment", phase="executing",
                acquisition=t("From the virtualisation platform of the IT services.", "De la plataforma de virtualización del SIC."),
                provided_by=[ids["sic"]], responsible=[ids["pm"]])

    # --- governance --------------------------------------------------------------------------
    def role(id_, num, name_, role_, assignee, resp):
        return p.add("role-assignment", id_, {":Proteus-code": num, ":Proteus-name": name_, "pm2-role": role_,
                                              "assignee": assignee, "responsibilities": resp})
    roles = [
        role("role-1", "001", t("Project Owner", "Propietario del proyecto"), "po", [ids["po"]],
             t("Funds the project, chairs the steering committee and accepts the deliverables.",
               "Financia el proyecto, preside el comité de dirección y acepta los entregables.")),
        role("role-2", "002", t("Business Manager", "Responsable de negocio"), "bm", [ids["secretary"]],
             t("Represents the secretariat, defines the procedure and leads its implementation in the school.",
               "Representa a la secretaría, define el procedimiento y dirige su implantación en la escuela.")),
        role("role-3", "003", t("Solution Provider", "Proveedor de la solución"), "sp", [ids["sp"]],
             t("Accountable for the system delivered by the IT services.", "Responde del sistema que entrega el SIC.")),
        role("role-4", "004", t("Project Manager", "Jefe de proyecto"), "pm", [ids["pm"]],
             t("Manages the project day to day and reports to the steering committee.",
               "Gestiona el proyecto en el día a día e informa al comité de dirección.")),
        role("role-5", "005", t("Steering committee", "Comité de dirección"), "psc",
             [ids["po"], ids["secretary"], ids["sp"], ids["pm"]],
             t("Steers the project and approves the changes of scope, budget and milestones.",
               "Dirige el proyecto y aprueba los cambios de alcance, presupuesto e hitos.")),
        role("role-6", "006", t("User representatives", "Representantes de los usuarios"), "ur",
             [ids["students"], ids["initiator"]],
             t("Represent students and supervisors in the requirements and acceptance tests.",
               "Representan a estudiantes y tutores en los requisitos y las pruebas de aceptación.")),
    ]

    ref3 = p.add("bibliography-item", "ref-3", {
        ":Proteus-name": t("Business Case, version 1.0", "Caso de negocio, versión 1.0"),
        "publication_authors": "Molina Vega, J.",
        "publication_details": t("Document management system of the school, " + DATE + ".",
                                 "Gestor documental de la escuela, " + DATE + ".")})

    # --- document ----------------------------------------------------------------------------
    a1 = p.add("approval", "pc-approval-1", {":Proteus-name": t("Approval by the PO", "Aprobación del PO"),
                                              "approver": [ids["po"]], "action": "approve"})
    a2 = p.add("approval", "pc-approval-2", {":Proteus-name": t("Review by the SP", "Revisión del SP"),
                                              "approver": [ids["sp"]], "action": "review"})
    r1 = p.add("revision", "pc-revision-1", {":Proteus-name": t("First version", "Primera versión"),
                                              "revision": "1.0", "created-by": [ids["pm"]],
                                              "changes": t("First version of the Project Charter.",
                                                           "Primera versión del acta de constitución.")})
    control = p.add("document-control", "pc-control", {}, [a1, a2, r1])

    items = {
        "summary": [para("pc-summary-text", t(
            "The project replaces the manual management of final degree and master projects of the school with an "
            "electronic procedure supported by a system integrated with the corporate services of the university. "
            "It is developed in-house by the IT services in 2027 and goes live for the first call of the 2027-28 "
            "academic year, with an effort of about 120 person-days.",
            "El proyecto sustituye la gestión manual de los trabajos fin de grado y fin de máster de la escuela por un "
            "procedimiento electrónico, soportado por un sistema integrado con los servicios corporativos de la "
            "universidad. Lo desarrolla el SIC en 2027 y entra en producción para la primera convocatoria del curso "
            "2027-28, con un esfuerzo de unos 120 días-persona."))],
        "considerations": [para("pc-considerations-text", t(
            "The urgency of the current situation has increased: the new regulations apply from the 2027-28 academic "
            "year, so the deadline of the project cannot be moved.",
            "La urgencia de la situación actual ha aumentado: la nueva normativa se aplica desde el curso 2027-28, por "
            "lo que la fecha límite del proyecto no puede moverse."))] + L(ids["sit-1"]),
        "scope-in": L(ids["scp-1"], ids["scp-2"], ids["scp-3"]) + [scp6],
        "scope-out": L(ids["scp-4"], ids["scp-5"]),
        "scope-statement": [para("pc-scope-statement-text", t(
            "Electronic procedure and management system for the final projects of the School of Computer Engineering, "
            "integrated with the corporate services, with the training of its users.",
            "Procedimiento electrónico y sistema de gestión de los trabajos fin de estudios de la ETSII, integrado con "
            "los servicios corporativos, con la formación de sus usuarios."))],
        "success": L(ids["sc-5"], ids["sc-6"], ids["sc-1"]),
        "needs": [need1, need2, need3, need4, need5],
        "deliverables": [dlv4] + L(ids["dlv-2"], ids["dlv-3"]),
        "features": features,
        "constraints": L(ids["con-1"], ids["con-2"], ids["con-3"]) + [con4],
        "assumptions": L(ids["asm-1"], ids["asm-2"], ids["asm-3"]),
        "risks": L(ids["rsk-1"], ids["rsk-2"], ids["rsk-3"], ids["rsk-4"]),
        "costs": L(ids["cost-plan"]),
        "milestones": L(ids["ms-1"]) + [ms5] + L(ids["ms-2"], ids["ms-3"], ids["ms-4"]) + [ms6],
        "resources": [res1, res2, res3],
        "methodology": [para("pc-methodology-text", t(
            "The project follows PM². The system is developed with an iterative approach, with a version every month "
            "reviewed with the user representatives.",
            "El proyecto sigue PM². El sistema se desarrolla de forma iterativa, con una versión cada mes revisada con "
            "los representantes de los usuarios."))],
        "project-change": [para("pc-project-change-text", t(
            "Changes are requested to the Project Manager, assessed by the core team and approved by the steering "
            "committee, as described in the Project Handbook.",
            "Los cambios se solicitan al jefe de proyecto, los evalúa el equipo central y los aprueba el comité de "
            "dirección, según el manual del proyecto."))],
        "configuration": [para("pc-configuration-text", t(
            "The scope, the budget, the milestone dates and the approved artefacts are kept in PROTEUS and can only be "
            "changed with the approval of the steering committee.",
            "El alcance, el presupuesto, las fechas de los hitos y los artefactos aprobados se mantienen en PROTEUS y "
            "solo pueden cambiarse con la aprobación del comité de dirección."))],
        "organisational-change": [para("pc-organisational-change-text", t(
            "The secretariat and the supervisors are trained before the pilot, and the students are informed at the "
            "beginning of the academic year.",
            "La secretaría y los tutores se forman antes del piloto, y los estudiantes se informan al comienzo del "
            "curso."))],
        "structure": [para("pc-structure-text", t(
            "The steering committee is formed by the Project Owner, the Business Manager, the Solution Provider and "
            "the Project Manager, who leads the core team of the IT services.",
            "El comité de dirección lo forman el propietario del proyecto, la responsable de negocio, la proveedora de "
            "la solución y el jefe de proyecto, que dirige el equipo central del SIC."))],
        "roles": roles,
        "other-stakeholders": L(ids["initiator"], ids["secretary"], ids["students"]),
    }
    secs = _tree(p, items, True)
    p.document("pc", document_values(lang, {
        "_args": (PC_ACRONYM, PC_NAME, PC_DESCRIPTION), "version": "1.0", "sensitivity": "sensitive-basic",
        "document-author": [ids["pm"]], "project-manager": [ids["pm"]],
        "document-location": t("the document management system of the school", "el gestor documental de la escuela"),
        "prepared-for": [ids["us"]], "prepared-by": [ids["sic"]]}),
        [control] + secs + [_references(p, [ref3], True)])

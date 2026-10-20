# Project archetypes of the PM2 profile: an empty project and a sample project.
from pathlib import Path
from model import t, DATE
import business_case
import project_charter
from guidance import guidance as guidance_text, GUIDANCE_NAME

# Assets of the basic archetypes, copied into this profile
BASIC_ASSETS = Path(__file__).resolve().parent.parent / "archetypes" / "es_es" / "objects"

# ---------------------------------------------------------------------------
# Sections of the documents, with the guidance shown as a comment
# ---------------------------------------------------------------------------

PIR_SECTIONS = [
    ("context", t("Context / situation", "Contexto y situación"),
     t("Describe why the project should be initiated: the business need it responds to, the problem it "
       "solves or the opportunity it takes advantage of (or a combination of them). Add a **business "
       "situation** for each need, problem or opportunity.",
       "Describa por qué debe iniciarse el proyecto: la necesidad de negocio a la que responde, el "
       "problema que resuelve o la oportunidad que aprovecha (o una combinación). Añada una **situación de "
       "negocio** por cada necesidad, problema u oportunidad."), ["business-situation"]),
    ("legal", t("Legal basis", "Base legal"),
     t("State the legal basis of the request, if any (acts, directives of the senior management, internal "
       "regulations), and the **strategic goals** of the organisation the project is aligned with.",
       "Indique la base legal de la solicitud, si la hay (normas, directrices de la dirección, normativa "
       "interna), y los **objetivos estratégicos** de la organización con los que se alinea el proyecto."), ["legal-basis", "strategic-goal"]),
    ("outcomes", t("Outcomes", "Resultados esperados"),
     t("Describe at a high level the main **outcomes** expected from the project: the future or desired "
       "state that the change brought by the project will produce. Measurable benefits should be linked "
       "to them later.",
       "Describa a alto nivel los principales **resultados** que se esperan del proyecto: la situación "
       "futura o deseada que producirá el cambio. Más adelante se les asociarán beneficios medibles."), ["outcome"]),
    ("impact", t("Impact", "Impacto"),
     t("Describe the **impact** of the current situation and of the desired solution inside the "
       "organisation (processes, people, culture) and on its external stakeholders. Keep it at a high level.",
       "Describa el **impacto** de la situación actual y de la solución deseada dentro de la organización "
       "(procesos, personas, cultura) y sobre sus partes interesadas externas. Manténgalo a alto nivel."), ["impact"]),
    ("success", t("Success criteria", "Criterios de éxito"),
     t("Describe the high level **criteria** to evaluate the project as a success or a failure, e.g. on "
       "scope, schedule and cost.",
       "Describa los **criterios** de alto nivel para evaluar si el proyecto es un éxito o un fracaso, por "
       "ejemplo de alcance, plazo y coste."), ["success-criterion"]),
    ("assumptions", t("Assumptions", "Supuestos")
     , t("List the **assumptions** about business, technology, resources, organisational environment, "
         "scope, expectations or schedule. They are taken as facts at this stage, but they must be "
         "validated: an assumption that is not validated may become a risk.",
         "Enumere los **supuestos** sobre negocio, tecnología, recursos, entorno organizativo, alcance, "
         "expectativas o plazos. En esta fase se toman como hechos, pero deben validarse: un supuesto no "
         "validado puede convertirse en un riesgo."), ["assumption"]),
    ("constraints", t("Constraints", "Restricciones"),
     t("List the key **constraints** on schedule, budget, resources or products to be used, and also "
       "decisions, compliance and constraints coming from the organisation and its environment.",
       "Enumere las **restricciones** clave de plazo, presupuesto, recursos o productos que se deben usar, "
       "así como decisiones, cumplimiento normativo y restricciones de la organización y su entorno."), ["constraint"]),
    ("risks", t("Risks", "Riesgos"),
     t("List the initial **risks** identified, focusing on business risks. At this stage only the "
       "description and the category are needed; the assessment and the response are completed later.",
       "Enumere los **riesgos** iniciales identificados, centrándose en los de negocio. En esta fase basta "
       "con la descripción y la categoría; la evaluación y la respuesta se completan más adelante."), ["risk"]),
]

STK_SECTIONS = [
    ("organisations", t("Organisations", "Organizaciones"),
     t("Organisations and units involved in the project: the requesting organisation and units, the "
       "solution provider, the governance bodies...",
       "Organizaciones y unidades que intervienen en el proyecto: la organización y unidades "
       "solicitantes, el proveedor de la solución, los órganos de gobierno..."), ["organization"]),
    ("stakeholders", t("Stakeholders", "Partes interesadas"),
     t("People involved in the project. The roles of the project (initiator, project owner, solution "
       "provider, project manager...) are traces from the documents to these stakeholders.",
       "Personas que intervienen en el proyecto. Los roles del proyecto (iniciador, propietario, "
       "proveedor de la solución, jefe de proyecto...) son trazas desde los documentos a estas partes "
       "interesadas."), ["stakeholder"]),
]

PIR_ACRONYM = t("PIR", "SIP")
PIR_NAME = t("Project Initiation Request", "Solicitud de inicio del proyecto")
PIR_DESCRIPTION = t("Initial request to start a project (PM² artefact of the initiating phase).",
                    "Solicitud inicial para poner en marcha un proyecto (artefacto PM² de la fase de inicio).")
STK_ACRONYM = t("STK", "OPI")
STK_NAME = t("Organisations and stakeholders", "Organizaciones y partes interesadas")
STK_DESCRIPTION = t("Organisations and people involved in the project.",
                    "Organizaciones y personas que intervienen en el proyecto.")


def sections(p, prefix, specs, items=None, guidance=True):
    ids = []
    for key, title, help_, objects in specs:
        kids = []
        if guidance:
            kids.append(p.add("comment", f"{prefix}-{key}-help", {":Proteus-name": GUIDANCE_NAME,
                                                                 "text": guidance_text(help_, objects)}))
        kids += (items or {}).get(key, [])
        ids.append(p.add("section", f"{prefix}-{key}", {":Proteus-name": title}, kids))
    return ids

# ---------------------------------------------------------------------------
# Empty project
# ---------------------------------------------------------------------------

def build_empty(lang, Project, document_values):
    p = Project(lang, "pm2-empty", "pm2-empty",
                t("PM² project", "Proyecto PM²"),
                t("Empty PM² project with a Project Initiation Request, a Business Case, a Project Charter and the organisations and stakeholders of the project.",
                  "Proyecto PM² vacío con una solicitud de inicio, un caso de negocio, un acta de constitución y las organizaciones y partes interesadas del proyecto."))
    approval = p.add("approval", "pir-approval-1")
    revision = p.add("revision", "pir-revision-1")
    control = p.add("document-control", "pir-control", {}, [approval, revision])
    request = p.add("initiation-request", "pir-request")
    secs = sections(p, "pir", PIR_SECTIONS)
    p.document("pir", document_values(lang, {"_args": (PIR_ACRONYM, PIR_NAME, PIR_DESCRIPTION)}),
               [control, request] + secs)
    business_case.empty(p, lang, document_values)
    project_charter.empty(p, lang, document_values)
    stk = sections(p, "stk", STK_SECTIONS)
    p.document("stakeholders", document_values(lang, {"_args": (STK_ACRONYM, STK_NAME, STK_DESCRIPTION)}), stk)
    p.save()

# ---------------------------------------------------------------------------
# Sample project: electronic management of final degree projects at a school
# ---------------------------------------------------------------------------

def build_sample(lang, Project, document_values):
    p = Project(lang, "pm2-sample", "pm2-sample",
                t("Electronic management of final projects", "Gestión electrónica de TFG y TFM"),
                t("Sample PM² project: Project Initiation Request, Business Case and Project Charter for the electronic management of the final "
                  "degree and master projects of a school of the University of Seville. People and figures are fictitious.",
                  "Proyecto PM² de ejemplo: solicitud de inicio, caso de negocio y acta de constitución para la gestión electrónica de los trabajos fin "
                  "de grado y fin de máster de una escuela de la Universidad de Sevilla. Las personas y las cifras son ficticias."))

    # --- organisations and stakeholders --------------------------------------------------
    org = lambda id_, name_, desc, web="", logo="organization_logo.png", email="": p.add(
        "organization", id_, {":Proteus-name": name_, "description": desc, "web": web,
                              "logo": logo, "email": email})
    us = org("org-us", t("University of Seville", "Universidad de Sevilla"),
             t("Public university that funds the project and benefits from its outputs.",
               "Universidad pública que financia el proyecto y se beneficia de sus resultados."),
             "https://www.us.es", "us-logo.jpg")
    school = org("org-school", t("School of Computer Engineering (ETSII)", "Escuela Técnica Superior de Ingeniería Informática (ETSII)"),
                 t("School of the University of Seville that requests the project. Its secretariat manages "
                   "the final degree and master projects.",
                   "Escuela de la Universidad de Sevilla que solicita el proyecto. Su secretaría gestiona los "
                   "trabajos fin de grado y fin de máster."), email="secretaria-etsii@example.us.es")
    sic = org("org-sic", t("IT Services (SIC)", "Servicio de Informática y Comunicaciones (SIC)"),
              t("IT service of the university, in charge of developing and operating the corporate applications.",
                "Servicio de informática de la universidad, encargado de desarrollar y explotar las aplicaciones corporativas."))
    board = org("org-board", t("School Board", "Junta de Escuela"),
                t("Governing body of the school that approves the projects of the school.",
                  "Órgano de gobierno de la escuela que aprueba los proyectos del centro."))

    students = org("org-students", t("Student delegation of the school", "Delegación de estudiantes de la escuela"),
                   t("Body that represents the students of the school.",
                     "Órgano que representa a los estudiantes de la escuela."))

    def person(id_, name_, role, category, works_for, **extra):
        values = {":Proteus-name": name_, "role": role, "category": category,
                  "email": id_.replace("stk-", "") + "@example.us.es", "works-for": [works_for]}
        values.update({k.replace("_", "-"): v for k, v in extra.items()})
        return p.add("stakeholder", id_, values)

    po = person("stk-ruiz", "Ruiz Delgado, Marta", t("Director of the school", "Directora de la escuela"), "customer", school,
                profile=t("Head of the school, she funds the project and chairs the School Board.",
                          "Directora de la escuela, financia el proyecto y preside la Junta de Escuela."),
                perceived_problems=t("Delays in the graduation of students and complaints about the procedure.",
                                     "Retrasos en la titulación de los estudiantes y quejas sobre el procedimiento."))
    initiator = person("stk-herrera", "Herrera Campos, Luis",
                       t("Deputy director for academic affairs", "Subdirector de ordenación académica"), "customer", school,
                       profile=t("Responsible for the academic organisation of the school, including the final projects.",
                                 "Responsable de la ordenación académica de la escuela, incluidos los trabajos fin de estudios."),
                       perceived_problems=t("Supervisors and committees have no shared view of the status of the final projects.",
                                            "Tutores y comisiones no tienen una visión compartida del estado de los trabajos."))
    sp = person("stk-ortega", "Ortega Navas, Elena",
                t("Head of the development service", "Jefa del servicio de desarrollo"), "developer", sic)
    pm = person("stk-molina", "Molina Vega, Javier", t("Project manager", "Jefe de proyecto"), "developer", sic)
    secretary = person("stk-castro", "Castro Lirio, Rocío",
                       t("Head of the school secretariat", "Jefa de la secretaría de la escuela"), "user", school,
                       profile=t("Manages the administrative procedure of the final projects with two assistants.",
                                 "Gestiona el procedimiento administrativo de los trabajos con dos auxiliares."),
                       perceived_problems=t("Lost documents, missed deadlines and many status enquiries by e-mail.",
                                            "Documentos perdidos, plazos incumplidos y muchas consultas de estado por correo."))

    # --- PIR content -------------------------------------------------------------------
    def item(arch, id_, num, name_, desc, **values):
        v = {":Proteus-code": num, ":Proteus-name": name_, "description": desc}
        v.update({k.replace("_", "-"): x for k, x in values.items()})
        return p.add(arch, id_, v)

    sit1 = item("business-situation", "sit-1", "001", t("Manual handling of final projects", "Gestión manual de los trabajos fin de estudios"),
                t("Currently, proposals, assignments and defences of final projects are handled by e-mail and "
                  "spreadsheets, which causes errors, duplicated work and delays in the secretariat.",
                  "Actualmente, las propuestas, asignaciones y defensas de los trabajos fin de estudios se "
                  "gestionan por correo electrónico y hojas de cálculo, lo que provoca errores, trabajo "
                  "duplicado y retrasos en la secretaría."), kind="problem",
                urgency=t("High: the errors already delay the graduation of some students, and the new "
                          "regulations apply from the 2027-28 academic year.",
                          "Alta: los errores ya retrasan la titulación de algunos estudiantes, y la nueva "
                          "normativa se aplica desde el curso 2027-28."))
    sit2 = item("business-situation", "sit-2", "002", t("Electronic processing required", "Tramitación electrónica obligatoria"),
                t("Currently, administrative procedures must be processed electronically, which requires "
                  "the school to digitise the whole life cycle of final projects.",
                  "Actualmente, los procedimientos administrativos deben tramitarse por medios electrónicos, lo "
                  "que obliga a la escuela a digitalizar todo el ciclo de vida de los trabajos."), kind="need")
    sit3 = item("business-situation", "sit-3", "003", t("Corporate e-administration services", "Servicios corporativos de administración electrónica"),
                t("Currently, the university offers single sign-on, electronic signature and an electronic "
                  "registry, which can be reused to build the new system at a lower cost.",
                  "Actualmente, la universidad ofrece identificación única, firma electrónica y registro "
                  "electrónico, que pueden reutilizarse para construir el nuevo sistema con menor coste."),
                kind="opportunity")
    sg1 = item("strategic-goal", "sg-1", "001", t("Digital transformation", "Transformación digital"),
               t("Digital transformation of the administrative processes of the university.",
                 "Transformación digital de los procesos administrativos de la universidad."), owner=[us])
    lb1 = item("legal-basis", "lb-1", "001", t("Common administrative procedure act", "Ley del procedimiento administrativo común"),
               t("Act 39/2015 on the common administrative procedure establishes that public "
                 "administrations shall process their procedures electronically.",
                 "La Ley 39/2015 del procedimiento administrativo común establece que las administraciones "
                 "públicas deben tramitar sus procedimientos por medios electrónicos."),
               kind="legislation", reference="https://www.boe.es/eli/es/l/2015/10/01/39/con", supports=[sg1])
    lb2 = item("legal-basis", "lb-2", "002", t("Final project regulations", "Normativa de trabajos fin de estudios"),
               t("The university regulations on final degree and master projects establish the steps, "
                 "deadlines and committees of the procedure.",
                 "La normativa de la universidad sobre trabajos fin de grado y fin de máster establece los "
                 "pasos, plazos y comisiones del procedimiento."), kind="policy", supports=[sg1])
    out1 = item("outcome", "out-1", "001", t("Fully electronic procedure", "Procedimiento totalmente electrónico"),
                t("After the project, the whole procedure, from the proposal to the defence and the filing "
                  "of the final project, is processed electronically.",
                  "Tras el proyecto, todo el procedimiento, desde la propuesta hasta la defensa y el depósito "
                  "del trabajo, se tramita electrónicamente."),
                addresses=[sit1, sit2], contributes_to=[sg1])
    out2 = item("outcome", "out-2", "002", t("Status known at any time", "Estado conocido en todo momento"),
                t("After the project, students and supervisors know the status of their final projects at any time.",
                  "Tras el proyecto, estudiantes y tutores conocen en todo momento el estado de sus trabajos."),
                addresses=[sit1])
    out3 = item("outcome", "out-3", "003", t("Less administrative workload", "Menos carga administrativa"),
                t("After the project, the secretariat devotes less time to managing final projects.",
                  "Tras el proyecto, la secretaría dedica menos tiempo a la gestión de los trabajos."),
                addresses=[sit1], contributes_to=[sg1])
    imp1 = item("impact", "imp-1", "001", t("New secretariat procedures", "Nuevos procedimientos de secretaría"),
                t("The solution affects the procedures of the secretariat because the paper and e-mail "
                  "steps are replaced by electronic ones.",
                  "La solución afecta a los procedimientos de la secretaría porque los pasos en papel y por "
                  "correo se sustituyen por pasos electrónicos."),
                perspective="internal", area="processes", source="solution", affects=[school])
    imp2 = item("impact", "imp-2", "002", t("Staff training", "Formación del personal"),
                t("The solution affects the secretariat staff and the supervisors because they must learn "
                  "to use the new system.",
                  "La solución afecta al personal de secretaría y a los tutores porque deben aprender a usar "
                  "el nuevo sistema."),
                perspective="internal", area="people", source="solution", affects=[secretary])
    imp3 = item("impact", "imp-3", "003", t("Delays for students", "Retrasos para los estudiantes"),
                t("The current situation affects the students because delays in the procedure may postpone "
                  "their graduation.",
                  "La situación actual afecta a los estudiantes porque los retrasos del procedimiento pueden "
                  "aplazar su titulación."),
                perspective="external", area="external-stakeholders", source="current-situation")
    sc1 = item("success-criterion", "sc-1", "001", t("In production on time", "En producción a tiempo"),
               t("The project will be considered a success if the system is in production before the first "
                 "call of the 2027-28 academic year.",
                 "El proyecto se considerará un éxito si el sistema está en producción antes de la primera "
                 "convocatoria del curso 2027-28."), dimension="schedule", target="2027-09-15", evaluates=[out1])
    sc2 = item("success-criterion", "sc-2", "002", t("All proposals submitted electronically", "Todas las propuestas por vía electrónica"),
               t("The project will be considered a success if all the proposals of the first call are "
                 "submitted through the system.",
                 "El proyecto se considerará un éxito si todas las propuestas de la primera convocatoria se "
                 "presentan a través del sistema."), dimension="scope", target="100 %", evaluates=[out1])
    sc3 = item("success-criterion", "sc-3", "003", t("Within the estimated effort", "Dentro del esfuerzo estimado"),
               t("The project will be considered a success if it does not exceed the estimated effort by more than 10 %.",
                 "El proyecto se considerará un éxito si no supera en más de un 10 % el esfuerzo estimado."),
               dimension="cost", target=t("132 person-days at most", "132 días-persona como máximo"))
    sc4 = item("success-criterion", "sc-4", "004", t("User satisfaction", "Satisfacción de los usuarios"),
               t("The project will be considered a success if students and supervisors rate the system with "
                 "at least 4 out of 5 in the first satisfaction survey.",
                 "El proyecto se considerará un éxito si estudiantes y tutores valoran el sistema con al menos "
                 "un 4 sobre 5 en la primera encuesta de satisfacción."),
               dimension="quality", target=t("4 out of 5 or more", "4 sobre 5 o más"), evaluates=[out2])
    rsk1 = item("risk", "rsk-1", "001", t("Staff not available", "Personal no disponible"),
                t("Because of the overlap with the enrolment period, it might be that the IT staff are not "
                  "available, which will lead to delays in the development.",
                  "Debido a la coincidencia con el periodo de matrícula, podría ocurrir que el personal del "
                  "SIC no esté disponible, lo que provocaría retrasos en el desarrollo."),
                category="staffing", identified_by=[sp], related=["asm-1"], status="assessing",
                likelihood="medium", impact="high", risk_owner=[pm])
    rsk2 = item("risk", "rsk-2", "002", t("Low adoption by supervisors", "Baja adopción por los tutores"),
                t("Because of the habit of managing final projects by e-mail, it might be that supervisors do "
                  "not use the system, which will lead to keeping the manual procedure in parallel.",
                  "Debido a la costumbre de gestionar los trabajos por correo, podría ocurrir que los tutores no "
                  "usen el sistema, lo que provocaría mantener en paralelo el procedimiento manual."),
                category="business", identified_by=[initiator])
    rsk3 = item("risk", "rsk-3", "003", t("Change of the regulations", "Cambio de la normativa"),
                t("Because of the ongoing review of the final project regulations, it might be that the "
                  "procedure changes during the project, which will lead to rework.",
                  "Debido a la revisión en curso de la normativa de trabajos fin de estudios, podría ocurrir que "
                  "el procedimiento cambie durante el proyecto, lo que provocaría retrabajo."),
                category="legal", identified_by=[initiator], related=["asm-3"])
    asm1 = item("assumption", "asm-1", "001", t("Development team", "Equipo de desarrollo"),
                t("It is assumed that the IT services assign two developers to the project from January 2027.",
                  "Se asume que el SIC asigna dos desarrolladores al proyecto a partir de enero de 2027."),
                area="resources", may_become=[rsk1])
    asm2 = item("assumption", "asm-2", "002", t("Corporate services available", "Servicios corporativos disponibles"),
                t("It is assumed that the single sign-on and the electronic signature services can be "
                  "integrated without changes.",
                  "Se asume que los servicios de identificación única y de firma electrónica pueden integrarse "
                  "sin cambios."), area="technology", validation="validated")
    asm3 = item("assumption", "asm-3", "003", t("Stable regulations", "Normativa estable"),
                t("It is assumed that the final project regulations do not change during the project.",
                  "Se asume que la normativa de trabajos fin de estudios no cambia durante el proyecto."),
                area="organisation", may_become=[rsk3])
    con1 = item("constraint", "con-1", "001", t("Deadline", "Fecha límite"),
                t("The project must be in production before September 15, 2027.",
                  "El proyecto debe estar en producción antes del 15 de septiembre de 2027."), area="schedule")
    con2 = item("constraint", "con-2", "002", t("Personal data protection", "Protección de datos personales"),
                t("The project must comply with the GDPR and the Spanish personal data protection act.",
                  "El proyecto debe cumplir el RGPD y la LOPDGDD."), area="compliance")
    con3 = item("constraint", "con-3", "003", t("Corporate technologies", "Tecnologías corporativas"),
                t("The project must use the technologies and infrastructure supported by the IT services.",
                  "El proyecto debe usar las tecnologías e infraestructura soportadas por el SIC."), area="products")
    # --- PIR document ------------------------------------------------------------------
    a1 = p.add("approval", "pir-approval-1", {":Proteus-name": t("Approval by the PO", "Aprobación del PO"),
                                               "approver": [po], "action": "approve"})
    a2 = p.add("approval", "pir-approval-2", {":Proteus-name": t("Review by the SP", "Revisión del SP"),
                                               "approver": [sp], "action": "review"})
    r1 = p.add("revision", "pir-revision-1", {":Proteus-name": t("First draft", "Primer borrador"),
                                               "revision": "0.1", ":Proteus-date": "2026-10-05",
                                               "created-by": [initiator],
                                               "changes": t("First version of the request.", "Primera versión de la solicitud.")})
    r2 = p.add("revision", "pir-revision-2", {":Proteus-name": t("Reviewed version", "Versión revisada"),
                                               "revision": "1.0", ":Proteus-date": DATE, "created-by": [initiator],
                                               "changes": t("Effort and risks reviewed with the IT services.",
                                                            "Esfuerzo y riesgos revisados con el SIC.")})
    control = p.add("document-control", "pir-control", {}, [a1, a2, r2, r1])
    request = p.add("initiation-request", "pir-request", {
        "initiator": [initiator], "requesting-unit": [school], "project-owner": [po],
        "solution-provider": [sp], "approving-authority": [board], "request-date": "2026-10-15",
        "estimated-effort": "120",
        "other-costs": t("No licences are needed. Training of the secretariat staff: 2 sessions.",
                         "No se necesitan licencias. Formación del personal de secretaría: 2 sesiones."),
        "target-delivery-date": "2027-09-15", "delivery-type": "in-house"})
    items = {"context": [sit1, sit2, sit3], "legal": [lb1, lb2, sg1], "outcomes": [out1, out2, out3],
             "impact": [imp1, imp2, imp3], "success": [sc1, sc2, sc3, sc4],
             "assumptions": [asm1, asm2, asm3], "constraints": [con1, con2, con3],
             "risks": [rsk1, rsk2, rsk3]}
    secs = sections(p, "pir", PIR_SECTIONS, items)
    p.document("pir", document_values(lang, {
        "_args": (PIR_ACRONYM, PIR_NAME, PIR_DESCRIPTION), "version": "1.0", "sensitivity": "sensitive-basic",
        "document-author": [initiator], "project-manager": [pm],
        "document-location": t("the document management system of the school", "el gestor documental de la escuela"),
        "prepared-for": [us], "prepared-by": [school]}), [control, request] + secs)
    business_case.sample(p, lang, document_values, {
        "us": us, "school": school, "sic": sic, "board": board, "po": po, "sp": sp, "pm": pm,
        "secretary": secretary, "sit-1": sit1, "sit-2": sit2, "sit-3": sit3, "out-1": out1,
        "out-2": out2, "out-3": out3, "sc-2": sc2, "asm-2": asm2})
    # The Project Charter links objects of the PIR and the Business Case by id
    ids = {x: x for x in ("scp-1", "scp-2", "scp-3", "scp-4", "scp-5", "dlv-1", "dlv-2", "dlv-3",
                          "sc-1", "sc-5", "sc-6", "con-1", "con-2", "con-3", "asm-1", "asm-2", "asm-3",
                          "rsk-1", "rsk-2", "rsk-3", "rsk-4", "ms-1", "ms-2", "ms-3", "ms-4",
                          "sit-1", "sit-2", "out-1", "out-2")}
    ids.update({"cost-plan": "bc-cost-plan", "us": us, "school": school, "sic": sic, "po": po, "sp": sp,
                "pm": pm, "secretary": secretary, "initiator": initiator, "students": students})
    project_charter.sample(p, lang, document_values, ids)
    stk = sections(p, "stk", STK_SECTIONS,
                   {"organisations": [us, school, board, sic, students],
                    "stakeholders": [po, initiator, secretary, sp, pm]})
    p.document("stakeholders", document_values(lang, {
        "_args": (STK_ACRONYM, STK_NAME, STK_DESCRIPTION), "version": "1.0",
        "document-author": [initiator], "project-manager": [pm],
        "prepared-for": [us], "prepared-by": [school]}), stk)
    p.save([BASIC_ASSETS / "00_document/assets/us-logo.jpg",
            BASIC_ASSETS / "01_organisation/assets/organization_logo.png",
            BASIC_ASSETS / "01_organisation/assets/stakeholder_photo.png"])


def build(lang, Project, document_values):
    build_empty(lang, Project, document_values)
    build_sample(lang, Project, document_values)

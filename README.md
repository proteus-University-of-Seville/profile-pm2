# PM² profile

Bilingual (English/Spanish) [PROTEUS](https://github.com/proteus-University-of-Seville/proteus-core)
profile for the [PM²](https://www.pm2alliance.eu/) project management methodology. It extends the
archetypes of the `basic` profile with the artefacts of the initiating phase: the
**Project Initiation Request** (PIR), the **Business Case** (BC) and the **Project Charter** (PC).

## Usage

Point PROTEUS at this folder in the settings dialog, or in `proteus.ini`:

```ini
[settings]
using_default_profile = False
custom_profile_path = C:/proteus-profiles/pm2
```

Then create a project from one of the project archetypes:

- **PM² project** (`pm2-empty`): a Project Initiation Request, a Business Case and a Project
  Charter with their sections and guidance, and a document for the organisations and
  stakeholders of the project. The business processes are defined in the Business Case
  (section 2.2.1), as in the PM² template.
- **Electronic management of final projects** (`pm2-sample`): a complete sample PIR, BC and PC
  for a school of the University of Seville (people and figures are fictitious).

## Conceptual model

One class per PM² concept, not per document. Every list item is a traceable object with a
code; people and organisations are the `stakeholder` and `organization` archetypes of `basic`,
and the PM² roles are traces to them.

An object identified in an artefact is reused in the next ones:

- with a **symbolic link** when it is used as it is (e.g. the business situations and outcomes
  of the PIR in the BC): it is shown in both documents and edited once;
- with a new object that **refines** it (trace `refines`, in every traceable PM² class) when the
  later artefact needs a different version (e.g. a success criterion of the PIR made critical in
  the BC).

| Class | Code (en / es) | Main properties | Traces |
| --- | --- | --- | --- |
| `initiation-request` | | initiator, organisation/unit, PO, SP, approving authority, dates, estimated effort (person-days), other costs, type of delivery | to stakeholders and organisations |
| `business-process` | PROC- / PROC- | process category (the 16 categories of the PM² templates), domain, sub-domain, macro process | owner → organisation, stakeholder |
| `business-situation` | SIT- / SIT- | kind (need, problem, opportunity), urgency | |
| `strategic-goal` | GOAL- / OBJ- | | owner → organisation |
| `legal-basis` | LEG- / LEG- | kind, reference (URL) | supports → strategic goal |
| `outcome` | OUT- / RESU- | | addresses → business situation, contributes to → strategic goal |
| `impact` | IMP- / IMP- | perspective, area, caused by (current situation or solution), impact on owners and users | affects → stakeholder, organisation; affected processes → business process |
| `benefit` | BEN- / BEN- | indicator, baseline, target | derives from → outcome, perceived by → stakeholder, organisation |
| `alternative` | ALT- / ALT- | kind (do nothing, reuse, simple, sophisticated), SWOT, qualitative assessment, chosen, reasons for the choice | addresses → business situation |
| `scope-item` | SCP- / ALC- | inclusion (in, out), kind | realises → alternative |
| `deliverable` | DLV- / ENTR- | kind; may contain sub-deliverables | within → scope item, contributes to → outcome |
| `need` | NEED- / NEC- | priority (essential, desirable, optional), desired solution, justification, how it is addressed today | stakeholders → stakeholder, organisation; addresses → business situation |
| `feature` | FEAT- / FUN- | high level capability (what and why, not how) | satisfies → need, delivered in → deliverable |
| `milestone` | MILE- / HITO- | kind (start, milestone, end of phase, delivery), PM² phase, planned date | delivers → deliverable |
| `resource-requirement` | RSRC- / RECU- | kind (staff, equipment, facilities, tools), quantity, skills, phase, how it will be obtained | provided by → organisation, responsible → stakeholder |
| `cost-plan` | | first year, funding source, previous investments; its children are the costs | |
| `cost-item` | | group (solution or business implementation), category, nature (staff in FTE, other in k€), budget line, years 1 to 5 | |
| `role-assignment` | ROLE- / ROL- | PM² role (AGB, PSC, PO, BM, SP, PM, BIG, UR, PCT, PSO), responsibilities, deviations from the standard | assignee → stakeholder, organisation |
| `stakeholder` | | the properties of `basic` plus profile and perceived problems (generated, not copied from `basic`) | works for → organisation |
| `success-criterion` | SUCC- / CEXI- | dimension (scope, schedule, cost...), target, critical, applies to (project, product) | evaluates → outcome |
| `assumption` | ASM- / SUP- | area, validation | may become → risk |
| `constraint` | CON- / REST- | area | |
| `risk` | RISK- / RIES- | the columns of the PM² Risk Log: category, status, likelihood, impact, owner, response strategy, actions, escalation | related to → assumption, constraint |
| `interdependency` | DEP- / DEP- | kind (interrelation, interdependency, synergy, IT reuse, request or sharing), scope | related to → business situation, alternative, deliverable |
| `document-control` | | approvals and revisions of the document (children) | |
| `approval` | | approver, action (approve, review) | approver → stakeholder |
| `revision` | | revision, author, changes | created by → stakeholder |

PM² documents are plain `:Proteus-document` objects with the PM² document control properties
(sensitivity, author, project manager, location).

The default view and the LaTeX template are those of `basic`, plus these modules
(`archetypes/pm2/`):

- **document control**: control information (the Project Owner comes from the initiation
  request of the document or, if it only links to it, of the project), approvers and reviewers,
  history;
- **alternative**: the SWOT analysis as a 2×2 grid (HTML) and the chosen alternative marked in
  the header;
- **cost plan**: the Total Cost of Ownership tables of the Business Case and the Project Charter,
  by group and year, with the budget lines, the total of each cost and the totals of staff (FTE)
  and of other costs (k€);
- **risk**: its level (likelihood × impact) in the header.

## Toolbar

The archetypes are grouped by kind of concept, not by PM² phase, so that the artefacts of the
next phases add buttons to the same tabs:

| Tab | Buttons |
| --- | --- |
| Document | section, appendix, paragraph, comment, figure, symbolic link, document control (approvals and revisions in its context menu) |
| Organisation | organisation, stakeholder, business process, role assignment, meeting, project initiation request |
| Rationale | business situation, strategic goal, legal basis, outcome, impact, benefit |
| Solution | alternative, scope item, need, feature, deliverable |
| Planning | milestone, resource, cost plan (costs in its context menu) |
| Conditions | success criterion, assumption, constraint, risk, interdependency |
| References | glossary item, bibliography item, traceability matrix |

## Regenerating the archetypes

The PM² archetypes, the `objects.xml` of every tab (`TABS` in `tools/model.py`, which also
places the archetypes copied from `basic`), the `pm2_*.yaml` translations and the project
archetypes are generated from a single definition, so that both languages keep the same ids,
classes and properties. Change `tools/model.py` (archetypes, tabs and labels),
`tools/content.py` (project archetypes and the PIR), `tools/business_case.py` (the Business
Case) or `tools/project_charter.py` (the Project Charter) and run, with the Python environment of PROTEUS. Every section of the project
archetypes gets a guidance comment with what it contains and the objects to use in it (their
class label and toolbar tab, built by `tools/guidance.py` from the model, so they stay up to
date):

```
python tools/gen.py
```

The icons of the PM² classes are drawn in `tools/icons.py`: `python tools/icons.py` writes
each one to `icons/` (toolbar, tree and menus) and to `xslt/default/resources/images/` (the
class pills of the HTML view, which load `templates:///default/resources/images/<class>.png`).

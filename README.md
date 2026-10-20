# PM² profile

Bilingual (English/Spanish) [PROTEUS](https://github.com/proteus-University-of-Seville/proteus-core)
profile for the [PM²](https://www.pm2alliance.eu/) project management methodology. It extends the
archetypes of the `basic` profile with the artefacts of the initiating phase, starting with the
**Project Initiation Request** (PIR).

## Usage

Point PROTEUS at this folder in the settings dialog, or in `proteus.ini`:

```ini
[settings]
using_default_profile = False
custom_profile_path = C:/proteus-profiles/pm2
```

Then create a project from one of the project archetypes:

- **PM² project** (`pm2-empty`): a Project Initiation Request with its sections and guidance,
  and a document for the organisations and stakeholders of the project.
- **Electronic management of final projects** (`pm2-sample`): a complete sample PIR for a
  school of the University of Seville (people and figures are fictitious).

## Conceptual model

One class per PM² concept, not per document: the PIR identifies these elements at a high
level, and the Business Case and the Project Charter refine the same objects. Every list item
is a traceable object with a code; people and organisations are the `stakeholder` and
`organization` archetypes of `basic`, and the PM² roles are traces to them.

| Class | Code | Main properties | Traces |
| --- | --- | --- | --- |
| `initiation-request` | | initiator, organisation/unit, PO, SP, approving authority, dates, estimated effort (person-days), other costs, type of delivery | to stakeholders and organisations |
| `business-situation` | SIT- | kind (need, problem, opportunity) | |
| `strategic-goal` | SG- | | owner → organisation |
| `legal-basis` | LB- | kind, reference (URL) | supports → strategic goal |
| `outcome` | OUT- | | addresses → business situation, contributes to → strategic goal |
| `impact` | IMP- | perspective, area, caused by (current situation or solution) | affects → stakeholder, organisation |
| `success-criterion` | SC- | dimension (scope, schedule, cost...), target | evaluates → outcome |
| `assumption` | ASM- | area, validation | may become → risk |
| `constraint` | CON- | area | |
| `risk` | RSK- | the columns of the PM² Risk Log: category, status, likelihood, impact, owner, response strategy, actions, escalation | related to → assumption, constraint |
| `document-control` | | approvals and revisions of the document (children) | |
| `approval` | | approver, action (approve, review) | approver → stakeholder |
| `revision` | | revision, author, changes | created by → stakeholder |

PIR documents are plain `:Proteus-document` objects with the PM² document control properties
(sensitivity, author, project manager, location).

The default view and the LaTeX template are those of `basic`, plus two modules
(`archetypes/pm2/`): the document control block (control information, approvers and
reviewers, history) and the risk, which shows its level (likelihood × impact) in the header.

## Toolbar

The archetypes are grouped by kind of concept, not by PM² phase, so that the artefacts of the
next phases add buttons to the same tabs:

| Tab | Buttons |
| --- | --- |
| Document | section, appendix, paragraph, comment, figure, symbolic link |
| Organisation | organisation, stakeholder, meeting, document control (approvals and revisions in its context menu) |
| Rationale | project initiation request, business situation, strategic goal, legal basis, outcome, impact |
| Conditions | success criterion, assumption, constraint, risk |
| References | glossary item, bibliography item, traceability matrix |

## Regenerating the archetypes

The PM² archetypes, the `objects.xml` of every tab (`TABS` in `tools/model.py`, which also
places the archetypes copied from `basic`), the `pm2_*.yaml` translations and the project
archetypes are generated from a single definition, so that both languages keep the same ids,
classes and properties. Change `tools/model.py` (archetypes, tabs and labels) or
`tools/content.py` (project archetypes) and run, with the Python environment of PROTEUS:

```
python tools/gen.py
```

The icons of the PM² classes are drawn in `tools/icons.py`:
`python tools/icons.py icons`.

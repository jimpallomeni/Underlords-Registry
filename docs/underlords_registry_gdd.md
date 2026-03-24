# The Underlord's Registry
## Game Design Document — Series Bible & Season One

**Version 1.0 | Solo Development | Top-Down Management RPG**

---

> *Hell is a corporation. You are middle management. Something is very wrong with the org chart.*

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [The World — The Infernal Bureaucracy](#2-the-world--the-infernal-bureaucracy)
3. [Series Structure & Arc](#3-series-structure--arc)
4. [Gameplay Systems](#4-gameplay-systems)
5. [Season One — The Department of Final Intake](#5-season-one--the-department-of-final-intake)
6. [Art Direction & Audio](#6-art-direction--audio)
7. [Solo Development Strategy](#7-solo-development-strategy)
8. [Appendices](#8-appendices)

---

# 1. Project Overview

| Field | Details |
|---|---|
| **Title** | The Underlord's Registry — Season One: The Department of Final Intake |
| **Genre** | Top-Down Management RPG / Dark Comedy |
| **Platform** | PC (Windows, Linux, Mac) — Console to follow |
| **Engine** | Godot 4 |
| **Team Size** | Solo Developer |
| **Target Rating** | M (Mature) — Dark themes, bureaucratic horror, dark comedy |
| **Tone** | Darkly comic. Office satire slowly curdling into something much worse. |
| **Series Arc** | Episodic — 3 seasons planned, each in a different department, each closer to the truth |
| **Target Audience** | Fans of Disco Elysium, Papers Please, Hades, Untitled Goose Game (the spite version) |

## Elevator Pitch

Hell is not fire and brimstone. It is fluorescent lighting, outdated software, mandatory training seminars, and a HR department that processes ten billion souls per fiscal year. You are a mid-level bureaucrat in the Infernal Registry — the department responsible for classifying, processing, and routing newly arrived souls. The work is tedious. Your supervisor is incompetent. Your coworkers are hiding something. And the forms you've been stamping CONDEMNED without reading for six years may have been routing the wrong souls to the wrong places for a very long time. Each season takes place in a new department. The overarching mystery: the entire afterlife is a front. The question is for what.

## Core Design Philosophy

- Comedy is the entry point. Horror is the destination. The transition should be imperceptible until it isn't.
- The mundane is the mechanism. Stamping forms, filing reports, and navigating office politics are how the player interacts with the world — and how the world's wrongness slowly reveals itself.
- Every system that seems like satire is also a clue.
- Constraints create character. The player character is not a hero. They are a bureaucrat who became inconvenient.
- Tone shifts are earned, not cheap. The darkness only lands because the comedy was genuine.

---

# 2. The World — The Infernal Bureaucracy

## Concept

The afterlife operates as a multi-tiered corporate structure called the Infernal Bureaucracy, headquartered in a structure known simply as the Registry — a building of indeterminate size that has been under renovation for approximately four thousand years. The Registry processes the newly dead, assigns them to appropriate eternal arrangements, manages appeals, handles exceptions, and produces an almost incomprehensible volume of paperwork.

Hell, as traditionally imagined, exists — but it is one of many contract-managed facilities in a vendor relationship with the Registry. Heaven also exists, in some form, and is also in a vendor relationship with the Registry. Neither vendor has ever met with Registry leadership in living memory. Complaints from both go to a ticketing system that has a current backlog of eleven million unread items.

Most Registry employees have no idea what the organization actually does. They have job titles, performance reviews, and a subsidized cafeteria. This is enough.

## The Registry's Structure

| Division | Function | Public-Facing? |
|---|---|---|
| **Department of Final Intake** | Processes newly arrived souls. First point of contact. | Yes |
| **Department of Classification** | Determines each soul's eternal assignment. Highly secretive. | No |
| **Department of Appeals** | Handles disputes from souls contesting their assignment. Perpetually backlogged. | Yes |
| **Department of Special Circumstances** | Processes unusual cases — saints, demons, the technically still-living, etc. | Restricted |
| **Office of Institutional Memory** | Maintains Registry records going back to the founding. No one has ever seen the deepest archives. | No |
| **Executive Suite** | The leadership of the Registry. No employee below Senior Director has ever seen a member of the Executive Suite in person. | No |

## The Registry as a Place

The Registry is a building in the way that an ocean is wet — technically accurate, vastly insufficient. Different floors have different architectures, different lighting temperatures, different apparent eras of construction. The lower floors, accessed only by employees with Clearance Level 4 or above, are rumored to predate the concept of buildings. The cafeteria is inexplicably excellent. The coffee is the worst anyone has ever had. No one has ever reconciled this.

Notable locations:

### The Intake Floor
Ground level. Fluorescent-lit open-plan office. Soul Processing Terminals. Filing cabinets. The ambient sound of ten thousand people trying to remember their passwords. The Intake Floor is where Season One takes place.

### The Atrium
The central vertical space of the Registry. Looking up from the ground floor, the building appears to extend upward without visible end. Looking down from any floor, the Atrium appears to go equally far in that direction. The Registry maintains that the building has forty-seven floors. It does not explain the Atrium.

### The Archival Depths
Subbasements containing physical records predating digital systems — which at the Registry means records predating writing. Physical access requires Clearance Level 5. The records room is staffed by an archivist who has been there since the Registry was founded and who seems, upon extended acquaintance, to not quite be a person.

### The Executive Suite
Rumored to occupy the highest floors. No one in the player's part of the building has ever been above floor twelve. The elevator has buttons for floors 1–12 and then, after a gap, a button marked simply with a small circle. No one has pressed it. It glows faintly.

## Factions & Power Players

### Registry Management (The Supervisors)
The layer of middle and senior management that runs day-to-day operations. Mostly focused on metrics, quarterly reviews, and not attracting the attention of the Executive Suite. Several of them know something is wrong. None of them are doing anything about it.

### The Union
The Registry Workers Union has existed since approximately the second century CE and has never successfully negotiated a single demand. It continues to exist. It continues to try. Its current shop steward is the most competent person in the building.

### The Condemned (NPC Pool)
The souls flowing through the Intake process. Each is a person — with history, complaints, personality, and, frequently, information the player needs. Treating them well is not required. It matters anyway.

### The Auditors
An external oversight body that arrives periodically to review Registry operations. No one knows who they report to. When they come, things that were hidden get found. When they leave, sometimes things that existed no longer do.

### The Older Staff
A small number of Registry employees who have been here much longer than any HR record reflects. They are not forthcoming. They are not hostile. They watch. When the player starts asking the right questions, the Older Staff begin to notice.

---

# 3. Series Structure & Arc

## The Three-Season Arc

The Underlord's Registry is designed as a three-season series, each season set in a different department of the Registry. Each season escalates the player's understanding of what the Registry actually is and what it is concealing. Comedy remains present throughout — it just increasingly coexists with something much less funny.

| Season | Department | Central Question |
|---|---|---|
| **Season 1: Final Intake** | Department of Final Intake | Why are certain souls being misrouted, and who benefits? |
| **Season 2: Special Circumstances** | Department of Special Circumstances | What are the exceptions the Registry has been hiding? What category of being generates a "Special Circumstance" file? |
| **Season 3: The Office of Institutional Memory** | Deepest Archives | What did the Registry exist to do before it became what it is? Who founded it, and why? What is behind the door in the lowest archive? |

## Series-Wide Lore Threads

- The Registry was not always called the Registry. Its original name appears in no surviving document, but certain very old employees respond to it as though hearing their own name called.
- Souls are not the only thing being processed. The forms have fields that standard intake procedures never populate. What goes in them, and when, is Season Two's first mystery.
- The Executive Suite communicates exclusively through memos. The memos are in a language everyone can read but no one can remember after reading.
- The Auditors are not from any external body anyone can name. They have been auditing the Registry since before anyone currently employed can remember. They have never found a discrepancy. This is statistically impossible.

## Episode Structure Within Season One

| Episode | Title & Hook |
|---|---|
| **Episode 1** | *Standard Processing* — Your first day back after medical leave. The forms have changed. Your predecessor's desk has been emptied. No one will say where she went. |
| **Episode 2** | *The Backlog* — A processing error from six years ago has surfaced: 40,000 souls sent to the wrong eternal assignment. You are asked to quietly correct it. The correction forms don't exist. |
| **Episode 3** | *An Appeal* — A soul contests their assignment with documentation that should be impossible to have. The Appeals department refuses to take the case. It lands on your desk. |
| **Episode 4** | *The Audit* — The Auditors arrive. You have three days to make sure they don't find what you've found. Or to make sure they do. |
| **Episode 5** | *Classification Review* — You are offered a promotion to the Department of Classification. The offer is not optional. What you see on your first day there ends Season One and begins Season Two. |

---

# 4. Gameplay Systems

## Core Gameplay Loop

> **Receive assignment → Process cases (forms, interviews, decisions) → Investigate irregularities → Navigate office politics → Escalate or suppress what you've found → Live with your filing decisions.**

## Perspective & Controls

Top-down view of the Intake Floor office environment. WASD movement. Interaction via mouse cursor. The player moves between their desk, coworkers' desks, the Soul Processing Terminals, filing areas, the break room, and other office spaces. The building's layout expands as the player's clearance and story progress allow access to new floors and restricted areas.

## The Processing System

### The Soul Processing Terminal

The player's primary interface. Each work shift presents a queue of souls to process. Each soul has a file: name, date of death, relevant biographical details, and a set of form fields requiring decisions. Standard processing is fast and routine. Irregularities require investigation.

Processing decisions the player makes are tracked. Souls are not abstractions — they have names, stories, and (occasionally) faces. Routing a soul incorrectly has consequences the player may not see until much later.

### Form Taxonomy

| Form Type | Purpose | Complication |
|---|---|---|
| **Form 7-A: Standard Intake** | Routes souls to standard assignment queues. | Routine, until it isn't. |
| **Form 7-B: Contested Identity** | Used when a soul's identity cannot be verified. | Requires supervisor co-sign. Supervisors avoid this. |
| **Form 9: Hold & Review** | Flags a soul for further review. Removes them from the standard queue. | Triggers a departmental inquiry. Use carefully. |
| **Form 12: Special Circumstances Referral** | Routes a soul to the Department of Special Circumstances. | Requires Clearance Level 3. Generates an Auditor notification. |
| **Form 0: Classification Override** | Supersedes the assigned classification. | Requires Clearance Level 5. The player should not have this form. They will find one anyway. |

### The Irregularity Log

As the player processes cases, they accumulate an Irregularity Log — a personal record of anomalies, inconsistencies, and things that don't add up. This functions similarly to The Pale Commission's evidence board: the player manually connects entries. Confirmed connections unlock new dialogue options, restricted areas, or additional forms. The Irregularity Log is personal — it is not an official Registry document. Keeping it is, technically, a violation of information policy.

## Office Navigation & Social Systems

### Coworker Relationships

The player works alongside a small cast of coworkers, each with their own knowledge, loyalties, and limits. Relationships develop based on how the player interacts with them across the season. Some coworkers will share information with a trusted colleague that they will never put in writing. Some coworkers are reporting on the player to someone. Some coworkers are doing both.

### The Approval System

Certain actions require sign-off from supervisors or colleagues. The Approval System models office politics directly: getting approval requires understanding what a person wants, what they fear, and what they're already covering up. Approval can be obtained through:

- **Legitimate channels** — Follow procedure. Slow. Sometimes impossible.
- **Favors** — Help a coworker with their problem first. Creates mutual obligation.
- **Leverage** — You know something. They know you know. This creates options and enemies simultaneously.
- **Forgery** — The forms have signatures. Signatures can be learned. The risk scales with what's being signed.

### Shift Management

Work happens in shifts. Each shift has a quota — a number of souls that must be processed before the shift ends. Falling short of quota generates a Performance Warning. Three warnings in a season triggers a formal review. The formal review is not the worst thing that can happen, but it is in the top five.

Time spent investigating is time not spent processing. This is the game's central tension: doing the job, or understanding what the job actually is.

## Character Progression

### Professional Standing

The player has a Professional Standing score tracked by the Registry's HR system. It reflects performance reviews, quota completion, disciplinary actions, and commendations. High Standing opens access to better resources and more cooperative supervisors. Low Standing attracts scrutiny. The player can game this system — up to a point.

### Unofficial Knowledge

Separate from Professional Standing, the player accumulates Unofficial Knowledge — a hidden score representing how much they actually understand about the Registry's true operations. This score is not displayed numerically; it manifests as changes in how the Older Staff and other key NPCs interact with the player. At certain thresholds, new options become available. At the highest levels, certain doors open that the Registry would prefer stayed closed.

### The Player Character's Voice

The protagonist is not defined by class selection or background choices. Their personality emerges through dialogue decisions across the season. The game tracks the player's dominant tone: **Sardonic**, **Diligent**, **Compassionate**, or **Complicit**. Each tone unlocks distinct internal observations and NPC reactions, and determines how the protagonist processes (in both senses) what they're discovering.

---

# 5. Season One — The Department of Final Intake

## Setting

The Intake Floor. A large open-plan office on the Registry's ground level. Rows of Soul Processing Terminals. Cubicles. A break room with a microwave that has never been cleaned. Emergency exits that, per Registry policy, cannot be used by employees for entry or exit during standard processing hours. A supervisor's office with blinds that are always partially closed. An elevator that the player cannot access above floor three until Episode Four.

The Intake Floor has been here, in this configuration, for approximately eight hundred years of internal Registry time. The carpet pattern has not been updated. There is a suggestion box that is bolted shut. A sign above the door reads: **YOUR WORK IS ETERNAL. MAKE IT COUNT.**

## The Protagonist: Registry Processor Second Class, Designation K-7 (Kael)

> *You have been here for six years. You are good at the job. You recently took medical leave for reasons the HR record lists as "personal circumstances" and which you do not discuss. Your predecessor at this desk, a woman named Mira, left while you were gone. The file says she transferred. The box under her desk still has her mug in it.*

| Field | Details |
|---|---|
| **Role** | Registry Processor, Second Class, Intake Floor |
| **Tenure** | Six years, returning from medical leave |
| **Clearance Level** | 2 (Standard) at episode start |
| **Starting Relationships** | Supervisor: Cautious / Union: Neutral / Coworkers: Familiar but distant |
| **Personal Arc** | Kael returned to work because routine felt safer than thinking. The job will not allow them to stop thinking. |

*Note: Kael's name and pronouns are player-selected at the start of Season One.*

## Key Characters

| Name | Role | What They Know | What They're Hiding |
|---|---|---|---|
| **Supervisor Dolen** | Department head, Intake Floor | Something went wrong with the routing system six years ago | He reported it. The report was filed. Nothing happened. He hasn't asked why. |
| **Pressa** | Senior Processor, 40+ years tenure | More than she lets on. She was here before the current HR system. | Why she's still here. What she saw that made her stop asking questions. |
| **Fen** | Union Shop Steward, Kael's desk neighbor | Every procedural violation the department has committed in the last decade | He keeps copies. He's never been able to use them. He's waiting for someone to help. |
| **The Soul in Terminal 7** | A soul that refuses to move through standard processing | Their own case, which doesn't fit any existing form | They are not the first soul to refuse. The others were routed anyway. |
| **Director Amm** | Senior Director, Registry-wide | The scope of the misrouting problem | That correcting it would require acknowledging it. This is unacceptable. |
| **The Archivist** | Subbasement records, designation unknown | Everything | Nothing they have chosen to share yet |

## Episode Breakdown

### Episode 1: Standard Processing

Kael returns from medical leave. The forms have been updated. A mandatory reorientation session covers changes to policy. Kael's predecessor's desk has been cleaned out. HR's answer: "transfer." The new routing system flags an unusual number of souls for Exception Hold — a rate that shouldn't be mathematically possible given the standard distribution. Kael's first investigation begins as an attempt to fix a processing error and becomes something else by the end of the shift.

**Key Mechanic Introduced:** The Processing Terminal and standard form workflow.
**Mystery Hook:** Why is the Exception Hold rate 0.3%? It should be 0.003%.

### Episode 2: The Backlog

A routine audit of Kael's historical case files surfaces a systematic error spanning six years: a classification modifier that was applied to a specific soul profile type has been routing them to an incorrect eternal assignment. The number of affected souls: approximately 40,000. Supervisor Dolen asks Kael to quietly run a correction. The correction form (Form 11-C: Retroactive Classification Adjustment) does not exist in the current form library. It exists in the archive. The archive access requires Clearance Level 3. Kael has Level 2. This is solvable. The solution introduces Kael to Fen, the Union, and the concept that the Registry's policies may be designed to prevent exactly this kind of correction.

**Key Mechanic Introduced:** Approval System and Leverage chains.
**Mystery Hook:** The 40,000 souls were all routed to the same non-standard destination — a facility code that doesn't appear in any public Registry directory.

### Episode 3: An Appeal

A soul in the standard queue — designation A-1109, previously unremarkable — produces documentation contesting their eternal assignment. The documentation includes a Registry form that was discontinued approximately 300 years ago, filled out correctly, referencing case law that predates the current afterlife administrative framework. The Appeals department declines jurisdiction on procedural grounds. The soul's file lands back on Kael's desk with a sticky note from Supervisor Dolen: *Handle this.*

Kael cannot process A-1109 normally. A-1109 is also, in the way of souls with no remaining options, completely willing to talk. At length.

**Key Mechanic Introduced:** Extended soul interview system.
**Mystery Hook:** A-1109 knows about the facility code from Episode 2. She was almost sent there. She wasn't, because of a form error that she has spent her entire afterlife being grateful for.

### Episode 4: The Audit

The Auditors arrive. Three individuals. No stated organizational affiliation. Clearance that supersedes anything currently employed staff possess. They will be on-site for seventy-two hours. Kael has an Irregularity Log containing evidence of systematic misrouting, a 40,000-soul correction that was never filed, and testimony from a soul that shouldn't have that information. They have three days to decide: bury it, surface it carefully, or hand it directly to the Auditors and see what happens. All three paths are playable. None of them are safe.

**Key Mechanic Introduced:** Timed decision windows; consequences branch significantly here.
**Mystery Hook:** One of the three Auditors is the same person as someone Kael has been told is dead. Or was never alive. The HR records on all three predate the HR system.

### Episode 5: Classification Review

Regardless of how Episode 4 resolves, Kael receives a promotion offer to the Department of Classification — framed as a reward. The offer comes with a memo written in the Executive Suite's characteristic language (readable in the moment, forgotten afterward). The player has one shift to decide whether to take it, resist it, or attempt to use the situation to surface what they've found. The episode ends with Kael's first day in Classification. The final scene is a single establishing shot of the Classification floor. The player's last input is choosing which terminal to sit at. The screen fades to black. The Season Two hook text appears.

**Key Mechanic Introduced:** Season transition — choices made across Season One determine Kael's starting reputation, available resources, and which NPCs survived the transition in Season Two.

## Season One Endings

Season One does not have a single "correct" resolution. The Auditors depart. The misrouting may be corrected, publicly acknowledged, buried again, or have triggered a process that is now beyond any single employee's control. The forty thousand souls have been routed somewhere. Whether it was the right somewhere depends on what the player did in Episode 2.

The measure of a Season One "win" is not whether Kael exposed the truth. It is whether Kael knows what truth they are now carrying into Classification.

---

# 6. Art Direction & Audio

## Visual Style

Top-down office environment rendered in a deliberately constrained palette — fluorescent-gray, institutional beige, the particular green of old carpet. Think 1980s government building. The contrast between the mundane visual language and the increasingly strange content is intentional and should never be resolved in the art direction's favor. Even when deeply weird things are happening, the fluorescents stay on.

Character sprites are expressive, slightly stylized, and readable at top-down scale. Soul sprites use a distinct visual treatment — slightly translucent, slightly de-saturated — that marks them as categorically different from Registry employees without being overtly supernatural.

Environmental storytelling carries significant weight. Players who look at the right walls, read the right notices, and check the right filing cabinets will find a secondary layer of narrative that the main plot never explicitly states.

## Environmental Color Language

| Location | Palette | Atmosphere |
|---|---|---|
| **Intake Floor** | Fluorescent white, institutional gray-green, beige | Familiar, slightly oppressive, theoretically normal |
| **Break Room** | Warmer tones, worn surfaces, actual color | The only genuinely human space in the building |
| **Supervisor's Office** | Darker, more saturated, more deliberate | Someone chose this. That's notable. |
| **Subbasement Archives** | Deep amber, old paper, deep shadow | Something is being preserved down here |
| **Classification Floor** (Season 2) | Unknown, deliberately withheld from Season 1 assets | The player's imagination is the best asset here |

## Music

The score lives in the space between elevator music and ambient dread. Upbeat corporate-adjacent themes for standard processing shifts, slowing and deepening as investigations develop. Key scenes use a recurring musical phrase — something almost cheerful — that begins to acquire dissonance as the season progresses. By Episode 5, the same phrase sounds like a warning. It was always a warning.

Environmental audio: the hum of Soul Processing Terminals, distant typing, a phone that rings occasionally with no one on the other end, the particular silence of the Registry at night.

## Sound Design

- The Registry's ambient audio is designed to feel like a real office — until the player pays close attention to it. The typing is slightly irregular. The ventilation sounds like breathing when no one is near it.
- Each soul has a distinct audio signature — a brief musical motif — that plays when their file is opened. Some motifs recur. The player may not consciously notice until it's pointed out.
- The elevator is always slightly slower than it should be. This is represented in sound.

---

# 7. Solo Development Strategy

## Why This Game Works for Solo Development

The Underlord's Registry is built around dialogue, environmental storytelling, and form-based mechanics — all areas where writing and design quality outweigh production volume. The office setting severely limits required art assets: one main tileset, a small cast of recurring characters, and a tight location set that expands deliberately rather than all at once.

The dark comedy tone is a practical asset as well as a narrative one: a slightly rough visual edge or a recycled asset reads as intentional in a game about corporate underinvestment. The aesthetic forgives, to a degree, what the budget cannot solve.

## Scope Principles

- Season One takes place almost entirely on one floor of one building. This is intentional. The world expands in Season Two.
- The Processing Terminal mechanic is the mechanical heart — all other systems feed into or out of it. Scope the combat and exploration relative to this, not as their own systems.
- NPCs are the primary content. A richly characterized cast of eight is worth more than a large cast of thin ones.
- No voice acting in Season One. A single narrator voice for key transitions only.

## Development Status

| Deliverable | Status | Location |
|---|---|---|
| Game Design Document | Complete | `docs/underlords_registry_gdd.md` |
| Core Mystery Bible | Locked | Appendix C (this document) |
| Episode 1 Script | Complete | `scripts/episode_1_standard_processing.md` |
| Episode 2 Script | Not Started | — |
| Episode 3 Script | Not Started | — |
| Episode 4 Script | Not Started | — |
| Episode 5 Script | Not Started | — |
| Godot Prototype | Not Started | — |

## Development Phases — Season One

| Phase | Description | Est. Duration |
|---|---|---|
| **Phase 1 — Prototype** | Processing terminal loop, basic form workflow, movement and interaction. | 6–8 weeks |
| **Phase 2 — Vertical Slice** | Episode 1 complete: Intake Floor functional, Dolen and Fen fully written, one soul interaction loop. | 8 weeks |
| **Phase 3 — Content Build** | All five episodes, all characters, Irregularity Log system, Approval chains. | 14–18 weeks |
| **Phase 4 — Polish** | Audio, environmental storytelling layer, playtesting, balance. | 6–8 weeks |
| **Phase 5 — Release** | PC via Steam. Demo: Episode 1 only. Post-launch support, begin Season Two. | — |

## Engine: Godot 4

- Same rationale as The Pale Commission. Strong 2D pipeline, zero licensing cost, active community.
- The Processing Terminal UI is an ideal use case for Godot's Control node system.
- Dialogic 2 plugin handles dialogue trees without building a custom system.

## Risk Management

| Risk | Likelihood | Mitigation |
|---|---|---|
| Tone balance — comedy vs. horror | High | Playtest early and often specifically for tone. The horror should feel earned, not sudden. |
| Form mechanics becoming tedious | Medium | Each episode introduces a new form or wrinkle. Routine is the setup; disruption is the game. |
| NPC cast becoming too large | Medium | Cap at 8 named recurring NPCs. Additional characters are souls (episodic, non-recurring). |
| World-building overwhelm | Medium | The Registry's mysteries should always be one layer deeper than what the player can currently access. Don't resolve what you don't need to. |
| Art consistency across a long dev cycle | Low–Medium | Finalize and lock the tileset and character style guide before Phase 3. |

## Monetization

- Season One: Premium purchase, $12.99 USD. Episodes released as free updates.
- Season Two and Three: Separate purchases with returning-player discount.
- Optional: Lore compendium / "Registry Employee Handbook" PDF at launch — low production cost, adds worldbuilding depth for engaged players.
- No microtransactions.

---

# 8. Appendices

## Appendix A: Glossary

| Term | Definition |
|---|---|
| **The Registry** | The Infernal Bureaucracy's central administrative body. Processes souls and manages the afterlife's operational infrastructure. |
| **The Intake Floor** | Ground-level department responsible for initial soul processing. Season One's primary setting. |
| **Soul Processing Terminal** | The player's primary workstation. Displays soul files and the form interface. |
| **Form 0** | Classification Override form. Clearance Level 5 required. The player should not have this. |
| **Exception Hold** | A processing status that removes a soul from the standard queue pending review. |
| **Irregularity Log** | The player's personal record of anomalies. Unofficial. Technically a policy violation. |
| **Professional Standing** | The Registry's official metric of employee performance. |
| **Unofficial Knowledge** | Hidden score tracking how much the player understands about the Registry's true nature. |
| **The Auditors** | External oversight body. Unclear who they report to. Their clearance supersedes all staff. |
| **The Older Staff** | Registry employees whose tenure predates any HR record. They know things. |
| **The Executive Suite** | Registry leadership. Communicates only by memo. No employee below Senior Director has seen them. |

## Appendix B: Tone Reference

The Underlord's Registry sits at the intersection of several distinct tonal registers, and maintaining the balance between them is the primary creative challenge of the series.

- **The Office / Parks and Recreation** — Workplace comedy grounded in recognizable human dynamics
- **Kafka / The Trial** — Bureaucracy as existential trap; systems that cannot be reasoned with
- **Disco Elysium** — Interior monologue as characterization; politics embedded in every interaction
- **Papers Please** — Complicity through routine; the violence of the stamp
- **Hades** — Repeated systems revealing character and story over time
- **The Magnus Archives** — Horror that builds through accumulation, not incident

## Appendix C: Core Mystery Bible

The following answers are locked for series continuity. All writing must align with these decisions.

### What is the Registry actually concealing?

**The Registry predates the afterlife. Souls are a retrofit.**

The Registry was not built to process the dead. It is far older than death as a concept. The forms, the architecture, the Clearance Levels, the entire bureaucratic infrastructure existed before souls entered the system. Something else was being processed first—something the current documentation never names.

When the afterlife was created (or discovered, or conquered—the truth is unclear), souls were routed into the existing system as a workaround. The forms were adapted. New departments were created. But the original system never stopped running. It continues underneath, in parallel, using the same infrastructure.

The 40,000 misrouted souls weren't sent to the wrong afterlife destination. They were sent to the *original* system—the one that predates Heaven, Hell, and the entire soul-processing framework. What happens to them there is Season 2's central question.

This explains:
- Why the Older Staff predate HR records (they were here before HR existed)
- Why the Archivist "isn't quite a person" (they predate personhood)
- Why the subbasement archives contain records from before writing (the system predates language)
- Why the Executive Suite communicates in a language no one remembers after reading (it's the original operating language)

### What are the Auditors?

**The Auditors are refugees from the original system—whatever was being processed before souls.**

When the Registry was repurposed for soul processing, the original "clients" (for lack of a better term) were grandfathered into administrative roles. The Auditors are what remains of them. They were given oversight authority because they remember what the Registry was supposed to do.

They can never find discrepancies because, from their perspective, *processing souls is the discrepancy*. The entire afterlife is an anomaly running on their infrastructure. They audit not to find errors in soul processing, but to monitor how much of the original system remains intact underneath.

The Auditors appear humanoid because that's how souls perceive them—but their HR records predate the HR system because they predate the concept of employment. They don't report to anyone in the current hierarchy because they predate the hierarchy.

One Auditor being "the same person" as someone Kael knew who died is not a continuity error. The Auditors occasionally incorporate souls who get too close to understanding what they are. It's not malicious. It's administrative.

The Older Staff (Pressa, the Archivist, others) are on the same trajectory. Enough time in the Registry, enough exposure to the original system, and the boundary between "employee" and "Auditor" begins to blur. The "promotion" to Classification that Kael receives is a step on this path.

### Does the player have an inventory?

**The Irregularity Log is the inventory.**

There is no separate inventory system. Physical items (keycards, Form 0 copies, Mira's mug, evidence documents) are logged as entries in the Irregularity Log alongside observations and connections.

The Log functions as a hybrid journal/evidence board/inventory:
- **Observations** — Things Kael notices (text entries)
- **Evidence** — Physical items logged as documentation (usable in conversations/terminals)
- **Connections** — Player-drawn links between entries that unlock new options

Items are "used" by presenting them—selecting an evidence entry during dialogue or at a terminal. This reinforces the core theme: in the Registry, *documentation is power*. You don't "have" things; you have *records* of things.

Implementation note: The Log should be accessible at any time via hotkey. Evidence entries show a small icon distinguishing them from observation entries. Maximum ~30 entries per episode to prevent overwhelm; older routine observations auto-archive.

### How much of the 40,000-soul misrouting can the player correct?

**A handful of personal interventions, plus a variable systemic outcome.**

The player cannot personally reroute 40,000 souls. The scale is beyond any individual employee's capacity, and that's the point—systemic failures require systemic solutions.

However, the player can:

1. **Directly intervene for 5-10 specific souls** encountered during Episodes 2-4. These are named NPCs with faces and stories. The player can pull them from the misroute queue, flag them for manual review, or (with enough leverage) get them properly classified. Each successful intervention is visible and emotionally resonant.

2. **Influence the systemic outcome** through cumulative choices. Player decisions across the season determine what happens to the remaining 39,990:

| Path | Outcome | Epilogue Number |
|------|---------|-----------------|
| Bury it | Problem remains hidden; misrouting continues | 0 corrected |
| Quiet fix | Supervisor Dolen's original request; partial correction | Hundreds corrected |
| Public acknowledgment | Force official recognition; triggers review process | Thousands flagged for correction |
| Auditor intervention | Hand evidence to Auditors; they act on it | All 40,000 addressed—but "addressed" by Auditors means something different than Kael intended |

The final number is revealed in the Season 1 epilogue as a Registry memo. The tone of the memo varies based on outcome (triumphant, bureaucratic, ominous, or redacted).

Season 2 starting conditions vary based on this outcome—primarily in NPC attitudes toward Kael and whether certain characters survived the fallout.

### Does Kael have internal monologue?

**Minimal observations at key moments. Not a running commentary—punctuation.**

Kael is not a silent protagonist, but neither do they have constant internal narration. Internal voice appears as brief, single-sentence observations at significant beats:

- **First encounters** — When Kael sees something strange for the first time, a line of internal reaction contextualizes it.
- **Moral weight moments** — When a choice matters, Kael's internal voice can surface the stakes without dictating the "right" answer.
- **Callbacks** — When something connects to an earlier discovery, Kael's recognition makes the connection explicit for players who missed it.
- **Tone expression** — The Sardonic/Diligent/Compassionate/Complicit tone tracking manifests here. The same moment might prompt different internal lines based on Kael's established voice.

Target volume: **20-30 internal lines per episode**. This is enough to characterize without overwhelming, and keeps writing scope manageable.

Example (same moment, different tones):
- **Sardonic:** *The form asks for "reason for existence." There's no box for "still figuring that out."*
- **Diligent:** *Form 7-B, Section 12. I've never seen this field populated. Time to find out why.*
- **Compassionate:** *She's been waiting six years for someone to read her file. I'm reading it.*
- **Complicit:** *If I don't see the problem, there's no problem to report.*

### What is on floor 13?

**Not yet locked. Tentative direction: where the original system still runs.**

Floor 13 is reserved as Season 3's final revelation. It should accrue mystery through Seasons 1-2 without being directly addressed.

Working hypothesis (to be confirmed before Season 3 writing):

The elevator goes 1-12, then the circle button. Floor 13 is not skipped—the building's architecture simply doesn't include it. Official Registry position: Floor 13 does not exist.

The truth: Floor 13 is not a floor. It's a *depth*. The Office of Institutional Memory's lowest archive—the one requiring Clearance Level 5, staffed by the Archivist—eventually opens onto it. The facility code from the 40,000-soul misrouting resolves to Floor 13. It's where the original system continues to run.

What's there: The answer to what was being processed before souls. The reason the Registry was built. The thing the Executive Suite has been managing since before "management" existed.

Season 1 references to Floor 13 should be:
- The elevator button gap (visible but uncommented)
- One NPC aside ("They used to say thirteen was bad luck. Now they just say it isn't.")
- A single line in a very old document in the Archival Depths, listing a department that was "relocated to Floor 13" before the relocation was struck from the record

Do not explain. Do not elaborate. Let it accrue.

---

*The Underlord's Registry | Game Design Document | Version 1.0 | Confidential — Internal Development Document*

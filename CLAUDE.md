# The Underlord's Registry — Project Memory

## Project Overview

**Title:** The Underlord's Registry — Season One: The Department of Final Intake
**Genre:** Top-Down Management RPG / Dark Comedy
**Engine:** Godot 4
**Team:** Solo Developer

**Premise:** Hell is a corporation. You are middle management. The player is Kael, a Registry Processor returning from medical leave to discover something is very wrong with the soul processing system.

## Current Status

- **GDD:** Complete (v1.0) — `docs/underlords_registry_gdd.md`
- **Core Mystery Bible:** Locked in Appendix C of GDD
- **Episode 1 Script:** Complete — `scripts/episode_1_standard_processing.md`
- **Episode 2 Script:** Complete — `scripts/episode_2_the_backlog.md`
- **Episode 3 Script:** Complete — `scripts/episode_3_an_appeal.md`
- **Episode 4 Script:** Complete — `scripts/episode_4_the_audit.md`
- **Episode 5 Script:** Complete — `scripts/episode_5_classification_review.md`
- **SEASON ONE:** COMPLETE

## Core Lore Decisions (Locked)

These are canon and must be consistent across all content:

1. **The Registry predates the afterlife** — Souls are a retrofit to an older system
2. **The Auditors are refugees from the original system** — Whatever was processed before souls
3. **Irregularity Log = Inventory** — Hybrid journal/evidence/inventory system
4. **40,000 souls:** Player can save 5-10 personally + variable systemic outcome
5. **Kael's voice:** Minimal internal monologue (20-30 lines/episode)
6. **Floor 13:** Reserved for Season 3; tentatively "where the original system runs"

## File Structure

```
/docs
  underlords_registry_gdd.md        — Main design document

/scripts
  episode_1_standard_processing.md  — Episode 1 full script
  episode_2_the_backlog.md          — Episode 2 full script
  episode_3_an_appeal.md            — Episode 3 full script
  episode_4_the_audit.md            — Episode 4 full script
  episode_5_classification_review.md — Episode 5 full script

/godot_prototype                    — Godot 4.6 prototype (placeholder graphics)

/renpy_prototype                    — Ren'Py 8.3 prototype (noir art)
  /game
    script.rpy                      — Main Act I content
    characters.rpy                  — Character definitions
    game_state.rpy                  — GameState class
    souls.rpy                       — Soul queue generation
    screens.rpy                     — UI screens (terminal, log)
    processing.rpy                  — Terminal action handlers
    images.rpy                      — Image definitions
    /images                         — Generated art assets
    /interviews
      rebecca_thorne.rpy            — Full branching interview
  generate_art.py                   — A1111 art generation script
  art_prompts.md                    — Art generation prompts reference
```

## Episode 1 Summary

**Title:** Standard Processing
**Runtime:** 45-60 min
**Key Mechanic:** Processing Terminal, Form 7-A workflow
**Mystery Hook:** Exception Hold rate is 0.3% (should be 0.003%)

**Characters Introduced:**
- Kael (player) — Protagonist, Processor Second Class
- Supervisor Dolen — Knows more than he says
- Pressa — Ancient, warns Kael to stop asking questions
- Fen — Union steward, potential ally
- Mira (absent) — Previous processor, disappeared after investigating
- Rebecca Thorne — Exception Hold soul, former compliance auditor

**Carryover Flags:**
- Fen relationship (Alliance/Neutral/Distant)
- Irregularity Log entries (0-3)
- Mira's note (logged or not)
- Tone tracking (Sardonic/Diligent/Compassionate/Complicit)

## Episode 2 Summary

**Title:** The Backlog
**Runtime:** 50-70 min
**Key Mechanic:** Approval System and Leverage chains
**Mystery Hook:** 40,000 souls routed to F-13.PROC.LEGACY — the original processing system

**Characters Developed:**
- Supervisor Dolen — Knows the truth, chose complicity 6 years ago
- Pressa — 400 years old, knows about original system, warns Kael
- The Archivist — Ancient, shows Kael the Charter
- Director Amm — Blocking corrections deliberately

**Major Revelations:**
- The Registry predates souls — was built for "the PROCESS"
- Souls are raw material being refined into something
- The Executive Suite ordered the modifier 6 years ago
- Mira was processed into F-13 (confirmed via file E-7712)
- Exception Hold threshold was set to REVEAL the problem, not cause it

**Four Main Paths Established:**
1. LEGITIMATE — Force corrections through proper channels (slow, documented)
2. FORM 0 — Bypass authorization with Classification Override (fast, dangerous)
3. AUDITOR — Wait for external oversight in Episode 4 (medium risk)
4. COMPLICIT — Bury the truth, protect yourself (safe, soul-destroying)

**Carryover Flags:**
- Path chosen (Legitimate/Form 0/Auditor/Complicit)
- Form 0 acquired (yes/no)
- Fen relationship (Alliance/Neutral/Distant/Broken)
- Irregularity Log entries (up to 9)
- Evidence gathered (Charter, Project Legacy, Mira's file)
- Dolen relationship (varies by path)
- Archivist relationship (aware — showed Charter)

## Episode 3 Summary

**Title:** An Appeal
**Runtime:** 55-75 min
**Key Mechanic:** Extended Soul Interview System
**Mystery Hook:** Vera Okonkwo's 307-year wait, grandmother's hidden documentation

**Characters Introduced:**
- Vera Okonkwo (A-1109) — Soul waiting 307 years, grandmother was Older Staff
- Yemi Okonkwo (referenced) — Former processor who left with evidence

**Major Revelations:**
- CM-7.1.3 has been active for 339 years, not 6 years
- Total refined souls: estimated 2+ million over centuries
- Executive Suite memo (Year 3,680) proves authorization
- The PURPOSE is "approaching completion phase"
- Auditors are refined Primordials with independent judgment
- Emergency device can invoke Protocol Zero — full investigation

**Key Items Acquired (if mission accepted):**
- Form 3-Ω (classification challenge key)
- Yemi's Documentation (339 years of evidence)
- Emergency Summons Device (Protocol Zero trigger)

**Carryover Flags:**
- Vera's mission (Accepted/Deferred/Declined)
- Emergency device (acquired/not)
- Rapport with Vera (High/Medium/Low)
- Fen information level (Full/Partial/None)
- Days until Auditors: 11

## Episode 4 Summary

**Title:** The Audit
**Runtime:** 60-80 min
**Key Mechanic:** Timed Decision Windows (72-hour audit)
**Mystery Hook:** Auditor Tertiary is Mira — refined and incorporated

**The Three Auditors:**
- PRIMARY — Leans toward termination, remembers being refined
- SECONDARY — Votes for acceleration, fully supports PROCESS
- TERTIARY (Mira) — Undecided, carries ghost of Mira's values

**Major Revelations:**
- The PURPOSE: Building a vast unified consciousness from refined souls
- The Auditors are the first generation of output (refined Primordials)
- Mira was processed and became Tertiary — she left E-7712 for Kael during transition
- Protocol Zero forces a vote — majority rules, any outcome possible
- The PURPOSE is almost complete — two million souls already refined

**Ending Paths:**
1. TERMINATION (2-1 vote) — PROCESS ends, 60% of souls saved, Registry restructures
   - Oversight path: Kael joins rebuilding committee
   - Processing path: Kael continues honorable work
2. ACCELERATION (2-1 vote) — PURPOSE completes immediately
   - Witness path: Kael survives, PURPOSE exists
   - Integration path: Kael joins PURPOSE (ambiguous)
3. CLASSIFICATION — Reassignment to Classification department (Season 2 setup)
4. PROCESSED — Bad ending (escape attempt without device)

**Season 1 Resolutions:**
- Vera Okonkwo: Released after 307 years (Termination path)
- Fen: Becomes Union leader (Termination path)
- Pressa: Retires after 400 years (Termination path)
- Dolen: Demoted to processor (Termination path)
- Executive Suite: Removed from authority

## Episode 5 Summary

**Title:** Classification Review
**Runtime:** 40-55 min
**Key Mechanic:** Season Transition — all choices carry forward
**Mystery Hook:** The locked door beneath the Archives, sealed since before the Charter

**Classification Introduction:**
- Kael sees complete lives — every choice, every secret, every truth
- Standard classification: moral weight calculation, queue assignment
- Anomalous cases require Special Circumstances referral

**Key Cases:**
- C-0006: The Twelve-Lived Woman — soul with 12 conscious iterations (1847-2019)
- C-0007: Sealed case with message from "V.O." — reveals the locked door

**Final Terminal Choice (Season 2 hook):**
- Terminal 7: Investigation path (Twelve-Lived Woman)
- Terminal 9: F-13 Investigation path (Returned Soul memories)
- Terminal 13: Direct mystery path (The locked door and its key)

**Season 2 Setup:**
- The locked door beneath the Archives predates the Charter
- "V.O." is a mysterious benefactor with impossible authority
- The key to the door is a soul in Kael's queue
- Floor 13 is "a depth, not a floor" — where secrets live

## Season 2 Carryover (Established)

**Starting State:**
- Department: Classification
- Clearance: Level 4
- Supervisor: Voss

**Mysteries for Season 2:**
- The locked door (what's behind it, why it was sealed)
- What the Registry processed before souls
- V.O.'s identity (Vera Okonkwo? Someone else?)
- The Twelve-Lived Woman's origin
- What F-13 survivors remember

**NPCs Carrying Forward:**
- Vera Okonkwo (if saved)
- Fen (alliance level varies)
- Pressa (retired but may return)
- Supervisor Voss (new mentor)
- The Archivist (ally)
- Mira/Tertiary (if still exists)

## Writing Conventions

- Internal monologue uses 4 tone variants
- Player choices formatted as `**> "Choice text"**`
- Terminal interfaces use code blocks with box-drawing characters
- Scene headings: `### SCENE X.X — LOCATION`

## Godot Prototype Status

**Location:** `godot_prototype/`
**Engine:** Godot 4.6
**Status:** Core systems implemented, placeholder graphics

### Implemented Systems

| System | Status | Files |
|--------|--------|-------|
| Processing Terminal | Working | `scripts/terminal/processing_terminal.gd` |
| Player Movement | Working | `scripts/player/player.gd` |
| Dialogue System | Working | `scripts/autoload/dialogue_manager.gd` |
| Game State | Working | `scripts/autoload/game_state.gd` |
| HUD & Log | Working | `scripts/ui/hud.gd` |
| Main Menu | Working | `scripts/ui/main_menu.gd`, `scenes/ui/main_menu.tscn` |
| Pause Menu | Working | `scripts/ui/pause_menu.gd`, `scenes/ui/pause_menu.tscn` |
| Settings Panel | Working | `scripts/ui/settings_panel.gd`, `scenes/ui/settings_panel.tscn` |
| Display Settings | Working | `scripts/autoload/display_settings.gd` |
| NPC System | Working | `scripts/npc/npc.gd`, `scenes/npc.tscn` |
| Interview System | Working | `scripts/terminal/processing_terminal.gd`, `scripts/autoload/dialogue_manager.gd` |

### Interview System Details

The interview system allows players to talk to souls before deciding their fate.

**How it works:**
1. Press [3] on a soul in the terminal to start an interview
2. Terminal hides, dialogue box appears with branching choices
3. After interview ends, terminal returns with interview notes
4. Soul is marked as interviewed (can't be re-interviewed)

**Implemented interviews:**
- **Rebecca Thorne (R-0012):** 15+ dialogue nodes with branching paths. She's a former compliance auditor who reveals information about the Exception Hold anomaly. Key flags: `interviewed_rebecca`, `rebecca_hinted_metadata`, `rebecca_revealed_count`, `rebecca_revealed_discrepancies`, `rebecca_revealed_destination`
- **Generic souls:** Simple 2-node interview for non-special souls

**Story flags set during interviews** affect post-interview display (e.g., metadata hint appears if `rebecca_hinted_metadata` is set).

### Scene Structure

- `scenes/game.tscn` — Root scene with menu system (currently disabled for testing)
- `scenes/main_simple.tscn` — Self-contained game scene (current main scene)
- `scenes/npc.tscn` — Reusable NPC template (instanced for Pressa, Dolen, Fen)
- `scenes/ui/` — Menu and UI scenes

### Known Issues

- **Resolution settings:** Only work when running standalone, not in editor's embedded window
- **Display scaling:** Changed to "expand" aspect mode — higher resolutions show more world
- To test resolution changes: Run from terminal with `godot4 --path . res://scenes/main_simple.tscn`

### Controls

| Key | Action |
|-----|--------|
| WASD | Move |
| E | Interact |
| L | Toggle Irregularity Log |
| M | Toggle metadata (in terminal) |
| 1-4 | Terminal shortcuts |
| ESC | Pause menu |
| T | Debug: Open terminal |

### Placeholder Assets

Using ColorRect nodes. Recommended free assets documented in `godot_prototype/README.md`:
- Fonts: [Monogram](https://datagoblin.itch.io/monogram) (CC0)
- Tilesets: [Cainos Top Down Basic](https://cainos.itch.io/pixel-art-top-down-basic)
- Sprites: [OpenGameArt CC0](https://opengameart.org/content/cc0-resources)

### TODO

- [ ] Fix resolution/scaling in embedded editor
- [ ] Add actual sprite graphics
- [ ] Tilemap-based office environment
- [x] NPC characters (Pressa, Dolen, Fen)
- [x] Interview scenes (Rebecca Thorne + generic interviews)
- [ ] Sound effects and music
- [ ] Save/Load system UI
- [ ] Episode transitions

## Ren'Py Prototype Status

**Location:** `renpy_prototype/`
**Engine:** Ren'Py 8.3.4
**Status:** Act I playable with noir-style art

### Implemented Systems

| System | Status | Files |
|--------|--------|-------|
| Game State | Working | `game/game_state.rpy` |
| Processing Terminal | Working | `game/screens.rpy`, `game/processing.rpy` |
| Irregularity Log | Working | `game/screens.rpy` (L key toggle) |
| Soul Queue | Working | `game/souls.rpy` |
| Tone System | Working | 4-tone tracking (sardonic/diligent/compassionate/complicit) |
| Relationships | Working | -100 to 100 scale for NPCs |
| Interview System | Working | `game/interviews/rebecca_thorne.rpy` |

### Art Assets

Generated using Stable Diffusion (A1111 WebUI) with noir style.

**Characters (768x768):**
- Kael: neutral, sardonic, concerned, surprised
- Pressa: neutral, warning, disapproving
- Dolen: neutral, nervous, relieved, warning
- Fen: neutral, concerned, hopeful, disappointed
- Rebecca: neutral, guarded, intense, resigned

**Backgrounds (1280x720):**
- elevator, intake_floor, dolens_office, interview_booth, terminal_closeup, break_room

**Style:** Noir/minimalist — high contrast, dramatic lighting, limited palette, desaturated

See `renpy_prototype/art_prompts.md` for full generation prompts.

### Running the Prototype

```bash
# Using Ren'Py SDK
/path/to/renpy-sdk/renpy.sh renpy_prototype/

# Or via Ren'Py launcher, select renpy_prototype folder
```

### Controls

| Key | Action |
|-----|--------|
| Click/Enter | Advance dialogue |
| L | Toggle Irregularity Log |
| M | Toggle metadata (in terminal) |
| 1-4 | Terminal action shortcuts |
| ESC | Game menu |

### Playable Content

- Cold open (Registry welcome)
- Elevator scene (Memo 7.4.1 choice)
- Intake floor arrival
- Pressa introduction (3 dialogue branches)
- Dolen's office briefing
- Processing terminal tutorial
- Rebecca Thorne interview (15+ branching nodes)

## Next Steps

1. ~~Ren'Py prototype with Act I~~ ✓
2. ~~Generate noir-style art~~ ✓
3. Add sound effects and music
4. Continue implementing Episodes 2-5 in Ren'Py
5. Season 1 polish pass (consistency check across all 5 episodes)
6. Write Season 2 episode outlines (if continuing)

## Season One Statistics

- **Total Scripts:** 5 episodes
- **Estimated Wordcount:** ~55,000 words (full exploration)
- **Main Paths:** ~35,000 words
- **Branching Paths:** 4 major endings, dozens of minor variations
- **NPCs Introduced:** 12 named characters
- **Mysteries Established:** 15+ plot threads
- **Mysteries Resolved:** 8 major revelations

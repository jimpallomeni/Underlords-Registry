# The Underlord's Registry — Ren'Py Prototype

A Ren'Py prototype demonstrating core gameplay systems from The Underlord's Registry.

## Overview

This prototype covers Act I of Episode 1: Standard Processing, including:

- **Cold Open** — Registry welcome screen
- **Elevator Scene** — Memo 7.4.1 confirmation choice
- **Intake Floor Arrival** — Discovering Mira's belongings
- **Pressa Introduction** — 3 dialogue branches
- **Dolen's Office** — Return-to-work briefing with mystery hints
- **First Processing Session** — Terminal tutorial with soul processing
- **Rebecca Thorne Interview** — Full 15+ node branching conversation
- **Metadata Discovery** — First irregularity log entry opportunity

## Requirements

- [Ren'Py 8.0+](https://www.renpy.org/latest.html)

## Running the Prototype

### Option 1: Ren'Py Launcher

1. Open the Ren'Py launcher
2. Click "preferences" → Set "Projects Directory" to the parent folder of `renpy_prototype`
3. Refresh projects
4. Select "renpy_prototype" and click "Launch Project"

### Option 2: Command Line

```bash
# From the renpy_prototype directory
renpy .

# Or specify the full path
renpy /path/to/renpy_prototype
```

### Option 3: Direct Ren'Py Binary

```bash
# Linux/Mac
/path/to/renpy-8.x.x-sdk/renpy.sh /path/to/renpy_prototype

# Windows
C:\path\to\renpy-8.x.x-sdk\renpy.exe C:\path\to\renpy_prototype
```

## Controls

| Key | Action |
|-----|--------|
| Space/Enter | Advance dialogue |
| L | Toggle Irregularity Log |
| M | Toggle metadata (in terminal) |
| 1-4 | Terminal action shortcuts |
| ESC | Skip / Menu |
| Ctrl | Skip seen text |
| S | Save |
| Q | Quick save |

## Systems Implemented

### 1. Game State (`game/game_state.rpy`)
- Player info (Kael, K-7, clearance 2)
- Shift tracking (quota 40, souls processed)
- **4-tone system**: sardonic, diligent, compassionate, complicit
- **Relationships**: fen, pressa, dolen, mira (-100 to 100)
- **Irregularity Log**: entries with category-coded colors
- **Story flags**: boolean state tracking

### 2. Processing Terminal (`game/screens/terminal.rpy`)
- Form 7-A display with soul information
- Exception Hold status highlighting (amber)
- Metadata view toggle (M key)
- Action buttons with keyboard shortcuts
- Queue counter and progress display

### 3. Irregularity Log (`game/screens/irregularity_log.rpy`)
- Overlay screen (non-modal, toggle with L)
- Color-coded entries:
  - Green: Observations
  - Amber: Evidence
  - Blue: Connections
- Scrollable entry list

### 4. Internal Monologue
- 4 character variants with distinct colors:
  - Sardonic: #b080c0 (purple)
  - Diligent: #80b0e0 (blue)
  - Compassionate: #80e099 (green)
  - Complicit: #b0b0b0 (gray)
- Automatically selects based on dominant tone

### 5. Soul Queue (`game/souls.rpy`)
- Rebecca Thorne as special Exception Hold case
- 47 generated souls with random attributes
- ~10% exception hold rate

### 6. Rebecca Thorne Interview (`game/interviews/rebecca_thorne.rpy`)
- 15+ dialogue nodes with branching paths
- Story flags set based on revelations
- Interview notes populated dynamically
- Multiple ending tones

## File Structure

```
renpy_prototype/
├── game/
│   ├── script.rpy              # Main entry, Act I content
│   ├── characters.rpy          # Character definitions + colors
│   ├── game_state.rpy          # GameState class
│   ├── souls.rpy               # Soul data + queue generation
│   ├── gui.rpy                 # GUI configuration
│   ├── options.rpy             # Project settings
│   ├── processing.rpy          # Terminal action handlers
│   ├── screens/
│   │   ├── terminal.rpy        # Processing Terminal screen
│   │   └── irregularity_log.rpy # Log overlay
│   └── interviews/
│       └── rebecca_thorne.rpy  # Full branching interview
└── README.md
```

## Verification Checklist

- [ ] Start game → See cold open text sequence
- [ ] Elevator → Choose memo confirmation (2 options)
- [ ] Intake floor → See description, discover Mira's mug
- [ ] Pressa → 3 dialogue options with different responses
- [ ] Dolen's office → Return-to-work briefing
- [ ] First shift → Tutorial soul processing
- [ ] Rebecca Thorne → Full interview with 15+ nodes
- [ ] Metadata → View exception hold statistics
- [ ] Irregularity Log → Press L to toggle, see entries
- [ ] End screen → View session statistics

## Notes

- This is a prototype; full Episode 1 content would continue with:
  - Reorientation scene (Conference Room B)
  - Fen conversation (Break Room)
  - Pressa's warning
  - Mira's hidden note discovery
  - Elevator epilogue

- The prototype demonstrates all core systems that would be used throughout the full game.

## License

Part of The Underlord's Registry project. See main project for license details.

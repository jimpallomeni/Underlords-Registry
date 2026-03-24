# The Underlord's Registry — Godot Prototype

A prototype implementation of the Processing Terminal loop and core game systems.

## Requirements

- Godot 4.2 or later
- No external dependencies (placeholder assets included)

## Running the Prototype

1. Open Godot 4.2+
2. Import the project (select the `godot_prototype` folder)
3. The project should load with `scenes/main_simple.tscn` as the main scene
4. Press F5 or click Play to run

## Controls

| Key | Action |
|-----|--------|
| WASD | Move |
| E | Interact / Use Terminal |
| L | Toggle Irregularity Log |
| M | Toggle Metadata (in terminal) |
| 1-4 | Terminal action shortcuts |
| ESC | Close terminal / Pause |
| T | Debug: Open terminal directly |

## Project Structure

```
godot_prototype/
├── project.godot          # Godot project file
├── scenes/
│   ├── main_simple.tscn   # Main game scene (self-contained)
│   ├── main.tscn          # Modular version (uses external scenes)
│   ├── player.tscn        # Player character
│   ├── processing_terminal.tscn  # Terminal UI
│   └── ui/
│       ├── dialogue_box.tscn    # Dialogue display
│       └── hud.tscn             # HUD overlay
├── scripts/
│   ├── main.gd            # Main scene controller
│   ├── interactable.gd    # Base interactable class
│   ├── autoload/
│   │   ├── game_state.gd      # Global game state
│   │   └── dialogue_manager.gd # Dialogue system
│   ├── player/
│   │   └── player.gd      # Player controller
│   ├── terminal/
│   │   └── processing_terminal.gd  # Terminal logic
│   └── ui/
│       ├── dialogue_box.gd    # Dialogue UI
│       └── hud.gd             # HUD controller
├── assets/
│   ├── sprites/           # Character/object sprites
│   ├── tilesets/          # Environment tiles
│   ├── fonts/             # Terminal fonts
│   └── ui/                # UI elements
└── resources/             # Godot resources
```

## Core Systems Implemented

### 1. Game State (Autoload)
- Soul queue generation and management
- Quota and shift tracking
- Tone system (Sardonic/Diligent/Compassionate/Complicit)
- Relationship tracking
- Irregularity Log
- Story flags

### 2. Processing Terminal
- Form 7-A display
- Standard soul processing
- Exception Hold cases
- Metadata view with anomaly discovery
- Action buttons (Approve, Hold, Override, Interview, Escalate)

### 3. Dialogue System
- NPC dialogue trees
- Player choices with tone tracking
- Internal monologue with four variants
- Relationship changes based on choices

### 4. Player Controller
- Top-down WASD movement
- Interaction system
- Freezing during dialogue/terminals

## Recommended Free Assets

The prototype uses placeholder graphics. For better visuals, consider these free assets:

### Tilesets (Office Environment)
- [Cainos - Pixel Art Top Down Basic](https://cainos.itch.io/pixel-art-top-down-basic) — 32x32 basic tileset
- [Anokolisa - Free RPG Tileset](https://anokolisa.itch.io/free-pixel-art-asset-pack-topdown-tileset-rpg-16x16-sprites) — 16x16 with 500+ sprites

### Character Sprites
- [OpenGameArt CC0 Resources](https://opengameart.org/content/cc0-resources) — Various CC0 sprites
- [DENZI's Public Domain Art](https://opengameart.org/content/denzis-public-domain-art) — 32x32 overhead sprites

### Fonts (Terminal)
- [Monogram](https://datagoblin.itch.io/monogram) — Free monospace pixel font (CC0)
- [OpenGameArt CC0 Fonts](https://opengameart.org/content/cc0-fonts) — Various bitmap fonts

## Adding Real Assets

1. **Sprites**: Place in `assets/sprites/` and update scene references
2. **Tilesets**: Import to `assets/tilesets/`, create TileSet resource, add to TileMapLayers
3. **Fonts**: Import to `assets/fonts/`, create FontFile, update theme overrides

## What's Missing (TODO)

- [ ] Actual sprite graphics (currently rectangles)
- [ ] Tilemap-based office environment
- [ ] NPC characters (Pressa, Dolen, Fen)
- [ ] Interview scenes
- [ ] Sound effects and music
- [ ] Save/Load system UI
- [ ] Episode transitions

## Episode 1 Features to Add

Based on the script, these features should be implemented:

1. **Elevator Intro Scene** — Cold open with confirmation dialogue
2. **Intake Floor Navigation** — Walk to Dolen's office, break room, etc.
3. **NPC Interactions** — Pressa, Dolen, Fen with full dialogue trees
4. **Reorientation Scene** — Conference Room B cutscene
5. **Rebecca Thorne Interview** — Extended interview system
6. **Mira's Note Discovery** — Evidence gathering
7. **End of Shift Sequence** — Elevator message, final shot

## Development Notes

The dialogue system includes Episode 1's key conversations:
- Elevator introduction
- Pressa's greeting
- Dolen's briefing (exception rate reveal)
- Fen's alliance offer

The Processing Terminal implements the core loop:
- Soul queue with standard and exception cases
- Rebecca Thorne as a special case
- Metadata view showing the 100x anomaly

## License

Prototype code is part of The Underlord's Registry project.
Asset licenses vary by source — check individual asset pages.

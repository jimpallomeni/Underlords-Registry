## images.rpy — The Underlord's Registry
## Image definitions for characters, backgrounds, and UI

# =============================================================================
# CHARACTERS
# =============================================================================

# Kael (Player Character)
# Expressions: neutral, concerned, sardonic, surprised
image kael neutral = "images/characters/kael/neutral.png"
image kael concerned = "images/characters/kael/concerned.png"
image kael sardonic = "images/characters/kael/sardonic.png"
image kael surprised = "images/characters/kael/surprised.png"

# Pressa
# Expressions: neutral, warning, disapproving
image pressa neutral = "images/characters/pressa/neutral.png"
image pressa warning = "images/characters/pressa/warning.png"
image pressa disapproving = "images/characters/pressa/disapproving.png"

# Supervisor Dolen
# Expressions: neutral, nervous, relieved, warning
image dolen neutral = "images/characters/dolen/neutral.png"
image dolen nervous = "images/characters/dolen/nervous.png"
image dolen relieved = "images/characters/dolen/relieved.png"
image dolen warning = "images/characters/dolen/warning.png"

# Fen
# Expressions: neutral, concerned, hopeful, disappointed
image fen neutral = "images/characters/fen/neutral.png"
image fen concerned = "images/characters/fen/concerned.png"
image fen hopeful = "images/characters/fen/hopeful.png"
image fen disappointed = "images/characters/fen/disappointed.png"

# Rebecca Thorne (Soul - translucent)
# Expressions: neutral, guarded, intense, resigned
image rebecca neutral = "images/characters/rebecca/neutral.png"
image rebecca guarded = "images/characters/rebecca/guarded.png"
image rebecca intense = "images/characters/rebecca/intense.png"
image rebecca resigned = "images/characters/rebecca/resigned.png"

# =============================================================================
# BACKGROUNDS
# =============================================================================

image bg elevator = "images/backgrounds/elevator.png"
image bg intake_floor = "images/backgrounds/intake_floor.png"
image bg dolens_office = "images/backgrounds/dolens_office.png"
image bg interview_booth = "images/backgrounds/interview_booth.png"
image bg terminal_closeup = "images/backgrounds/terminal_closeup.png"
image bg break_room = "images/backgrounds/break_room.png"
image bg hallway = "images/backgrounds/hallway.png"
image bg conference_room = "images/backgrounds/conference_room.png"

# =============================================================================
# UI ELEMENTS
# =============================================================================

image ui terminal_frame = "images/ui/terminal_frame.png"
image ui log_frame = "images/ui/log_frame.png"

# =============================================================================
# PLACEHOLDER GENERATION
# =============================================================================
# Remove this section once real art is added

init python:
    import pygame

    def create_placeholder(width, height, color, label=""):
        """Generate a placeholder surface with label."""
        surf = pygame.Surface((width, height))
        surf.fill(color)
        # Add border
        pygame.draw.rect(surf, (80, 255, 80), (0, 0, width, height), 2)
        return surf

# Placeholder colors for missing images
# These will show colored rectangles until real art is added
image placeholder_character = Solid("#2a4a2a", xsize=300, ysize=500)
image placeholder_background = Solid("#1a2a1a", xsize=1280, ysize=720)

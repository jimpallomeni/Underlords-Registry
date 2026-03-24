## characters.rpy — The Underlord's Registry
## Character definitions and internal monologue variants

# Main characters
define kael = Character("Kael", color="#99ccff")
define pressa = Character("Pressa", color="#cc99dd")
define dolen = Character("Dolen", color="#b3b380")
define fen = Character("Fen", color="#80e680")
define rebecca = Character("Rebecca", color="#e69966")
define registry_voice = Character("Registry", color="#4d994d")
define trainer = Character("Trainer", color="#999999")

# Internal monologue variants (different colors for each tone)
define kael_sardonic = Character("Kael", color="#b080c0", what_prefix="{i}", what_suffix="{/i}")
define kael_diligent = Character("Kael", color="#80b0e0", what_prefix="{i}", what_suffix="{/i}")
define kael_compassionate = Character("Kael", color="#80e099", what_prefix="{i}", what_suffix="{/i}")
define kael_complicit = Character("Kael", color="#b0b0b0", what_prefix="{i}", what_suffix="{/i}")

# Narrator for stage directions and descriptions (ADV mode - one line at a time)
define narrator = Character(None)

# System messages (terminal output, etc.)
define system = Character(None, what_color="#80ff80", what_font="DejaVuSansMono.ttf")

# Helper function to show internal monologue with the right character
init python:
    def internal_monologue(sardonic=None, diligent=None, compassionate=None, complicit=None):
        """
        Returns a tuple of (character, text) for internal monologue
        based on current dominant tone.
        """
        tone = game_state.get_dominant_tone()
        if tone == "neutral":
            tone = "diligent"

        texts = {
            "sardonic": sardonic,
            "diligent": diligent,
            "compassionate": compassionate,
            "complicit": complicit
        }

        chars = {
            "sardonic": kael_sardonic,
            "diligent": kael_diligent,
            "compassionate": kael_compassionate,
            "complicit": kael_complicit
        }

        text = texts.get(tone)
        char = chars.get(tone)

        return (char, text)

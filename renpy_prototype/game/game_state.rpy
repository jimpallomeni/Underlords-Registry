## game_state.rpy — The Underlord's Registry
## Core game state management: tone, relationships, irregularity log, flags

init python:
    class IrregularityEntry:
        """A single entry in the Irregularity Log."""
        def __init__(self, id, title, content, category="observation"):
            self.id = id
            self.title = title
            self.content = content
            self.category = category  # observation, evidence, connection
            self.timestamp = "Day 147, 4019"  # Could be dynamic

        def get_color(self):
            """Return color based on category."""
            colors = {
                "observation": "#80e099",  # green
                "evidence": "#ffcc66",      # amber
                "connection": "#80b0e0"     # blue
            }
            return colors.get(self.category, "#ffffff")

    class GameState:
        """Central game state tracking for The Underlord's Registry."""

        def __init__(self):
            # Player info
            self.player_name = "Kael"
            self.player_designation = "K-7"
            self.clearance_level = 2

            # Shift tracking
            self.shift_quota = 40
            self.souls_processed = 0
            self.hours_remaining = 8
            self.exception_holds = 0
            self.escalations = 0
            self.interviews_conducted = 0

            # Tone system (each tracks cumulative choices)
            self.tones = {
                "sardonic": 0,
                "diligent": 0,
                "compassionate": 0,
                "complicit": 0
            }

            # Relationships (-100 to 100)
            self.relationships = {
                "fen": 0,
                "pressa": 0,
                "dolen": 0,
                "mira": 0  # Can still track even though absent
            }

            # Irregularity Log
            self.irregularity_log = []
            self.next_entry_id = 1

            # Story flags (boolean states)
            self.flags = {}

        def get_dominant_tone(self):
            """Return the tone with highest value, or 'neutral' if tied/zero."""
            max_val = max(self.tones.values())
            if max_val == 0:
                return "neutral"

            # Find all tones at max value
            top_tones = [t for t, v in self.tones.items() if v == max_val]

            # If tied, return first alphabetically for consistency
            return sorted(top_tones)[0]

        def add_tone(self, tone, amount=1):
            """Add to a tone's value."""
            if tone in self.tones:
                self.tones[tone] += amount

        def change_relationship(self, character, amount):
            """Modify a relationship value, clamped to -100/100."""
            if character in self.relationships:
                new_val = self.relationships[character] + amount
                self.relationships[character] = max(-100, min(100, new_val))

        def get_relationship_status(self, character):
            """Return a text description of relationship level."""
            if character not in self.relationships:
                return "unknown"

            val = self.relationships[character]
            if val >= 50:
                return "alliance"
            elif val >= 20:
                return "friendly"
            elif val >= -20:
                return "neutral"
            elif val >= -50:
                return "distant"
            else:
                return "hostile"

        def add_irregularity(self, title, content, category="observation"):
            """Add a new entry to the Irregularity Log."""
            entry = IrregularityEntry(
                id=self.next_entry_id,
                title=title,
                content=content,
                category=category
            )
            self.irregularity_log.append(entry)
            self.next_entry_id += 1
            return entry

        def has_irregularity(self, title_substring):
            """Check if log contains an entry with title containing substring."""
            for entry in self.irregularity_log:
                if title_substring.lower() in entry.title.lower():
                    return True
            return False

        def set_flag(self, flag_name, value=True):
            """Set a story flag."""
            self.flags[flag_name] = value

        def get_flag(self, flag_name, default=False):
            """Get a story flag value."""
            return self.flags.get(flag_name, default)

        def process_soul(self, is_exception_hold=False):
            """Record processing a soul."""
            self.souls_processed += 1
            if is_exception_hold:
                self.exception_holds += 1

        def quota_met(self):
            """Check if quota has been met."""
            return self.souls_processed >= self.shift_quota

# Initialize global game state
default game_state = GameState()

# Helper function for showing tone-based internal monologue
init python:
    def show_internal(texts):
        """
        Show internal monologue based on dominant tone.
        texts should be a dict with keys: sardonic, diligent, compassionate, complicit
        Returns the appropriate text.
        """
        tone = game_state.get_dominant_tone()
        if tone == "neutral":
            # Default to diligent if neutral
            tone = "diligent"
        return texts.get(tone, texts.get("diligent", "..."))

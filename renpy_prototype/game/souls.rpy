## souls.rpy — The Underlord's Registry
## Soul data structures and queue generation

init python:
    import random

    class Soul:
        """Represents a soul in the processing queue."""

        def __init__(self, designation, name, cause, summary,
                     is_exception_hold=False, is_special=False,
                     classification="STANDARD ASSIGNMENT",
                     routing="Queue 7 (General Population)"):
            self.designation = designation
            self.name = name
            self.cause = cause
            self.summary = summary
            self.is_exception_hold = is_exception_hold
            self.is_special = is_special
            self.classification = classification
            self.routing = routing
            self.interviewed = False
            self.processed = False
            self.interview_notes = ""

        def get_status_color(self):
            """Return color for terminal display."""
            if self.is_exception_hold:
                return "#ffaa44"  # Amber for exception hold
            return "#80ff80"  # Green for standard

    # Rebecca Thorne - special Exception Hold case
    REBECCA_THORNE = Soul(
        designation="R-0012",
        name="Rebecca Thorne",
        cause="[REDACTED — CLEARANCE LEVEL 3 REQUIRED]",
        summary="""Former compliance auditor, financial sector.
47 years of life. Died Year 4,019, Day 142.
Career: 23 years investigating financial discrepancies.
Notable: Three days before death, was preparing major report.
File Note: Cause of death classification contested.""",
        is_exception_hold=True,
        is_special=True,
        classification="██████████",
        routing="██████████"
    )

    # Name pools for random generation
    FIRST_NAMES = [
        "Harold", "Maria", "Dmitri", "Susan", "Theodore", "Amara", "James",
        "Elena", "Marcus", "Patricia", "Chen", "Yuki", "Olga", "Samuel",
        "Fatima", "Bernard", "Grace", "Viktor", "Lucia", "Ahmed", "Sophie",
        "Robert", "Mei", "Antonio", "Ingrid", "Kwame", "Hannah", "Diego"
    ]

    LAST_NAMES = [
        "Mencken", "Vance", "Holloway", "Park", "Bright", "Osei", "Chen",
        "Novak", "Torres", "Williams", "Kowalski", "Sato", "Petrov", "Davis",
        "Al-Hassan", "Dubois", "Singh", "Mueller", "Costa", "Andersen",
        "Nakamura", "Okonkwo", "Schmidt", "Fernandez", "Johansson", "Kim"
    ]

    CAUSES_OF_DEATH = [
        "Natural (Cardiovascular)",
        "Natural (Respiratory)",
        "Natural (Neurological)",
        "Illness (Terminal)",
        "Illness (Complications)",
        "Accident (Vehicular)",
        "Accident (Industrial)",
        "Accident (Domestic)",
        "Natural (Age-Related)",
        "Illness (Infectious)"
    ]

    LIFE_SUMMARIES = [
        "Lived a quiet life. Worked steadily. Loved occasionally. Died peacefully.",
        "Teacher for 34 years. Remembered by students. Forgot to remember self.",
        "Built things with hands. Houses, furniture, a family. Left them all standing.",
        "Traveled extensively. Sought meaning. Found postcards.",
        "Devoted to family. Three children, seven grandchildren. Missed the eighth.",
        "Artist of moderate success. Work hangs in two museums. Neither famous.",
        "Accountant. Numbers balanced. Life less so.",
        "Farmer. Grew enough to feed a village. Died in the city.",
        "Doctor. Saved hundreds. Couldn't save the one that mattered most.",
        "Writer. Published six books. Read by dozens.",
        "Engineer. Bridges that stand. Relationships that didn't.",
        "Soldier once. Civilian longer. Memories of both.",
        "Musician. Local fame. Universal obscurity.",
        "Scientist. One minor discovery. One major regret.",
        "Chef. Fed thousands. Ate alone."
    ]

    def generate_soul(index, force_exception_hold=False):
        """Generate a random soul for the queue."""
        # ~10% exception hold rate unless forced
        is_exception = force_exception_hold or (random.random() < 0.10)

        # Generate designation
        letter = random.choice("ABCDEFGHJKLMNPQRSTUVWXYZ")
        number = random.randint(1000, 9999)
        designation = f"{letter}-{number}"

        # Generate name
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        name = f"{first} {last}"

        # Generate cause
        cause = random.choice(CAUSES_OF_DEATH)

        # Generate summary
        summary = random.choice(LIFE_SUMMARIES)

        soul = Soul(
            designation=designation,
            name=name,
            cause=cause,
            summary=summary,
            is_exception_hold=is_exception
        )

        if is_exception:
            soul.classification = "PENDING REVIEW"
            soul.routing = "Exception Hold Queue"

        return soul

    def generate_soul_queue(count=47, insert_rebecca_at=7):
        """Generate a queue of souls with Rebecca Thorne at specified position."""
        queue = []

        for i in range(count):
            if i == insert_rebecca_at:
                queue.append(REBECCA_THORNE)
            else:
                queue.append(generate_soul(i))

        return queue

# Initialize the soul queue
default soul_queue = generate_soul_queue()
default current_soul_index = 0

## rebecca_thorne.rpy — The Underlord's Registry
## Full branching interview with Rebecca Thorne (15+ nodes)

label rebecca_thorne_interview:
    """Full interview with Rebecca Thorne, Exception Hold soul R-0012."""

    scene black with dissolve

    "KAEL walks to Interview Booth 7—a small enclosed space with two chairs, a table, and a one-way window."
    "The fluorescent light here is slightly warmer. A small concession to the concept of comfort."

    "REBECCA THORNE sits in the soul's chair. She is translucent, like all souls, but her features are sharp."
    "A woman in her forties, professional attire, the bearing of someone who was used to being listened to."

    "She looks at KAEL. She has been waiting a long time. She is used to waiting."

    rebecca "Finally."

    menu rebecca_opening:
        "I'm Processor K-7. I have some questions about your file.":
            jump rebecca_questions

        "Your file was flagged for Exception Hold. Do you know why?":
            jump rebecca_exception_direct

        "Tell me about yourself, Rebecca.":
            jump rebecca_about_self

label rebecca_questions:
    rebecca "Of course you do. Everyone has questions. No one has answers."

    "She gestures at the booth."

    rebecca "I've been in queues for five days. Five days since I died."
    rebecca "Do you know how long that is when you're dead?"
    rebecca "It's exactly five days. Death doesn't make time move differently."
    rebecca "It just makes it feel more wasted."

    jump rebecca_main_menu

label rebecca_exception_direct:
    rebecca "No. Do you?"

    kael "The cause of death is redacted. That's unusual."

    "REBECCA's expression shifts. Something guarded."

    rebecca "Is it."

    $ game_state.set_flag("rebecca_asked_about_exception")

    jump rebecca_main_menu

label rebecca_about_self:
    "REBECCA laughs. It's not a happy sound."

    rebecca "Now someone wants to know. After forty-seven years of life and five days of death, someone finally asks."

    "She leans back."

    rebecca "I was a compliance auditor. Financial sector."
    rebecca "I spent my life finding discrepancies in systems that were designed to hide them."

    "She looks at KAEL."

    rebecca "I was very good at my job."

    $ game_state.set_flag("rebecca_revealed_profession")

    jump rebecca_main_menu

label rebecca_main_menu:
    menu:
        "Tell me more about your work." if not game_state.get_flag("rebecca_revealed_profession"):
            jump rebecca_work

        "You said you were a compliance auditor. What did you find?" if game_state.get_flag("rebecca_revealed_profession"):
            jump rebecca_findings

        "What happened when you died?":
            jump rebecca_death

        "Why do you think you were flagged?":
            jump rebecca_why_flagged

        "I've heard enough. Let's finish this.":
            jump rebecca_conclude

label rebecca_work:
    rebecca "I was a compliance auditor. Financial sector."
    rebecca "Twenty-three years of finding the numbers that didn't add up."
    rebecca "The transactions that went nowhere. The accounts that existed only on paper."

    "She meets KAEL's eyes."

    rebecca "I was very good at finding things people wanted hidden."

    $ game_state.set_flag("rebecca_revealed_profession")
    jump rebecca_main_menu

label rebecca_findings:
    rebecca "You want to know what I found?"

    "She pauses."

    rebecca "I found a pattern. Three days before I died, I was preparing a report."
    rebecca "The kind of report that ends careers. The kind that makes powerful people very nervous."

    menu:
        "What was in the report?":
            jump rebecca_report_details

        "You think that's why you died?":
            jump rebecca_murder_theory

        "That sounds like mortal business. What does it have to do with your afterlife?":
            jump rebecca_afterlife_connection

label rebecca_report_details:
    rebecca "Numbers. Discrepancies. A hundred million in transactions that went... somewhere."
    rebecca "Not where they were supposed to go. Not where the books said they went."

    "She looks down at her translucent hands."

    rebecca "I never got to file that report. Heart attack, they said. Very sudden."

    $ game_state.set_flag("rebecca_revealed_report")
    jump rebecca_main_menu

label rebecca_murder_theory:
    rebecca "I think I died at a very convenient time for certain people."
    rebecca "The afterlife bureaucracy classified my death as 'natural causes.'"
    rebecca "But they also redacted the details from my file."

    "She looks at KAEL steadily."

    rebecca "In my experience, you don't redact things that don't matter."

    $ game_state.set_flag("rebecca_suggested_murder")
    jump rebecca_main_menu

label rebecca_afterlife_connection:
    rebecca "That's what I'm trying to figure out."

    "She leans forward."

    rebecca "In life, I learned to read systems. The way data flows. The patterns that form."
    rebecca "This place—your Registry—it's a system too. And something about my case is making the system... nervous."

    menu:
        "What do you mean, nervous?":
            jump rebecca_system_nervous

        "The system doesn't get nervous. It's just procedures.":
            jump rebecca_procedures

label rebecca_system_nervous:
    rebecca "I've been in three different queues in five days. Each time, I get moved before anyone processes me."
    rebecca "My file has redactions that don't appear on standard forms."
    rebecca "And now I'm in Exception Hold—a category that, from what I can tell, barely existed a month ago."

    "She tilts her head."

    rebecca "Either I'm the unluckiest soul in the afterlife, or something is trying very hard not to look at me directly."

    $ game_state.set_flag("rebecca_revealed_discrepancies")
    jump rebecca_main_menu

label rebecca_procedures:
    rebecca "That's what the people who designed the hidden accounts always said."
    rebecca "'It's just procedures. It's just how things are done.'"

    "She smiles, and there's no warmth in it."

    rebecca "And then I'd find the procedure that moved money into pockets it wasn't supposed to reach."
    rebecca "Systems don't have intentions. But the people who design them do."

    jump rebecca_main_menu

label rebecca_death:
    rebecca "I died five days ago. Heart attack, according to the official report."

    "She pauses."

    rebecca "I was forty-seven. No history of heart problems. Regular checkups. Healthy diet."
    rebecca "Three days before a major report was due."

    menu:
        "That does seem... coincidental.":
            jump rebecca_coincidence

        "Heart attacks can happen to anyone.":
            jump rebecca_denial

label rebecca_coincidence:
    rebecca "Convenient is the word I'd use."
    rebecca "But then, I've always been suspicious. Occupational hazard."

    $ game_state.set_flag("rebecca_death_discussed")
    jump rebecca_main_menu

label rebecca_denial:
    rebecca "They can. And maybe that's all this was."

    "She doesn't sound convinced."

    rebecca "But in my line of work, I learned that coincidences are usually the first thing you investigate."

    $ game_state.set_flag("rebecca_death_discussed")
    jump rebecca_main_menu

label rebecca_why_flagged:
    rebecca "I've been thinking about that."

    "She stands, pacing the small booth."

    rebecca "Your system flagged me automatically. Exception Hold, Code 7.4.1-E."
    rebecca "That code didn't exist a month ago. I checked—talked to other souls in the queues."
    rebecca "The whole Exception Hold system was changed recently."

    menu:
        "How do you know all this?":
            jump rebecca_how_know

        "What do you think they're looking for?":
            jump rebecca_what_looking_for

label rebecca_how_know:
    rebecca "I spent my life auditing systems. You think I'd stop just because I'm dead?"

    "She smiles slightly."

    rebecca "The souls in the queues talk. Most processors don't pay attention. But I do."
    rebecca "There's been a... surge. More Exception Holds. More souls waiting. More confusion."

    $ game_state.set_flag("rebecca_revealed_count")
    jump rebecca_main_menu

label rebecca_what_looking_for:
    rebecca "That's the question, isn't it?"

    "She stops pacing."

    rebecca "The old threshold caught edge cases. Statistical noise. Maybe one in thirty thousand."
    rebecca "The new threshold catches... more. A lot more."
    rebecca "But what they all have in common? That's what I can't figure out."

    menu:
        "Maybe I can help you look.":
            jump rebecca_offer_help

        "I'm not sure I should be getting involved.":
            jump rebecca_hesitant

label rebecca_offer_help:
    "REBECCA studies KAEL for a long moment."

    rebecca "You're different from the other processors I've seen."
    rebecca "Most of them just want to stamp and move on. You're actually asking questions."

    "She leans closer."

    rebecca "Look at my file. Really look at it. Not the summary. The metadata. The routing codes."
    rebecca "I spent my life reading what systems tried to hide. Your system is hiding something too."

    $ game_state.set_flag("rebecca_hinted_metadata")
    $ game_state.change_relationship("mira", 5)  # Indirect connection to Mira's investigation

    jump rebecca_conclude

label rebecca_hesitant:
    rebecca "No one should be getting involved. That's the whole point of bureaucracy."
    rebecca "Keep your head down. Process the forms. Don't ask questions."

    "She looks at KAEL."

    rebecca "But you came here. You requested this interview. That means something."

    jump rebecca_conclude

label rebecca_conclude:
    "REBECCA settles back in her chair."

    rebecca "Whatever you decide to do with my case... I just want you to know one thing."

    rebecca "I spent my life trying to make systems accountable."
    rebecca "I found the discrepancies. I wrote the reports. And in the end, it didn't save me."

    "She looks at KAEL with something that might be hope, or might be resignation."

    rebecca "Maybe it's different here. Maybe asking questions actually leads somewhere."
    rebecca "Or maybe the afterlife is just another system designed to grind you down."

    menu rebecca_final:
        "I'll look into this. I promise.":
            $ game_state.add_tone("compassionate", 2)
            $ game_state.set_flag("rebecca_promised_help")
            rebecca "Thank you. That's more than anyone else has said."

        "I'll do my job. Whatever that means.":
            $ game_state.add_tone("diligent", 2)
            rebecca "I understand. We all have our roles to play."

        "I shouldn't have come here.":
            $ game_state.add_tone("complicit", 2)
            rebecca "No. You probably shouldn't have. But you did. That means something."

    "The interview concludes. REBECCA fades slightly, waiting to be returned to the queue."

    # Set interview notes based on what was revealed
    python:
        notes = "Interview with R-0012 (Rebecca Thorne):\n"
        if game_state.get_flag("rebecca_revealed_profession"):
            notes += "- Former compliance auditor (23 years)\n"
        if game_state.get_flag("rebecca_suggested_murder"):
            notes += "- Claims death was 'convenient' timing\n"
        if game_state.get_flag("rebecca_revealed_report"):
            notes += "- Was preparing major financial report before death\n"
        if game_state.get_flag("rebecca_revealed_discrepancies"):
            notes += "- Notes discrepancies in own file processing\n"
        if game_state.get_flag("rebecca_revealed_count"):
            notes += "- Aware of increased Exception Hold rate\n"
        if game_state.get_flag("rebecca_hinted_metadata"):
            notes += "- Suggested examining file metadata\n"
        notes += "Status: Pending further review"

        # Find Rebecca in the queue and set notes
        for soul in soul_queue:
            if soul.designation == "R-0012":
                soul.interview_notes = notes
                break

    return

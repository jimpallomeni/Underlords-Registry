## script.rpy — The Underlord's Registry
## Main entry point and Act I content (Episode 1: Standard Processing)

label start:
    # Initialize
    $ game_state = GameState()
    $ soul_queue = generate_soul_queue()
    $ current_soul_index = 0
    $ show_irregularity_log = False

    jump cold_open

## ═══════════════════════════════════════════════════════════════════════════
## COLD OPEN
## ═══════════════════════════════════════════════════════════════════════════

label cold_open:
    scene black
    with fade

    pause 0.5

    centered "{font=DejaVuSansMono.ttf}{size=24}{color=#80ff80}THE REGISTRY{/color}{/size}{/font}"

    pause 0.8

    centered "{font=DejaVuSansMono.ttf}{size=18}{color=#80ff80}Department of Final Intake{/color}{/size}{/font}"
    centered "{font=DejaVuSansMono.ttf}{size=18}{color=#80ff80}Employee Return-to-Work Processing{/color}{/size}{/font}"

    pause 0.5

    centered "{font=DejaVuSansMono.ttf}{size=16}{color=#80ff80}PROCESSOR: [game_state.player_name], [game_state.player_designation]{/color}{/size}{/font}"
    centered "{font=DejaVuSansMono.ttf}{size=16}{color=#80ff80}STATUS: Medical Leave (Personal Circumstances){/color}{/size}{/font}"
    centered "{font=DejaVuSansMono.ttf}{size=16}{color=#80ff80}DURATION: 6 weeks, 4 days{/color}{/size}{/font}"
    centered "{font=DejaVuSansMono.ttf}{size=16}{color=#80ff80}RETURN DATE: Today{/color}{/size}{/font}"

    pause 0.8

    centered "{font=DejaVuSansMono.ttf}{size=16}{color=#80ff80}Please report to Intake Floor, Terminal 7.{/color}{/size}{/font}"
    centered "{font=DejaVuSansMono.ttf}{size=16}{color=#80ff80}Your reorientation packet is waiting.{/color}{/size}{/font}"

    pause 1.0

    centered "{font=DejaVuSansMono.ttf}{size=20}{color=#80ff80}Welcome back.{/color}{/size}{/font}"

    pause 1.5

    jump scene_elevator

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 1.1 — THE ELEVATOR
## ═══════════════════════════════════════════════════════════════════════════

label scene_elevator:
    scene black
    with dissolve

    "Interior. A service elevator. Fluorescent lighting."

    "The walls are beige metal. A certificate in a plastic frame reads:"
    "{i}THIS ELEVATOR INSPECTED — YEAR OF OUR REGISTRY 4,012.{/i}"
    "The current year is 4,019."

    "KAEL stands alone, facing the doors. They wear the standard Registry uniform: gray-beige, slightly too formal, slightly too uncomfortable."

    "They hold a small box of personal effects."

    "The elevator descends. Floor numbers tick past: 5... 4... 3... 2..."

    "The elevator stops at 1. The doors do not open."

    "A CHIME sounds."

    registry_voice "Welcome back, Processor [game_state.player_designation]."
    registry_voice "Before you return to your duties, please confirm you have reviewed the updated Policy Memorandum 7.4.1, \"Changes to Standard Intake Processing.\""

    "A small screen beside the door illuminates. Two buttons:"

    menu elevator_choice:
        "CONFIRM: I HAVE REVIEWED THE MEMORANDUM":
            jump elevator_confirm

        "REQUEST: SEND ME THE MEMORANDUM":
            jump elevator_request

label elevator_confirm:
    "The doors open immediately."

    registry_voice "Acknowledged. Compliance logged."

    $ game_state.set_flag("confirmed_memo_unread")
    $ game_state.add_tone("sardonic")
    $ game_state.add_tone("complicit")

    # Show internal monologue based on tone
    $ tone = game_state.get_dominant_tone()
    if tone == "sardonic" or tone == "neutral":
        kael_sardonic "I haven't read it. No one reads them. That's why they make you confirm."
    elif tone == "diligent":
        kael_diligent "I should have read it. I'll find a copy at my desk."
    elif tone == "compassionate":
        kael_compassionate "Six weeks away. Whatever changed, I'll figure it out."
    else:
        kael_complicit "Check the box. Move on. That's how this works."

    jump scene_intake_floor

label elevator_request:
    "A pause. Longer than expected."

    registry_voice "Memorandum 7.4.1 will be delivered to your terminal."
    registry_voice "Processing time: three to five business days."

    "The doors open."

    registry_voice "In the interim, please proceed with standard duties."

    $ game_state.set_flag("requested_memo")
    $ game_state.add_tone("diligent")

    $ tone = game_state.get_dominant_tone()
    if tone == "sardonic" or tone == "neutral":
        kael_sardonic "Three to five days for an email. The system works."
    elif tone == "diligent":
        kael_diligent "I'll ask Pressa. She always knows what's actually changed."
    elif tone == "compassionate":
        kael_compassionate "At least I asked."
    else:
        kael_complicit "Should've just confirmed."

    jump scene_intake_floor

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 1.2 — THE INTAKE FLOOR
## ═══════════════════════════════════════════════════════════════════════════

label scene_intake_floor:
    scene black
    with dissolve

    "The elevator doors open onto the Intake Floor."

    "A vast open-plan office. Rows of identical desks, each with a Soul Processing Terminal."

    "Fluorescent lights hum overhead—the particular frequency of institutional lighting that exists nowhere in nature."

    "The carpet is green-gray, patterned in a way that was probably modern four hundred years ago."

    "Souls drift through processing queues—slightly translucent figures, waiting."
    "Some sit. Some stand. Some have been standing so long they've forgotten they could sit."

    "Registry employees move between desks with the careful efficiency of people who have learned not to rush."
    "Rushing attracts attention."

    "KAEL steps onto the floor. Stops."

    kael_diligent "Six weeks. It looks exactly the same. It always looks exactly the same."

    "A beat. Then KAEL notices:"

    "Terminal 7. KAEL's desk. The personal effects are gone."
    "No mug. No photos. No small plant that was definitely against policy but everyone had one."

    "The desk has been cleaned. Completely."

    "KAEL approaches slowly. Sets down their box of belongings."

    "Under the desk: a cardboard box. Not KAEL's."
    "A mug inside—hand-painted, amateur, a design of stars."
    "A name on the bottom: MIRA."

    kael_diligent "That's Mira's mug. Why is Mira's mug under my desk?"

    jump scene_pressa

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 1.3 — PRESSA
## ═══════════════════════════════════════════════════════════════════════════

label scene_pressa:
    "KAEL looks up."

    "At the next desk—Terminal 8—sits PRESSA."

    "She is old in a way that doesn't invite questions about how old."
    "She has been at the Registry longer than anyone currently employed can verify."
    "Her posture is perfect. Her expression is carefully neutral."

    "She is already looking at KAEL."

    pressa "[game_state.player_designation]. You're back."

    "She does not phrase it as a welcome."

    menu pressa_greeting:
        "Good to be back.":
            jump pressa_good

        "Where's Mira?":
            jump pressa_mira

        "What happened to my desk?":
            jump pressa_desk

label pressa_good:
    "PRESSA studies KAEL for a moment."

    pressa "Is it."

    "Not a question. She returns to her terminal."

    $ game_state.add_tone("complicit")
    jump pressa_conclude

label pressa_mira:
    "PRESSA's fingers pause over her keyboard. A fraction of a second. Then she resumes typing."

    pressa "Transferred."

    kael "Transferred where?"

    pressa "Away."

    "She doesn't look up."

    $ game_state.add_tone("diligent")
    $ game_state.set_flag("asked_pressa_about_mira")
    jump pressa_conclude

label pressa_desk:
    pressa "Standard cleaning. You were gone six weeks. Maintenance needed the space."

    kael "They cleaned Mira's things too."

    pressa "She transferred. Her things were processed."

    kael "Her mug is still here."

    "PRESSA stops typing. Looks at KAEL."

    pressa "Then you should return it to Lost and Found. When you have time."

    $ game_state.add_tone("sardonic")
    $ game_state.set_flag("noticed_mira_mug")
    jump pressa_conclude

label pressa_conclude:
    "A beat."

    pressa "Dolen wants to see you before your shift starts. His office."

    jump scene_dolen_office

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 1.5 — SUPERVISOR DOLEN'S OFFICE
## ═══════════════════════════════════════════════════════════════════════════

label scene_dolen_office:
    scene black
    with dissolve

    "KAEL enters the supervisor's office."

    "It's nicer than the floor—actual walls, a door that closes, a window that looks out onto... something."
    "The view is always slightly unclear, as if the glass itself is uncertain what it's showing."

    "SUPERVISOR DOLEN sits behind his desk."
    "He is middle-aged in an eternal way. He has been middle-aged, and a supervisor, for as long as anyone can remember."
    "He is not a bad manager. He is not a good one. He is the manager the Registry produced."

    "His blinds are half-closed. They are always half-closed."

    dolen "[game_state.player_designation]. Sit down."

    "KAEL sits."

    dolen "How are you feeling?"

    menu dolen_feeling:
        "Better. Ready to work.":
            dolen "Good. That's good. We need people ready to work."
            "He shuffles papers on his desk. A nervous habit."
            $ game_state.add_tone("diligent")

        "I'd rather not discuss it.":
            dolen "Of course. Personal circumstances. I understand."
            "He clearly doesn't. He's also clearly relieved not to have to."
            $ game_state.add_tone("complicit")

        "Where's Mira?":
            jump dolen_mira

    jump dolen_reorientation

label dolen_mira:
    "DOLEN's expression flickers. Something passes across his face—discomfort, or something closer to fear. Then it's gone."

    dolen "Mira transferred to another department. It was... sudden. An opportunity came up."

    kael "What department?"

    dolen "I don't have that information."

    kael "You were her supervisor."

    dolen "The transfer was handled above my level."

    "A beat."

    dolen "Let's focus on your return."

    $ game_state.add_tone("sardonic")
    $ game_state.set_flag("asked_dolen_about_mira")
    $ game_state.change_relationship("dolen", -5)

    jump dolen_reorientation

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 1.6 — THE REORIENTATION
## ═══════════════════════════════════════════════════════════════════════════

label dolen_reorientation:
    dolen "There have been some changes while you were away. Policy updates. New form fields. Nothing dramatic."

    "He slides a thin folder across the desk."

    dolen "The reorientation session this afternoon will cover everything formally."
    dolen "But I wanted to brief you personally on one item."

    "He opens the folder. Inside: a single form. Form 7-A: Standard Intake."
    "It looks almost identical to the version KAEL remembers. Almost."

    dolen "The Exception Hold threshold has been adjusted."

    "He points to a field near the bottom of the form:"
    "{i}EXCEPTION HOLD TRIGGER — AUTOMATED THRESHOLD.{/i}"

    dolen "Previously, the system flagged cases for Exception Hold at a rate of approximately 0.003%%. Standard statistical variance. Edge cases."

    "He taps the new field."

    dolen "The new threshold produces a flag rate of approximately 0.3%%."

    menu dolen_threshold:
        "That's a hundred times higher.":
            dolen "Yes."
            kael "Why?"
            dolen "The memorandum cites \"improved detection parameters.\""
            kael "Detection of what?"
            "DOLEN doesn't answer immediately. When he does:"
            dolen "The memorandum doesn't specify."
            $ game_state.add_tone("sardonic")

        "What does Exception Hold do, exactly?":
            dolen "It removes a soul from the standard processing queue. Flags them for further review."
            kael "Review by whom?"
            dolen "The appropriate department."
            kael "Which is?"
            "A beat."
            dolen "That depends on the case."
            $ game_state.add_tone("diligent")

        "Understood. I'll review the forms.":
            "DOLEN looks relieved."
            dolen "Good. That's the right attitude."

            $ tone = game_state.get_dominant_tone()
            if tone == "sardonic" or tone == "neutral":
                kael_sardonic "The right attitude is not asking questions. Message received."
            elif tone == "diligent":
                kael_diligent "Something changed. I need to understand what."
            elif tone == "compassionate":
                kael_compassionate "A hundred times more souls flagged. That's a hundred times more people in limbo."
            else:
                kael_complicit "New threshold, same job. Process the forms."

            $ game_state.add_tone("complicit")

    jump dolen_warning

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 1.7 — DOLEN'S WARNING
## ═══════════════════════════════════════════════════════════════════════════

label dolen_warning:
    "DOLEN closes the folder. Slides it back toward himself."

    dolen "One more thing."

    "He lowers his voice. Not conspiratorially—nervously."

    dolen "While you were gone, there was... scrutiny. Of the department. Our metrics were reviewed."

    kael "And?"

    dolen "And we're fine. We're meeting quota. But..."

    "He glances at the half-closed blinds."

    dolen "The people who reviewed our metrics are still here. Somewhere in the building. I don't know which floor."

    kael "Who are they?"

    dolen "I don't know. The email signature just said \"Office of Internal Assessment.\""

    "Beat."

    dolen "I've never heard of that office."

    "Another beat."

    dolen "If anyone from an office you don't recognize asks you questions, you are to answer truthfully and then report the interaction to me immediately."

    menu dolen_warning_response:
        "Are we in trouble?":
            dolen "No. No, we're not in trouble."
            "He doesn't sound certain."
            dolen "Just... do your job. Process your queue. Don't attract attention."
            $ game_state.add_tone("compassionate")

        "What kind of questions?":
            dolen "I don't know. They didn't ask me anything. They just... observed. Made notes."
            "He looks at KAEL."
            dolen "If they talk to you, just answer honestly. And tell me afterward."
            $ game_state.add_tone("diligent")

        "Understood.":
            dolen "Good."
            $ game_state.add_tone("complicit")

    "He stands. Meeting over."

    dolen "Welcome back, [game_state.player_designation]. Your first shift starts in ten minutes."
    dolen "Reorientation is at 14:00—attendance is mandatory."

    "He pauses at the door."

    dolen "Mira was a good processor. You're a good processor too."

    "It sounds like a warning."

    $ game_state.set_flag("dolen_warning_received")

    jump scene_first_shift

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 2.1 — TERMINAL 7 (First Shift)
## ═══════════════════════════════════════════════════════════════════════════

label scene_first_shift:
    scene black
    with dissolve

    "KAEL returns to their desk. The Processing Terminal hums to life as they sit down."

    system "REGISTRY SOUL PROCESSING TERMINAL v7.4.1"
    system "PROCESSOR: [game_state.player_designation]"
    system "SHIFT: Day Cycle 1 of 5"
    system "QUEUE: [len(soul_queue)] SOULS PENDING"
    system "QUOTA: [game_state.shift_quota] SOULS PROCESSED"

    kael_diligent "Forty souls. Eight hours. Five minutes per soul if nothing goes wrong. Things always go wrong."

    "Ready to begin?"

    menu begin_shift:
        "BEGIN SHIFT":
            jump processing_tutorial

label processing_tutorial:
    "The first soul file appears on screen."

    # Process first few standard souls as tutorial
    $ tutorial_soul = soul_queue[0]

    system "═══════════════════════════════════════════════════════"
    system "FORM 7-A: STANDARD INTAKE"
    system "═══════════════════════════════════════════════════════"
    system "SOUL DESIGNATION: [tutorial_soul.designation]"
    system "NAME (LIFE): [tutorial_soul.name]"
    system "CAUSE: [tutorial_soul.cause]"
    system "CLASSIFICATION RECOMMENDATION: STANDARD ASSIGNMENT"
    system "ROUTING: Queue 7 (General Population)"

    "Most souls receive a CLASSIFICATION RECOMMENDATION from the automated system."
    "Your job is to verify this recommendation and approve routing."

    menu tutorial_choice:
        "APPROVE ROUTING":
            $ tutorial_soul.processed = True
            $ game_state.process_soul()
            $ current_soul_index += 1
            system "PROCESSED"

    "The file closes. A stamp animation: PROCESSED."
    "The queue counter updates."

    kael_diligent "One down. Thirty-nine to go."

    jump processing_montage

label processing_montage:
    "A brief montage of standard processing. Files appear, are approved, close. The rhythm establishes itself."

    # Process souls 2-7 automatically
    python:
        for i in range(1, 7):
            if i < len(soul_queue):
                soul_queue[i].processed = True
                game_state.process_soul()
        current_soul_index = 7

    system "Soul 2: Maria Vance. Natural causes. PROCESSED."
    system "Soul 3: Dmitri Holloway. Accident. PROCESSED."
    system "Soul 4: Susan Park. Natural causes. PROCESSED."
    system "Soul 5: Theodore Bright. Natural causes. PROCESSED."
    system "Soul 6: Amara Osei. Natural causes. PROCESSED."
    system "Soul 7: James Chen. Illness. PROCESSED."

    system "QUEUE: [len(soul_queue) - current_soul_index] SOULS PENDING"

    $ tone = game_state.get_dominant_tone()
    if tone == "sardonic" or tone == "neutral":
        kael_sardonic "Seven souls. Seven lives reduced to form fields. Seven eternities assigned with a click."
    elif tone == "diligent":
        kael_diligent "Seven down, efficient pace. At this rate, I'll clear quota with time to spare."
    elif tone == "compassionate":
        kael_compassionate "Seven people. They had names. Families. I didn't even read their summaries."
    else:
        kael_complicit "Seven processed. The system works."

    jump first_exception_hold

## ═══════════════════════════════════════════════════════════════════════════
## SCENE 2.4 — THE FIRST EXCEPTION HOLD (Rebecca Thorne)
## ═══════════════════════════════════════════════════════════════════════════

label first_exception_hold:
    "The eighth file appears. Something is different."

    $ rebecca = soul_queue[7]  # Rebecca is at index 7

    system "═══════════════════════════════════════════════════════"
    system "FORM 7-A: STANDARD INTAKE"
    system "═══════════════════════════════════════════════════════"
    system "SOUL DESIGNATION: {color=#ffaa44}[rebecca.designation]{/color}"
    system "NAME (LIFE): [rebecca.name]"
    system "CAUSE: {color=#ffcc00}[rebecca.cause]{/color}"
    system "CLASSIFICATION RECOMMENDATION: {color=#ff6666}██████████{/color}"
    system "ROUTING: {color=#ff6666}██████████{/color}"
    system "EXCEPTION HOLD: {color=#ffaa44}[■] AUTOMATICALLY FLAGGED{/color}"
    system "─────────────────────────────────────────────────────"
    system "STATUS: EXCEPTION HOLD TRIGGERED"
    system "REASON: Threshold Parameter Exceeded (Code 7.4.1-E)"

    kael_diligent "Exception Hold. The new threshold Dolen mentioned."

    "Some souls are automatically flagged for Exception Hold based on system parameters."

    menu exception_hold_choice:
        "CONFIRM EXCEPTION HOLD — Route to Review Queue":
            $ rebecca.processed = True
            $ game_state.process_soul(is_exception_hold=True)
            $ current_soul_index += 1

            system "HELD FOR REVIEW"

            $ tone = game_state.get_dominant_tone()
            if tone == "sardonic" or tone == "neutral":
                kael_sardonic "Held for review. By whom? For how long? The form doesn't say."
            elif tone == "diligent":
                kael_diligent "Proper procedure. The system flagged her for a reason."
            elif tone == "compassionate":
                kael_compassionate "She'll wait in a queue somewhere. Another queue. Forever queues."
            else:
                kael_complicit "Not my decision. Not my problem."

            jump prototype_end

        "INTERVIEW SOUL — Request direct interaction":
            $ game_state.set_flag("chose_interview_rebecca")
            jump interview_rebecca

        "OVERRIDE EXCEPTION HOLD — Return to Standard Processing":
            jump override_rebecca

        "ESCALATE TO SUPERVISOR — Request Clearance Level 3 review":
            $ game_state.escalations += 1
            system "ESCALATION REQUEST SUBMITTED"
            system "Supervisor Dolen has been notified."
            system "Expected response time: 2-4 hours."

            kael_sardonic "Two to four hours. For one soul. At this rate, quota's a dream."

            $ current_soul_index += 1
            jump prototype_end

label interview_rebecca:
    system "SOUL INTERVIEW REQUEST — R-0012 (Rebecca Thorne)"
    system "STATUS: Pending"
    system "ESTIMATED WAIT: 4 minutes"
    system "The soul will be routed to Interview Booth 7."

    call rebecca_thorne_interview

    # After interview, show metadata discovery
    jump post_interview_metadata

label post_interview_metadata:
    scene black
    with dissolve

    "KAEL returns to Terminal 7. Rebecca's file is still open."

    if game_state.get_flag("rebecca_hinted_metadata"):
        kael_diligent "She said to look at the metadata. The routing codes."

    "Press M to expand the file's metadata section."

    menu view_metadata:
        "View Metadata [M]":
            pass

    system "═══════════════════════════════════════════════════════"
    system "FILE METADATA — R-0012 (Rebecca Thorne)"
    system "═══════════════════════════════════════════════════════"
    system "INTAKE TIMESTAMP: 4019.147.0342"
    system "PROCESSING STATUS: Exception Hold (Auto)"
    system "EXCEPTION CODE: 7.4.1-E"
    system "ROUTING HISTORY:"
    system "  → Initial: Queue 7 (General Population)"
    system "  → Modified: {color=#ff6666}[REDACTED]{/color}"
    system "  → Current: Exception Hold Queue"
    system "EXCEPTION TRIGGER PARAMETER:"
    system "  Threshold exceeded on field: {color=#ff6666}[DATA EXPUNGED]{/color}"
    system "─────────────────────────────────────────────────────"
    system "SIMILAR CASES (Last 30 Days): {color=#ffcc00}2,847{/color}"
    system "SIMILAR CASES (Last 365 Days): {color=#ff6666}14,221{/color}"
    system "SIMILAR CASES (Historical Avg/Year): 142"

    "KAEL stares at the numbers."

    kael_diligent "14,221 Exception Holds in the past year. The historical average is 142."
    kael_diligent "That's not a statistical adjustment. That's a hundred-fold increase."

    menu log_observation:
        "LOG OBSERVATION — Add to Irregularity Log":
            $ game_state.add_irregularity(
                "Exception Hold Rate Anomaly",
                "Exception Hold cases have increased 100x from historical average. 14,221 cases in the past year vs. typical 142/year. Change coincides with Policy Memo 7.4.1.\n\nQuestions:\n- What parameter changed?\n- Where are Exception Hold souls routed?\n- Who authorized this change?\n\nRelated: Soul R-0012 (Rebecca Thorne)",
                "observation"
            )
            system "IRREGULARITY LOG UPDATED"
            system "Entry 001 — Exception Hold Rate Anomaly"

            $ tone = game_state.get_dominant_tone()
            if tone == "sardonic" or tone == "neutral":
                kael_sardonic "A hundred times more souls flagged. Someone knows why. Someone decided not to tell the processors."
            elif tone == "diligent":
                kael_diligent "This needs documentation. If there's an error, it needs to be reported. Through proper channels."
            elif tone == "compassionate":
                kael_compassionate "Fourteen thousand souls in limbo. Because a parameter changed."
            else:
                kael_complicit "I shouldn't be logging this. This is exactly the kind of thing that attracts attention."

        "DISMISS — Close metadata panel":
            $ tone = game_state.get_dominant_tone()
            if tone == "sardonic" or tone == "neutral":
                kael_sardonic "Not my problem. I'm just here to stamp forms."
            elif tone == "diligent":
                kael_diligent "I'll remember the numbers. I don't need to write them down."
            elif tone == "compassionate":
                kael_compassionate "Maybe there's a good reason. Maybe the system is working as intended."
            else:
                kael_complicit "Smart. Don't leave a trail."

    jump prototype_end

label override_rebecca:
    system "WARNING: Override requires written justification."
    system "All overrides are logged and reviewed quarterly."

    menu override_confirm:
        "Submit Override — Return to standard processing":
            $ rebecca = soul_queue[7]
            $ rebecca.processed = True
            $ game_state.process_soul()
            $ current_soul_index += 1

            system "PROCESSED (OVERRIDE)"

            kael_diligent "Override logged. My name on it. If anyone asks why I sent an Exception Hold case to standard processing, I'll need a better answer."

            $ game_state.add_tone("sardonic")

        "Cancel — Return to terminal":
            jump first_exception_hold

    jump prototype_end

## ═══════════════════════════════════════════════════════════════════════════
## PROTOTYPE END
## ═══════════════════════════════════════════════════════════════════════════

label prototype_end:
    scene black
    with dissolve

    centered "{size=28}ACT I COMPLETE{/size}"
    centered "{size=20}The Underlord's Registry — Ren'Py Prototype{/size}"

    pause 1.0

    system "═══════════════════════════════════════════════════════"
    system "SESSION STATISTICS"
    system "═══════════════════════════════════════════════════════"
    system "Souls Processed: [game_state.souls_processed]"
    system "Exception Holds: [game_state.exception_holds]"
    system "Interviews Conducted: [game_state.interviews_conducted]"
    system "Escalations: [game_state.escalations]"
    system "Irregularity Log Entries: [len(game_state.irregularity_log)]"
    system "─────────────────────────────────────────────────────"
    system "Dominant Tone: [game_state.get_dominant_tone().upper()]"

    # Show relationship status
    if game_state.get_flag("asked_pressa_about_mira"):
        system "Pressa: Knows you're asking questions"
    if game_state.get_flag("asked_dolen_about_mira"):
        system "Dolen: Noticed your interest in Mira"
    if game_state.get_flag("rebecca_promised_help"):
        system "Rebecca Thorne: Trusts you to investigate"

    system "═══════════════════════════════════════════════════════"

    "Press L to view your Irregularity Log."
    "Thank you for playing the prototype."

    menu end_menu:
        "Return to Main Menu":
            return

        "View Irregularity Log":
            $ show_irregularity_log = True
            "Press L to toggle the log, or choose an option below."
            jump end_menu

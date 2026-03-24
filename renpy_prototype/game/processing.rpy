## processing.rpy — The Underlord's Registry
## Terminal action handlers and processing logic

# Labels for processing actions

label process_soul(soul):
    """Main entry point for processing a soul via terminal."""

    # Show the terminal
    $ result = renpy.call_screen("processing_terminal", soul)

    if result == "close":
        return

    elif result == "approve" or result == "confirm":
        # Standard approval / confirm exception hold
        $ soul.processed = True
        $ game_state.process_soul(is_exception_hold=soul.is_exception_hold)

        if soul.is_exception_hold:
            system "HELD FOR REVIEW"

            # Show tone-based internal response
            $ tone = game_state.get_dominant_tone()
            if tone == "sardonic" or tone == "neutral":
                kael_sardonic "Held for review. By whom? For how long? The form doesn't say."
            elif tone == "diligent":
                kael_diligent "Proper procedure. The system flagged her for a reason."
            elif tone == "compassionate":
                kael_compassionate "She'll wait in a queue somewhere. Another queue. Forever queues."
            else:  # complicit
                kael_complicit "Not my decision. Not my problem."
        else:
            system "PROCESSED"

        $ current_soul_index += 1
        return

    elif result == "override":
        # Override exception hold
        call override_exception_hold(soul)
        return

    elif result == "interview":
        # Interview the soul
        call interview_soul(soul)
        # Return to terminal after interview
        jump expression "process_soul"
        return

    elif result == "escalate":
        # Escalate to supervisor
        call escalate_soul(soul)
        return

    elif result == "modify":
        # Modify routing (stub)
        system "ROUTING MODIFICATION"
        system "Feature not available in prototype."
        jump expression "process_soul"
        return

label override_exception_hold(soul):
    """Handle exception hold override."""

    system "WARNING: Override requires written justification."
    system "All overrides are logged and reviewed quarterly."

    menu:
        "Yes, override the exception hold":
            $ soul.processed = True
            $ game_state.process_soul(is_exception_hold=False)
            system "PROCESSED (OVERRIDE)"

            $ tone = game_state.get_dominant_tone()
            if tone == "sardonic" or tone == "neutral":
                kael_sardonic "Override logged. My name on it. If anyone asks why, I'll need a better answer than 'I was curious.'"
            elif tone == "diligent":
                kael_diligent "Override logged. I should document my reasoning."
            elif tone == "compassionate":
                kael_compassionate "At least she won't be stuck in limbo."
            else:
                kael_complicit "One less Exception Hold. Quota thanks me."

            $ current_soul_index += 1

        "No, return to terminal":
            pass

    return

label escalate_soul(soul):
    """Escalate soul to supervisor."""

    system "ESCALATION REQUEST SUBMITTED"
    system "Supervisor Dolen has been notified."
    system "Expected response time: 2-4 hours."
    system "Soul [soul.designation] has been placed in Holding Queue pending supervisor review."

    $ game_state.escalations += 1

    $ tone = game_state.get_dominant_tone()
    if tone == "sardonic" or tone == "neutral":
        kael_sardonic "Two to four hours. For one soul. At this rate, quota's a dream."
    elif tone == "diligent":
        kael_diligent "Proper channels. Dolen will know what to do."
    elif tone == "compassionate":
        kael_compassionate "More waiting. But at least someone with answers will look at this."
    else:
        kael_complicit "Escalated. Not my problem anymore."

    $ current_soul_index += 1
    return

label interview_soul(soul):
    """Route to appropriate interview based on soul."""

    $ game_state.interviews_conducted += 1

    if soul.designation == "R-0012":
        # Rebecca Thorne - special interview
        call rebecca_thorne_interview
    else:
        # Generic interview
        call generic_interview(soul)

    $ soul.interviewed = True
    return

label generic_interview(soul):
    """Generic interview for non-special souls."""

    scene black with dissolve
    "The soul [soul.name] materializes in Interview Booth 7."

    "Soul" "You wanted to talk to me?"

    menu:
        "Yes. Tell me about your life.":
            "Soul" "[soul.summary]"
            "Soul" "That's... that's all there is, really."

        "Just a routine check. You can go.":
            "Soul" "Oh. Alright then."

    "The soul fades, returning to the queue."
    $ soul.interview_notes = "Standard interview conducted. No anomalies noted."

    return

# Helper label for checking if we should offer to log an observation
label offer_log_observation(title, content, category="observation"):
    """Prompt player to log an observation."""

    $ should_log = renpy.call_screen("log_observation_prompt", title, content, category)

    if should_log:
        $ game_state.add_irregularity(title, content, category)
        system "IRREGULARITY LOG UPDATED"
        system "Entry [game_state.next_entry_id - 1] — [title]"
    else:
        $ tone = game_state.get_dominant_tone()
        if tone == "sardonic" or tone == "neutral":
            kael_sardonic "Not my problem. I'm just here to stamp forms."
        elif tone == "diligent":
            kael_diligent "I'll remember the numbers. I don't need to write them down."
        elif tone == "compassionate":
            kael_compassionate "Maybe there's a good reason. Maybe the system is working as intended."
        else:
            kael_complicit "Smart. Don't leave a trail."

    return

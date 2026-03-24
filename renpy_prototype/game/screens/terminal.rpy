## terminal.rpy — The Underlord's Registry
## Processing Terminal screen with Form 7-A display

screen processing_terminal(soul):
    modal True
    zorder 100

    default show_metadata = False

    # Dark overlay
    add Solid("#0a0a0a") alpha 0.95

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 650
        background Solid("#0a1a0a")
        padding (20, 20)

        vbox:
            spacing 10

            # Header
            hbox:
                xfill True
                text "═" * 55 style "registry_terminal_text"

            hbox:
                xfill True
                text "FORM 7-A: STANDARD INTAKE" style "registry_header_text" xalign 0.5

            hbox:
                xfill True
                text "═" * 55 style "registry_terminal_text"

            null height 10

            # Soul info
            vbox:
                spacing 5

                hbox:
                    text "SOUL DESIGNATION: " style "registry_terminal_text"
                    if soul.is_exception_hold:
                        text "[soul.designation]" style "registry_exception_text"
                    else:
                        text "[soul.designation]" style "registry_terminal_text"

                hbox:
                    text "NAME (LIFE): " style "registry_terminal_text"
                    text "[soul.name]" style "registry_terminal_text"

                hbox:
                    text "CAUSE: " style "registry_terminal_text"
                    if "[REDACTED" in soul.cause:
                        text "[soul.cause]" style "registry_warning_text"
                    else:
                        text "[soul.cause]" style "registry_terminal_text"

                hbox:
                    text "LIFE SUMMARY: " style "registry_terminal_text"

                frame:
                    background Solid("#0a2a0a")
                    xfill True
                    padding (10, 10)
                    text "[soul.summary]" style "registry_terminal_text" size 16

            null height 5

            # Classification and routing
            hbox:
                xfill True
                text "─" * 55 style "registry_terminal_text"

            vbox:
                spacing 5

                hbox:
                    text "CLASSIFICATION: " style "registry_terminal_text"
                    if "██" in soul.classification:
                        text "[soul.classification]" style "registry_error_text"
                    else:
                        text "[soul.classification]" style "registry_terminal_text"

                hbox:
                    text "ROUTING: " style "registry_terminal_text"
                    if "██" in soul.routing:
                        text "[soul.routing]" style "registry_error_text"
                    else:
                        text "[soul.routing]" style "registry_terminal_text"

                # Exception Hold status
                if soul.is_exception_hold:
                    null height 5
                    hbox:
                        text "EXCEPTION HOLD: " style "registry_terminal_text"
                        text "[■] AUTOMATICALLY FLAGGED" style "registry_exception_text"

                    hbox:
                        text "REASON: " style "registry_terminal_text"
                        text "Threshold Parameter Exceeded (Code 7.4.1-E)" style "registry_warning_text"

            # Interview notes if present
            if soul.interviewed and soul.interview_notes:
                null height 5
                hbox:
                    xfill True
                    text "─" * 55 style "registry_terminal_text"
                text "INTERVIEW NOTES:" style "registry_terminal_text"
                frame:
                    background Solid("#1a2a1a")
                    xfill True
                    padding (10, 5)
                    text "[soul.interview_notes]" style "registry_terminal_text" size 16

            # Metadata section (toggled with M)
            if show_metadata:
                null height 5
                hbox:
                    xfill True
                    text "─" * 55 style "registry_terminal_text"

                text "FILE METADATA" style "registry_header_text" size 18

                vbox:
                    spacing 3
                    text "INTAKE TIMESTAMP: 4019.147.0342" style "registry_terminal_text" size 16
                    text "PROCESSING STATUS: Exception Hold (Auto)" style "registry_terminal_text" size 16
                    text "EXCEPTION CODE: 7.4.1-E" style "registry_terminal_text" size 16

                    null height 5
                    text "SIMILAR CASES (Last 30 Days): {color=#ffcc00}2,847{/color}" style "registry_terminal_text" size 16
                    text "SIMILAR CASES (Last 365 Days): {color=#ff6666}14,221{/color}" style "registry_terminal_text" size 16
                    text "SIMILAR CASES (Historical Avg/Year): 142" style "registry_terminal_text" size 16

            null height 10

            # Action buttons
            hbox:
                xfill True
                text "─" * 55 style "registry_terminal_text"

            text "PROCESSOR ACTION REQUIRED:" style "registry_terminal_text"

            null height 5

            hbox:
                spacing 20
                xalign 0.5

                if soul.is_exception_hold:
                    textbutton "[1] CONFIRM HOLD":
                        action Return("confirm")
                        style "terminal_button"

                    textbutton "[2] OVERRIDE":
                        action Return("override")
                        style "terminal_button"
                else:
                    textbutton "[1] APPROVE":
                        action Return("approve")
                        style "terminal_button"

                    textbutton "[2] MODIFY":
                        action Return("modify")
                        style "terminal_button"

                if not soul.interviewed:
                    textbutton "[3] INTERVIEW":
                        action Return("interview")
                        style "terminal_button"
                else:
                    textbutton "[3] INTERVIEWED" style "terminal_button_disabled"

                textbutton "[4] ESCALATE":
                    action Return("escalate")
                    style "terminal_button"

            null height 10

            # Footer with queue info and controls
            hbox:
                xfill True
                text "═" * 55 style "registry_terminal_text"

            hbox:
                xfill True
                spacing 30

                text "Queue: [current_soul_index + 1]/[len(soul_queue)]" style "registry_terminal_text" size 14
                text "Processed: [game_state.souls_processed]/[game_state.shift_quota]" style "registry_terminal_text" size 14
                text "[M] Metadata" style "registry_terminal_text" size 14
                text "[ESC] Close" style "registry_terminal_text" size 14

    # Keyboard shortcuts
    key "m" action ToggleScreenVariable("show_metadata")
    key "M" action ToggleScreenVariable("show_metadata")

    if soul.is_exception_hold:
        key "1" action Return("confirm")
    else:
        key "1" action Return("approve")

    if soul.is_exception_hold:
        key "2" action Return("override")
    else:
        key "2" action Return("modify")

    if not soul.interviewed:
        key "3" action Return("interview")

    key "4" action Return("escalate")
    key "escape" action Return("close")

style terminal_button:
    background Solid("#1a3a1a")
    hover_background Solid("#2a4a2a")
    padding (15, 8)
    color "#80ff80"
    hover_color "#aaffaa"
    font "DejaVuSansMono.ttf"
    size 16

style terminal_button_disabled:
    background Solid("#1a1a1a")
    padding (15, 8)
    color "#404040"
    font "DejaVuSansMono.ttf"
    size 16

# Log observation prompt screen
screen log_observation_prompt(title, content, category="observation"):
    modal True
    zorder 110

    add Solid("#000000") alpha 0.8

    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        background Solid("#0a1a0a")
        padding (20, 20)

        vbox:
            spacing 15

            text "LOG THIS OBSERVATION?" style "registry_header_text" xalign 0.5

            null height 10

            frame:
                background Solid("#0a2a0a")
                xfill True
                padding (15, 15)

                vbox:
                    spacing 5
                    text "[title]" style "registry_terminal_text" bold True
                    null height 5
                    text "[content]" style "registry_terminal_text" size 16

            null height 10

            text "The Irregularity Log is your personal record of" style "registry_terminal_text" size 14 xalign 0.5
            text "anomalies encountered during processing." style "registry_terminal_text" size 14 xalign 0.5

            null height 15

            hbox:
                xalign 0.5
                spacing 30

                textbutton "LOG OBSERVATION":
                    action Return(True)
                    style "terminal_button"

                textbutton "DISMISS":
                    action Return(False)
                    style "terminal_button"

    key "escape" action Return(False)
    key "Return" action Return(True)

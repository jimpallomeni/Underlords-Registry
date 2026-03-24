## irregularity_log.rpy — The Underlord's Registry
## Overlay screen for the Irregularity Log (toggle with L)

# Track log visibility globally
default show_irregularity_log = False

screen irregularity_log():
    zorder 90
    modal False

    if show_irregularity_log:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -20
            yoffset 20
            xsize 400
            ymaximum 500
            background Solid("#0a0a1a", alpha=0.95)
            padding (15, 15)

            vbox:
                spacing 10

                # Header
                hbox:
                    xfill True
                    text "═" * 30 color "#80b0e0" font "DejaVuSansMono.ttf" size 14

                text "IRREGULARITY LOG" color "#80b0e0" font "DejaVuSansMono.ttf" size 18 bold True xalign 0.5
                text "Processor [game_state.player_designation]" color "#80b0e0" font "DejaVuSansMono.ttf" size 12 xalign 0.5

                hbox:
                    xfill True
                    text "═" * 30 color "#80b0e0" font "DejaVuSansMono.ttf" size 14

                null height 5

                # Entries
                if len(game_state.irregularity_log) == 0:
                    text "No entries logged." color "#666666" font "DejaVuSansMono.ttf" size 14 xalign 0.5

                else:
                    viewport:
                        ymaximum 350
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 10

                            for entry in game_state.irregularity_log:
                                frame:
                                    background Solid("#0a1a2a")
                                    xfill True
                                    padding (10, 8)

                                    vbox:
                                        spacing 3

                                        hbox:
                                            text "Entry [entry.id]" color "[entry.get_color()]" font "DejaVuSansMono.ttf" size 12
                                            text " — " color "#666666" font "DejaVuSansMono.ttf" size 12
                                            text "[entry.category.upper()]" color "[entry.get_color()]" font "DejaVuSansMono.ttf" size 12

                                        text "[entry.title]" color "#ffffff" font "DejaVuSansMono.ttf" size 14 bold True

                                        null height 3

                                        text "[entry.content]" color "#cccccc" font "DejaVuSansMono.ttf" size 12

                null height 5

                # Footer
                hbox:
                    xfill True
                    text "─" * 30 color "#80b0e0" font "DejaVuSansMono.ttf" size 14

                text "[L] Close Log" color "#666666" font "DejaVuSansMono.ttf" size 12 xalign 0.5

# Global key binding for log toggle
screen log_toggle_key():
    zorder 0
    key "l" action ToggleVariable("show_irregularity_log")
    key "L" action ToggleVariable("show_irregularity_log")

# Initialize the log toggle key listener
init python:
    config.overlay_screens.append("log_toggle_key")
    config.overlay_screens.append("irregularity_log")

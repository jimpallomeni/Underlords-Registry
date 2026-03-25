## screens.rpy — The Underlord's Registry
## Complete menu system with noir aesthetic

################################################################################
## Say Screen
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 185
    background Solid("#000000cc")

style namebox:
    xpos 240
    xanchor 0.0
    ypos 0
    background Solid("#000000aa")
    padding (5, 5, 5, 5)

style say_label:
    font "DejaVuSans.ttf"
    size 24
    color "#80ff80"
    xalign 0.0
    yalign 0.5

style say_dialogue:
    font "DejaVuSans.ttf"
    size 22
    color "#ffffff"
    xpos 268
    xsize 744
    ypos 50

################################################################################
## Input Screen
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign 0.0
            xpos 268
            xsize 744
            ypos 50

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input_prompt:
    font "DejaVuSans.ttf"
    size 22
    color "#80ff80"

style input:
    font "DejaVuSans.ttf"
    size 22
    color "#ffffff"

################################################################################
## Choice Screen
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing 22

style choice_button:
    xsize 790
    padding (20, 10, 20, 10)
    background Solid("#1a3a1a")
    hover_background Solid("#2a5a2a")

style choice_button_text:
    xalign 0.5
    color "#cccccc"
    hover_color "#80ff80"
    font "DejaVuSans.ttf"
    size 22

################################################################################
## Quick Menu Screen
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -10

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button:
    background Solid("#00000088")
    hover_background Solid("#1a3a1a")
    padding (8, 4, 8, 4)

style quick_button_text:
    font "DejaVuSansMono.ttf"
    size 12
    color "#666666"
    hover_color "#80ff80"
    selected_color "#80ff80"

################################################################################
## Main Menu Screen
################################################################################

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add Solid("#0a0a0a")

    frame:
        xalign 0.5
        yalign 0.4
        background None

        vbox:
            spacing 10
            xalign 0.5

            text "{font=DejaVuSansMono.ttf}{size=14}{color=#1a3a1a}+======================================================+{/color}{/size}{/font}" xalign 0.5

            null height 10

            text "{size=42}{color=#80ff80}THE UNDERLORD'S REGISTRY{/color}{/size}" xalign 0.5
            text "{size=18}{color=#4d994d}Season One: The Department of Final Intake{/color}{/size}" xalign 0.5

            null height 5

            text "{font=DejaVuSansMono.ttf}{size=14}{color=#1a3a1a}+======================================================+{/color}{/size}{/font}" xalign 0.5

    frame:
        xalign 0.5
        yalign 0.75
        background None

        vbox:
            spacing 15
            xalign 0.5

            textbutton _("NEW SHIFT") action Start() xalign 0.5
            textbutton _("CONTINUE") action ShowMenu("load") xalign 0.5
            textbutton _("PREFERENCES") action ShowMenu("preferences") xalign 0.5
            textbutton _("QUIT") action Quit(confirm=False) xalign 0.5

    text "{size=12}{color=#333333}Ren'Py Prototype v0.1{/color}{/size}":
        xalign 1.0
        yalign 1.0
        xoffset -10
        yoffset -10

style main_menu_frame:
    background None

style main_menu_vbox:
    spacing 15

style main_menu_button:
    xsize 300
    padding (20, 10, 20, 10)
    background Solid("#0a0a0a")
    hover_background Solid("#1a3a1a")

style main_menu_button_text:
    font "DejaVuSansMono.ttf"
    size 20
    color "#4d994d"
    hover_color "#80ff80"
    xalign 0.5

################################################################################
## Game Menu Base Screen
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    add Solid("#0a0a0acc")

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"
                use navigation

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude

                else:
                    transclude

    frame:
        xpos 300
        ypos 30
        background None
        text "{size=28}{color=#80ff80}[title]{/color}{/size}"

    textbutton _("< Return"):
        style "return_button"
        action Return()
        xpos 40
        ypos 30

    key "game_menu" action Return()

style game_menu_outer_frame:
    background None
    xfill True
    yfill True

style game_menu_navigation_frame:
    xsize 250
    yfill True
    background Solid("#0f0f0f")

style game_menu_content_frame:
    left_margin 20
    right_margin 20
    top_margin 80
    bottom_margin 20

style return_button:
    background None
    hover_background Solid("#1a3a1a")
    padding (10, 5, 10, 5)

style return_button_text:
    font "DejaVuSansMono.ttf"
    size 16
    color "#666666"
    hover_color "#80ff80"

################################################################################
## Navigation Screen
################################################################################

screen navigation():
    style_prefix "navigation"

    vbox:
        xalign 0.5
        ypos 100
        spacing 8

        if main_menu:
            textbutton _("New Shift") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            null height 20
            textbutton _("Main Menu") action MainMenu()

        null height 20
        textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button:
    xsize 200
    padding (15, 8, 15, 8)
    background None
    hover_background Solid("#1a3a1a")
    selected_background Solid("#1a3a1a")

style navigation_button_text:
    font "DejaVuSansMono.ttf"
    size 16
    color "#666666"
    hover_color "#80ff80"
    selected_color "#80ff80"
    xalign 0.5

################################################################################
## Save and Load Screens
################################################################################

screen save():
    tag menu
    use file_slots(_("Save Game"))

screen load():
    tag menu
    use file_slots(_("Load Game"))

screen file_slots(title):
    use game_menu(title):

        fixed:
            hbox:
                style_prefix "page"
                xalign 0.5
                ypos 0
                spacing 10

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("Auto") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("Quick") action FilePage("quick")

                for page in range(1, 6):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

            grid 3 2:
                style_prefix "slot"
                xalign 0.5
                yalign 0.6
                spacing 20

                for i in range(6):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        vbox:
                            xalign 0.5
                            spacing 5

                            add FileScreenshot(slot):
                                xalign 0.5

                            text FileTime(slot, format=_("%b %d, %H:%M"), empty=_("- Empty -")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

style page_button:
    padding (10, 5, 10, 5)
    background Solid("#1a1a1a")
    hover_background Solid("#2a4a2a")
    selected_background Solid("#1a3a1a")

style page_button_text:
    font "DejaVuSansMono.ttf"
    size 14
    color "#666666"
    hover_color "#80ff80"
    selected_color "#80ff80"

style slot_button:
    xsize 280
    ysize 200
    padding (10, 10, 10, 10)
    background Solid("#1a1a1a")
    hover_background Solid("#2a4a2a")
    selected_background Solid("#1a3a1a")

style slot_time_text:
    font "DejaVuSansMono.ttf"
    size 14
    color "#80ff80"
    xalign 0.5

style slot_name_text:
    font "DejaVuSansMono.ttf"
    size 12
    color "#888888"
    xalign 0.5

################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:
            xalign 0.5
            spacing 30

            hbox:
                style_prefix "pref"
                box_wrap True
                spacing 40

                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Windowed") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")

            null height 20

            vbox:
                style_prefix "slider"
                spacing 20

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                vbox:
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

            null height 20

            vbox:
                style_prefix "slider"
                spacing 20

                vbox:
                    label _("Music Volume")
                    bar value Preference("music volume")

                vbox:
                    label _("Sound Volume")
                    bar value Preference("sound volume")

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "check_button"

style pref_label:
    top_margin 10
    bottom_margin 5

style pref_label_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#80ff80"

style radio_label is pref_label
style radio_label_text is pref_label_text

style radio_button:
    padding (20, 5, 5, 5)
    background None
    hover_background Solid("#1a3a1a22")

style radio_button_text:
    font "DejaVuSansMono.ttf"
    size 16
    color "#666666"
    hover_color "#aaffaa"
    selected_color "#80ff80"

style check_label is pref_label
style check_label_text is pref_label_text

style check_button:
    padding (20, 5, 5, 5)
    background None
    hover_background Solid("#1a3a1a22")

style check_button_text:
    font "DejaVuSansMono.ttf"
    size 16
    color "#666666"
    hover_color "#aaffaa"
    selected_color "#80ff80"

style slider_label:
    top_margin 5
    bottom_margin 5

style slider_label_text:
    font "DejaVuSansMono.ttf"
    size 16
    color "#80ff80"

style slider_slider:
    xsize 500
    ysize 24
    base_bar Solid("#1a1a1a")
    hover_base_bar Solid("#2a2a2a")
    thumb Solid("#80ff80")
    hover_thumb Solid("#aaffaa")

style slider_vbox:
    xsize 600

################################################################################
## History Screen
################################################################################

screen history():
    tag menu
    predict False

    use game_menu(_("History"), scroll="viewport", yinitial=1.0):
        style_prefix "history"

        for h in _history_list:
            window:
                has hbox:
                    spacing 20

                if h.who:
                    text h.who:
                        style "history_name"
                        min_width 150
                else:
                    text "":
                        min_width 150

                text h.what:
                    style "history_text"

        if not _history_list:
            text _("The dialogue history is empty."):
                xalign 0.5
                color "#666666"

define config.history_length = 250

style history_window:
    xfill True
    ysize 80
    background Solid("#0a0a0a")
    padding (10, 5, 10, 5)

style history_name:
    font "DejaVuSans.ttf"
    size 16
    color "#80ff80"
    text_align 1.0

style history_text:
    font "DejaVuSans.ttf"
    size 16
    color "#cccccc"

################################################################################
## Confirm Screen
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#000000dd")

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            xalign 0.5
            spacing 30

            text "{font=DejaVuSansMono.ttf}{size=12}{color=#4d994d}+========================================+{/color}{/size}{/font}" xalign 0.5

            text "[message]":
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 50

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

            text "{font=DejaVuSansMono.ttf}{size=12}{color=#4d994d}+========================================+{/color}{/size}{/font}" xalign 0.5

    key "game_menu" action no_action

style confirm_frame:
    background Solid("#0a0a0a")
    padding (50, 30, 50, 30)

style confirm_prompt:
    font "DejaVuSansMono.ttf"
    size 20
    color "#80ff80"
    text_align 0.5

style confirm_button:
    xsize 120
    padding (20, 10, 20, 10)
    background Solid("#1a3a1a")
    hover_background Solid("#2a5a2a")

style confirm_button_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#80ff80"
    hover_color "#aaffaa"
    xalign 0.5

################################################################################
## Skip Indicator Screen
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("SKIPPING")
            text ">" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text ">" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text ">" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame:
    ypos 10
    xpos 10
    background Solid("#0a0a0a")
    padding (15, 8, 15, 8)

style skip_text:
    font "DejaVuSansMono.ttf"
    size 14
    color "#80ff80"

style skip_triangle:
    font "DejaVuSansMono.ttf"
    size 14
    color "#80ff80"

################################################################################
## Notify Screen
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame:
    ypos 25
    xalign 0.5
    background Solid("#1a3a1a")
    padding (20, 10, 20, 10)

style notify_text:
    font "DejaVuSansMono.ttf"
    size 16
    color "#80ff80"

################################################################################
## NVL Screen (Required but not used)
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing 10

        for d in dialogue:
            window:
                id d.window_id

                fixed:
                    if d.who is not None:
                        text d.who id d.who_id

                    text d.what id d.what_id

        for i in items:
            textbutton i.caption:
                action i.action

style nvl_window:
    xfill True
    yfill True
    background Solid("#000000dd")
    padding (20, 20, 20, 20)

################################################################################
## Scrollbar Styles
################################################################################

style vscrollbar:
    xsize 12
    base_bar Solid("#1a1a1a")
    thumb Solid("#404040")
    hover_thumb Solid("#606060")

################################################################################
## Irregularity Log Screen
################################################################################

screen irregularity_log():
    tag log
    modal False
    zorder 50

    frame:
        xalign 1.0
        yalign 0.0
        xsize 400
        ysize 500
        xoffset -20
        yoffset 20
        background Solid("#0a0a0acc")
        padding (15, 15, 15, 15)

        vbox:
            spacing 10

            text "{color=#80ff80}== IRREGULARITY LOG =={/color}":
                font "DejaVuSansMono.ttf"
                size 16
                xalign 0.5

            null height 5

            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 400

                vbox:
                    spacing 10

                    if hasattr(store, 'game_state') and game_state.irregularity_log:
                        for entry in game_state.irregularity_log:
                            frame:
                                background Solid("#1a1a1a")
                                padding (10, 8, 10, 8)
                                xfill True

                                vbox:
                                    spacing 3
                                    $ cat_color = "#80ff80" if entry.get("category") == "observation" else ("#ffaa00" if entry.get("category") == "evidence" else "#6699ff")
                                    text "[entry[title]]":
                                        font "DejaVuSansMono.ttf"
                                        size 14
                                        color cat_color
                                    text "[entry[content]]":
                                        font "DejaVuSans.ttf"
                                        size 12
                                        color "#999999"
                    else:
                        text "{i}No irregularities logged.{/i}":
                            font "DejaVuSans.ttf"
                            size 14
                            color "#666666"
                            xalign 0.5

            text "{color=#666666}Press L to close{/color}":
                font "DejaVuSansMono.ttf"
                size 12
                xalign 0.5

    key "l" action Hide("irregularity_log")
    key "L" action Hide("irregularity_log")

init python:
    config.keymap['toggle_log'] = ['l', 'L']

    def toggle_log():
        if renpy.get_screen("irregularity_log"):
            renpy.hide_screen("irregularity_log")
        else:
            renpy.show_screen("irregularity_log")

    config.underlay.append(renpy.Keymap(toggle_log=toggle_log))

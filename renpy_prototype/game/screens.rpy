## screens.rpy — The Underlord's Registry
## Standard Ren'Py screens (minimal implementation)

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

    # Side images disabled
    # if not renpy.variant("small"):
    #     add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Solid("#000000cc")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Solid("#000000aa")
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

################################################################################
## Input Screen
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

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
    spacing gui.choice_spacing

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
    # Disabled for prototype - no GUI images
    pass

init python:
    # Quick menu disabled for prototype
    pass

default quick_menu = False

style quick_button:
    background None
    padding (5, 2, 5, 2)

style quick_button_text:
    font "DejaVuSansMono.ttf"
    size 14
    color "#888888"
    hover_color "#aaffaa"

################################################################################
## Main Menu Screen
################################################################################

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add Solid("#0a0a0a")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 600

        vbox:
            spacing 20
            xalign 0.5

            text "{size=36}{color=#80ff80}THE UNDERLORD'S REGISTRY{/color}{/size}" xalign 0.5
            text "{size=18}{color=#666666}Season One: The Department of Final Intake{/color}{/size}" xalign 0.5
            text "{size=14}{color=#444444}Ren'Py Prototype{/color}{/size}" xalign 0.5

            null height 30

            textbutton _("Start") action Start() xalign 0.5
            textbutton _("Load") action ShowMenu("load") xalign 0.5
            textbutton _("Preferences") action ShowMenu("preferences") xalign 0.5
            textbutton _("Quit") action Quit(confirm=not main_menu) xalign 0.5

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_vbox:
    xalign 0.5
    yalign 0.5
    spacing 20

style main_menu_text:
    font "DejaVuSansMono.ttf"
    size 22
    color "#80ff80"
    hover_color "#aaffaa"

################################################################################
## Game Menu Screen
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add Solid("#0a0a0a")

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

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

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

################################################################################
## Navigation Screen
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos 40
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()

        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button:
    size_group "navigation"
    padding (10, 5, 10, 5)
    background None
    hover_background Solid("#1a3a1a")

style navigation_button_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#80ff80"
    hover_color "#aaffaa"

################################################################################
## Save and Load Screens
################################################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing 10

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "slider"
                    box_wrap True

                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

            if config.has_music or config.has_sound:
                null height 20

                hbox:
                    box_wrap True

                    if config.has_music:
                        vbox:
                            style_prefix "slider"
                            label _("Music Volume")
                            hbox:
                                bar value Preference("music volume")

                    if config.has_sound:
                        vbox:
                            style_prefix "slider"
                            label _("Sound Volume")
                            hbox:
                                bar value Preference("sound volume")

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

################################################################################
## History Screen
################################################################################

screen history():
    tag menu
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"

        for h in _history_list:
            window:
                has hbox:
                    yfill True
                    spacing 10

                text (h.who or "") style "history_name"
                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")

define config.history_length = 250

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

################################################################################
## Confirm Screen
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#000000cc")

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Solid("#222222ee")
    padding (40, 40, 40, 40)
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

################################################################################
## Skip Indicator Screen
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos 10
    background Solid("#000000aa")
    padding (16, 5, 50, 5)

style skip_text:
    size 16

style skip_triangle:
    font "DejaVuSans.ttf"

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

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos 25
    background Solid("#000000aa")
    padding (16, 5, 40, 5)

################################################################################
## NVL Screen
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background Solid("#000000dd")
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_thought_xalign else "tex")

style nvl_button:
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

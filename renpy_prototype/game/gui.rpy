## gui.rpy — The Underlord's Registry
## Minimal GUI configuration for the prototype

init python:
    gui.init(1280, 720)

# Colors matching the Registry aesthetic
define gui.accent_color = '#80ff80'
define gui.idle_color = '#888888'
define gui.idle_small_color = '#aaaaaa'
define gui.hover_color = '#aaffaa'
define gui.selected_color = '#80ff80'
define gui.insensitive_color = '#444444'
define gui.muted_color = '#3d8c3d'
define gui.hover_muted_color = '#5ab45a'

define gui.text_color = '#ffffff'
define gui.interface_text_color = '#80ff80'

# Dialogue
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSansMono.ttf"

define gui.text_size = 22
define gui.name_text_size = 24
define gui.interface_text_size = 18

define gui.textbox_height = 185
define gui.textbox_yalign = 1.0

define gui.name_xpos = 240
define gui.name_ypos = 0
define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50
define gui.dialogue_width = 744
define gui.dialogue_text_xalign = 0.0

# Buttons
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

# Choice buttons
define gui.choice_spacing = 22
define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#80ff80"
define gui.choice_button_text_insensitive_color = "#444444"

# Quick menu
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

# Scrollbars
define gui.scrollbar_size = 12
define gui.scrollbar_tile = False
define gui.unscrollable = "hide"

# Bars and Sliders
define gui.bar_size = 25
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.bar_tile = False
define gui.vbar_borders = Borders(4, 4, 4, 4)

define gui.slider_size = 25
define gui.slider_borders = Borders(4, 4, 4, 4)
define gui.slider_tile = False
define gui.vslider_borders = Borders(4, 4, 4, 4)

# Slots
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

# History
define gui.history_height = 140
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0

# NVL mode
define gui.nvl_borders = Borders(0, 10, 0, 20)
define gui.nvl_height = 115
define gui.nvl_spacing = 10
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

# Preferences
define gui.pref_button_spacing = 0
define gui.pref_slider_width = 350
define gui.page_spacing = 0
define gui.navigation_spacing = 4

# Mobile
define gui.skip_indicator = False

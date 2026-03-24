## options.rpy — The Underlord's Registry

define config.name = _("The Underlord's Registry")
define config.version = "0.1.0"

define gui.show_name = True
define config.window_title = "The Underlord's Registry — Season One"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 30
default preferences.afm_time = 15

define config.save_directory = "UnderlordRegistry-Prototype"

# Save system configuration
define config.has_autosave = True
define config.autosave_on_quit = True
define config.autosave_slots = 5

define config.has_quicksave = True
define config.quicksave_slots = 5

# Screenshot configuration for save slots
define config.thumbnail_width = 256
define config.thumbnail_height = 144

define config.window_icon = None

define build.name = "UnderlordRegistry"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)
    build.classify('game/cache/**', None)

define build.documentation = set()

# Custom styles for the Registry terminal aesthetic
init python:
    import random

style registry_terminal_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#80ff80"

style registry_header_text:
    font "DejaVuSansMono.ttf"
    size 22
    color "#80ff80"
    bold True

style registry_warning_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#ffcc00"

style registry_error_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#ff6666"

style registry_exception_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#ffaa44"

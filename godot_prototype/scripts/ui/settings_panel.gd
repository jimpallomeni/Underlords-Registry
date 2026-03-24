extends Control
class_name SettingsPanel
## Settings panel with resolution and display options

@onready var resolution_option: OptionButton = $PanelContainer/VBoxContainer/ResolutionRow/ResolutionOption
@onready var scale_option: OptionButton = $PanelContainer/VBoxContainer/ScaleRow/ScaleOption
@onready var fullscreen_check: CheckButton = $PanelContainer/VBoxContainer/FullscreenRow/FullscreenCheck
@onready var btn_apply: Button = $PanelContainer/VBoxContainer/ButtonRow/BtnApply
@onready var btn_back: Button = $PanelContainer/VBoxContainer/ButtonRow/BtnBack

# Common resolutions
const RESOLUTIONS = [
	Vector2i(1280, 720),
	Vector2i(1366, 768),
	Vector2i(1600, 900),
	Vector2i(1920, 1080),
	Vector2i(2560, 1440),
	Vector2i(3840, 2160),
]

# Scale factors
const SCALES = [
	{"label": "100%", "value": 1.0},
	{"label": "125%", "value": 1.25},
	{"label": "150%", "value": 1.5},
	{"label": "175%", "value": 1.75},
	{"label": "200%", "value": 2.0},
]

var pending_resolution: Vector2i
var pending_scale: float
var pending_fullscreen: bool

func _ready() -> void:
	_populate_options()
	_load_current_settings()

	btn_apply.pressed.connect(_on_apply_pressed)
	btn_back.pressed.connect(_on_back_pressed)

	resolution_option.item_selected.connect(_on_resolution_selected)
	scale_option.item_selected.connect(_on_scale_selected)
	fullscreen_check.toggled.connect(_on_fullscreen_toggled)

func _populate_options() -> void:
	# Resolutions
	resolution_option.clear()
	for res in RESOLUTIONS:
		resolution_option.add_item("%dx%d" % [res.x, res.y])

	# Scales
	scale_option.clear()
	for s in SCALES:
		scale_option.add_item(s["label"])

func _load_current_settings() -> void:
	# Load from DisplaySettings autoload
	var current_res = DisplaySettings.current_resolution
	var current_scale = DisplaySettings.current_scale
	var is_fullscreen = DisplaySettings.is_fullscreen

	# Find matching resolution
	pending_resolution = current_res
	for i in range(RESOLUTIONS.size()):
		if RESOLUTIONS[i] == current_res:
			resolution_option.select(i)
			break

	# Find matching scale
	pending_scale = current_scale
	for i in range(SCALES.size()):
		if absf(SCALES[i]["value"] - current_scale) < 0.1:
			scale_option.select(i)
			break

	fullscreen_check.button_pressed = is_fullscreen
	pending_fullscreen = is_fullscreen

func _on_resolution_selected(index: int) -> void:
	pending_resolution = RESOLUTIONS[index]

func _on_scale_selected(index: int) -> void:
	pending_scale = SCALES[index]["value"]

func _on_fullscreen_toggled(pressed: bool) -> void:
	pending_fullscreen = pressed

func _on_apply_pressed() -> void:
	# Use DisplaySettings autoload for persistent settings
	DisplaySettings.current_resolution = pending_resolution
	DisplaySettings.current_scale = pending_scale
	DisplaySettings.is_fullscreen = pending_fullscreen
	DisplaySettings.apply_settings()
	DisplaySettings.save_settings()

func _on_back_pressed() -> void:
	visible = false

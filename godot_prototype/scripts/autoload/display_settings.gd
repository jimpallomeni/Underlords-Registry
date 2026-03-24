extends Node
## Autoload for managing display settings across scenes

const SETTINGS_PATH = "user://settings.cfg"

var current_resolution: Vector2i = Vector2i(1280, 720)
var current_scale: float = 1.0
var is_fullscreen: bool = false

func _ready() -> void:
	load_settings()

func load_settings() -> void:
	var config = ConfigFile.new()
	if config.load(SETTINGS_PATH) == OK:
		current_resolution.x = config.get_value("display", "resolution_x", 1280)
		current_resolution.y = config.get_value("display", "resolution_y", 720)
		current_scale = config.get_value("display", "scale", 1.0)
		is_fullscreen = config.get_value("display", "fullscreen", false)
		apply_settings()

func apply_settings() -> void:
	var window = get_window()

	if is_fullscreen:
		window.mode = Window.MODE_FULLSCREEN
	else:
		window.mode = Window.MODE_WINDOWED
		window.size = current_resolution
		# Center window
		var screen_size = DisplayServer.screen_get_size()
		window.position = (screen_size - current_resolution) / 2

	window.content_scale_factor = current_scale

func save_settings() -> void:
	var config = ConfigFile.new()
	config.set_value("display", "resolution_x", current_resolution.x)
	config.set_value("display", "resolution_y", current_resolution.y)
	config.set_value("display", "scale", current_scale)
	config.set_value("display", "fullscreen", is_fullscreen)
	config.save(SETTINGS_PATH)

func set_resolution(res: Vector2i) -> void:
	current_resolution = res
	apply_settings()
	save_settings()

func set_scale(scale: float) -> void:
	current_scale = scale
	apply_settings()
	save_settings()

func set_fullscreen(enabled: bool) -> void:
	is_fullscreen = enabled
	apply_settings()
	save_settings()

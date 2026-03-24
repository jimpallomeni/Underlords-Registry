extends Control
class_name PauseMenu
## Pause menu with resume, settings, and quit options

signal resumed
signal quit_to_menu

@onready var btn_resume: Button = $PausePanel/VBoxContainer/BtnResume
@onready var btn_settings: Button = $PausePanel/VBoxContainer/BtnSettings
@onready var btn_quit: Button = $PausePanel/VBoxContainer/BtnQuit
@onready var settings_panel: Control = $SettingsPanel

var is_paused: bool = false

func _ready() -> void:
	btn_resume.pressed.connect(_on_resume_pressed)
	btn_settings.pressed.connect(_on_settings_pressed)
	btn_quit.pressed.connect(_on_quit_pressed)

	if settings_panel:
		settings_panel.visible = false

	visible = false
	process_mode = Node.PROCESS_MODE_ALWAYS

func _input(event: InputEvent) -> void:
	if event.is_action_pressed("pause_menu"):
		if settings_panel and settings_panel.visible:
			settings_panel.visible = false
		elif is_paused:
			unpause()
		else:
			pause()

func pause() -> void:
	is_paused = true
	visible = true
	get_tree().paused = true

func unpause() -> void:
	is_paused = false
	visible = false
	get_tree().paused = false
	emit_signal("resumed")

func _on_resume_pressed() -> void:
	unpause()

func _on_settings_pressed() -> void:
	if settings_panel:
		settings_panel.visible = true

func _on_quit_pressed() -> void:
	unpause()
	emit_signal("quit_to_menu")

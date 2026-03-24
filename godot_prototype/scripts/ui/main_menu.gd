extends Control
class_name MainMenu
## Main menu with title and options

signal start_game
signal quit_game

@onready var title_label: Label = $VBoxContainer/TitleLabel
@onready var subtitle_label: Label = $VBoxContainer/SubtitleLabel
@onready var btn_start: Button = $VBoxContainer/ButtonContainer/BtnStart
@onready var btn_settings: Button = $VBoxContainer/ButtonContainer/BtnSettings
@onready var btn_quit: Button = $VBoxContainer/ButtonContainer/BtnQuit
@onready var settings_panel: Control = $SettingsPanel

func _ready() -> void:
	btn_start.pressed.connect(_on_start_pressed)
	btn_settings.pressed.connect(_on_settings_pressed)
	btn_quit.pressed.connect(_on_quit_pressed)

	# Hide settings initially
	if settings_panel:
		settings_panel.visible = false

	# Flicker effect for terminal aesthetic
	_start_flicker()

func _start_flicker() -> void:
	var tween = create_tween().set_loops()
	tween.tween_property(title_label, "modulate:a", 0.85, 0.05)
	tween.tween_property(title_label, "modulate:a", 1.0, 0.05)
	tween.tween_interval(2.0 + randf() * 3.0)

func _on_start_pressed() -> void:
	emit_signal("start_game")

func _on_settings_pressed() -> void:
	if settings_panel:
		settings_panel.visible = true

func _on_quit_pressed() -> void:
	emit_signal("quit_game")
	get_tree().quit()

extends Node
## Root scene that manages main menu and game transitions

@onready var main_menu: Control = $UILayer/MainMenu
@onready var game_container: Node2D = $GameContainer
@onready var pause_menu: Control = $UILayer/PauseMenu

const GAME_SCENE = "res://scenes/main_simple.tscn"

var game_instance: Node = null

func _ready() -> void:
	# Connect menu signals
	main_menu.start_game.connect(_on_start_game)
	pause_menu.quit_to_menu.connect(_on_quit_to_menu)

	# Start at menu
	_show_main_menu()

func _show_main_menu() -> void:
	main_menu.visible = true
	pause_menu.visible = false

	# Clean up existing game if any
	if game_instance:
		game_instance.queue_free()
		game_instance = null

	get_tree().paused = false

func _on_start_game() -> void:
	main_menu.visible = false

	# Load game scene
	var game_scene = load(GAME_SCENE)
	game_instance = game_scene.instantiate()
	game_container.add_child(game_instance)

	# Connect pause menu to player if needed
	pause_menu.visible = false

func _on_quit_to_menu() -> void:
	_show_main_menu()

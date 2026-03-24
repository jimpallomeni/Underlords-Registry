extends Node2D
## Main scene controller for The Underlord's Registry
## Handles scene transitions, game flow, and high-level state

@onready var player: Player = $Player
@onready var terminal_ui: ProcessingTerminal = $CanvasLayer/ProcessingTerminal
@onready var dialogue_box: DialogueBoxUI = $CanvasLayer/DialogueBox
@onready var hud: HUD = $CanvasLayer/HUD

# Terminal reference
@onready var terminal_7: StaticBody2D = $IntakeFloor/Furniture/Terminal7

var game_started: bool = false

func _ready() -> void:
	# Allow this node to process input even when game is paused
	process_mode = Node.PROCESS_MODE_ALWAYS

	# Connect terminal interaction
	_setup_terminal()

	# Start the game with the elevator intro
	await get_tree().create_timer(0.5).timeout
	_start_intro_sequence()

func _setup_terminal() -> void:
	# Make terminal 7 interactable
	if terminal_7:
		terminal_7.set_meta("interact_callback", _on_terminal_interact)

func _on_terminal_interact() -> void:
	# Open the processing terminal
	terminal_ui.open_terminal()

func _start_intro_sequence() -> void:
	# Play the elevator intro dialogue
	player.freeze()
	DialogueManager.start_dialogue("elevator_intro")

	# Wait for dialogue to complete, then show floor
	await DialogueManager.dialogue_ended

	# Brief pause, then start shift
	await get_tree().create_timer(1.0).timeout
	player.unfreeze()
	GameState.start_shift()
	game_started = true

	# Show initial prompt
	_show_tutorial_prompt()

func _show_tutorial_prompt() -> void:
	# Brief tutorial message
	DialogueManager.show_internal("Terminal 7. My desk. Time to start processing.", "diligent")

func _input(event: InputEvent) -> void:
	# Debug: Press T to open terminal directly (for testing)
	if event is InputEventKey and event.pressed and event.keycode == KEY_T:
		if not terminal_ui.is_open:
			terminal_ui.open_terminal()

# Called when player interacts with something
func _on_player_interaction(interactable: Node2D) -> void:
	if interactable.is_in_group("terminals"):
		terminal_ui.open_terminal()
	elif interactable.is_in_group("npcs"):
		_start_npc_dialogue(interactable)

func _start_npc_dialogue(npc: Node2D) -> void:
	var dialogue_id = npc.get("dialogue_id") if npc.get("dialogue_id") else ""
	if dialogue_id != "":
		DialogueManager.start_dialogue(dialogue_id)

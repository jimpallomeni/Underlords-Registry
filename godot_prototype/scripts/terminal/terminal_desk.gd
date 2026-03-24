extends StaticBody2D
class_name TerminalDesk
## An interactable terminal desk on the Intake Floor

@export var terminal_id: String = "7"
@export var terminal_name: String = "Terminal 7"

func _ready() -> void:
	add_to_group("interactable")
	add_to_group("terminals")

func interact(_player: Node2D) -> void:
	# Find the processing terminal UI and open it
	var terminal_ui = get_tree().get_first_node_in_group("terminal_ui")
	if terminal_ui and terminal_ui.has_method("open_terminal"):
		terminal_ui.open_terminal()
	else:
		# Fallback: find by path
		var canvas = get_tree().current_scene.get_node_or_null("CanvasLayer/ProcessingTerminal")
		if canvas and canvas.has_method("open_terminal"):
			canvas.open_terminal()

func get_interaction_prompt() -> String:
	return "[E] Use %s" % terminal_name

extends StaticBody2D
class_name Interactable
## Base class for interactable objects in the Registry

signal interacted(player: Node2D)

@export var interaction_prompt: String = "[E] Interact"
@export var one_time_only: bool = false

var has_been_used: bool = false

func interact(player: Node2D) -> void:
	if one_time_only and has_been_used:
		return

	has_been_used = true
	emit_signal("interacted", player)

	# Check for callback in metadata
	if has_meta("interact_callback"):
		var callback = get_meta("interact_callback")
		if callback is Callable:
			callback.call()

func _ready() -> void:
	add_to_group("interactable")

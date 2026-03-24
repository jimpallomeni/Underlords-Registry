extends CharacterBody2D
class_name Player
## Player controller for Kael
## Top-down movement with interaction system

signal interaction_available(interactable: Node2D)
signal interaction_unavailable

@export var move_speed: float = 150.0
@export var interaction_range: float = 50.0

@onready var sprite: CanvasItem = $Sprite2D
@onready var interaction_area: Area2D = $InteractionArea
@onready var interaction_ray: RayCast2D = $InteractionRay

var current_interactable: Node2D = null
var is_frozen: bool = false  # Frozen during dialogue, menus, etc.
var facing_direction: Vector2 = Vector2.DOWN

# Animation states
enum AnimState { IDLE, WALKING }
var current_anim_state: AnimState = AnimState.IDLE

func _ready() -> void:
	# Connect to dialogue signals to freeze during dialogue
	DialogueManager.dialogue_started.connect(_on_dialogue_started)
	DialogueManager.dialogue_ended.connect(_on_dialogue_ended)

	# Set up interaction area
	if interaction_area:
		interaction_area.body_entered.connect(_on_interaction_body_entered)
		interaction_area.body_exited.connect(_on_interaction_body_exited)
		interaction_area.area_entered.connect(_on_interaction_area_entered)
		interaction_area.area_exited.connect(_on_interaction_area_exited)

func _physics_process(delta: float) -> void:
	if is_frozen:
		velocity = Vector2.ZERO
		return

	# Get input
	var input_dir = Input.get_vector("move_left", "move_right", "move_up", "move_down")

	# Update facing direction
	if input_dir != Vector2.ZERO:
		facing_direction = input_dir.normalized()
		_update_interaction_ray()

	# Calculate velocity
	velocity = input_dir * move_speed

	# Move
	move_and_slide()

	# Update animation state
	if velocity.length() > 0:
		current_anim_state = AnimState.WALKING
	else:
		current_anim_state = AnimState.IDLE

	_update_sprite()

func _input(event: InputEvent) -> void:
	if is_frozen:
		return

	# Interaction
	if event.is_action_pressed("interact"):
		_try_interact()

	# Toggle irregularity log
	if event.is_action_pressed("toggle_log"):
		_toggle_irregularity_log()

func _update_sprite() -> void:
	# Update sprite based on facing direction
	# Only flip if it's an actual Sprite2D (not a ColorRect placeholder)
	if sprite is Sprite2D:
		if facing_direction.x < 0:
			sprite.flip_h = true
		elif facing_direction.x > 0:
			sprite.flip_h = false

	# Could add animation frames here based on current_anim_state
	# For prototype, we'll keep it simple

func _update_interaction_ray() -> void:
	if interaction_ray:
		interaction_ray.target_position = facing_direction * interaction_range

func _try_interact() -> void:
	if current_interactable and current_interactable.has_method("interact"):
		current_interactable.interact(self)

func _toggle_irregularity_log() -> void:
	# Signal to UI to toggle the log display
	# This would be connected to the UI system
	pass

func _on_interaction_body_entered(body: Node2D) -> void:
	if body.is_in_group("interactable"):
		current_interactable = body
		emit_signal("interaction_available", body)

func _on_interaction_body_exited(body: Node2D) -> void:
	if body == current_interactable:
		current_interactable = null
		emit_signal("interaction_unavailable")

func _on_interaction_area_entered(area: Area2D) -> void:
	var parent = area.get_parent()
	if parent and parent.is_in_group("interactable"):
		current_interactable = parent
		emit_signal("interaction_available", parent)

func _on_interaction_area_exited(area: Area2D) -> void:
	var parent = area.get_parent()
	if parent == current_interactable:
		current_interactable = null
		emit_signal("interaction_unavailable")

func _on_dialogue_started(_speaker: String) -> void:
	is_frozen = true
	velocity = Vector2.ZERO

func _on_dialogue_ended() -> void:
	is_frozen = false

func freeze() -> void:
	is_frozen = true
	velocity = Vector2.ZERO

func unfreeze() -> void:
	is_frozen = false

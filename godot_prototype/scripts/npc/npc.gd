extends CharacterBody2D
class_name NPC
## Base NPC class for Registry employees

@export var npc_name: String = "NPC"
@export var npc_id: String = "generic"
@export var dialogue_id: String = ""
@export var can_talk: bool = true
@export var body_color: Color = Color(0.5, 0.5, 0.6, 1)
@export var head_color: Color = Color(0.7, 0.65, 0.6, 1)

@onready var sprite: CanvasItem = $Sprite2D
@onready var head_sprite: CanvasItem = $HeadSprite
@onready var name_label: Label = $NameLabel

func _ready() -> void:
	add_to_group("interactable")
	add_to_group("npcs")

	if name_label:
		name_label.text = npc_name

	# Apply initial colors
	if sprite and sprite is ColorRect:
		(sprite as ColorRect).color = body_color
	if head_sprite and head_sprite is ColorRect:
		(head_sprite as ColorRect).color = head_color

func interact(_player: Node2D) -> void:
	if not can_talk:
		return

	if dialogue_id != "":
		DialogueManager.start_dialogue(dialogue_id)
	else:
		# Generic response
		DialogueManager.say(npc_name.to_upper(), "...")

func get_interaction_prompt() -> String:
	return "[E] Talk to %s" % npc_name

# Update NPC appearance based on relationship
func update_appearance() -> void:
	var relationship = GameState.get_relationship_level(npc_id)
	# Tint the whole NPC based on relationship
	var tint := Color(1, 1, 1, 1)
	match relationship:
		"alliance":
			tint = Color(0.85, 1.0, 0.85, 1)
		"hostile":
			tint = Color(1.0, 0.75, 0.75, 1)
	if sprite:
		sprite.modulate = tint
	if head_sprite:
		head_sprite.modulate = tint

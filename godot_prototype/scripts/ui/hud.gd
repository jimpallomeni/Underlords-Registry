extends Control
class_name HUD
## Main HUD display - shift info, interaction prompts, irregularity log

@onready var top_bar: Panel = $TopBar
@onready var shift_info: Label = $TopBar/ShiftInfo
@onready var interaction_prompt: Panel = $InteractionPrompt
@onready var interaction_label: Label = $InteractionPrompt/Label
@onready var log_panel: Panel = $IrregularityLogPanel
@onready var log_entries: RichTextLabel = $IrregularityLogPanel/VBoxContainer/LogEntries

var is_log_visible: bool = false

func _ready() -> void:
	# Connect to GameState signals
	GameState.quota_changed.connect(_on_quota_changed)
	GameState.irregularity_logged.connect(_on_irregularity_logged)

	# Connect to player signals
	await get_tree().process_frame
	var player = get_tree().get_first_node_in_group("player")
	if player:
		if player.has_signal("interaction_available"):
			player.interaction_available.connect(_on_interaction_available)
		if player.has_signal("interaction_unavailable"):
			player.interaction_unavailable.connect(_on_interaction_unavailable)

	# Initial update
	_update_shift_info()
	_update_log_display()
	log_panel.visible = false
	interaction_prompt.visible = false

func _input(event: InputEvent) -> void:
	if event.is_action_pressed("toggle_log"):
		_toggle_log()

func _toggle_log() -> void:
	is_log_visible = not is_log_visible
	log_panel.visible = is_log_visible
	if is_log_visible:
		_update_log_display()

func _update_shift_info() -> void:
	var shift = GameState.current_shift
	var processed = GameState.souls_processed
	var quota = GameState.shift_quota
	shift_info.text = "SHIFT: Day Cycle %d | Processed: %d/%d" % [shift, processed, quota]

func _on_quota_changed(_current: int, _target: int) -> void:
	_update_shift_info()

func _on_interaction_available(interactable: Node2D) -> void:
	interaction_prompt.visible = true
	if interactable.is_in_group("terminals"):
		interaction_label.text = "[E] Use Terminal"
	elif interactable.is_in_group("npcs"):
		var npc_name = interactable.get("npc_name") if interactable.get("npc_name") else "NPC"
		interaction_label.text = "[E] Talk to %s" % npc_name
	else:
		interaction_label.text = "[E] Interact"

func _on_interaction_unavailable() -> void:
	interaction_prompt.visible = false

func _on_irregularity_logged(_entry: Dictionary) -> void:
	_update_log_display()
	# Flash the log header to indicate new entry
	_flash_log_notification()

func _update_log_display() -> void:
	if GameState.irregularity_log.is_empty():
		log_entries.text = "[color=#666666]No entries yet.[/color]"
		return

	var text = ""
	for entry in GameState.irregularity_log:
		var category_color = _get_category_color(entry.get("category", "observation"))
		text += "[color=%s]Entry %03d — %s[/color]\n" % [
			category_color,
			entry.get("id", 0),
			entry.get("title", "Untitled")
		]
		text += "[color=#aaaaaa]%s[/color]\n\n" % entry.get("content", "")

	log_entries.text = text

func _get_category_color(category: String) -> String:
	match category:
		"evidence":
			return "#ffaa00"  # Amber
		"connection":
			return "#00aaff"  # Blue
		_:  # observation
			return "#33ff33"  # Green

func _flash_log_notification() -> void:
	# Brief flash effect on the shift info bar
	var original_color = shift_info.get_theme_color("font_color")
	shift_info.add_theme_color_override("font_color", Color(1, 0.8, 0.2, 1))

	var tween = create_tween()
	tween.tween_interval(0.3)
	tween.tween_callback(func():
		shift_info.add_theme_color_override("font_color", original_color)
	)

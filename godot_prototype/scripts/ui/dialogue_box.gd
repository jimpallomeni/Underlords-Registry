extends Control
class_name DialogueBoxUI
## UI component for displaying dialogue, choices, and internal monologue

@onready var panel: Panel = $Panel
@onready var speaker_label: Label = $Panel/MarginContainer/VBoxContainer/SpeakerLabel
@onready var dialogue_text: RichTextLabel = $Panel/MarginContainer/VBoxContainer/DialogueText
@onready var choices_container: VBoxContainer = $Panel/MarginContainer/VBoxContainer/ChoicesContainer
@onready var continue_prompt: Label = $Panel/MarginContainer/VBoxContainer/ContinuePrompt
@onready var internal_panel: Panel = $InternalMonologue
@onready var internal_label: Label = $InternalMonologue/Label

var choice_buttons: Array[Button] = []
var is_showing_choices: bool = false
var can_advance: bool = true

# Tone colors
const TONE_COLORS = {
	"sardonic": Color(0.7, 0.5, 0.8, 1),     # Purple
	"diligent": Color(0.5, 0.7, 0.9, 1),      # Blue
	"compassionate": Color(0.5, 0.9, 0.6, 1), # Green
	"complicit": Color(0.7, 0.7, 0.7, 1),     # Gray
}

func _ready() -> void:
	visible = false

	# Connect to DialogueManager signals
	DialogueManager.dialogue_started.connect(_on_dialogue_started)
	DialogueManager.dialogue_line.connect(_on_dialogue_line)
	DialogueManager.dialogue_choices.connect(_on_dialogue_choices)
	DialogueManager.dialogue_ended.connect(_on_dialogue_ended)
	DialogueManager.internal_monologue.connect(_on_internal_monologue)

func _input(event: InputEvent) -> void:
	if not visible:
		return

	# Handle choice selection with number keys
	if is_showing_choices:
		if event.is_action_pressed("dialogue_choice_1") and choice_buttons.size() > 0:
			_on_choice_selected(0)
		elif event.is_action_pressed("dialogue_choice_2") and choice_buttons.size() > 1:
			_on_choice_selected(1)
		elif event.is_action_pressed("dialogue_choice_3") and choice_buttons.size() > 2:
			_on_choice_selected(2)
		return

	if event.is_action_pressed("ui_accept") or event.is_action_pressed("interact"):
		if can_advance:
			DialogueManager.advance_dialogue()

func _on_dialogue_started(_dialogue_id: String) -> void:
	visible = true
	panel.visible = true
	internal_panel.visible = false
	is_showing_choices = false
	continue_prompt.visible = true

func _on_dialogue_line(speaker: String, text: String, _portrait: String) -> void:
	# Update speaker label with appropriate color
	speaker_label.text = speaker
	match speaker:
		"KAEL":
			speaker_label.add_theme_color_override("font_color", Color(0.6, 0.8, 1, 1))
		"PRESSA":
			speaker_label.add_theme_color_override("font_color", Color(0.8, 0.6, 0.9, 1))
		"DOLEN":
			speaker_label.add_theme_color_override("font_color", Color(0.7, 0.7, 0.5, 1))
		"FEN":
			speaker_label.add_theme_color_override("font_color", Color(0.5, 0.9, 0.5, 1))
		"REGISTRY_VOICE":
			speaker_label.add_theme_color_override("font_color", Color(0.3, 0.6, 0.3, 1))
		"REBECCA":
			speaker_label.add_theme_color_override("font_color", Color(0.9, 0.6, 0.4, 1))  # Warm orange for Rebecca
		"SOUL":
			speaker_label.add_theme_color_override("font_color", Color(0.6, 0.6, 0.7, 1))  # Muted gray for generic souls
		_:
			speaker_label.add_theme_color_override("font_color", Color(0.8, 0.7, 0.2, 1))

	dialogue_text.text = text
	is_showing_choices = false
	continue_prompt.visible = true
	_clear_choices()

func _on_dialogue_choices(choices: Array) -> void:
	is_showing_choices = true
	continue_prompt.visible = false
	_clear_choices()

	choices_container.visible = true

	for i in range(choices.size()):
		var choice = choices[i]
		var button = Button.new()
		button.text = "[%d] %s" % [i + 1, choice.get("text", "...")]
		button.flat = true
		button.alignment = HORIZONTAL_ALIGNMENT_LEFT

		# Style based on tone if present
		var tone = choice.get("tone", "")
		if tone in TONE_COLORS:
			button.add_theme_color_override("font_color", TONE_COLORS[tone])
		else:
			button.add_theme_color_override("font_color", Color(0.9, 0.9, 0.9, 1))

		button.add_theme_color_override("font_hover_color", Color(1, 1, 1, 1))

		# Connect button press
		var choice_index = i
		button.pressed.connect(func(): _on_choice_selected(choice_index))

		choices_container.add_child(button)
		choice_buttons.append(button)

func _on_choice_selected(index: int) -> void:
	DialogueManager.select_choice(index)
	is_showing_choices = false
	_clear_choices()

func _clear_choices() -> void:
	choices_container.visible = false
	for button in choice_buttons:
		button.queue_free()
	choice_buttons.clear()

func _on_dialogue_ended() -> void:
	visible = false
	is_showing_choices = false
	_clear_choices()

func _on_internal_monologue(text: String, tone: String) -> void:
	internal_panel.visible = true
	internal_label.text = "> " + text

	# Color based on tone
	if tone in TONE_COLORS:
		internal_label.add_theme_color_override("font_color", TONE_COLORS[tone])

	# Fade out after a few seconds
	var tween = create_tween()
	tween.tween_interval(4.0)
	tween.tween_property(internal_panel, "modulate:a", 0.0, 1.0)
	tween.tween_callback(func():
		internal_panel.visible = false
		internal_panel.modulate.a = 1.0
	)

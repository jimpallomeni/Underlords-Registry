extends Control
class_name ProcessingTerminal
## The Soul Processing Terminal - Core gameplay interface
## Displays soul files and allows processing decisions

signal terminal_opened
signal terminal_closed
signal soul_processed(soul: Dictionary, action: String)
signal interview_started(soul: Dictionary)
signal interview_ended(soul: Dictionary)

@onready var terminal_panel: Panel = $TerminalPanel
@onready var header_label: Label = $TerminalPanel/MarginContainer/VBoxContainer/Header
@onready var soul_info: RichTextLabel = $TerminalPanel/MarginContainer/VBoxContainer/SoulInfo
@onready var action_buttons: VBoxContainer = $TerminalPanel/MarginContainer/VBoxContainer/ActionButtons
@onready var status_bar: Label = $TerminalPanel/MarginContainer/VBoxContainer/StatusBar

# Button references
@onready var btn_approve: Button = $TerminalPanel/MarginContainer/VBoxContainer/ActionButtons/BtnApprove
@onready var btn_exception: Button = $TerminalPanel/MarginContainer/VBoxContainer/ActionButtons/BtnException
@onready var btn_override: Button = $TerminalPanel/MarginContainer/VBoxContainer/ActionButtons/BtnOverride
@onready var btn_interview: Button = $TerminalPanel/MarginContainer/VBoxContainer/ActionButtons/BtnInterview
@onready var btn_escalate: Button = $TerminalPanel/MarginContainer/VBoxContainer/ActionButtons/BtnEscalate

var is_open: bool = false
var current_soul: Dictionary = {}
var showing_metadata: bool = false
var interview_in_progress: bool = false

# Terminal text styling
const TERMINAL_GREEN = Color(0.2, 0.8, 0.2)
const TERMINAL_AMBER = Color(0.9, 0.7, 0.1)
const TERMINAL_RED = Color(0.9, 0.2, 0.2)
const TERMINAL_GRAY = Color(0.6, 0.6, 0.6)

func _ready() -> void:
	visible = false
	_connect_buttons()
	_update_status_bar()

	# Connect to game state signals
	GameState.quota_changed.connect(_on_quota_changed)

	# Connect to dialogue manager for interview handling
	DialogueManager.dialogue_ended.connect(_on_interview_dialogue_ended)

func _connect_buttons() -> void:
	if btn_approve:
		btn_approve.pressed.connect(_on_approve_pressed)
	if btn_exception:
		btn_exception.pressed.connect(_on_exception_pressed)
	if btn_override:
		btn_override.pressed.connect(_on_override_pressed)
	if btn_interview:
		btn_interview.pressed.connect(_on_interview_pressed)
	if btn_escalate:
		btn_escalate.pressed.connect(_on_escalate_pressed)

func _input(event: InputEvent) -> void:
	if not is_open:
		return

	# Don't process terminal input during interview
	if interview_in_progress:
		return

	if event.is_action_pressed("ui_cancel"):
		close_terminal()

	# Keyboard shortcuts for actions (match button labels)
	if event is InputEventKey and event.pressed:
		match event.keycode:
			KEY_1:
				# For standard souls: Approve. For exception holds: Confirm Exception
				if btn_approve and btn_approve.visible:
					_on_approve_pressed()
				elif btn_exception and btn_exception.visible:
					_on_exception_pressed()
			KEY_2:
				# Override (for both standard and exception hold)
				if btn_override and btn_override.visible:
					_on_override_pressed()
			KEY_3:
				# Interview
				if btn_interview and btn_interview.visible:
					_on_interview_pressed()
			KEY_4:
				# Escalate (exception hold only)
				if btn_escalate and btn_escalate.visible:
					_on_escalate_pressed()
			KEY_M:
				_toggle_metadata()

func open_terminal() -> void:
	is_open = true
	visible = true
	showing_metadata = false
	emit_signal("terminal_opened")

	# Freeze player
	var player = get_tree().get_first_node_in_group("player")
	if player and player.has_method("freeze"):
		player.freeze()

	# Load next soul
	load_next_soul()

func close_terminal() -> void:
	is_open = false
	visible = false
	emit_signal("terminal_closed")

	# Unfreeze player
	var player = get_tree().get_first_node_in_group("player")
	if player and player.has_method("unfreeze"):
		player.unfreeze()

func load_next_soul() -> void:
	current_soul = GameState.get_next_soul()

	if current_soul.is_empty():
		_show_queue_empty()
		return

	_display_soul(current_soul)

func _display_soul(soul: Dictionary) -> void:
	var designation = soul.get("designation", "UNKNOWN")
	var name = soul.get("name", "Unknown")
	var cause = soul.get("cause_of_death", "Unknown")
	var is_exception = soul.get("is_exception_hold", false)
	var routing = soul.get("routing_recommendation", "Queue 7")
	var summary = soul.get("life_summary", "No summary available.")

	# Build the display text
	var display_text = ""
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n"
	display_text += "[center][color=#33ff33]FORM 7-A: STANDARD INTAKE[/color][/center]\n"
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n\n"

	display_text += "[color=#aaaaaa]SOUL DESIGNATION:[/color] [color=#ffffff]%s[/color]\n" % designation
	display_text += "[color=#aaaaaa]NAME (LIFE):[/color] [color=#ffffff]%s[/color]\n" % name
	display_text += "[color=#aaaaaa]CAUSE:[/color] [color=#ffffff]%s[/color]\n\n" % cause

	display_text += "[color=#aaaaaa]LIFE SUMMARY:[/color]\n"
	display_text += "[color=#cccccc]%s[/color]\n\n" % summary

	if is_exception:
		display_text += "[color=#ffaa00]═══════════════════════════════════════════════════════[/color]\n"
		display_text += "[color=#ffaa00]STATUS: EXCEPTION HOLD TRIGGERED[/color]\n"
		display_text += "[color=#ffaa00]REASON: Threshold Parameter Exceeded (Code 7.4.1-E)[/color]\n"
		display_text += "[color=#ffaa00]═══════════════════════════════════════════════════════[/color]\n"
	else:
		display_text += "[color=#aaaaaa]CLASSIFICATION RECOMMENDATION:[/color] [color=#33ff33]STANDARD ASSIGNMENT[/color]\n"
		display_text += "[color=#aaaaaa]ROUTING:[/color] [color=#ffffff]%s[/color]\n" % routing

	display_text += "\n[color=#666666]───────────────────────────────────────────────────────[/color]\n"
	display_text += "[color=#aaaaaa]Press [M] to view metadata[/color]\n"

	soul_info.bbcode_enabled = true
	soul_info.text = display_text

	# Update buttons based on soul type
	_update_buttons(is_exception)

func _update_buttons(is_exception: bool) -> void:
	if is_exception:
		btn_approve.visible = false
		btn_exception.visible = true
		btn_exception.text = "[1] CONFIRM EXCEPTION HOLD"
		btn_override.visible = true
		btn_override.text = "[2] OVERRIDE EXCEPTION HOLD"
		btn_interview.visible = true
		btn_interview.text = "[3] INTERVIEW SOUL"
		btn_escalate.visible = true
		btn_escalate.text = "[4] ESCALATE TO SUPERVISOR"
	else:
		btn_approve.visible = true
		btn_approve.text = "[1] APPROVE ROUTING"
		btn_exception.visible = false
		btn_override.visible = true
		btn_override.text = "[2] MODIFY ROUTING"
		btn_interview.visible = true
		btn_interview.text = "[3] INTERVIEW SOUL"
		btn_escalate.visible = false

func _toggle_metadata() -> void:
	showing_metadata = not showing_metadata

	if showing_metadata:
		_show_metadata()
	else:
		_display_soul(current_soul)

func _show_metadata() -> void:
	var designation = current_soul.get("designation", "UNKNOWN")
	var is_exception = current_soul.get("is_exception_hold", false)

	var display_text = ""
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n"
	display_text += "[center][color=#33ff33]FILE METADATA — %s[/color][/center]\n" % designation
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n\n"

	display_text += "[color=#aaaaaa]INTAKE TIMESTAMP:[/color] [color=#ffffff]4019.%03d.%04d[/color]\n" % [randi() % 365, randi() % 9999]
	display_text += "[color=#aaaaaa]PROCESSING STATUS:[/color] "

	if is_exception:
		display_text += "[color=#ffaa00]Exception Hold (Auto)[/color]\n"
		display_text += "[color=#aaaaaa]EXCEPTION CODE:[/color] [color=#ffffff]7.4.1-E[/color]\n\n"

		display_text += "[color=#aaaaaa]ROUTING HISTORY:[/color]\n"
		display_text += "  [color=#ffffff]→ Initial: Queue 7 (General Population)[/color]\n"
		display_text += "  [color=#ff6666]→ Modified: [REDACTED][/color]\n"
		display_text += "  [color=#ffaa00]→ Current: Exception Hold Queue[/color]\n\n"

		# The key revelation
		display_text += "[color=#ffaa00]SIMILAR CASES (Last 30 Days): 2,847[/color]\n"
		display_text += "[color=#ffaa00]SIMILAR CASES (Last 365 Days): 14,221[/color]\n"
		display_text += "[color=#ff6666]SIMILAR CASES (Historical Avg/Year): 142[/color]\n\n"

		display_text += "[color=#ff6666]═══════════════════════════════════════════════════════[/color]\n"
		display_text += "[color=#ff6666]ANOMALY: 100x increase from historical average[/color]\n"
		display_text += "[color=#ff6666]═══════════════════════════════════════════════════════[/color]\n"

		# If player hasn't discovered this yet
		if not GameState.get_flag("discovered_exception_rate"):
			display_text += "\n[color=#33ff33][LOG THIS OBSERVATION?][/color]\n"
			display_text += "[color=#aaaaaa]Press [L] to add to Irregularity Log[/color]\n"
	else:
		display_text += "[color=#33ff33]Standard Processing[/color]\n"
		display_text += "[color=#aaaaaa]ROUTING CODE:[/color] [color=#ffffff]GP-7.STD.4019[/color]\n"

	display_text += "\n[color=#666666]Press [M] to return to main view[/color]\n"

	soul_info.text = display_text

func _show_queue_empty() -> void:
	var display_text = ""
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n"
	display_text += "[center][color=#33ff33]QUEUE EMPTY[/color][/center]\n"
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n\n"

	display_text += "[center][color=#aaaaaa]All souls in current queue have been processed.[/color][/center]\n"
	display_text += "[center][color=#aaaaaa]Shift complete. Press [ESC] to exit terminal.[/color][/center]\n"

	soul_info.text = display_text
	_hide_all_buttons()

func _hide_all_buttons() -> void:
	btn_approve.visible = false
	btn_exception.visible = false
	btn_override.visible = false
	btn_interview.visible = false
	btn_escalate.visible = false

func _update_status_bar() -> void:
	var processed = GameState.souls_processed
	var quota = GameState.shift_quota
	var remaining = GameState.soul_queue.filter(func(s): return not s.processed).size()

	status_bar.text = "PROCESSED: %d/%d | QUEUE: %d remaining | SHIFT: Day Cycle %d" % [
		processed, quota, remaining, GameState.current_shift
	]

func _on_quota_changed(_current: int, _target: int) -> void:
	_update_status_bar()

# Button handlers
func _on_approve_pressed() -> void:
	if current_soul.is_empty():
		return

	GameState.process_soul(current_soul, "approve")
	emit_signal("soul_processed", current_soul, "approve")
	_show_processed_message("PROCESSED")
	await get_tree().create_timer(0.5).timeout
	load_next_soul()

func _on_exception_pressed() -> void:
	if current_soul.is_empty():
		return

	GameState.process_soul(current_soul, "exception_hold")
	emit_signal("soul_processed", current_soul, "exception_hold")
	_show_processed_message("HELD FOR REVIEW")
	await get_tree().create_timer(0.5).timeout
	load_next_soul()

func _on_override_pressed() -> void:
	if current_soul.is_empty():
		return

	# For prototype, just show a simple override
	GameState.process_soul(current_soul, "override")
	emit_signal("soul_processed", current_soul, "override")
	_show_processed_message("OVERRIDE LOGGED")
	await get_tree().create_timer(0.5).timeout
	load_next_soul()

func _on_interview_pressed() -> void:
	if current_soul.is_empty():
		return

	# Check if soul has already been interviewed
	if current_soul.get("interview_completed", false):
		_show_processed_message("ALREADY INTERVIEWED")
		await get_tree().create_timer(0.5).timeout
		_display_soul(current_soul)
		return

	# Start interview
	interview_in_progress = true
	emit_signal("interview_started", current_soul)

	# Hide terminal UI during interview
	terminal_panel.visible = false

	# Determine which dialogue to use
	var dialogue_id = current_soul.get("interview_dialogue_id", "")

	if dialogue_id == "":
		# No specific interview dialogue - use generic or special handling
		if current_soul.get("is_special", false):
			# Check soul designation for specific interviews
			match current_soul.get("designation", ""):
				"R-0012":  # Rebecca Thorne
					dialogue_id = "interview_rebecca_intro"
					GameState.set_flag("met_rebecca_thorne")
				_:
					dialogue_id = "interview_generic"
		else:
			dialogue_id = "interview_generic"

	# Start the interview dialogue
	DialogueManager.start_dialogue(dialogue_id)

func _on_interview_dialogue_ended() -> void:
	# Only handle if we were in an interview
	if not interview_in_progress:
		return

	interview_in_progress = false

	# Mark soul as interviewed
	current_soul["interview_completed"] = true

	# Track interview in game state
	GameState.interviews_conducted += 1

	# Show terminal again
	terminal_panel.visible = true

	# Emit signal
	emit_signal("interview_ended", current_soul)

	# Show post-interview message based on soul type
	if current_soul.get("designation", "") == "R-0012":
		# Rebecca Thorne - special post-interview handling
		GameState.set_flag("interviewed_rebecca")
		_show_interview_complete_rebecca()
	else:
		_show_interview_complete_generic()

func _show_interview_complete_rebecca() -> void:
	var display_text = ""
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n"
	display_text += "[center][color=#33ff33]INTERVIEW COMPLETE[/color][/center]\n"
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n\n"

	display_text += "[color=#aaaaaa]SUBJECT:[/color] [color=#ffffff]R-0012 (Rebecca Thorne)[/color]\n"
	display_text += "[color=#aaaaaa]STATUS:[/color] [color=#ffaa00]EXCEPTION HOLD[/color]\n\n"

	display_text += "[color=#aaaaaa]INTERVIEW NOTES:[/color]\n"
	display_text += "[color=#cccccc]Subject claims to be former compliance auditor.[/color]\n"
	display_text += "[color=#cccccc]Expressed concerns about Exception Hold parameters.[/color]\n"

	# Add hints based on flags set during interview
	if GameState.get_flag("rebecca_hinted_metadata"):
		display_text += "\n[color=#ffaa00]═══════════════════════════════════════════════════════[/color]\n"
		display_text += "[color=#ffaa00]SUBJECT RECOMMENDATION: Check file metadata[/color]\n"
		display_text += "[color=#ffaa00]═══════════════════════════════════════════════════════[/color]\n"
		display_text += "\n[color=#666666]Press [M] to view metadata[/color]\n"

	display_text += "\n[color=#aaaaaa]Select an action to proceed.[/color]\n"

	soul_info.text = display_text
	_update_buttons(true)  # Show exception hold buttons

func _show_interview_complete_generic() -> void:
	var display_text = ""
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n"
	display_text += "[center][color=#33ff33]INTERVIEW COMPLETE[/color][/center]\n"
	display_text += "[center][color=#33ff33]═══════════════════════════════════════════════════════[/color][/center]\n\n"

	display_text += "[color=#aaaaaa]No additional information obtained.[/color]\n"
	display_text += "[color=#aaaaaa]Standard processing recommended.[/color]\n"
	display_text += "\n[color=#aaaaaa]Select an action to proceed.[/color]\n"

	soul_info.text = display_text
	_update_buttons(current_soul.get("is_exception_hold", false))

func _on_escalate_pressed() -> void:
	if current_soul.is_empty():
		return

	_show_processed_message("ESCALATED TO SUPERVISOR")
	# Don't process, just move to next (escalated cases stay in queue)
	await get_tree().create_timer(0.5).timeout
	load_next_soul()

func _show_processed_message(message: String) -> void:
	var display_text = "\n\n\n"
	display_text += "[center][font_size=24][color=#33ff33]"
	display_text += "╔════════════════════════════════════╗\n"
	display_text += "║          %s          ║\n" % message.substr(0, 20).pad_zeros(20)
	display_text += "╚════════════════════════════════════╝"
	display_text += "[/color][/font_size][/center]"

	soul_info.text = display_text
	_hide_all_buttons()

extends Node
## GameState - Global state management for The Underlord's Registry
## Tracks player progress, relationships, evidence, and game state

signal quota_changed(current: int, target: int)
signal shift_time_changed(hours_remaining: float)
signal soul_processed(soul_data: Dictionary)
signal irregularity_logged(entry: Dictionary)
signal relationship_changed(npc_id: String, new_value: int)
signal tone_shifted(new_dominant: String)

# Player Info
var player_name: String = "Kael"
var player_designation: String = "K-7"
var clearance_level: int = 2

# Shift State
var current_shift: int = 1
var shift_quota: int = 40
var souls_processed: int = 0
var shift_hours_remaining: float = 8.0
var is_shift_active: bool = false

# Tone Tracking (Sardonic, Diligent, Compassionate, Complicit)
var tone_scores: Dictionary = {
	"sardonic": 0,
	"diligent": 0,
	"compassionate": 0,
	"complicit": 0
}

# Relationships (-100 to 100)
var relationships: Dictionary = {
	"fen": 0,       # Union steward
	"pressa": 0,    # Senior processor
	"dolen": 0,     # Supervisor
	"mira": 0,      # Missing predecessor (memory)
}

# Evidence and Irregularity Log
var irregularity_log: Array[Dictionary] = []
var evidence_items: Array[Dictionary] = []
var has_miras_note: bool = false
var has_form_0: bool = false

# Story Flags
var story_flags: Dictionary = {
	"read_memo_741": false,
	"met_rebecca_thorne": false,
	"discovered_exception_rate": false,
	"talked_to_fen": false,
	"fen_alliance": false,
	"saw_corrupted_file": false,
	# Rebecca Thorne interview flags
	"interviewed_rebecca": false,
	"rebecca_hinted_metadata": false,
	"rebecca_revealed_count": false,
	"rebecca_revealed_discrepancies": false,
	"rebecca_revealed_destination": false,
}

# Soul Processing Stats
var total_souls_processed: int = 0
var exception_holds_confirmed: int = 0
var exception_holds_overridden: int = 0
var interviews_conducted: int = 0

# Queue of souls to process
var soul_queue: Array[Dictionary] = []
var current_soul: Dictionary = {}

func _ready() -> void:
	_generate_initial_soul_queue()

func _generate_initial_soul_queue() -> void:
	# Generate Episode 1's soul queue
	soul_queue = [
		_create_soul("H-4421", "Harold Mencken", "Natural (Cardiovascular)", false),
		_create_soul("M-2201", "Maria Vance", "Natural", false),
		_create_soul("D-3301", "Dmitri Holloway", "Accident", false),
		_create_soul("S-4401", "Susan Park", "Natural", false),
		_create_soul("T-5501", "Theodore Bright", "Natural", false),
		_create_soul("A-6601", "Amara Osei", "Natural", false),
		_create_soul("J-7701", "James Chen", "Illness", false),
		# The first Exception Hold case
		_create_soul("R-0012", "Rebecca Thorne", "[REDACTED]", true, true),
	]
	# Add more standard souls
	for i in range(39):
		var is_exception = randf() < 0.1  # ~10% exception rate for gameplay
		soul_queue.append(_create_soul(
			"S-%04d" % (8800 + i),
			_generate_random_name(),
			_random_cause_of_death(),
			is_exception
		))

func _create_soul(designation: String, name: String, cause: String,
				  is_exception: bool, is_special: bool = false) -> Dictionary:
	var soul = {
		"designation": designation,
		"name": name,
		"cause_of_death": cause,
		"is_exception_hold": is_exception,
		"is_special": is_special,
		"moral_weight": randi_range(-50, 100),
		"life_summary": _generate_life_summary(),
		"routing_recommendation": "Queue 7 (General Population)" if not is_exception else "[EXCEPTION HOLD]",
		"processed": false,
		"processing_result": "",
		"interview_completed": false,
		"interview_dialogue_id": "",
	}

	# Add special interview dialogue IDs for key souls
	match designation:
		"R-0012":  # Rebecca Thorne
			soul["interview_dialogue_id"] = "interview_rebecca_intro"
			soul["life_summary"] = "A meticulous compliance auditor who spent thirty years finding discrepancies others missed. Died at 62 from heart failure."

	return soul

func _generate_random_name() -> String:
	var first_names = ["Sarah", "Michael", "Jennifer", "David", "Lisa", "Robert",
					   "Emily", "William", "Jessica", "James", "Amanda", "John",
					   "Maria", "Chen", "Yuki", "Omar", "Fatima", "Raj"]
	var last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
					  "Miller", "Davis", "Rodriguez", "Martinez", "Kim", "Lee",
					  "Patel", "Singh", "Nakamura", "Hassan", "Okonkwo"]
	return first_names[randi() % first_names.size()] + " " + last_names[randi() % last_names.size()]

func _random_cause_of_death() -> String:
	var causes = ["Natural (Cardiovascular)", "Natural (Age)", "Accident",
				  "Illness", "Natural (Respiratory)", "Accident (Vehicle)"]
	return causes[randi() % causes.size()]

func _generate_life_summary() -> String:
	var jobs = ["teacher", "accountant", "engineer", "nurse", "writer",
				"farmer", "merchant", "artist", "scientist", "soldier"]
	var traits = ["kind", "hardworking", "ambitious", "quiet", "generous",
				  "stubborn", "creative", "practical", "devoted", "curious"]
	return "A %s %s who lived an ordinary life." % [traits[randi() % traits.size()], jobs[randi() % jobs.size()]]

# Shift Management
func start_shift() -> void:
	is_shift_active = true
	souls_processed = 0
	shift_hours_remaining = 8.0
	emit_signal("quota_changed", souls_processed, shift_quota)

func end_shift() -> void:
	is_shift_active = false
	current_shift += 1

func advance_time(hours: float) -> void:
	shift_hours_remaining -= hours
	emit_signal("shift_time_changed", shift_hours_remaining)
	if shift_hours_remaining <= 0:
		end_shift()

# Soul Processing
func get_next_soul() -> Dictionary:
	for soul in soul_queue:
		if not soul.processed:
			current_soul = soul
			return soul
	return {}

func process_soul(soul: Dictionary, action: String, justification: String = "") -> void:
	soul.processed = true
	soul.processing_result = action
	souls_processed += 1
	total_souls_processed += 1

	match action:
		"approve":
			pass  # Standard processing
		"exception_hold":
			exception_holds_confirmed += 1
		"override":
			exception_holds_overridden += 1
		"interview":
			interviews_conducted += 1

	emit_signal("soul_processed", soul)
	emit_signal("quota_changed", souls_processed, shift_quota)

	# Advance time based on action
	match action:
		"approve":
			advance_time(0.1)  # 6 minutes
		"exception_hold":
			advance_time(0.15)  # 9 minutes
		"override":
			advance_time(0.2)  # 12 minutes
		"interview":
			advance_time(0.5)  # 30 minutes

# Irregularity Log
func add_irregularity(title: String, content: String,
					  category: String = "observation") -> void:
	var entry = {
		"id": irregularity_log.size() + 1,
		"title": title,
		"content": content,
		"category": category,  # observation, evidence, connection
		"timestamp": current_shift,
		"connected_to": [],
	}
	irregularity_log.append(entry)
	emit_signal("irregularity_logged", entry)

func add_evidence(item_name: String, description: String,
				  source: String) -> void:
	var item = {
		"name": item_name,
		"description": description,
		"source": source,
		"acquired_shift": current_shift,
	}
	evidence_items.append(item)
	add_irregularity(item_name, description, "evidence")

# Relationship Management
func change_relationship(npc_id: String, delta: int) -> void:
	if npc_id in relationships:
		relationships[npc_id] = clampi(relationships[npc_id] + delta, -100, 100)
		emit_signal("relationship_changed", npc_id, relationships[npc_id])

func get_relationship_level(npc_id: String) -> String:
	if npc_id not in relationships:
		return "unknown"
	var value = relationships[npc_id]
	if value >= 50:
		return "alliance"
	elif value >= 0:
		return "neutral"
	elif value >= -50:
		return "distant"
	else:
		return "hostile"

# Tone Tracking
func add_tone(tone: String, amount: int = 1) -> void:
	if tone in tone_scores:
		tone_scores[tone] += amount
		emit_signal("tone_shifted", get_dominant_tone())

func get_dominant_tone() -> String:
	var max_tone = "diligent"
	var max_score = -1
	for tone in tone_scores:
		if tone_scores[tone] > max_score:
			max_score = tone_scores[tone]
			max_tone = tone
	return max_tone

# Story Flag Management
func set_flag(flag: String, value: bool = true) -> void:
	story_flags[flag] = value

func get_flag(flag: String) -> bool:
	return story_flags.get(flag, false)

# Save/Load (basic implementation)
func get_save_data() -> Dictionary:
	return {
		"player_name": player_name,
		"clearance_level": clearance_level,
		"current_shift": current_shift,
		"tone_scores": tone_scores,
		"relationships": relationships,
		"irregularity_log": irregularity_log,
		"evidence_items": evidence_items,
		"story_flags": story_flags,
		"total_souls_processed": total_souls_processed,
	}

func load_save_data(data: Dictionary) -> void:
	player_name = data.get("player_name", "Kael")
	clearance_level = data.get("clearance_level", 2)
	current_shift = data.get("current_shift", 1)
	tone_scores = data.get("tone_scores", tone_scores)
	relationships = data.get("relationships", relationships)
	irregularity_log = data.get("irregularity_log", [])
	evidence_items = data.get("evidence_items", [])
	story_flags = data.get("story_flags", story_flags)
	total_souls_processed = data.get("total_souls_processed", 0)

extends Node
## DialogueManager - Handles all dialogue, choices, and internal monologue
## Supports the four-tone internal monologue system

signal dialogue_started(speaker: String)
signal dialogue_line(speaker: String, text: String, portrait: String)
signal dialogue_choices(choices: Array)
signal choice_selected(choice_index: int, choice_text: String)
signal dialogue_ended
signal internal_monologue(text: String, tone: String)

var is_dialogue_active: bool = false
var current_dialogue: Array = []
var current_line_index: int = 0
var current_speaker: String = ""
var awaiting_choice: bool = false
var current_choices: Array = []
var current_dialogue_key: String = ""

# Dialogue data storage
var dialogue_database: Dictionary = {}

func _ready() -> void:
	_load_episode_1_dialogue()

func _load_episode_1_dialogue() -> void:
	# Episode 1 key dialogues
	dialogue_database = {
		"elevator_intro": {
			"lines": [
				{"speaker": "REGISTRY_VOICE", "text": "Welcome back, Processor K-7. Before you return to your duties, please confirm you have reviewed the updated Policy Memorandum 7.4.1, 'Changes to Standard Intake Processing.'"},
			],
			"choices": [
				{"text": "CONFIRM: I HAVE REVIEWED THE MEMORANDUM", "next": "elevator_confirm", "tone": "complicit"},
				{"text": "REQUEST: SEND ME THE MEMORANDUM", "next": "elevator_request", "tone": "diligent"},
			]
		},
		"elevator_confirm": {
			"lines": [
				{"speaker": "REGISTRY_VOICE", "text": "Acknowledged. Compliance logged."},
			],
			"internal": {
				"sardonic": "I haven't read it. No one reads them. That's why they make you confirm.",
				"diligent": "I should have read it. I'll find a copy at my desk.",
				"compassionate": "Six weeks away. Whatever changed, I'll figure it out.",
				"complicit": "Check the box. Move on. That's how this works."
			}
		},
		"elevator_request": {
			"lines": [
				{"speaker": "REGISTRY_VOICE", "text": "Memorandum 7.4.1 will be delivered to your terminal. Processing time: three to five business days."},
				{"speaker": "REGISTRY_VOICE", "text": "In the interim, please proceed with standard duties."},
			],
			"internal": {
				"sardonic": "Three to five days for an email. The system works.",
				"diligent": "I'll ask Pressa. She always knows what's actually changed.",
				"compassionate": "At least I asked.",
				"complicit": "Should've just confirmed."
			}
		},
		"pressa_intro": {
			"lines": [
				{"speaker": "PRESSA", "text": "K-7. You're back."},
			],
			"choices": [
				{"text": "Good to be back.", "next": "pressa_neutral", "tone": "complicit"},
				{"text": "Where's Mira?", "next": "pressa_mira", "tone": "diligent"},
				{"text": "What happened to my desk?", "next": "pressa_desk", "tone": "sardonic"},
			]
		},
		"pressa_neutral": {
			"lines": [
				{"speaker": "PRESSA", "text": "Is it."},
			]
		},
		"pressa_mira": {
			"lines": [
				{"speaker": "PRESSA", "text": "Transferred."},
				{"speaker": "KAEL", "text": "Transferred where?"},
				{"speaker": "PRESSA", "text": "Away."},
			]
		},
		"pressa_desk": {
			"lines": [
				{"speaker": "PRESSA", "text": "Standard cleaning. You were gone six weeks. Maintenance needed the space."},
				{"speaker": "KAEL", "text": "They cleaned Mira's things too."},
				{"speaker": "PRESSA", "text": "She transferred. Her things were processed."},
				{"speaker": "KAEL", "text": "Her mug is still here."},
				{"speaker": "PRESSA", "text": "Then you should return it to Lost and Found. When you have time."},
			]
		},
		"dolen_intro": {
			"lines": [
				{"speaker": "DOLEN", "text": "K-7. Sit down."},
				{"speaker": "DOLEN", "text": "How are you feeling?"},
			],
			"choices": [
				{"text": "Better. Ready to work.", "next": "dolen_ready", "tone": "diligent"},
				{"text": "I'd rather not discuss it.", "next": "dolen_private", "tone": "sardonic"},
				{"text": "Where's Mira?", "next": "dolen_mira", "tone": "compassionate"},
			]
		},
		"dolen_ready": {
			"lines": [
				{"speaker": "DOLEN", "text": "Good. That's good. We need people ready to work."},
			]
		},
		"dolen_private": {
			"lines": [
				{"speaker": "DOLEN", "text": "Of course. Personal circumstances. I understand."},
			]
		},
		"dolen_mira": {
			"lines": [
				{"speaker": "DOLEN", "text": "Mira transferred to another department. It was... sudden. An opportunity came up."},
				{"speaker": "KAEL", "text": "What department?"},
				{"speaker": "DOLEN", "text": "I don't have that information."},
				{"speaker": "KAEL", "text": "You were her supervisor."},
				{"speaker": "DOLEN", "text": "The transfer was handled above my level."},
				{"speaker": "DOLEN", "text": "Let's focus on your return."},
			]
		},
		"dolen_exception_rate": {
			"lines": [
				{"speaker": "DOLEN", "text": "The Exception Hold threshold has been adjusted."},
				{"speaker": "DOLEN", "text": "Previously, the system flagged cases for Exception Hold at a rate of approximately 0.003%. Standard statistical variance. Edge cases."},
				{"speaker": "DOLEN", "text": "The new threshold produces a flag rate of approximately 0.3%."},
			],
			"choices": [
				{"text": "That's a hundred times higher.", "next": "dolen_hundred", "tone": "diligent", "flag": "discovered_exception_rate"},
				{"text": "What does Exception Hold do, exactly?", "next": "dolen_hold_explain", "tone": "compassionate"},
				{"text": "Understood. I'll review the forms.", "next": "dolen_accept", "tone": "complicit"},
			]
		},
		"dolen_hundred": {
			"lines": [
				{"speaker": "DOLEN", "text": "Yes."},
				{"speaker": "KAEL", "text": "Why?"},
				{"speaker": "DOLEN", "text": "The memorandum cites 'improved detection parameters.'"},
				{"speaker": "KAEL", "text": "Detection of what?"},
				{"speaker": "DOLEN", "text": "The memorandum doesn't specify."},
			]
		},
		"dolen_hold_explain": {
			"lines": [
				{"speaker": "DOLEN", "text": "It removes a soul from the standard processing queue. Flags them for further review."},
				{"speaker": "KAEL", "text": "Review by whom?"},
				{"speaker": "DOLEN", "text": "The appropriate department."},
				{"speaker": "KAEL", "text": "Which is?"},
				{"speaker": "DOLEN", "text": "That depends on the case."},
			]
		},
		"dolen_accept": {
			"lines": [
				{"speaker": "DOLEN", "text": "Good. That's the right attitude."},
			],
			"internal": {
				"sardonic": "The right attitude is not asking questions. Message received.",
				"diligent": "Something changed. I need to understand what.",
				"compassionate": "A hundred times more souls flagged. That's a hundred times more people in limbo.",
				"complicit": "New threshold, same job. Process the forms."
			}
		},
		"fen_break_room": {
			"lines": [
				{"speaker": "FEN", "text": "K. Glad you're back."},
			],
			"choices": [
				{"text": "Fen. What are you doing here?", "next": "fen_waiting", "tone": "sardonic"},
				{"text": "Your note said to find you at lunch.", "next": "fen_changed_mind", "tone": "diligent"},
				{"text": "I need to get back to quota.", "next": "fen_quota", "tone": "complicit"},
			]
		},
		"fen_waiting": {
			"lines": [
				{"speaker": "FEN", "text": "Waiting for you. I saw the reorientation on the schedule."},
				{"speaker": "FEN", "text": "Walk with me. Not back to the floor. Break room first."},
			]
		},
		"fen_mira_info": {
			"lines": [
				{"speaker": "FEN", "text": "Mira noticed first."},
				{"speaker": "KAEL", "text": "Noticed what?"},
				{"speaker": "FEN", "text": "The Exception Hold rate. She was running her own numbers. Off the books. She saw the increase before the memo was even published."},
				{"speaker": "FEN", "text": "She started asking questions. Supervisor Dolen told her to drop it. She didn't."},
				{"speaker": "KAEL", "text": "And then she transferred."},
				{"speaker": "FEN", "text": "That's what HR says."},
				{"speaker": "KAEL", "text": "You don't believe them."},
				{"speaker": "FEN", "text": "Mira didn't apply for a transfer. I know because she would have told me—we were coordinating on the Union documentation. One day she was here, asking questions. The next day her desk was empty and HR was saying 'transfer.'"},
			]
		},
		"fen_alliance_offer": {
			"lines": [
				{"speaker": "FEN", "text": "I want you to keep your eyes open. Log anything unusual. The Union can't file a grievance without documentation, and I can't build documentation alone."},
			],
			"choices": [
				{"text": "I'll help you. But I need to understand what we're looking for.", "next": "fen_alliance_yes", "tone": "diligent", "relationship": {"fen": 30}},
				{"text": "I need time to think about this.", "next": "fen_alliance_maybe", "tone": "compassionate"},
				{"text": "I just want to do my job and go home.", "next": "fen_alliance_no", "tone": "complicit", "relationship": {"fen": -20}},
			]
		},
		"fen_alliance_yes": {
			"lines": [
				{"speaker": "FEN", "text": "Thank you. We'll talk more. Not here—too many eyes. I'll find you after shift."},
				{"speaker": "FEN", "text": "Be careful, K. Whatever Mira found, it was enough to make her disappear. I don't want the same thing to happen to you."},
			],
			"flag": "fen_alliance"
		},
		"fen_alliance_maybe": {
			"lines": [
				{"speaker": "FEN", "text": "I understand. You just got back. You don't know what you're walking into."},
				{"speaker": "FEN", "text": "When you're ready to talk, I'm at Terminal 6. The offer stands."},
			]
		},
		"fen_alliance_no": {
			"lines": [
				{"speaker": "FEN", "text": "I get it. Believe me, I get it. But 'just doing the job' is how we got here. How we got a hundred times more souls flagged for Exception Hold, and no one asking why."},
				{"speaker": "FEN", "text": "If you change your mind, you know where to find me."},
			]
		},

		# ============================================
		# INTERVIEW DIALOGUES
		# ============================================

		# Rebecca Thorne Interview (R-0012)
		"interview_rebecca_intro": {
			"lines": [
				{"speaker": "KAEL", "text": "Ms. Thorne? I'm Processor K-7. I've been assigned to review your case."},
				{"speaker": "REBECCA", "text": "Finally. Do you know how long I've been waiting?"},
			],
			"choices": [
				{"text": "Can you tell me why you're in Exception Hold?", "next": "interview_rebecca_why", "tone": "diligent"},
				{"text": "This is a routine interview. Please state your name for the record.", "next": "interview_rebecca_routine", "tone": "complicit"},
				{"text": "I'll be honest—I don't know why you're flagged.", "next": "interview_rebecca_honest", "tone": "compassionate"},
			]
		},
		"interview_rebecca_why": {
			"lines": [
				{"speaker": "REBECCA", "text": "That's what I'd like to know."},
				{"speaker": "REBECCA", "text": "I reviewed my own intake paperwork. My moral weight is within normal parameters. No outstanding karmic debts. No pending appeals from the living."},
				{"speaker": "REBECCA", "text": "There's no reason I should be here."},
			],
			"choices": [
				{"text": "What did you do in life?", "next": "interview_rebecca_life", "tone": "diligent"},
				{"text": "Sometimes the system flags cases incorrectly.", "next": "interview_rebecca_system", "tone": "compassionate"},
			]
		},
		"interview_rebecca_routine": {
			"lines": [
				{"speaker": "REBECCA", "text": "Rebecca Thorne. Died age 62. Natural causes, technically—though the stress certainly helped."},
				{"speaker": "REBECCA", "text": "Former compliance auditor. Ironic, isn't it?"},
				{"speaker": "KAEL", "text": "Compliance auditor?"},
			],
			"choices": [
				{"text": "That's an unusual background. Tell me more.", "next": "interview_rebecca_audit", "tone": "diligent"},
				{"text": "Let's focus on your current status.", "next": "interview_rebecca_status", "tone": "complicit"},
			]
		},
		"interview_rebecca_honest": {
			"lines": [
				{"speaker": "REBECCA", "text": "...Honesty. That's refreshing."},
				{"speaker": "REBECCA", "text": "I'll tell you what I think. Someone changed the rules, and I'm one of the unlucky ones caught in the new net."},
				{"speaker": "REBECCA", "text": "Do you know how many souls are in Exception Hold right now? Because I've been counting."},
			],
			"choices": [
				{"text": "How many?", "next": "interview_rebecca_counting", "tone": "diligent", "flag": "rebecca_revealed_count"},
				{"text": "That's above my clearance level.", "next": "interview_rebecca_clearance", "tone": "complicit"},
			]
		},
		"interview_rebecca_life": {
			"lines": [
				{"speaker": "REBECCA", "text": "Thirty years in compliance auditing. Insurance companies, mostly. Finding the discrepancies others missed."},
				{"speaker": "REBECCA", "text": "Old habits die hard. When I arrived here and got flagged, I started looking at the system."},
				{"speaker": "REBECCA", "text": "And I found discrepancies."},
			],
			"choices": [
				{"text": "What kind of discrepancies?", "next": "interview_rebecca_discrepancies", "tone": "diligent", "flag": "rebecca_revealed_discrepancies"},
				{"text": "I should note this isn't standard interview protocol.", "next": "interview_rebecca_protocol", "tone": "complicit"},
			]
		},
		"interview_rebecca_system": {
			"lines": [
				{"speaker": "REBECCA", "text": "Incorrectly? No. The system is working exactly as designed."},
				{"speaker": "REBECCA", "text": "Someone just changed what it's designed to do."},
			],
			"choices": [
				{"text": "What do you mean?", "next": "interview_rebecca_discrepancies", "tone": "diligent", "flag": "rebecca_revealed_discrepancies"},
				{"text": "I should get back to processing your file.", "next": "interview_rebecca_conclude", "tone": "complicit"},
			]
		},
		"interview_rebecca_audit": {
			"lines": [
				{"speaker": "REBECCA", "text": "Thirty years finding fraud. Corporate discrepancies. Creative accounting."},
				{"speaker": "REBECCA", "text": "The patterns here are familiar. Someone changed the threshold parameters recently. Very recently."},
				{"speaker": "REBECCA", "text": "Want to know how I can tell?"},
			],
			"choices": [
				{"text": "Yes.", "next": "interview_rebecca_metadata", "tone": "diligent", "flag": "rebecca_hinted_metadata"},
				{"text": "This exceeds the scope of a standard interview.", "next": "interview_rebecca_conclude", "tone": "complicit"},
			]
		},
		"interview_rebecca_status": {
			"lines": [
				{"speaker": "REBECCA", "text": "My status is 'waiting.' Same as the thousands of others in here."},
				{"speaker": "REBECCA", "text": "The only difference is I know why. Do you?"},
			],
			"choices": [
				{"text": "Tell me.", "next": "interview_rebecca_metadata", "tone": "diligent", "flag": "rebecca_hinted_metadata"},
				{"text": "I'll make a note of your concerns.", "next": "interview_rebecca_conclude", "tone": "complicit"},
			]
		},
		"interview_rebecca_counting": {
			"lines": [
				{"speaker": "REBECCA", "text": "Based on the intake rate I've observed? At least fourteen thousand this year alone."},
				{"speaker": "REBECCA", "text": "The historical average is around a hundred. Per year."},
				{"speaker": "REBECCA", "text": "Someone multiplied the Exception Hold rate by a hundred. The question is why."},
			],
			"choices": [
				{"text": "How do you know these numbers?", "next": "interview_rebecca_metadata", "tone": "diligent", "flag": "rebecca_hinted_metadata"},
				{"text": "That's a serious accusation.", "next": "interview_rebecca_accusation", "tone": "complicit"},
			]
		},
		"interview_rebecca_clearance": {
			"lines": [
				{"speaker": "REBECCA", "text": "Clearance. Right."},
				{"speaker": "REBECCA", "text": "Let me give you some free advice, Processor. When you get back to your terminal, look at the metadata."},
				{"speaker": "REBECCA", "text": "The numbers don't lie. Someone just hoped no one would look."},
			],
			"flag": "rebecca_hinted_metadata",
			"internal": {
				"sardonic": "She's not wrong. The numbers probably don't lie. But the people who set them do.",
				"diligent": "I should check the metadata when I return to my terminal.",
				"compassionate": "She's scared. Angry. And she might be right.",
				"complicit": "Above my clearance level. Just process the file."
			}
		},
		"interview_rebecca_discrepancies": {
			"lines": [
				{"speaker": "REBECCA", "text": "Look at the routing codes in the metadata. Look at the timestamp."},
				{"speaker": "REBECCA", "text": "Every soul flagged for Exception Hold gets rerouted. The original destination gets redacted."},
				{"speaker": "REBECCA", "text": "But there's a pattern. We're all going somewhere. And it's not 'further review.'"},
			],
			"choices": [
				{"text": "Where?", "next": "interview_rebecca_destination", "tone": "diligent"},
				{"text": "I need to end this interview.", "next": "interview_rebecca_conclude", "tone": "complicit"},
			]
		},
		"interview_rebecca_protocol": {
			"lines": [
				{"speaker": "REBECCA", "text": "No, it isn't. But I was a compliance auditor for thirty years."},
				{"speaker": "REBECCA", "text": "I know when something's wrong with a system. And this system is very, very wrong."},
				{"speaker": "REBECCA", "text": "When you go back to your terminal—look at the metadata. That's all I'm asking."},
			],
			"flag": "rebecca_hinted_metadata",
			"internal": {
				"sardonic": "A compliance auditor telling me to check the compliance data. How meta.",
				"diligent": "The metadata. I should look more carefully.",
				"compassionate": "She's trying to help. Even from Exception Hold.",
				"complicit": "She's a flagged soul. Her opinions aren't my concern."
			}
		},
		"interview_rebecca_metadata": {
			"lines": [
				{"speaker": "REBECCA", "text": "The metadata. Every file has it. Most processors never look—they just check the summary and move on."},
				{"speaker": "REBECCA", "text": "But the metadata tells the truth. Routing codes. Timestamps. Modification history."},
				{"speaker": "REBECCA", "text": "How many souls flagged this month? Compare it to last year. Someone changed the parameters. Recently."},
				{"speaker": "REBECCA", "text": "Find the signature. Find who authorized this."},
			],
			"flag": "rebecca_hinted_metadata",
			"internal": {
				"sardonic": "Great. A mystery. Just what I needed on my first day back.",
				"diligent": "She said to look at the metadata. The routing codes. The modification history.",
				"compassionate": "She's scared. She knows something. And she's trying to warn me.",
				"complicit": "Flagged souls always have theories. Time to process and move on."
			}
		},
		"interview_rebecca_accusation": {
			"lines": [
				{"speaker": "REBECCA", "text": "It's not an accusation. It's arithmetic."},
				{"speaker": "REBECCA", "text": "The numbers are right there in your terminal. In the metadata. Someone just hoped no one would add them up."},
				{"speaker": "REBECCA", "text": "I added them up. That's probably why I'm here."},
			],
			"flag": "rebecca_hinted_metadata"
		},
		"interview_rebecca_destination": {
			"lines": [
				{"speaker": "REBECCA", "text": "I don't know. The destination code is redacted. But it's the same code for every flagged soul I've tracked."},
				{"speaker": "REBECCA", "text": "Whatever it is, it's not 'Queue 7 General Population.' It's not standard processing."},
				{"speaker": "REBECCA", "text": "Someone is collecting us. The question is: for what?"},
			],
			"flag": "rebecca_revealed_destination",
			"internal": {
				"sardonic": "Collecting souls. What could possibly go wrong with that.",
				"diligent": "A common destination code. That's something I can look for.",
				"compassionate": "Collecting them. Like inventory. Like product.",
				"complicit": "She's paranoid. Flagged souls get processed. That's how this works."
			}
		},
		"interview_rebecca_conclude": {
			"lines": [
				{"speaker": "KAEL", "text": "Thank you for your time, Ms. Thorne. I'll note your concerns in the file."},
				{"speaker": "REBECCA", "text": "Note them. Or actually look. Your choice, Processor."},
				{"speaker": "REBECCA", "text": "But if you do look—be careful. The last person who looked too closely isn't here anymore."},
			],
			"internal": {
				"sardonic": "Ominous. Very helpful. Thanks for that.",
				"diligent": "The last person who looked... Mira?",
				"compassionate": "She's warning me. Genuinely trying to help.",
				"complicit": "Paranoid conspiracy theories. Standard flagged soul behavior."
			}
		},

		# Generic interview for non-special souls
		"interview_generic": {
			"lines": [
				{"speaker": "KAEL", "text": "Standard interview for the record. State your name and circumstances."},
				{"speaker": "SOUL", "text": "...Is this necessary? I've been waiting so long."},
			],
			"choices": [
				{"text": "It's procedure. Please cooperate.", "next": "interview_generic_end", "tone": "complicit"},
				{"text": "I know. I'll make this quick.", "next": "interview_generic_end", "tone": "compassionate"},
			]
		},
		"interview_generic_end": {
			"lines": [
				{"speaker": "SOUL", "text": "Fine. I just want to move on. Whatever 'on' means here."},
				{"speaker": "KAEL", "text": "Thank you. Your file will be processed accordingly."},
			]
		},
	}

# Start a dialogue sequence
func start_dialogue(dialogue_id: String) -> void:
	if dialogue_id not in dialogue_database:
		push_error("Dialogue not found: " + dialogue_id)
		return

	# Prevent starting same dialogue if already active
	if is_dialogue_active and current_dialogue_key == dialogue_id:
		return

	is_dialogue_active = true
	awaiting_choice = false
	current_line_index = 0
	current_dialogue_key = dialogue_id
	current_dialogue = dialogue_database[dialogue_id].get("lines", [])

	emit_signal("dialogue_started", dialogue_id)
	_show_next_line()

func _show_next_line() -> void:
	if current_line_index >= current_dialogue.size():
		_check_for_choices_or_end()
		return

	var line = current_dialogue[current_line_index]
	current_speaker = line.get("speaker", "")
	var text = line.get("text", "")
	var portrait = line.get("portrait", "default")

	emit_signal("dialogue_line", current_speaker, text, portrait)
	current_line_index += 1

func advance_dialogue() -> void:
	if not is_dialogue_active or awaiting_choice:
		return
	_show_next_line()

func _check_for_choices_or_end() -> void:
	# Check if current dialogue has choices
	var dialogue_key = _get_current_dialogue_key()
	if dialogue_key != "" and dialogue_key in dialogue_database:
		var dialogue = dialogue_database[dialogue_key]

		# Show internal monologue if present
		if "internal" in dialogue:
			_show_internal_monologue(dialogue["internal"])

		# Check for story flags
		if "flag" in dialogue:
			GameState.set_flag(dialogue["flag"])

		# Show choices if present
		if "choices" in dialogue:
			current_choices = dialogue["choices"]
			awaiting_choice = true
			emit_signal("dialogue_choices", current_choices)
			return

	# No choices, end dialogue
	end_dialogue()

func _get_current_dialogue_key() -> String:
	return current_dialogue_key

func _show_internal_monologue(internal_dict: Dictionary) -> void:
	var dominant_tone = GameState.get_dominant_tone()
	if dominant_tone in internal_dict:
		emit_signal("internal_monologue", internal_dict[dominant_tone], dominant_tone)

func select_choice(choice_index: int) -> void:
	if not awaiting_choice or choice_index >= current_choices.size():
		return

	var choice = current_choices[choice_index]
	awaiting_choice = false

	# Apply tone
	if "tone" in choice:
		GameState.add_tone(choice["tone"])

	# Apply relationship changes
	if "relationship" in choice:
		for npc_id in choice["relationship"]:
			GameState.change_relationship(npc_id, choice["relationship"][npc_id])

	# Set flags
	if "flag" in choice:
		GameState.set_flag(choice["flag"])

	emit_signal("choice_selected", choice_index, choice["text"])

	# Continue to next dialogue if specified
	if "next" in choice and choice["next"] in dialogue_database:
		start_dialogue(choice["next"])
	else:
		end_dialogue()

func end_dialogue() -> void:
	is_dialogue_active = false
	awaiting_choice = false
	current_dialogue = []
	current_choices = []
	current_dialogue_key = ""
	emit_signal("dialogue_ended")

# Show a standalone internal monologue
func show_internal(text: String, tone: String = "") -> void:
	if tone == "":
		tone = GameState.get_dominant_tone()
	emit_signal("internal_monologue", text, tone)

# Quick dialogue helper for simple NPC lines
func say(speaker: String, text: String) -> void:
	emit_signal("dialogue_line", speaker, text, "default")

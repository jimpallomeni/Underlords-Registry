#!/usr/bin/env python3
"""
Art generation script for The Underlord's Registry
Noir/Minimalist style - high contrast, limited palette
"""

import requests
import base64
import json
from pathlib import Path
from PIL import Image
import io

API_URL = "http://127.0.0.1:7860"
OUTPUT_DIR = Path(__file__).parent / "game" / "images"

# Ensure directories exist
for char in ["kael", "pressa", "dolen", "fen", "rebecca"]:
    (OUTPUT_DIR / "characters" / char).mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "backgrounds").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "ui").mkdir(parents=True, exist_ok=True)

# Noir style settings
BASE_NEGATIVE = "colorful, vibrant, saturated, cartoon, anime, pixel art, pixelated, blurry, low quality, watermark, signature, text, deformed, ugly"

NOIR_STYLE = "noir style, high contrast, dramatic lighting, dark shadows, limited color palette, moody atmosphere, cinematic, film noir aesthetic, desaturated, muted colors, professional illustration"

def generate_image(prompt, negative_prompt=BASE_NEGATIVE, width=768, height=768, seed=-1):
    """Generate an image using A1111 API."""
    payload = {
        "prompt": f"{prompt}, {NOIR_STYLE}",
        "negative_prompt": negative_prompt,
        "steps": 30,
        "cfg_scale": 7.5,
        "width": width,
        "height": height,
        "sampler_name": "DPM++ 2M Karras",
        "seed": seed,
    }

    response = requests.post(f"{API_URL}/sdapi/v1/txt2img", json=payload)
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code}")

    result = response.json()
    image_data = base64.b64decode(result["images"][0])
    image = Image.open(io.BytesIO(image_data))

    info = json.loads(result["info"])
    used_seed = info.get("seed", -1)

    return image, used_seed

def save_image(image, path):
    """Save image directly (no pixelation for noir style)."""
    image.save(path, quality=95)
    print(f"Saved: {path}")

# Character definitions - Noir style
CHARACTERS = {
    "kael": {
        "base": "portrait of androgynous office worker, short brown hair, tired eyes, wearing gray bureaucrat uniform, neutral background, dramatic side lighting, shadows on face, melancholic expression",
        "expressions": {
            "neutral": "neutral calm expression, stoic",
            "sardonic": "slight knowing smirk, one eyebrow raised, cynical",
            "concerned": "worried furrowed brow, concerned eyes",
            "surprised": "wide eyes, raised eyebrows, startled",
        }
    },
    "pressa": {
        "base": "portrait of elderly woman, 70 years old, silver white hair in tight bun, sharp piercing eyes, wearing immaculate gray uniform, severe face, dramatic lighting from above, deep shadows",
        "expressions": {
            "neutral": "stern neutral expression, intimidating",
            "warning": "intense warning glare, slight frown, menacing",
            "disapproving": "disapproving narrowed eyes, judgmental",
        }
    },
    "dolen": {
        "base": "portrait of middle-aged man, 50 years old, receding hairline, slightly sweaty nervous face, wearing supervisor uniform with badge, office background with blinds, harsh fluorescent lighting",
        "expressions": {
            "neutral": "forced professional expression, underlying tension",
            "nervous": "visibly anxious, darting eyes, sweating, uncomfortable",
            "relieved": "relieved exhale, relaxed shoulders",
            "warning": "serious grave expression, lowered voice energy",
        }
    },
    "fen": {
        "base": "portrait of young adult, determined face, short dark hair, wearing gray uniform with small union pin, idealistic eyes, dramatic rim lighting",
        "expressions": {
            "neutral": "calm determined expression, resolute",
            "concerned": "worried concerned expression, empathetic",
            "hopeful": "hopeful slight smile, optimistic eyes",
            "disappointed": "disappointed downcast expression, sad",
        }
    },
    "rebecca": {
        "base": "portrait of ghostly translucent woman, 40 years old, professional business attire, ethereal blue-white glow, slightly transparent, sharp intelligent eyes, spectral apparition, dark void background",
        "expressions": {
            "neutral": "neutral professional waiting expression",
            "guarded": "guarded defensive expression, wary",
            "intense": "intense focused piercing stare, leaning forward",
            "resigned": "resigned accepting expression, weary",
        }
    },
}

BACKGROUNDS = {
    "elevator": "interior of service elevator, beige metal walls, harsh fluorescent lighting from above, floor indicator panel glowing, claustrophobic space, noir atmosphere, dramatic shadows, first person perspective, liminal space",

    "intake_floor": "vast dark open office interior, rows of old computer terminals with green glow, harsh overhead fluorescent lights creating pools of light, long shadows, cubicle farm stretching into darkness, oppressive corporate atmosphere, wide establishing shot",

    "dolens_office": "small supervisor office interior, cluttered desk with papers, venetian blinds half-closed casting striped shadows, single desk lamp creating dramatic lighting, oppressive atmosphere, noir interior",

    "interview_booth": "small stark interrogation room, two empty chairs facing each other across metal table, one-way mirror reflecting darkness, single harsh overhead light, noir atmosphere, minimalist cold space",

    "terminal_closeup": "extreme closeup of old CRT computer monitor, green phosphor text glowing in darkness, reflection of face barely visible in screen, retro technology, noir lighting",

    "break_room": "dingy office break room, old coffee machine, flickering fluorescent light, microwave with passive aggressive notes, sad small table, depressing corporate kitchen, noir atmosphere",
}

def generate_character(name, char_data, seed=None):
    """Generate all expressions for a character."""
    print(f"\n{'='*50}")
    print(f"Generating {name.upper()}")
    print(f"{'='*50}")
    base_prompt = char_data["base"]

    if seed is None:
        _, seed = generate_image(f"{base_prompt}, {char_data['expressions']['neutral']}")

    for expr_name, expr_prompt in char_data["expressions"].items():
        print(f"  {expr_name}...")
        full_prompt = f"{base_prompt}, {expr_prompt}"
        image, _ = generate_image(full_prompt, seed=seed)
        output_path = OUTPUT_DIR / "characters" / name / f"{expr_name}.png"
        save_image(image, output_path)

    return seed

def generate_background(name, prompt):
    """Generate a background image."""
    print(f"  {name}...")
    image, seed = generate_image(prompt, width=1280, height=720)
    output_path = OUTPUT_DIR / "backgrounds" / f"{name}.png"
    save_image(image, output_path)
    return seed

def main():
    print("=" * 60)
    print("The Underlord's Registry - NOIR Art Generation")
    print("=" * 60)

    # Generate characters
    for name, data in CHARACTERS.items():
        generate_character(name, data)

    # Generate backgrounds
    print(f"\n{'='*50}")
    print("Generating BACKGROUNDS")
    print(f"{'='*50}")
    for name, prompt in BACKGROUNDS.items():
        generate_background(name, prompt)

    print("\n" + "=" * 60)
    print("Generation complete!")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()

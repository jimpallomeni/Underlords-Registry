# Art Generation Prompts — The Underlord's Registry

## Style Guide

All images are generated using Stable Diffusion (A1111 WebUI API) with a consistent noir aesthetic.

### Base Style Token
```
noir style, high contrast, dramatic lighting, dark shadows, limited color palette, moody atmosphere, cinematic, film noir aesthetic, desaturated, muted colors, professional illustration
```

### Negative Prompt (applied to all)
```
colorful, vibrant, saturated, cartoon, anime, pixel art, pixelated, blurry, low quality, watermark, signature, text, deformed, ugly
```

### Generation Settings
- **Sampler:** DPM++ 2M Karras
- **Steps:** 30
- **CFG Scale:** 7.5
- **Character Size:** 768x768
- **Background Size:** 1280x720

---

## Character Prompts

### Kael (Player Character)
**Base prompt:**
```
portrait of androgynous office worker, short brown hair, tired eyes, wearing gray bureaucrat uniform, neutral background, dramatic side lighting, shadows on face, melancholic expression
```

| Expression | Additional prompt |
|------------|-------------------|
| neutral | neutral calm expression, stoic |
| sardonic | slight knowing smirk, one eyebrow raised, cynical |
| concerned | worried furrowed brow, concerned eyes |
| surprised | wide eyes, raised eyebrows, startled |

---

### Pressa (Ancient Processor)
**Base prompt:**
```
portrait of elderly woman, 70 years old, silver white hair in tight bun, sharp piercing eyes, wearing immaculate gray uniform, severe face, dramatic lighting from above, deep shadows
```

| Expression | Additional prompt |
|------------|-------------------|
| neutral | stern neutral expression, intimidating |
| warning | intense warning glare, slight frown, menacing |
| disapproving | disapproving narrowed eyes, judgmental |

---

### Dolen (Supervisor)
**Base prompt:**
```
portrait of middle-aged man, 50 years old, receding hairline, slightly sweaty nervous face, wearing supervisor uniform with badge, office background with blinds, harsh fluorescent lighting
```

| Expression | Additional prompt |
|------------|-------------------|
| neutral | forced professional expression, underlying tension |
| nervous | visibly anxious, darting eyes, sweating, uncomfortable |
| relieved | relieved exhale, relaxed shoulders |
| warning | serious grave expression, lowered voice energy |

---

### Fen (Union Steward)
**Base prompt:**
```
portrait of young adult, determined face, short dark hair, wearing gray uniform with small union pin, idealistic eyes, dramatic rim lighting
```

| Expression | Additional prompt |
|------------|-------------------|
| neutral | calm determined expression, resolute |
| concerned | worried concerned expression, empathetic |
| hopeful | hopeful slight smile, optimistic eyes |
| disappointed | disappointed downcast expression, sad |

---

### Rebecca Thorne (Exception Hold Soul)
**Base prompt:**
```
portrait of ghostly translucent woman, 40 years old, professional business attire, ethereal blue-white glow, slightly transparent, sharp intelligent eyes, spectral apparition, dark void background
```

| Expression | Additional prompt |
|------------|-------------------|
| neutral | neutral professional waiting expression |
| guarded | guarded defensive expression, wary |
| intense | intense focused piercing stare, leaning forward |
| resigned | resigned accepting expression, weary |

---

## Background Prompts

### elevator
```
interior of service elevator, beige metal walls, harsh fluorescent lighting from above, floor indicator panel glowing, claustrophobic space, noir atmosphere, dramatic shadows, first person perspective, liminal space
```

### intake_floor
```
vast dark open office interior, rows of old computer terminals with green glow, harsh overhead fluorescent lights creating pools of light, long shadows, cubicle farm stretching into darkness, oppressive corporate atmosphere, wide establishing shot
```

### dolens_office
```
small supervisor office interior, cluttered desk with papers, venetian blinds half-closed casting striped shadows, single desk lamp creating dramatic lighting, oppressive atmosphere, noir interior
```

### interview_booth
```
small stark interrogation room, two empty chairs facing each other across metal table, one-way mirror reflecting darkness, single harsh overhead light, noir atmosphere, minimalist cold space
```

### terminal_closeup
```
extreme closeup of old CRT computer monitor, green phosphor text glowing in darkness, reflection of face barely visible in screen, retro technology, noir lighting
```

### break_room
```
dingy office break room, old coffee machine, flickering fluorescent light, microwave with passive aggressive notes, sad small table, depressing corporate kitchen, noir atmosphere
```

---

## Usage

Run the generation script with A1111 WebUI running locally:

```bash
cd renpy_prototype
python generate_art.py
```

Images are saved to `game/images/characters/` and `game/images/backgrounds/`.

## Consistency Tips

- Use the same seed for all expressions of a character to maintain facial consistency
- The script automatically captures the seed from the first neutral expression and reuses it
- Adjust CFG scale (5-10) to balance prompt adherence vs creativity
- For translucent/ghostly effects (Rebecca), the model interprets "translucent" and "ethereal glow" reasonably well

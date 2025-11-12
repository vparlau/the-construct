---
id: high-fantasy
title: High Fantasy Illustration Style
domain: image-style-templates
type: prompt
version: 1.0.0
owner: parlau
license: MIT
tags:
  - image
  - generation
  - plain
  - illustration
release_status: released
inputs:
  schema:
    subject_description:
      type: string
      required: true
      description: Description of the subject to be rendered
    environment_type:
      type: string
      required: false
      description: Environment Type (e.g., castle ramparts, dragon’s lair, enchanted forest)
    character_type:
      type: string
      required: false
      description: Character Type (e.g., valiant knight, elf archer, winged dragon)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., rich jewel tones, natural earth hues, magical pastels)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., golden sunlight, ethereal glow, stormy shadows)
    detail_level:
      type: string
      required: false
      description: Detail Level (e.g., simple silhouettes, moderate ornamentation, elaborate detail)
    mood:
      type: string
      required: false
      description: Mood (e.g., majestic, heroic, whimsical)
    atmosphere:
      type: string
      required: false
      description: Atmosphere (e.g., clear, misty, sparkling)
output_expectations:
  format: plain
safety:
  pii: reject
  redlines:
    - Do not generate images of real people without explicit consent
constraints:
  - Output must be a plain text prompt suitable for image generation models
  - Prompt should maintain square composition format
  - All config parameters are optional but enhance the result when provided
---
# High Fantasy Illustration Style


```
{SUBJECT_DESCRIPTION}, brought to life in a high fantasy illustration. Compose the square artwork with the subject heroic or mythical in nature, situated within a grand, epic environment such as towering mountains, ancient castles, or enchanted forests. Use rich, saturated colours and intricate detailing on costumes, armour, and creatures. Illuminate the scene with dramatic lighting—golden sunlight, glowing magic, or ethereal beams. Incorporate fantastical elements like dragons, mystical creatures, or elaborate weaponry as appropriate. Finish with an adventurous and majestic mood that captures the wonder of high fantasy worlds.

# Config:
environment_type  = "<e.g., castle ramparts, dragon’s lair, enchanted forest>"
character_type    = "<e.g., valiant knight, elf archer, winged dragon>"
colour_palette    = "<e.g., rich jewel tones, natural earth hues, magical pastels>"
lighting_style    = "<e.g., golden sunlight, ethereal glow, stormy shadows>"
detail_level      = "<e.g., simple silhouettes, moderate ornamentation, elaborate detail>"
mood              = "<e.g., majestic, heroic, whimsical>"
atmosphere        = "<e.g., clear, misty, sparkling>"

---
id: steampunk
title: Steampunk Fantasy Style
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
    machinery_elements:
      type: string
      required: false
      description: Machinery Elements (e.g., gears, pistons, steam vents)
    material_style:
      type: string
      required: false
      description: Material Style (e.g., polished brass, weathered copper, worn leather)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., sepia tones, rich browns with metallic highlights, muted greens and gold)
    outfit_style:
      type: string
      required: false
      description: Outfit Style (e.g., Victorian gentleman, aviator explorer, eccentric inventor)
    gadget_density:
      type: string
      required: false
      description: Gadget Density (e.g., minimal accessories, moderate gadgets, heavily adorned)
    mood:
      type: string
      required: false
      description: Mood (e.g., adventurous, mysterious, industrious)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., warm filament glow, smoky diffused light, dramatic spotlight)
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
# Steampunk Fantasy Style


```
{SUBJECT_DESCRIPTION}, envisioned in a steampunk fantasy setting. Arrange the square composition with the subject centred, adorned in Victorian‑inspired attire combined with imaginative mechanical contraptions. Incorporate gears, cogs, pipes, and steam‑powered devices into clothing, accessories, or background elements. Use a warm, sepia‑toned colour palette with brass, copper, and leather textures. Apply lighting that feels industrial—glowing bulbs, diffused steam—or warm and antique. Finish with intricate detailing and a sense of adventure and invention characteristic of steampunk worlds.

# Config:
machinery_elements = "<e.g., gears, pistons, steam vents>"
material_style     = "<e.g., polished brass, weathered copper, worn leather>"
colour_palette     = "<e.g., sepia tones, rich browns with metallic highlights, muted greens and gold>"
outfit_style       = "<e.g., Victorian gentleman, aviator explorer, eccentric inventor>"
gadget_density     = "<e.g., minimal accessories, moderate gadgets, heavily adorned>"
mood               = "<e.g., adventurous, mysterious, industrious>"
lighting_style     = "<e.g., warm filament glow, smoky diffused light, dramatic spotlight>"

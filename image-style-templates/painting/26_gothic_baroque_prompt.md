---
id: gothic-baroque
title: Gothic / Baroque Ornamentation Style
domain: image-style-templates
type: prompt
version: 1.0.0
owner: parlau
license: MIT
tags:
  - image
  - generation
  - plain
  - painting
release_status: released
inputs:
  schema:
    subject_description:
      type: string
      required: true
      description: Description of the subject to be rendered
    ornamentation_level:
      type: string
      required: false
      description: Ornamentation Level (e.g., light tracery, moderate carvings, elaborate adornment)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., deep burgundy and gold, midnight blue and silver, dark emerald and brass)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., dramatic spotlight, candlelit, chiaroscuro)
    structural_elements:
      type: string
      required: false
      description: Structural Elements (e.g., pointed arches, gargoyles, baroque scrolls)
    mood:
      type: string
      required: false
      description: Mood (e.g., mystical, solemn, opulent)
    texture_detail:
      type: string
      required: false
      description: Texture Detail (e.g., smooth stone, rich fabrics, intricate lace)
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
# Gothic / Baroque Ornamentation Style


```
{SUBJECT_DESCRIPTION}, rendered in a Gothic or Baroque aesthetic. Frame the portrait as a square with the subject centred amid dark, opulent surroundings. Incorporate ornate architectural or decorative elements—arches, columns, intricate carvings—that evoke cathedrals or palatial interiors. Use a rich, deep colour palette accented with metallic golds or silvers. Employ dramatic lighting and strong contrasts to emphasise depth and shadow. Allow textures such as stone, velvet, or lace to show prominently. Finish with lavish detail and a mysterious or grand mood characteristic of Gothic and Baroque art.

# Config:
ornamentation_level = "<e.g., light tracery, moderate carvings, elaborate adornment>"
colour_palette      = "<e.g., deep burgundy and gold, midnight blue and silver, dark emerald and brass>"
lighting_style      = "<e.g., dramatic spotlight, candlelit, chiaroscuro>"
structural_elements = "<e.g., pointed arches, gargoyles, baroque scrolls>"
mood                = "<e.g., mystical, solemn, opulent>"
texture_detail      = "<e.g., smooth stone, rich fabrics, intricate lace>"

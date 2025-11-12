---
id: dark-fantasy
title: Dark Fantasy Illustration Style
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
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., desaturated earth tones, dark blues and purples, monochrome)
    creature_type:
      type: string
      required: false
      description: Creature Type (e.g., undead warrior, demonic beast, cursed animal)
    mood:
      type: string
      required: false
      description: Mood (e.g., foreboding, tragic, haunting)
    environment_type:
      type: string
      required: false
      description: Environment Type (e.g., ruined castle, dark forest, underground crypt)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., moonlit, firelight, dim ambient)
    gore_level:
      type: string
      required: false
      description: Gore Level (e.g., none, mild, intense)
    detail_level:
      type: string
      required: false
      description: Detail Level (e.g., simple forms, moderate detail, highly intricate)
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
# Dark Fantasy Illustration Style


```
{SUBJECT_DESCRIPTION}, reimagined within a dark fantasy setting. Design the square composition with the subject placed in a brooding, ominous environment—crumbling ruins, foggy forests, or shadowed caverns. Use a muted or desaturated colour palette with deep blacks, greys, and browns contrasted by occasional eerie glows. Incorporate sinister creatures, worn armour, or occult symbols as appropriate. Apply dramatic, low‑key lighting such as moonlight or flickering torches to heighten mood. Control the level of graphic content according to preference. Finish with a foreboding and atmospheric tone that evokes the tension and beauty of dark fantasy.

# Config:
colour_palette   = "<e.g., desaturated earth tones, dark blues and purples, monochrome>"
creature_type    = "<e.g., undead warrior, demonic beast, cursed animal>"
mood             = "<e.g., foreboding, tragic, haunting>"
environment_type = "<e.g., ruined castle, dark forest, underground crypt>"
lighting_style   = "<e.g., moonlit, firelight, dim ambient>"
gore_level       = "<e.g., none, mild, intense>"
detail_level     = "<e.g., simple forms, moderate detail, highly intricate>"

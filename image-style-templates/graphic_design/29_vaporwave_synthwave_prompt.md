---
id: vaporwave-synthwave
title: Vaporwave / Synthwave Retro Style
domain: image-style-templates
type: prompt
version: 1.0.0
owner: parlau
license: MIT
tags:
  - image
  - generation
  - plain
  - graphic-design
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
      description: Colour Palette (e.g., neon pink and teal, lavender and cyan, magenta and blue)
    background_elements:
      type: string
      required: false
      description: Background Elements (e.g., grid horizon, palm silhouettes, retro sun)
    retro_motifs:
      type: string
      required: false
      description: Retro Motifs (e.g., classical busts, VHS glitches, cassette tapes)
    texture_style:
      type: string
      required: false
      description: Texture Style (e.g., smooth gradient, VHS static, CRT scanlines)
    mood:
      type: string
      required: false
      description: Mood (e.g., nostalgic, surreal, mellow)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., soft neon glow, strong rim lighting, ambient haze)
    foreground_effects:
      type: string
      required: false
      description: Foreground Effects (e.g., lens flares, vapor trails, floating shapes)
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
# Vaporwave / Synthwave Retro Style


```
{SUBJECT_DESCRIPTION}, rendered in a vaporwave or synthwave aesthetic. Frame the image as a square with the subject centred against a backdrop of retro digital motifs. Use a vibrant colour palette dominated by neon pinks, purples, blues, and teals. Incorporate iconic elements such as sunset gradients, gridlines, palm trees, retro computer graphics, or classical statues. Apply soft glows, lens flares, and CRT‑style scanlines to evoke nostalgia. Keep compositions simple but evocative, balancing surreal atmosphere with retro futurist charm. Finish with an overall dreamy, nostalgic mood.

# Config:
colour_palette       = "<e.g., neon pink and teal, lavender and cyan, magenta and blue>"
background_elements  = "<e.g., grid horizon, palm silhouettes, retro sun>"
retro_motifs         = "<e.g., classical busts, VHS glitches, cassette tapes>"
texture_style        = "<e.g., smooth gradient, VHS static, CRT scanlines>"
mood                 = "<e.g., nostalgic, surreal, mellow>"
lighting_style       = "<e.g., soft neon glow, strong rim lighting, ambient haze>"
foreground_effects   = "<e.g., lens flares, vapor trails, floating shapes>"

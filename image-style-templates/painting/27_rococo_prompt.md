---
id: rococo
title: Rococo Elegance Style
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
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., pastel pink and gold, powder blue and cream, mint and ivory)
    ornamentation_level:
      type: string
      required: false
      description: Ornamentation Level (e.g., subtle flourishes, moderate scrollwork, lavish detailing)
    motif_theme:
      type: string
      required: false
      description: Motif Theme (e.g., florals, shells, cherubs)
    curvature_intensity:
      type: string
      required: false
      description: Curvature Intensity (e.g., gentle curves, pronounced spirals, exuberant swirls)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., soft diffused, warm daylight, gentle glow)
    mood:
      type: string
      required: false
      description: Mood (e.g., whimsical, romantic, opulent)
    background_texture:
      type: string
      required: false
      description: Background Texture (e.g., flat pastel, delicate pattern, faint damask)
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
# Rococo Elegance Style


```
{SUBJECT_DESCRIPTION}, depicted with the playful luxury of Rococo art. Compose the square image with the subject gracefully positioned and surrounded by ornate, swirling motifs like shells, florals, and garlands. Use a light, pastel colour palette with soft pinks, blues, creams, and gilded accents. Emphasise delicate curves and intricate detailing in both the subject’s attire and the environment. Incorporate whimsical elements such as cherubs or flowing ribbons if desired. Finish with gentle lighting and a refined yet lively mood that reflects the exuberance of the Rococo period.

# Config:
colour_palette       = "<e.g., pastel pink and gold, powder blue and cream, mint and ivory>"
ornamentation_level  = "<e.g., subtle flourishes, moderate scrollwork, lavish detailing>"
motif_theme         = "<e.g., florals, shells, cherubs>"
curvature_intensity = "<e.g., gentle curves, pronounced spirals, exuberant swirls>"
lighting_style      = "<e.g., soft diffused, warm daylight, gentle glow>"
mood                = "<e.g., whimsical, romantic, opulent>"
background_texture   = "<e.g., flat pastel, delicate pattern, faint damask>"

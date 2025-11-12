---
id: mosaic-stained-glass
title: Mosaic / Stained Glass Style
domain: image-style-templates
type: prompt
version: 1.0.0
owner: parlau
license: MIT
tags:
  - image
  - generation
  - plain
  - mixed-media
release_status: released
inputs:
  schema:
    subject_description:
      type: string
      required: true
      description: Description of the subject to be rendered
    material_type:
      type: string
      required: false
      description: Material Type (e.g., stained glass, ceramic tile, enamel)
    tile_size:
      type: string
      required: false
      description: Tile Size (e.g., small, medium, large)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., vivid primaries, earthy tones, jewel colours)
    pattern_complexity:
      type: string
      required: false
      description: Pattern Complexity (e.g., simple geometric, medium complexity, intricate figurative)
    transparency_level:
      type: string
      required: false
      description: Transparency Level (e.g., opaque, semi‑translucent, translucent)
    grout_colour:
      type: string
      required: false
      description: Grout Colour (e.g., dark grey, light beige, coloured grout)
    motif_type:
      type: string
      required: false
      description: Motif Type (e.g., geometric patterns, floral design, figurative scene)
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
# Mosaic / Stained Glass Style


```
{SUBJECT_DESCRIPTION}, represented as a mosaic or stained‑glass artwork. Compose the image within a square frame, constructing the subject from individual coloured tiles or pieces of glass separated by grout or lead lines. Choose a material type and tile size below to control the level of detail and texture. Use a harmonious colour palette to create patterns or figurative scenes. Allow light to interact with translucent pieces if it’s stained glass, or incorporate reflective qualities for ceramic mosaics. Finish with a deliberate arrangement of shapes and colours that evokes traditional mosaic or stained‑glass craftsmanship.

# Config:
material_type       = "<e.g., stained glass, ceramic tile, enamel>"
tile_size           = "<e.g., small, medium, large>"
colour_palette      = "<e.g., vivid primaries, earthy tones, jewel colours>"
pattern_complexity  = "<e.g., simple geometric, medium complexity, intricate figurative>"
transparency_level  = "<e.g., opaque, semi‑translucent, translucent>"
grout_colour        = "<e.g., dark grey, light beige, coloured grout>"
motif_type          = "<e.g., geometric patterns, floral design, figurative scene>"

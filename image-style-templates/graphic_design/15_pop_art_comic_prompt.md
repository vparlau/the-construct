---
id: pop-art-comic
title: Pop Art / Comic Pop Style
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
      description: Colour Palette (e.g., bright primaries, neon brights, limited duo-tone)
    pattern_type:
      type: string
      required: false
      description: Pattern Type (e.g., Ben‑Day dots, stripes, chequerboard)
    line_thickness:
      type: string
      required: false
      description: Line Thickness (e.g., thick black, medium coloured, thin accent)
    saturation_level:
      type: string
      required: false
      description: Saturation Level (e.g., vivid, standard, muted)
    iconography:
      type: string
      required: false
      description: Iconography (e.g., comic speech bubbles, pop culture icons, brand logos)
    contrast_level:
      type: string
      required: false
      description: Contrast Level (e.g., high, medium, low)
    background_pattern:
      type: string
      required: false
      description: Background Pattern (e.g., dotted field, comic burst, solid colour)
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
# Pop Art / Comic Pop Style


```
{SUBJECT_DESCRIPTION}, depicted in a pop art or comic‑pop aesthetic. Arrange the portrait as a square with the subject prominent and centered. Use bright, flat colours and bold outlines to evoke the look of mid‑20th‑century pop art. Incorporate halftone patterns, Ben‑Day dots or stripes into the fills and backgrounds as defined below. Apply minimal shading; rely on high contrast and flat shapes to convey form. Include optional text elements or graphic motifs that reference comic books or consumer culture. Finish with a playful, high‑energy composition that celebrates bold colour and graphic simplicity.

# Config:
colour_palette     = "<e.g., bright primaries, neon brights, limited duo-tone>"
pattern_type       = "<e.g., Ben‑Day dots, stripes, chequerboard>"
line_thickness     = "<e.g., thick black, medium coloured, thin accent>"
saturation_level   = "<e.g., vivid, standard, muted>"
iconography        = "<e.g., comic speech bubbles, pop culture icons, brand logos>"
contrast_level     = "<e.g., high, medium, low>"
background_pattern = "<e.g., dotted field, comic burst, solid colour>"

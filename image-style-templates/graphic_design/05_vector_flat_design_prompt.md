---
id: vector-flat-design
title: Vector / Flat Design Style
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
      description: Colour Palette (e.g., monochrome, triadic scheme, pastel set)
    line_presence:
      type: string
      required: false
      description: Line Presence (e.g., none, thin stroke, medium stroke)
    shape_style:
      type: string
      required: false
      description: Shape Style (e.g., rounded geometric, sharp angular, organic curves)
    gradient_use:
      type: string
      required: false
      description: Gradient Use (e.g., none, subtle, pronounced)
    background_style:
      type: string
      required: false
      description: Background Style (e.g., solid colour, two‑tone split, simple pattern)
    shadow_style:
      type: string
      required: false
      description: Shadow Style (e.g., none, long flat shadow, soft drop shadow)
    iconography_level:
      type: string
      required: false
      description: Iconography Level (e.g., high, medium, low)
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
# Vector / Flat Design Style


```
{SUBJECT_DESCRIPTION}, created as a clean vector or flat‑design portrait. Arrange the composition as a square with the subject centred and facing forward. Construct the figure using simple geometric shapes and smooth curves, avoiding visible brush strokes or realistic textures. Employ a limited colour palette with solid fills; use subtle gradients only when specified. Keep shading minimal—rely on flat colours and occasional soft shadows to imply depth. Choose an outline style (none or thin) that matches the modern, minimalist aesthetic. Define a background colour or basic pattern that contrasts with the subject without adding complexity. Finish with crisp, scalable rendering suitable for icons, infographics or logos.

# Config:
colour_palette     = "<e.g., monochrome, triadic scheme, pastel set>"
line_presence      = "<e.g., none, thin stroke, medium stroke>"
shape_style        = "<e.g., rounded geometric, sharp angular, organic curves>"
gradient_use       = "<e.g., none, subtle, pronounced>"
background_style   = "<e.g., solid colour, two‑tone split, simple pattern>"
shadow_style       = "<e.g., none, long flat shadow, soft drop shadow>"
iconography_level  = "<e.g., high, medium, low>"

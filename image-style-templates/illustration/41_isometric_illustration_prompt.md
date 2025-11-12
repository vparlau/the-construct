---
id: isometric-illustration
title: Isometric / 2.5D Illustration Style
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
    view_angle:
      type: string
      required: false
      description: View Angle (e.g., 30°, 45°, custom angle)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., muted pastels, vibrant synthwave tones, monochrome)
    line_presence:
      type: string
      required: false
      description: Line Presence (e.g., none, thin outlines, bold outlines)
    detail_level:
      type: string
      required: false
      description: Detail Level (e.g., simple shapes, moderate detail, intricate design)
    shading_style:
      type: string
      required: false
      description: Shading Style (e.g., flat colours, soft gradients, cel shading)
    grid_visible:
      type: string
      required: false
      description: Grid Visible (e.g., hidden, subtle, pronounced)
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
# Isometric / 2.5D Illustration Style


```
{SUBJECT_DESCRIPTION}, depicted in an isometric or 2.5D perspective. Design the square composition with the subject rendered using parallel projection, typically at a 30° or 45° angle, so there is no vanishing point. Construct forms from clean geometric shapes with consistent angles. Choose a colour palette that enhances the three‑dimensional effect while remaining cohesive. Decide on line presence and shading style below, such as flat shading or subtle gradients, to emphasise volume. Keep the grid implied or visible as desired. Finish with a tidy, structured look that evokes architectural drawings or game art.

# Config:
view_angle       = "<e.g., 30°, 45°, custom angle>"
colour_palette   = "<e.g., muted pastels, vibrant synthwave tones, monochrome>"
line_presence    = "<e.g., none, thin outlines, bold outlines>"
detail_level     = "<e.g., simple shapes, moderate detail, intricate design>"
shading_style    = "<e.g., flat colours, soft gradients, cel shading>"
grid_visible     = "<e.g., hidden, subtle, pronounced>"

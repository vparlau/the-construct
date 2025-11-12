---
id: chalkboard-chalk-art
title: Chalkboard / Chalk Art Style
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
    chalk_colour_palette:
      type: string
      required: false
      description: Chalk Colour Palette (e.g., classic white, pastel coloured chalks, vivid bright chalks)
    line_texture:
      type: string
      required: false
      description: Line Texture (e.g., clean strokes, dusty smudges, blended edges)
    background_style:
      type: string
      required: false
      description: Background Style (e.g., blackboard, coloured chalkboard, slate)
    drawing_style:
      type: string
      required: false
      description: Drawing Style (e.g., illustrative lettering, simple diagram, detailed portrait)
    smudge_level:
      type: string
      required: false
      description: Smudge Level (e.g., none, light, pronounced)
    mood:
      type: string
      required: false
      description: Mood (e.g., whimsical, educational, rustic)
    border_style:
      type: string
      required: false
      description: Border Style (e.g., none, chalk frame, decorative corners)
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
# Chalkboard / Chalk Art Style


```
{SUBJECT_DESCRIPTION}, illustrated in a chalkboard art aesthetic. Arrange the subject on a square, dark chalkboard background. Draw the figure and accompanying elements with chalk‑like lines and strokes, using white or coloured chalk to create contrast against the board. Allow visible chalk dust, smudges, and texture to enhance authenticity. Incorporate hand‑drawn lettering or decorative flourishes if appropriate. Keep shading simple, relying on hatching or thicker strokes rather than gradients. Finish with a playful, rustic, or educational mood that evokes hand‑rendered chalk art.

# Config:
chalk_colour_palette = "<e.g., classic white, pastel coloured chalks, vivid bright chalks>"
line_texture         = "<e.g., clean strokes, dusty smudges, blended edges>"
background_style     = "<e.g., blackboard, coloured chalkboard, slate>"
drawing_style        = "<e.g., illustrative lettering, simple diagram, detailed portrait>"
smudge_level         = "<e.g., none, light, pronounced>"
mood                 = "<e.g., whimsical, educational, rustic>"
border_style         = "<e.g., none, chalk frame, decorative corners>"

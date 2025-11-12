---
id: ink-and-wash
title: Ink and Wash Style
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
    ink_style:
      type: string
      required: false
      description: Ink Style (e.g., calligraphic strokes, bold outlines, fine linework)
    wash_intensity:
      type: string
      required: false
      description: Wash Intensity (e.g., light, medium, heavy)
    paper_texture:
      type: string
      required: false
      description: Paper Texture (e.g., rice paper, watercolor paper, smooth bristol)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., monochrome black, muted blues, earthy browns)
    brushstroke_fluidity:
      type: string
      required: false
      description: Brushstroke Fluidity (e.g., loose and flowing, controlled and precise, spontaneous)
    composition_balance:
      type: string
      required: false
      description: Composition Balance (e.g., asymmetric, centered, diagonal)
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
# Ink and Wash Style


```
{SUBJECT_DESCRIPTION}, executed in an ink and wash technique. Present the subject within a square composition, using expressive ink lines to define form and delicate washes to create tonal variation. Select an ink style—calligraphic, bold, or fine—and apply washes of varying intensity to suggest shading, depth, or background. Choose a limited colour palette (often monochrome or muted hues) that complements the ink work. Let the texture of the paper show through, and allow brushstrokes to bleed slightly for an organic feel. Balance positive and negative space carefully, leaving areas of the page untouched to enhance contrast. Finish with a harmonious blend of line and wash that reflects traditional East Asian or Western ink painting.

# Config:
ink_style         = "<e.g., calligraphic strokes, bold outlines, fine linework>"
wash_intensity    = "<e.g., light, medium, heavy>"
paper_texture     = "<e.g., rice paper, watercolor paper, smooth bristol>"
colour_palette    = "<e.g., monochrome black, muted blues, earthy browns>"
brushstroke_fluidity= "<e.g., loose and flowing, controlled and precise, spontaneous>"
composition_balance= "<e.g., asymmetric, centered, diagonal>"

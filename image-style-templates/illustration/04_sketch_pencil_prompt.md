---
id: sketch-pencil
title: Sketch / Pencil Style
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
    paper_texture:
      type: string
      required: false
      description: Paper Texture (e.g., smooth, rough sketchbook, aged parchment)
    line_weight:
      type: string
      required: false
      description: Line Weight (e.g., uniform, varied, light with occasional heavy accents)
    shading_density:
      type: string
      required: false
      description: Shading Density (e.g., light, moderate, heavy)
    tone:
      type: string
      required: false
      description: Tone (e.g., black and white, grayscale, warm sepia)
    background_detail:
      type: string
      required: false
      description: Background Detail (e.g., blank, light vignette, simple shapes)
    gesture_visibility:
      type: string
      required: false
      description: Gesture Visibility (e.g., none, subtle, prominent)
    border_style:
      type: string
      required: false
      description: Border Style (e.g., none, rough torn edges, clean border)
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
# Sketch / Pencil Style


```
{SUBJECT_DESCRIPTION}, drawn as a traditional pencil sketch. Compose the portrait in a square format with the subject centred and facing the viewer. Use confident, visible lines with varied weight and expressive strokes to define form. Build shading through hatching and cross‑hatching instead of smooth gradients, leaving some construction or gestural lines to enhance the sketch aesthetic. Apply the chosen tonal palette (e.g., grayscale or sepia) and optionally add subtle paper texture. Keep the background minimal—use negative space or a light vignette—to frame the subject. Avoid digital colouring; preserve the raw, hand‑drawn quality of the sketch.

# Config:
paper_texture      = "<e.g., smooth, rough sketchbook, aged parchment>"
line_weight        = "<e.g., uniform, varied, light with occasional heavy accents>"
shading_density    = "<e.g., light, moderate, heavy>"
tone               = "<e.g., black and white, grayscale, warm sepia>"
background_detail  = "<e.g., blank, light vignette, simple shapes>"
gesture_visibility= "<e.g., none, subtle, prominent>"
border_style       = "<e.g., none, rough torn edges, clean border>"

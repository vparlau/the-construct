---
id: western-cartoon-comic
title: Western Cartoon / Comic Style
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
    background_style:
      type: string
      required: false
      description: Background Style (e.g., solid primary colour, comic halftone pattern, speed lines)
    line_thickness:
      type: string
      required: false
      description: Line Thickness (e.g., thin, standard, thick)
    shading_style:
      type: string
      required: false
      description: Shading Style (e.g., none, flat cell, cross‑hatching)
    colour_scheme:
      type: string
      required: false
      description: Colour Scheme (e.g., primary colours, bright neon, muted tones)
    expression_mood:
      type: string
      required: false
      description: Expression Mood (e.g., heroic, cheerful, sarcastic)
    outline_colour:
      type: string
      required: false
      description: Outline Colour (e.g., black, dark brown, coloured lines)
    background_elements:
      type: string
      required: false
      description: Background Elements (e.g., speech bubbles, action lines, sound effects)
    texture_presence:
      type: string
      required: false
      description: Texture Presence (e.g., none, light paper grain, halftone dots)
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
# Western Cartoon / Comic Style


```
{SUBJECT_DESCRIPTION}, rendered in a Western cartoon or comic‑book portrait. Compose the image as a square with the character facing forward and centred. Use bold outlines with consistent line thickness and exaggerated features that convey personality. Colour the piece using flat or lightly gradient fills in a high‑contrast, saturated palette defined below. Apply simple shading sparingly—through flat shadows or cross‑hatching—to suggest form without photorealism. Select a background colour or pattern that complements the subject and supports the narrative. Keep textures minimal to preserve the graphic, illustrative quality. Finish with clean digital lines and colours to emulate contemporary comic art.

# Config:
background_style   = "<e.g., solid primary colour, comic halftone pattern, speed lines>"
line_thickness     = "<e.g., thin, standard, thick>"
shading_style      = "<e.g., none, flat cell, cross‑hatching>"
colour_scheme      = "<e.g., primary colours, bright neon, muted tones>"
expression_mood    = "<e.g., heroic, cheerful, sarcastic>"
outline_colour     = "<e.g., black, dark brown, coloured lines>"
background_elements= "<e.g., speech bubbles, action lines, sound effects>"
texture_presence   = "<e.g., none, light paper grain, halftone dots>"

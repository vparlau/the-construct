---
id: anime-manga
title: Anime / Manga Style
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
      description: Background Style (e.g., soft pastel, pure white, light gradient)
    line_weight:
      type: string
      required: false
      description: Line Weight (e.g., thin, medium, thick)
    shading_style:
      type: string
      required: false
      description: Shading Style (e.g., flat cell shading, soft gradient shading)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., vibrant, pastel, monochrome)
    eye_style:
      type: string
      required: false
      description: Eye Style (e.g., large sparkly, medium detailed, stylised)
    expression_mood:
      type: string
      required: false
      description: Expression Mood (e.g., happy, serious, melancholic)
    line_texture:
      type: string
      required: false
      description: Line Texture (e.g., clean digital, pencil‑like, inked)
    background_elements:
      type: string
      required: false
      description: Background Elements (e.g., none, simple shapes, abstract motifs)
    highlight_intensity:
      type: string
      required: false
      description: Highlight Intensity (e.g., subtle, medium, bright)
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
# Anime / Manga Style


```
{SUBJECT_DESCRIPTION}, illustrated in a stylised anime or manga portrait. Use a square composition with the character facing forward and centred within the frame. Draw clean, deliberate line art with controlled line weight to emphasise expressive facial features and stylised proportions (large eyes, small nose and mouth). Colour the image using the specified palette, employing flat or cell shading with subtle gradients to define volume. Keep the background simple or pastel, as defined below, to prevent distraction. Maintain smooth surfaces without realistic textures, and preserve the hand‑drawn feel. Finish with minimal post‑processing so the image retains an authentic anime aesthetic.

# Config:
background_style    = "<e.g., soft pastel, pure white, light gradient>"
line_weight         = "<e.g., thin, medium, thick>"
shading_style       = "<e.g., flat cell shading, soft gradient shading>"
colour_palette      = "<e.g., vibrant, pastel, monochrome>"
eye_style           = "<e.g., large sparkly, medium detailed, stylised>"
expression_mood     = "<e.g., happy, serious, melancholic>"
line_texture        = "<e.g., clean digital, pencil‑like, inked>"
background_elements = "<e.g., none, simple shapes, abstract motifs>"
highlight_intensity = "<e.g., subtle, medium, bright>"

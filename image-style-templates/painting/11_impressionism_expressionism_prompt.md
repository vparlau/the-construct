---
id: impressionism-expressionism
title: Impressionism / Expressionism Style
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
    brushstroke_style:
      type: string
      required: false
      description: Brushstroke Style (e.g., short dabs, broad sweeps, energetic lines)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., muted earth tones, vibrant primaries, cool pastels)
    light_quality:
      type: string
      required: false
      description: Light Quality (e.g., golden hour, overcast, artificial)
    abstraction_level:
      type: string
      required: false
      description: Abstraction Level (e.g., suggestive, moderate, high)
    texture_intensity:
      type: string
      required: false
      description: Texture Intensity (e.g., subtle, moderate, heavy)
    mood:
      type: string
      required: false
      description: Mood (e.g., serene, turbulent, joyful)
    perspective_type:
      type: string
      required: false
      description: Perspective Type (e.g., eye level, high view, low view)
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
# Impressionism / Expressionism Style


```
{SUBJECT_DESCRIPTION}, interpreted through an impressionist or expressionist lens. Compose the image as a square with the subject centred but allow loose, gestural brush strokes to capture movement and mood rather than precise detail. Use a palette of colours that evoke the chosen emotion, blending hues on the canvas to suggest light and atmosphere. Emphasise the interplay of light and shadow without sharp outlines, and allow the background to merge with the subject in places. Visible strokes and textures convey energy and emotion. Finish with an overall painterly surface that feels spontaneous and dynamic.

# Config:
brushstroke_style = "<e.g., short dabs, broad sweeps, energetic lines>"
colour_palette    = "<e.g., muted earth tones, vibrant primaries, cool pastels>"
light_quality     = "<e.g., golden hour, overcast, artificial>"
abstraction_level = "<e.g., suggestive, moderate, high>"
texture_intensity = "<e.g., subtle, moderate, heavy>"
mood              = "<e.g., serene, turbulent, joyful>"
perspective_type  = "<e.g., eye level, high view, low view>"

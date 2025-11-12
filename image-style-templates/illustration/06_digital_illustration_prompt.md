---
id: digital-illustration
title: Digital Illustration / Painterly Style
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
    brush_style:
      type: string
      required: false
      description: Brush Style (e.g., oil‑like bristles, watercolor wash, smooth airbrush)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., saturated vivid, muted earth tones, monochrome)
    texture_intensity:
      type: string
      required: false
      description: Texture Intensity (e.g., subtle, moderate, heavy)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., dramatic chiaroscuro, soft ambient, rim lighting)
    edge_softness:
      type: string
      required: false
      description: Edge Softness (e.g., sharp, medium, soft)
    background_detail:
      type: string
      required: false
      description: Background Detail (e.g., abstract brush strokes, soft gradient, simple vignette)
    stroke_visibility:
      type: string
      required: false
      description: Stroke Visibility (e.g., visible, semi‑blended, minimal)
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
# Digital Illustration / Painterly Style


```
{SUBJECT_DESCRIPTION}, portrayed as a richly rendered digital illustration. Compose the artwork as a square with the subject centred and facing forward. Use expressive digital brush strokes and layered colours to create a painterly feel, blending hues smoothly while retaining visible texture. Choose a colour palette that suits the mood and emphasise dynamic lighting to sculpt forms and convey depth. Keep the background simple or painterly, as defined below, so it supports rather than distracts from the subject. Finish with careful detailing and soft edges to achieve a cohesive, digitally painted look.

# Config:
brush_style       = "<e.g., oil‑like bristles, watercolor wash, smooth airbrush>"
colour_palette    = "<e.g., saturated vivid, muted earth tones, monochrome>"
texture_intensity = "<e.g., subtle, moderate, heavy>"
lighting_style    = "<e.g., dramatic chiaroscuro, soft ambient, rim lighting>"
edge_softness     = "<e.g., sharp, medium, soft>"
background_detail = "<e.g., abstract brush strokes, soft gradient, simple vignette>"
stroke_visibility = "<e.g., visible, semi‑blended, minimal>"

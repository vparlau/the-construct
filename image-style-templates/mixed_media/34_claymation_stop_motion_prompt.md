---
id: claymation-stop-motion
title: Claymation / Stop‑Motion Style
domain: image-style-templates
type: prompt
version: 1.0.0
owner: parlau
license: MIT
tags:
  - image
  - generation
  - plain
  - mixed-media
release_status: released
inputs:
  schema:
    subject_description:
      type: string
      required: true
      description: Description of the subject to be rendered
    material_texture:
      type: string
      required: false
      description: Material Texture (e.g., smooth clay, fingerprinted clay, mixed textures)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., bright cartoon colours, earthy natural tones, mixed)
    pose_variation:
      type: string
      required: false
      description: Pose Variation (e.g., static, mid‑action, expressive)
    background_style:
      type: string
      required: false
      description: Background Style (e.g., handmade set, coloured paper backdrop, miniature scenery)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., soft studio lighting, natural light, dramatic spotlight)
    mood:
      type: string
      required: false
      description: Mood (e.g., whimsical, eerie, playful)
    detail_level:
      type: string
      required: false
      description: Detail Level (e.g., simple forms, moderate detail, intricate sculpting)
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
# Claymation / Stop‑Motion Style


```
{SUBJECT_DESCRIPTION}, imagined as a claymation or stop‑motion figure. Compose the square image with the subject centred, sculpted from clay or similar materials. Show hand‑crafted textures, including fingerprints or tool marks, on the model’s surface. Use bold, saturated colours or natural clay tones according to the chosen palette. Pose the figure in a way that conveys character and movement. Select a handmade background or simple set appropriate to the scene. Finish with studio or natural lighting that enhances the tactile qualities, and optionally include small imperfections to reinforce the stop‑motion aesthetic.

# Config:
material_texture   = "<e.g., smooth clay, fingerprinted clay, mixed textures>"
colour_palette     = "<e.g., bright cartoon colours, earthy natural tones, mixed>"
pose_variation     = "<e.g., static, mid‑action, expressive>"
background_style   = "<e.g., handmade set, coloured paper backdrop, miniature scenery>"
lighting_style     = "<e.g., soft studio lighting, natural light, dramatic spotlight>"
mood               = "<e.g., whimsical, eerie, playful>"
detail_level       = "<e.g., simple forms, moderate detail, intricate sculpting>"

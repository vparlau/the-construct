---
id: retro-vintage-poster
title: Retro / Vintage Poster Style
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
    colour_scheme:
      type: string
      required: false
      description: Colour Scheme (e.g., muted retro palette, two‑tone vintage, faded primaries)
    texture_style:
      type: string
      required: false
      description: Texture Style (e.g., halftone dots, paper distress, canvas grain)
    font_style:
      type: string
      required: false
      description: Font Style (e.g., art deco, sans serif, script)
    layout_type:
      type: string
      required: false
      description: Layout Type (e.g., portrait layout, landscape banner, centred montage)
    border_style:
      type: string
      required: false
      description: Border Style (e.g., none, decorative frame, rough edge)
    accent_graphics:
      type: string
      required: false
      description: Accent Graphics (e.g., vintage icons, geometric shapes, sunburst)
    fading_intensity:
      type: string
      required: false
      description: Fading Intensity (e.g., subtle, moderate, heavy)
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
# Retro / Vintage Poster Style


```
{SUBJECT_DESCRIPTION}, designed as a retro or vintage poster. Compose the artwork in a square format reminiscent of mid‑century advertising or travel posters. Use bold, simplified shapes and a restrained colour palette inspired by aged inks or faded paints. Incorporate halftone dots, distressed textures, or paper grain to evoke the printing techniques of the era. Place typography and graphic elements (if applicable) strategically to balance the composition. Employ simple, flat shading and high contrast to make the subject stand out. Finish with a weathered or worn look to enhance authenticity.

# Config:
colour_scheme    = "<e.g., muted retro palette, two‑tone vintage, faded primaries>"
texture_style    = "<e.g., halftone dots, paper distress, canvas grain>"
font_style       = "<e.g., art deco, sans serif, script>"
layout_type      = "<e.g., portrait layout, landscape banner, centred montage>"
border_style     = "<e.g., none, decorative frame, rough edge>"
accent_graphics  = "<e.g., vintage icons, geometric shapes, sunburst>"
fading_intensity = "<e.g., subtle, moderate, heavy>"

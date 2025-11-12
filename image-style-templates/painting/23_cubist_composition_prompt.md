---
id: cubist-composition
title: Cubist Composition Style
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
    fragmentation_level:
      type: string
      required: false
      description: Fragmentation Level (e.g., light abstraction, moderate fragmentation, high fragmentation)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., muted earth tones, monochrome with accents, complementary colours)
    perspective_number:
      type: string
      required: false
      description: Perspective Number (e.g., two viewpoints, multiple viewpoints, shifting perspectives)
    shape_style:
      type: string
      required: false
      description: Shape Style (e.g., angular, curved facets, mixed)
    background_collage:
      type: string
      required: false
      description: Background Collage (e.g., plain, geometric patterns, newspaper clippings)
    texture_presence:
      type: string
      required: false
      description: Texture Presence (e.g., smooth, subtle texture, heavy texture)
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
# Cubist Composition Style


```
{SUBJECT_DESCRIPTION}, reinterpreted through a Cubist lens. Construct the portrait as a square composition, breaking the subject into geometric planes and facets that show multiple angles simultaneously. Use overlapping shapes and angular fragments to deconstruct forms while maintaining recognisable features. Choose a restrained colour palette—often earthy or muted—with occasional contrasting accents. Arrange the fragments in a dynamic yet balanced manner, incorporating background collage elements if desired. Finish with visible brush strokes or textured surfaces to evoke early Cubist paintings.

# Config:
fragmentation_level = "<e.g., light abstraction, moderate fragmentation, high fragmentation>"
colour_palette      = "<e.g., muted earth tones, monochrome with accents, complementary colours>"
perspective_number  = "<e.g., two viewpoints, multiple viewpoints, shifting perspectives>"
shape_style         = "<e.g., angular, curved facets, mixed>"
background_collage  = "<e.g., plain, geometric patterns, newspaper clippings>"
texture_presence    = "<e.g., smooth, subtle texture, heavy texture>"

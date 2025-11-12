---
id: graffiti-street-art
title: Graffiti / Street Art Style
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
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., neon brights, complementary primaries, monochrome)
    texture_presence:
      type: string
      required: false
      description: Texture Presence (e.g., rough brick, smooth concrete, metal wall)
    lettering_style:
      type: string
      required: false
      description: Lettering Style (e.g., wildstyle tags, stencil fonts, bubble letters)
    motif_type:
      type: string
      required: false
      description: Motif Type (e.g., abstract shapes, character portraits, calligraphic marks)
    layering_style:
      type: string
      required: false
      description: Layering Style (e.g., single layer, overlapping sprays, collage of stickers)
    mood:
      type: string
      required: false
      description: Mood (e.g., rebellious, energetic, playful)
    background_elements:
      type: string
      required: false
      description: Background Elements (e.g., city skyline hints, graffiti tags, none)
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
# Graffiti / Street Art Style


```
{SUBJECT_DESCRIPTION}, created in the bold, urban style of graffiti or street art. Compose the square image with the subject positioned prominently on an implied wall surface, using vibrant spray‑paint colours and dynamic lettering or characters. Incorporate drips, splatters, stencils, or tags to capture the raw energy of street art. Use high contrast and expressive strokes to make the image pop. Choose a textured backdrop—brick, concrete, metal—as defined below, and allow overlapping layers or collage elements for depth. Finish with a rebellious, energetic mood that reflects urban culture.

# Config:
colour_palette      = "<e.g., neon brights, complementary primaries, monochrome>"
texture_presence    = "<e.g., rough brick, smooth concrete, metal wall>"
lettering_style     = "<e.g., wildstyle tags, stencil fonts, bubble letters>"
motif_type          = "<e.g., abstract shapes, character portraits, calligraphic marks>"
layering_style      = "<e.g., single layer, overlapping sprays, collage of stickers>"
mood                = "<e.g., rebellious, energetic, playful>"
background_elements = "<e.g., city skyline hints, graffiti tags, none>"

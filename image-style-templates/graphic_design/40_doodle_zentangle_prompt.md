---
id: doodle-zentangle
title: Doodle / Zentangle Pattern Style
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
    pattern_density:
      type: string
      required: false
      description: Pattern Density (e.g., sparse, moderate, dense)
    motif_types:
      type: string
      required: false
      description: Motif Types (e.g., geometric shapes, floral patterns, abstract swirls)
    line_thickness:
      type: string
      required: false
      description: Line Thickness (e.g., fine, medium, varied)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., black and white, limited colours, rainbow)
    fill_style:
      type: string
      required: false
      description: Fill Style (e.g., simple outlines, filled patterns, negative space patterns)
    mood:
      type: string
      required: false
      description: Mood (e.g., playful, calming, chaotic)
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
# Doodle / Zentangle Pattern Style


```
{SUBJECT_DESCRIPTION}, transformed into an intricate doodle or zentangle composition. Arrange the square canvas with the subject at the centre, but fill the surrounding space—and/or the interior of the subject—with repetitive patterns, motifs, and whimsical shapes. Use flowing lines and varied motifs—geometric shapes, organic forms, and abstract patterns—as defined below. Choose a colour palette, often monochrome or limited hues, to maintain cohesion. Adjust pattern density to control visual complexity. Finish with a playful, meditative feel that showcases the art of detailed doodling.

# Config:
pattern_density   = "<e.g., sparse, moderate, dense>"
motif_types       = "<e.g., geometric shapes, floral patterns, abstract swirls>"
line_thickness    = "<e.g., fine, medium, varied>"
colour_palette    = "<e.g., black and white, limited colours, rainbow>"
fill_style        = "<e.g., simple outlines, filled patterns, negative space patterns>"
mood              = "<e.g., playful, calming, chaotic>"

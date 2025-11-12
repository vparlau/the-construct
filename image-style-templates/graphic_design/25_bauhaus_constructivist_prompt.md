---
id: bauhaus-constructivist
title: Bauhaus / Constructivist Design Style
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
    shape_composition:
      type: string
      required: false
      description: Shape Composition (e.g., rectangles and circles, angular lines, overlapping forms)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., primary triad, black and white with red accent, limited duo-tone)
    type_inclusion:
      type: string
      required: false
      description: Type Inclusion (e.g., none, minimal sans-serif text, bold typographic element)
    grid_alignment:
      type: string
      required: false
      description: Grid Alignment (e.g., strict grid, loose alignment, dynamic diagonal)
    texture_presence:
      type: string
      required: false
      description: Texture Presence (e.g., none, light paper grain, subtle halftone)
    background_style:
      type: string
      required: false
      description: Background Style (e.g., solid colour, intersecting shapes, divided fields)
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
# Bauhaus / Constructivist Design Style


```
{SUBJECT_DESCRIPTION}, executed in a Bauhaus or Constructivist design aesthetic. Present the subject in a square format using clean, geometric forms and a minimal composition. Employ simple shapes—rectangles, circles, lines—and a restricted palette dominated by primary colours (red, yellow, blue) along with black and white. Use a strong grid or aligned layout to organise elements, and integrate typography sparingly if appropriate. Avoid ornamental detail; focus on functional, abstract design. Finish with flat colours and crisp edges to achieve a modernist look.

# Config:
shape_composition  = "<e.g., rectangles and circles, angular lines, overlapping forms>"
colour_palette     = "<e.g., primary triad, black and white with red accent, limited duo-tone>"
type_inclusion     = "<e.g., none, minimal sans-serif text, bold typographic element>"
grid_alignment     = "<e.g., strict grid, loose alignment, dynamic diagonal>"
texture_presence   = "<e.g., none, light paper grain, subtle halftone>"
background_style   = "<e.g., solid colour, intersecting shapes, divided fields>"

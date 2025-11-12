---
id: watercolor-painting
title: Watercolor Painting Style
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
    brush_load:
      type: string
      required: false
      description: Brush Load (e.g., wet on wet, wet on dry, dry brush)
    pigment_intensity:
      type: string
      required: false
      description: Pigment Intensity (e.g., light, medium, saturated)
    wash_layer_count:
      type: string
      required: false
      description: Wash Layer Count (e.g., few layers, several layers, many layers)
    paper_texture:
      type: string
      required: false
      description: Paper Texture (e.g., cold press, hot press, rough)
    wetness_control:
      type: string
      required: false
      description: Wetness Control (e.g., loose blending, controlled edges, crisp shapes)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., soft pastels, vibrant primaries, earthy tones)
    outline_presence:
      type: string
      required: false
      description: Outline Presence (e.g., none, faint pencil, ink outlines)
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
# Watercolor Painting Style


```
{SUBJECT_DESCRIPTION}, rendered with transparent watercolor techniques. Compose the image as a square with the subject facing forward and centred. Use fluid washes and soft edges to build form, allowing colours to blend naturally on the paper. Layer multiple translucent washes to achieve depth, leaving white spaces for highlights. Avoid harsh outlines; suggest contours with subtle changes in tone. Choose a harmonious colour palette that suits the mood and let the texture of the paper contribute to the overall look. Finish with delicate details and controlled bleeds that capture the spontaneity of watercolor.

# Config:
brush_load         = "<e.g., wet on wet, wet on dry, dry brush>"
pigment_intensity  = "<e.g., light, medium, saturated>"
wash_layer_count   = "<e.g., few layers, several layers, many layers>"
paper_texture      = "<e.g., cold press, hot press, rough>"
wetness_control    = "<e.g., loose blending, controlled edges, crisp shapes>"
colour_palette     = "<e.g., soft pastels, vibrant primaries, earthy tones>"
outline_presence   = "<e.g., none, faint pencil, ink outlines>"

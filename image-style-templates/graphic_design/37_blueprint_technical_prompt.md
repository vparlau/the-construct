---
id: blueprint-technical
title: Blueprint / Technical Drawing Style
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
    line_colour:
      type: string
      required: false
      description: Line Colour (e.g., white, pale blue, light grey)
    background_colour:
      type: string
      required: false
      description: Background Colour (e.g., dark blue, navy, charcoal)
    scale_detail:
      type: string
      required: false
      description: Scale Detail (e.g., simplified outline, moderate detail, highly detailed)
    annotation_presence:
      type: string
      required: false
      description: Annotation Presence (e.g., none, minimal labels, full annotations)
    dimension_lines:
      type: string
      required: false
      description: Dimension Lines (e.g., hidden, selective, comprehensive)
    mood:
      type: string
      required: false
      description: Mood (e.g., industrial, futuristic, educational)
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
# Blueprint / Technical Drawing Style


```
{SUBJECT_DESCRIPTION}, presented as a blueprint or technical drawing. Frame the subject within a square canvas using precise, thin lines and schematic conventions. Use a dark or coloured background (often blue) with contrasting line work in white or light colours. Include annotations, dimension lines, and labels if needed, adhering to technical drafting standards. Choose the scale and level of detail below. Keep shading minimal; rely on line weight and hatching to convey depth. Finish with a clean, engineered aesthetic that emphasises precision and clarity.

# Config:
line_colour        = "<e.g., white, pale blue, light grey>"
background_colour  = "<e.g., dark blue, navy, charcoal>"
scale_detail       = "<e.g., simplified outline, moderate detail, highly detailed>"
annotation_presence= "<e.g., none, minimal labels, full annotations>"
dimension_lines    = "<e.g., hidden, selective, comprehensive>"
mood               = "<e.g., industrial, futuristic, educational>"

---
id: etching-engraving
title: Etching / Engraving Style
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
    line_density:
      type: string
      required: false
      description: Line Density (e.g., sparse, moderate, dense)
    shading_style:
      type: string
      required: false
      description: Shading Style (e.g., cross‑hatching, stippling, parallel lines)
    plate_tone:
      type: string
      required: false
      description: Plate Tone (e.g., black and white, sepia, coloured ink)
    border_style:
      type: string
      required: false
      description: Border Style (e.g., none, simple line, ornate frame)
    detail_level:
      type: string
      required: false
      description: Detail Level (e.g., minimal, moderate, highly intricate)
    mood:
      type: string
      required: false
      description: Mood (e.g., antique, scientific, whimsical)
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
# Etching / Engraving Style


```
{SUBJECT_DESCRIPTION}, rendered as an etching or engraved illustration. Construct the image on a square canvas using fine, precise lines and intricate cross‑hatching to build form and shading. Choose a plate tone—black and white or sepia—and let the paper texture show through. Include delicate decorative borders if desired. Control the density of lines to achieve depth and contrast. Avoid large flat areas of colour; rely on hatching and stippling instead. Finish with an antique, technical, or refined mood consistent with historical engravings.

# Config:
line_density      = "<e.g., sparse, moderate, dense>"
shading_style     = "<e.g., cross‑hatching, stippling, parallel lines>"
plate_tone        = "<e.g., black and white, sepia, coloured ink>"
border_style      = "<e.g., none, simple line, ornate frame>"
detail_level      = "<e.g., minimal, moderate, highly intricate>"
mood             = "<e.g., antique, scientific, whimsical>"

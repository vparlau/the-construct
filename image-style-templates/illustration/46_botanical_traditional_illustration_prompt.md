---
id: botanical-traditional-illustration
title: Botanical Illustration Style
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
    illustration_style:
      type: string
      required: false
      description: Illustration Style (e.g., watercolor washes, pen and ink, mixed media)
    plant_type:
      type: string
      required: false
      description: Plant Type (e.g., flowering herb, leafy fern, succulent)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., natural greens and browns, bright blooms, monochrome)
    background_type:
      type: string
      required: false
      description: Background Type (e.g., plain white, soft gradient, light parchment)
    annotation_presence:
      type: string
      required: false
      description: Annotation Presence (e.g., none, plant name, detailed labels)
    detail_level:
      type: string
      required: false
      description: Detail Level (e.g., simplified, moderate detail, highly detailed)
    mood:
      type: string
      required: false
      description: Mood (e.g., scientific, artistic, vintage)
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
# Botanical Illustration Style


```
{SUBJECT_DESCRIPTION}, illustrated in a traditional botanical style. Render the subject with scientific accuracy and aesthetic elegance on a square canvas. Use fine lines and precise shading to depict plant structures—leaves, stems, flowers—while maintaining clarity and realism. Choose an illustration medium, such as watercolor with delicate washes or pen and ink with cross‑hatching. Select a natural colour palette that reflects true plant hues. Optionally include annotations or field notes in a handwritten style. Keep backgrounds minimal or softly shaded to emphasise the specimen. Finish with a calm, informative mood that balances art and science.

# Config:
illustration_style = "<e.g., watercolor washes, pen and ink, mixed media>"
plant_type        = "<e.g., flowering herb, leafy fern, succulent>"
colour_palette    = "<e.g., natural greens and browns, bright blooms, monochrome>"
background_type   = "<e.g., plain white, soft gradient, light parchment>"
annotation_presence= "<e.g., none, plant name, detailed labels>"
detail_level      = "<e.g., simplified, moderate detail, highly detailed>"
mood              = "<e.g., scientific, artistic, vintage>"

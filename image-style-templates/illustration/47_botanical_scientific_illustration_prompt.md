---
id: botanical-scientific-illustration
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
    specimen_type:
      type: string
      required: false
      description: Specimen Type (e.g., flowering plant, succulent, fern, tree branch)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., natural greens and browns, soft pastels, monochrome pencil)
    annotation_level:
      type: string
      required: false
      description: Annotation Level (e.g., none, scientific labels, full botanical notes)
    line_style:
      type: string
      required: false
      description: Line Style (e.g., fine ink lines, pencil sketch, digital clean lines)
    background_style:
      type: string
      required: false
      description: Background Style (e.g., plain white, light wash, parchment texture)
    detail_intensity:
      type: string
      required: false
      description: Detail Intensity (e.g., moderate, high, hyper‑detailed)
    mood:
      type: string
      required: false
      description: Mood (e.g., educational, decorative, serene)
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
{SUBJECT_DESCRIPTION}, rendered as a scientific or botanical illustration. Arrange the square composition with the subject centred and clearly isolated on a neutral background. Depict plants, flowers, or botanical elements with meticulous accuracy and fine line work. Use naturalistic colours and careful shading to convey structure and texture. Include details such as roots, stems, leaves, and flowers, possibly adding annotations or labels for educational context. Keep the background minimal to highlight the specimen. Finish with a precise, elegant look that balances scientific fidelity and artistic beauty.

# Config:
specimen_type      = "<e.g., flowering plant, succulent, fern, tree branch>"
colour_palette     = "<e.g., natural greens and browns, soft pastels, monochrome pencil>"
annotation_level   = "<e.g., none, scientific labels, full botanical notes>"
line_style         = "<e.g., fine ink lines, pencil sketch, digital clean lines>"
background_style   = "<e.g., plain white, light wash, parchment texture>"
detail_intensity   = "<e.g., moderate, high, hyper‑detailed>"
mood               = "<e.g., educational, decorative, serene>"

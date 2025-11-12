---
id: medical-illustration
title: Medical Illustration Style
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
    anatomical_focus:
      type: string
      required: false
      description: Anatomical Focus (e.g., skeletal system, muscular anatomy, cellular cross‑section)
    diagram_type:
      type: string
      required: false
      description: Diagram Type (e.g., full body, cross‑section, exploded view)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., muted medical pastels, monochrome greyscale, colour‑coded)
    background_type:
      type: string
      required: false
      description: Background Type (e.g., plain white, light gradient, sterile operating room)
    annotation_style:
      type: string
      required: false
      description: Annotation Style (e.g., none, labeled parts, callouts with descriptions)
    shading_level:
      type: string
      required: false
      description: Shading Level (e.g., flat diagrams, moderate shading, fully rendered 3D)
    perspective:
      type: string
      required: false
      description: Perspective (e.g., frontal, lateral, isometric)
    mood:
      type: string
      required: false
      description: Mood (e.g., educational, clinical, illustrative)
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
# Medical Illustration Style


```
{SUBJECT_DESCRIPTION}, rendered in a medical illustration style. Depict the subject with clinical precision on a square canvas, focusing on anatomical accuracy and clear visual communication. Use crisp line work and smooth shading to reveal form and internal structures, such as muscles, organs, or cellular layers. Employ a neutral or white background to maintain focus and avoid distractions. Apply a colour scheme that enhances clarity—often subtle pastels or colour‑coded tints—and label key parts with precise typography if desired. Maintain a clean, informative composition that balances scientific detail with visual aesthetics.

# Config:
anatomical_focus   = "<e.g., skeletal system, muscular anatomy, cellular cross‑section>"
diagram_type       = "<e.g., full body, cross‑section, exploded view>"
colour_palette     = "<e.g., muted medical pastels, monochrome greyscale, colour‑coded>"
background_type    = "<e.g., plain white, light gradient, sterile operating room>"
annotation_style   = "<e.g., none, labeled parts, callouts with descriptions>"
shading_level      = "<e.g., flat diagrams, moderate shading, fully rendered 3D>"
perspective        = "<e.g., frontal, lateral, isometric>"
mood               = "<e.g., educational, clinical, illustrative>"
```
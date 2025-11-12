---
id: art-nouveau
title: Art Nouveau Illustration Style
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
    motif_theme:
      type: string
      required: false
      description: Motif Theme (e.g., florals, foliage, geometric patterns)
    line_style:
      type: string
      required: false
      description: Line Style (e.g., thin flowing, bold sweeping, intertwined)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., pastel tones, jewel hues, gold accents)
    decorative_elements:
      type: string
      required: false
      description: Decorative Elements (e.g., filigree, scrollwork, organic shapes)
    border_style:
      type: string
      required: false
      description: Border Style (e.g., ornate frame, simple arch, none)
    symmetry_level:
      type: string
      required: false
      description: Symmetry Level (e.g., highly symmetrical, moderately symmetrical, asymmetrical)
    background_texture:
      type: string
      required: false
      description: Background Texture (e.g., flat colour, subtle gradient, textured paper)
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
# Art Nouveau Illustration Style


```
{SUBJECT_DESCRIPTION}, illustrated in the flowing, decorative Art Nouveau style. Frame the portrait as a square, centring the subject and surrounding them with organic, curving lines and natural motifs. Use elegant, sinuous outlines to define forms, integrating floral patterns, vines, or other nature‑inspired elements. Choose a soft, harmonious colour palette often featuring muted pastels, creams, and golds. Incorporate ornamental borders or frames that complement the composition. Finish with intricate detailing and an overall sense of graceful movement characteristic of Art Nouveau.

# Config:
motif_theme        = "<e.g., florals, foliage, geometric patterns>"
line_style         = "<e.g., thin flowing, bold sweeping, intertwined>"
colour_palette     = "<e.g., pastel tones, jewel hues, gold accents>"
decorative_elements= "<e.g., filigree, scrollwork, organic shapes>"
border_style       = "<e.g., ornate frame, simple arch, none>"
symmetry_level     = "<e.g., highly symmetrical, moderately symmetrical, asymmetrical>"
background_texture = "<e.g., flat colour, subtle gradient, textured paper>"

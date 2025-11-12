---
id: propaganda-poster
title: Propaganda / Soviet Poster Style
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
    colour_scheme:
      type: string
      required: false
      description: Colour Scheme (e.g., red/black/white, blue/white/yellow, monochrome with accent)
    slogan_text:
      type: string
      required: false
      description: Slogan Text (e.g., optional slogan, none)
    composition_type:
      type: string
      required: false
      description: Composition Type (e.g., dynamic diagonal, symmetric centred, radiating lines)
    imagery_type:
      type: string
      required: false
      description: Imagery Type (e.g., heroic workers, industrial machinery, symbolic icons)
    font_style:
      type: string
      required: false
      description: Font Style (e.g., bold sans‑serif, constructivist type, block lettering)
    distress_level:
      type: string
      required: false
      description: Distress Level (e.g., clean modern, slightly aged, heavily distressed)
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
# Propaganda / Soviet Poster Style


```
{SUBJECT_DESCRIPTION}, designed as a vintage propaganda or Soviet poster. Compose the square image with a strong, central subject and bold geometric shapes. Utilise a restricted colour scheme dominated by powerful hues like reds, blacks, and whites—or choose another limited palette as defined below. Incorporate simple yet striking imagery such as heroic figures, industrial motifs, or symbolic objects. Add concise, impactful text or slogans in a blocky sans‑serif font if appropriate. Use diagonal compositions or radiating lines to create dynamism. Finish with clean shapes, high contrast, and a sense of urgency or unity.

# Config:
colour_scheme      = "<e.g., red/black/white, blue/white/yellow, monochrome with accent>"
slogan_text        = "<e.g., optional slogan, none>"
composition_type   = "<e.g., dynamic diagonal, symmetric centred, radiating lines>"
imagery_type       = "<e.g., heroic workers, industrial machinery, symbolic icons>"
font_style         = "<e.g., bold sans‑serif, constructivist type, block lettering>"
distress_level     = "<e.g., clean modern, slightly aged, heavily distressed>"

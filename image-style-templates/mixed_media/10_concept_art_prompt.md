---
id: concept-art
title: Concept Art / Matte Painting Style
domain: image-style-templates
type: prompt
version: 1.0.0
owner: parlau
license: MIT
tags:
  - image
  - generation
  - plain
  - mixed-media
release_status: released
inputs:
  schema:
    subject_description:
      type: string
      required: true
      description: Description of the subject to be rendered
    scene_type:
      type: string
      required: false
      description: Scene Type (e.g., character concept, landscape, architectural)
    mood:
      type: string
      required: false
      description: Mood (e.g., hopeful, ominous, mystical)
    colour_scheme:
      type: string
      required: false
      description: Colour Scheme (e.g., warm sunrise, cool twilight, desaturated ruins)
    brushwork_style:
      type: string
      required: false
      description: Brushwork Style (e.g., loose painterly, refined detailed, photobash)
    perspective_type:
      type: string
      required: false
      description: Perspective Type (e.g., eye level, aerial, worm’s eye)
    atmosphere_density:
      type: string
      required: false
      description: Atmosphere Density (e.g., clear, light haze, heavy fog)
    background_detail:
      type: string
      required: false
      description: Background Detail (e.g., minimal, detailed, abstract shapes)
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
# Concept Art / Matte Painting Style


```
{SUBJECT_DESCRIPTION}, rendered as concept art or a matte painting. Compose the piece in a square format, placing the subject prominently while leaving room for environmental context. Use dynamic perspective and atmospheric depth to establish a sense of scale. Paint with broad, expressive strokes blended with finer detailing to suggest form and texture. Choose a colour scheme that conveys the mood—dramatic, ethereal, dystopian, etc.—and apply lighting that supports the narrative. Incorporate environmental elements or abstract backgrounds as needed, defined below. Finish with layered textures and subtle atmospheric effects (haze, fog, light shafts) to evoke cinematic depth and world‑building.

# Config:
scene_type        = "<e.g., character concept, landscape, architectural>"
mood              = "<e.g., hopeful, ominous, mystical>"
colour_scheme     = "<e.g., warm sunrise, cool twilight, desaturated ruins>"
brushwork_style   = "<e.g., loose painterly, refined detailed, photobash>"
perspective_type  = "<e.g., eye level, aerial, worm’s eye>"
atmosphere_density= "<e.g., clear, light haze, heavy fog>"
background_detail = "<e.g., minimal, detailed, abstract shapes>"

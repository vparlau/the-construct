---
id: scifi-concept
title: Sci‑Fi Concept Illustration Style
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
    theme:
      type: string
      required: false
      description: Theme (e.g., distant planet, deep space exploration, advanced laboratory)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., metallic silvers and blues, alien greens and purples, cosmic gradients)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., bioluminescent glow, starlight, high‑tech beams)
    tech_level:
      type: string
      required: false
      description: Tech Level (e.g., sleek and pristine, mechanical and industrial, organic and bio‑engineered)
    mood:
      type: string
      required: false
      description: Mood (e.g., awe‑inspiring, eerie, lonely)
    environment_detail:
      type: string
      required: false
      description: Environment Detail (e.g., minimal, moderate, dense)
    perspective_type:
      type: string
      required: false
      description: Perspective Type (e.g., wide landscape, interior view, close‑up character)
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
# Sci‑Fi Concept Illustration Style


```
{SUBJECT_DESCRIPTION}, envisioned as a science‑fiction concept illustration distinct from cyberpunk. Create the square composition with the subject set against a futuristic backdrop—alien landscapes, advanced spacecraft interiors, or sprawling space stations. Use sleek, cutting‑edge designs or organic extraterrestrial forms. Choose a colour palette featuring cool metallics, cosmic hues, or luminescent accents. Apply imaginative lighting effects like bioluminescent glow, starlight, or energy beams. Incorporate advanced technology such as robots, holograms, or exosuits as defined below. Finish with a sense of wonder or isolation characteristic of sci‑fi worlds beyond Earth.

# Config:
theme              = "<e.g., distant planet, deep space exploration, advanced laboratory>"
colour_palette     = "<e.g., metallic silvers and blues, alien greens and purples, cosmic gradients>"
lighting_style     = "<e.g., bioluminescent glow, starlight, high‑tech beams>"
tech_level         = "<e.g., sleek and pristine, mechanical and industrial, organic and bio‑engineered>"
mood               = "<e.g., awe‑inspiring, eerie, lonely>"
environment_detail = "<e.g., minimal, moderate, dense>"
perspective_type   = "<e.g., wide landscape, interior view, close‑up character>"

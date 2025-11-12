---
id: futurist-dynamics
title: Futurist Dynamics Style
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
    motion_effect:
      type: string
      required: false
      description: Motion Effect (e.g., multiple exposure, motion blur, streaking lines)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., metallic greys with flashes of red, warm copper tones, cool chromes)
    subject_duplication:
      type: string
      required: false
      description: Subject Duplication (e.g., none, subtle repetition, pronounced duplication)
    perspective_type:
      type: string
      required: false
      description: Perspective Type (e.g., tilted, dynamic diagonal, straight on)
    energy_level:
      type: string
      required: false
      description: Energy Level (e.g., moderate, high, intense)
    industrial_motifs:
      type: string
      required: false
      description: Industrial Motifs (e.g., gears, machinery, abstract mechanical shapes)
    background_style:
      type: string
      required: false
      description: Background Style (e.g., simple gradient, abstract speed lines, geometric patterns)
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
# Futurist Dynamics Style


```
{SUBJECT_DESCRIPTION}, depicted in the energetic style of Futurism. Compose the square image with the subject centred but portrayed in motion—using repeated outlines, blurring, or fragmented forms to convey speed and dynamism. Incorporate mechanical or industrial motifs, such as gears or abstract shapes, to emphasise modernity and progress. Select a metallic or high‑contrast colour palette with bright highlights and deep shadows. Experiment with diagonal compositions and sweeping lines to guide the eye and suggest acceleration. Finish with rhythmic repetition and overlapping elements that capture the sensation of motion.

# Config:
motion_effect       = "<e.g., multiple exposure, motion blur, streaking lines>"
colour_palette      = "<e.g., metallic greys with flashes of red, warm copper tones, cool chromes>"
subject_duplication = "<e.g., none, subtle repetition, pronounced duplication>"
perspective_type    = "<e.g., tilted, dynamic diagonal, straight on>"
energy_level        = "<e.g., moderate, high, intense>"
industrial_motifs   = "<e.g., gears, machinery, abstract mechanical shapes>"
background_style    = "<e.g., simple gradient, abstract speed lines, geometric patterns>"

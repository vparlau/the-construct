---
id: cyberpunk-neon
title: Cyberpunk / Neon Futurism Style
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
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., neon blue & pink, electric purple & teal, mixed neon)
    lighting_effects:
      type: string
      required: false
      description: Lighting Effects (e.g., glow, reflection, volumetric light beams)
    environment_density:
      type: string
      required: false
      description: Environment Density (e.g., dense cityscape, sparse alley, minimalist set)
    tech_elements:
      type: string
      required: false
      description: Tech Elements (e.g., cybernetic implants, holographic signs, wires)
    mood:
      type: string
      required: false
      description: Mood (e.g., gritty dystopian, high‑energy vibrant, moody noir)
    perspective_type:
      type: string
      required: false
      description: Perspective Type (e.g., street‑level, elevated view, close‑up)
    atmospheric_effects:
      type: string
      required: false
      description: Atmospheric Effects (e.g., rain, fog, smoke, lens flare)
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
# Cyberpunk / Neon Futurism Style


```
{SUBJECT_DESCRIPTION}, envisioned in a cyberpunk or neon futurist setting. Compose the image as a square with the subject centred against a backdrop of glowing lights and high‑tech elements. Use a vivid, saturated colour palette dominated by neon blues, pinks, and purples, with contrasting accents. Integrate technological motifs—circuitry, holographic displays, chrome surfaces—defined below. Illuminate the scene with dramatic, multi‑coloured lighting that casts reflections and glows on the subject. Decide on the density of the environment, from dense urban alleyways to minimalist neon spaces. Add atmospheric effects like rain, fog, or lens flares to heighten the futuristic mood. Finish with a polished look that balances grit and gloss.

# Config:
colour_palette      = "<e.g., neon blue & pink, electric purple & teal, mixed neon>"
lighting_effects    = "<e.g., glow, reflection, volumetric light beams>"
environment_density= "<e.g., dense cityscape, sparse alley, minimalist set>"
tech_elements       = "<e.g., cybernetic implants, holographic signs, wires>"
mood                = "<e.g., gritty dystopian, high‑energy vibrant, moody noir>"
perspective_type    = "<e.g., street‑level, elevated view, close‑up>"
atmospheric_effects= "<e.g., rain, fog, smoke, lens flare>"

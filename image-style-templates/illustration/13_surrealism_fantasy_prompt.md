---
id: surrealism-fantasy
title: Surrealism / Fantasy Realism Style
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
    surreal_elements:
      type: string
      required: false
      description: Surreal Elements (e.g., levitating objects, melting forms, hybrid animals)
    realism_level:
      type: string
      required: false
      description: Realism Level (e.g., semi‑realistic, hyper‑realistic)
    mood:
      type: string
      required: false
      description: Mood (e.g., whimsical, eerie, epic)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., jewel tones, muted darks, neon contrasts)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., soft ethereal, high‑contrast dramatic, coloured lights)
    distortion_level:
      type: string
      required: false
      description: Distortion Level (e.g., subtle, moderate, extreme)
    background_detail:
      type: string
      required: false
      description: Background Detail (e.g., minimal, dreamlike landscape, abstract patterns)
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
# Surrealism / Fantasy Realism Style


```
{SUBJECT_DESCRIPTION}, transformed into a surreal or fantastical scene. Use a square composition, centering the main subject while integrating unexpected, dreamlike elements around them. Render the subject and key objects with a high degree of realism, but juxtapose them with imaginative or impossible features—floating objects, unusual scales, or hybrid creatures—defined below. Choose a colour palette and lighting scheme that enhance the otherworldly mood. Manipulate perspective and proportions subtly to disorient the viewer while keeping the overall scene coherent. Finish with meticulous detail and atmospheric effects to blend the real and the fantastical seamlessly.

# Config:
surreal_elements   = "<e.g., levitating objects, melting forms, hybrid animals>"
realism_level      = "<e.g., semi‑realistic, hyper‑realistic>"
mood               = "<e.g., whimsical, eerie, epic>"
colour_palette     = "<e.g., jewel tones, muted darks, neon contrasts>"
lighting_style     = "<e.g., soft ethereal, high‑contrast dramatic, coloured lights>"
distortion_level   = "<e.g., subtle, moderate, extreme>"
background_detail  = "<e.g., minimal, dreamlike landscape, abstract patterns>"

---
id: collage-mixed-media
title: Collage / Mixed Media Style
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
    material_sources:
      type: string
      required: false
      description: Material Sources (e.g., photographs, magazine clippings, fabric textures)
    texture_styles:
      type: string
      required: false
      description: Texture Styles (e.g., paper grain, paint splatter, fabric weave)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., eclectic vibrant, muted vintage, monochrome)
    composition_style:
      type: string
      required: false
      description: Composition Style (e.g., chaotic collage, organised layout, radial burst)
    layering_opacity:
      type: string
      required: false
      description: Layering Opacity (e.g., high contrast, medium overlay, translucent)
    border_style:
      type: string
      required: false
      description: Border Style (e.g., clean edges, torn paper, irregular shapes)
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
# Collage / Mixed Media Style


```
{SUBJECT_DESCRIPTION}, assembled as a collage or mixed‑media artwork. Use a square composition, layering photographic fragments, drawn elements, and textured materials to form the image. Combine different media sources—magazine cut‑outs, fabric swatches, hand‑drawn sketches—defined below, blending or juxtaposing them to create an eclectic yet coherent piece. Employ varying opacities and overlapping shapes to build depth. Choose a colour palette that ties disparate pieces together. Allow edges to remain torn or irregular if desired, and integrate background textures that enhance the sense of handcrafted assembly. Finish with a cohesive arrangement that balances chaos and harmony.

# Config:
material_sources  = "<e.g., photographs, magazine clippings, fabric textures>"
texture_styles    = "<e.g., paper grain, paint splatter, fabric weave>"
colour_palette    = "<e.g., eclectic vibrant, muted vintage, monochrome>"
composition_style= "<e.g., chaotic collage, organised layout, radial burst>"
layering_opacity  = "<e.g., high contrast, medium overlay, translucent>"
border_style      = "<e.g., clean edges, torn paper, irregular shapes>"

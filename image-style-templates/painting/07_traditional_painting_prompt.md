---
id: traditional-painting
title: Traditional Painting Style (Oil / Watercolor)
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
    painting_medium:
      type: string
      required: false
      description: Painting Medium (e.g., oil, watercolor)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., classical warm tones, cool impressionist hues, muted pastels)
    brushwork_detail:
      type: string
      required: false
      description: Brushwork Detail (e.g., loose expressive, controlled detailed, blended)
    texture_detail:
      type: string
      required: false
      description: Texture Detail (e.g., subtle canvas weave, pronounced brush strokes, smooth washes)
    lighting_style:
      type: string
      required: false
      description: Lighting Style (e.g., soft natural, dramatic studio, diffused daylight)
    background_style:
      type: string
      required: false
      description: Background Style (e.g., abstract colour fields, muted gradients, impressionistic shapes)
    varnish_finish:
      type: string
      required: false
      description: Varnish Finish (e.g., matte, semi‑gloss, gloss)
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
# Traditional Painting Style (Oil / Watercolor)


```
{SUBJECT_DESCRIPTION}, rendered as a traditional painting. Arrange the composition as a square with the subject centred, capturing the essence of classic media. Choose the painting medium below (oil or watercolor), then apply appropriate techniques: thick, textured brush strokes and rich, layered pigments for oils; or transparent washes and delicate bleeding edges for watercolor. Select a colour palette that reflects the chosen medium’s character, and employ traditional lighting to model form. Allow the texture of canvas or paper to show through where appropriate. Keep the background simple or impressionistic so it complements the subject. Finish with visible brushwork and authentic surface textures to evoke the feel of hand‑painted art.

# Config:
painting_medium   = "<oil, watercolor>"
colour_palette    = "<e.g., classical warm tones, cool impressionist hues, muted pastels>"
brushwork_detail  = "<e.g., loose expressive, controlled detailed, blended>"
texture_detail    = "<e.g., subtle canvas weave, pronounced brush strokes, smooth washes>"
lighting_style    = "<e.g., soft natural, dramatic studio, diffused daylight>"
background_style  = "<e.g., abstract colour fields, muted gradients, impressionistic shapes>"
varnish_finish    = "<e.g., matte, semi‑gloss, gloss>"

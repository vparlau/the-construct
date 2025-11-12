---
id: fashion-illustration
title: Fashion Illustration Style
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
    fashion_style:
      type: string
      required: false
      description: Fashion Style (e.g., haute couture, streetwear, avant‑garde)
    figure_silhouette:
      type: string
      required: false
      description: Figure Silhouette (e.g., elongated, stylised, realistic)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., neutral monochrome, vibrant jewel tones, pastel wash)
    background_type:
      type: string
      required: false
      description: Background Type (e.g., plain white, soft gradient, abstract pattern)
    fabric_texture:
      type: string
      required: false
      description: Fabric Texture (e.g., smooth silk, rough denim, glossy leather)
    pose_energy:
      type: string
      required: false
      description: Pose Energy (e.g., static, graceful movement, high drama)
    detail_level:
      type: string
      required: false
      description: Detail Level (e.g., simplified shapes, moderate detail, intricate embellishment)
    mood:
      type: string
      required: false
      description: Mood (e.g., elegant, edgy, playful)
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
# Fashion Illustration Style


```
{SUBJECT_DESCRIPTION}, depicted as a fashion illustration. Compose the subject on a square canvas, focusing on fluid lines and dynamic poses that emphasise garment shape and movement. Use elongated proportions and stylised figures to showcase clothing design rather than anatomical realism. Select a background that is minimal or lightly textured, keeping attention on the outfit. Choose a colour palette that complements the fashion theme—whether it’s bold haute couture hues or soft pastels—and apply textures to suggest fabric types like silk, denim, or leather. Add expressive brush strokes or line accents to capture motion and drape. Maintain a polished yet artistic mood suited to editorial or runway presentation.

# Config:
fashion_style    = "<e.g., haute couture, streetwear, avant‑garde>"
figure_silhouette= "<e.g., elongated, stylised, realistic>"
colour_palette   = "<e.g., neutral monochrome, vibrant jewel tones, pastel wash>"
background_type  = "<e.g., plain white, soft gradient, abstract pattern>"
fabric_texture   = "<e.g., smooth silk, rough denim, glossy leather>"
pose_energy      = "<e.g., static, graceful movement, high drama>"
detail_level     = "<e.g., simplified shapes, moderate detail, intricate embellishment>"
mood             = "<e.g., elegant, edgy, playful>"
```
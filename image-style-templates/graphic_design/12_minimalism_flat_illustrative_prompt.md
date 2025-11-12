---
id: minimalism-flat-illustrative
title: Minimalism / Flat Illustrative Style
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
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., monochrome, complementary duo, pastel trio)
    shape_style:
      type: string
      required: false
      description: Shape Style (e.g., geometric, organic, mixed)
    line_presence:
      type: string
      required: false
      description: Line Presence (e.g., none, thin outlines, bold outlines)
    negative_space_ratio:
      type: string
      required: false
      description: Negative Space Ratio (e.g., low, moderate, high)
    texture_presence:
      type: string
      required: false
      description: Texture Presence (e.g., none, subtle grain, light paper texture)
    accent_colour:
      type: string
      required: false
      description: Accent Colour (e.g., none, small highlight colour, contrasting pop)
    composition_balance:
      type: string
      required: false
      description: Composition Balance (e.g., symmetric, asymmetric, centred)
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
# Minimalism / Flat Illustrative Style


```
{SUBJECT_DESCRIPTION}, depicted using a minimalist, flat‑illustration approach. Compose the scene as a square with ample negative space, positioning the subject simply and clearly. Construct forms from basic shapes and clean lines, removing unnecessary detail. Use a limited colour palette with harmonious hues and few shades. Avoid gradients or textures unless specified; rely instead on flat areas of colour to define shapes. Maintain a calm, balanced composition with attention to proportions and spacing. Finish with a crisp, modern look that communicates the essence of the subject through minimal elements.

# Config:
colour_palette       = "<e.g., monochrome, complementary duo, pastel trio>"
shape_style          = "<e.g., geometric, organic, mixed>"
line_presence        = "<e.g., none, thin outlines, bold outlines>"
negative_space_ratio = "<e.g., low, moderate, high>"
texture_presence     = "<e.g., none, subtle grain, light paper texture>"
accent_colour        = "<e.g., none, small highlight colour, contrasting pop>"
composition_balance  = "<e.g., symmetric, asymmetric, centred>"

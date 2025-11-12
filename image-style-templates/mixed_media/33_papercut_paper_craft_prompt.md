---
id: papercut-paper-craft
title: Papercut / Paper Craft Style
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
    layer_count:
      type: string
      required: false
      description: Layer Count (e.g., two layers, three to five layers, many layers)
    edge_style:
      type: string
      required: false
      description: Edge Style (e.g., clean cut, torn, deckled)
    colour_palette:
      type: string
      required: false
      description: Colour Palette (e.g., monochrome shades, complementary colours, varied hues)
    shadow_depth:
      type: string
      required: false
      description: Shadow Depth (e.g., none, subtle, pronounced)
    paper_texture:
      type: string
      required: false
      description: Paper Texture (e.g., smooth cardstock, fibrous handmade, metallic sheen)
    shape_style:
      type: string
      required: false
      description: Shape Style (e.g., geometric, organic, mixed)
    composition_density:
      type: string
      required: false
      description: Composition Density (e.g., minimal, moderate, elaborate)
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
# Papercut / Paper Craft Style


```
{SUBJECT_DESCRIPTION}, crafted as a layered papercut artwork. Design the square composition by cutting shapes from coloured paper and stacking them to form the subject and background. Specify the number of layers and edge treatment below. Use a limited palette for cohesion, with contrasting hues to distinguish different layers. Cast subtle shadows between layers to create depth and dimension. Choose the paper texture that influences the final look. Finish with clean or torn edges and a balanced arrangement that highlights the handcrafted nature of paper craft.

# Config:
layer_count       = "<e.g., two layers, three to five layers, many layers>"
edge_style        = "<e.g., clean cut, torn, deckled>"
colour_palette    = "<e.g., monochrome shades, complementary colours, varied hues>"
shadow_depth      = "<e.g., none, subtle, pronounced>"
paper_texture     = "<e.g., smooth cardstock, fibrous handmade, metallic sheen>"
shape_style       = "<e.g., geometric, organic, mixed>"
composition_density= "<e.g., minimal, moderate, elaborate>"

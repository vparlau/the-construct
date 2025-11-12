# Usage Guide — Image Style Templates

This guide explains how to use image generation prompt templates effectively to create high-quality images with consistent style.

---

## 1) Find and select a template

1. Open the domain **[INDEX.md](./INDEX.md)** to browse available styles by category.
2. Each category (photography, illustration, painting, etc.) contains related style templates.
3. Select a template that matches your desired visual aesthetic and output style.

## 2) Read the front-matter

At the top of each template file, you'll find YAML front-matter that describes:

- **Inputs (`inputs.schema`)** — Required and optional parameters:
  - `subject_description` (required): Description of what you want to generate
  - Additional config parameters (optional): Style-specific settings like lighting, colors, backgrounds
- **Output expectations** — Format is `plain` (a text prompt ready for image generation models)
- **Tags** — Help identify the style category and characteristics
- **Constraints** — Guidelines for best results

## 3) Prepare your inputs

### Required input
- **`subject_description`**: Provide a clear, concise description of your subject. Be specific about:
  - What the subject is (person, object, scene, etc.)
  - Key visual characteristics
  - Any important details you want included

### Optional config parameters
Each template includes optional style parameters (like `colour_palette`, `lighting_style`, `background_style`, etc.). These enhance the result when provided:

- Review the `inputs.schema` section to see all available parameters
- Use the example values as guidance (e.g., "warm vibrant, neutral muted, cool pastel" for colour_palette)
- You can omit optional parameters if you want the template to use defaults

## 4) Generate the prompt

1. **Replace placeholders**: In the template, replace `{SUBJECT_DESCRIPTION}` with your actual subject description.
2. **Fill config values**: Replace the example values in the `# Config:` section with your chosen parameters, or remove lines for parameters you're not using.
3. **Copy the complete prompt**: The entire text block (from the opening backticks to the closing backticks) becomes your image generation prompt.

## 5) Use with image generation models

- Copy the generated prompt into your image generation tool (DALL·E, Midjourney, Stable Diffusion, etc.)
- The prompts are designed for square format (1:1 aspect ratio)
- Adjust model-specific parameters (resolution, steps, etc.) as needed for your tool

## 6) Best practices

### Subject descriptions
- Be specific but concise
- Include important visual details (clothing, expression, pose, etc.)
- Avoid overly complex descriptions that might confuse the model

### Style parameters
- Start with minimal config parameters, then add more to refine
- Use the example values as inspiration but feel free to customize
- Some parameters work better together (e.g., matching colour_palette with lighting_style)

### Iteration
- Generate a first version with basic parameters
- Refine by adjusting specific config values
- Try different templates for the same subject to compare styles

## 7) Troubleshooting

- **Output doesn't match style?** Check that you've included all relevant config parameters and that values match the template's examples.
- **Subject not appearing correctly?** Ensure your `subject_description` is clear and specific.
- **Style too strong or too weak?** Adjust the detail_level, intensity, or other control parameters if available.
- **Composition issues?** All templates assume square format; adjust aspect ratio in your image generation tool if needed.

---

## Category overview

- **Photography**: Realistic photographic styles (studio, noir, neon noir)
- **Illustration**: Artistic illustration styles (anime, cartoon, fantasy, botanical, etc.)
- **Painting**: Traditional and artistic painting styles (oil, watercolor, impressionism, etc.)
- **3D**: Three-dimensional rendering styles (CGI, low-poly, sculpture)
- **Pixel**: Retro pixel art styles
- **Graphic Design**: Design-focused styles (vector, poster art, typography)
- **Mixed Media**: Combined techniques (concept art, collage, cyberpunk, etc.)

Each category's README.md provides more details about the styles included.


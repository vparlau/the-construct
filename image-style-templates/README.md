# Image Style Templates

A catalog of image generation prompt templates organized by visual style categories. Each template provides a structured prompt format with configurable style parameters for consistent, high-quality image generation.

---

## What this domain contains

This domain provides **51 prompt templates** for image generation, organized into **8 style categories**:

- **Photography** — Realistic photographic styles (studio portraits, noir, neon noir)
- **Illustration** — Artistic illustration styles (anime, cartoon, fantasy, botanical, fashion, medical, children's book)
- **Painting** — Traditional and artistic painting styles (oil, watercolor, impressionism, cubist, gothic, rococo)
- **3D** — Three-dimensional rendering styles (CGI, low-poly geometric, sculpture/relief)
- **Pixel** — Retro pixel art styles (8-bit, 16-bit)
- **Graphic Design** — Design-focused styles (vector/flat, minimalism, poster art, typography, street art, technical)
- **Mixed Media** — Combined techniques (concept art, collage, cyberpunk, mosaic, papercut, claymation)

---

## Quick start

1. Open **[INDEX.md](./INDEX.md)** to browse templates by category
2. Select a template that matches your desired style
3. Read the template's **YAML front-matter** to understand inputs and parameters
4. Follow the **[USAGE-GUIDE.md](./USAGE-GUIDE.md)** for detailed instructions
5. Replace `{SUBJECT_DESCRIPTION}` and configure style parameters
6. Use the generated prompt with your image generation tool

---

## Structure

### Categories (not subdomains)

The subdirectories (`photography/`, `illustration/`, `painting/`, etc.) are **style categories** within this domain, not separate domains. They organize templates by visual style for easier navigation.

Each category contains:
- Template files (`*_prompt.md`)
- A `README.md` explaining the category and included styles

### Template format

Each template file includes:
- **YAML front-matter**: Metadata, input schema, tags, safety guidelines
- **Prompt template**: A structured prompt with `{SUBJECT_DESCRIPTION}` placeholder
- **Config section**: Optional style parameters with example values

---

## Template metadata

All templates follow the repository's front-matter schema:
- **Required input**: `subject_description` (what to generate)
- **Optional inputs**: Style-specific parameters (lighting, colors, backgrounds, etc.)
- **Output format**: Plain text prompt ready for image generation models
- **Tags**: Categorization (image, generation, style category, plain)
- **Safety**: PII rejection and content guidelines

---

## Usage

See **[USAGE-GUIDE.md](./USAGE-GUIDE.md)** for:
- How to select and use templates
- Best practices for subject descriptions
- Configuring style parameters
- Troubleshooting common issues

---

## Updates

See **[CHANGELOG.md](./CHANGELOG.md)** for version history and changes.

---

## Related

- Global repository documentation: **[../README.md](../README.md)**
- Repository usage guide: **[../USAGE-GUIDE.md](../USAGE-GUIDE.md)**
- Start here: **[../START-HERE.md](../START-HERE.md)**

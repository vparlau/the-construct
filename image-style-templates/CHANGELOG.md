# Changelog — Image Style Templates

All notable changes to the image-style-templates domain are documented here.

---

## [Unreleased]

## [2025-01-XX] — Initial release

### Added
- 51 image generation prompt templates organized across 8 style categories:
  - **Photography** (3 templates): Realistic photographic, noir/chiaroscuro, neon noir
  - **Illustration** (13 templates): Anime/manga, cartoon, sketch, digital illustration, fantasy styles, botanical, fashion, medical, children's book
  - **Painting** (8 templates): Traditional painting, impressionism, watercolor, ink wash, cubist, futurist, gothic/baroque, rococo
  - **3D** (3 templates): 3D render/CGI, low-poly geometric, carved sculpture/relief
  - **Pixel** (1 template): Pixel art/8-bit/16-bit
  - **Graphic Design** (13 templates): Vector/flat design, minimalism, retro/vintage poster, pop art, Bauhaus, vaporwave, graffiti, chalkboard, propaganda poster, blueprint, woodcut, etching, doodle/zentangle, glitch
  - **Mixed Media** (6 templates): Concept art, collage, cyberpunk/neon, mosaic/stained glass, papercut, claymation/stop motion
- YAML front-matter added to all templates with standardized metadata:
  - Input schema definitions (required `subject_description` + optional style parameters)
  - Tags for categorization and search
  - Safety guidelines and constraints
  - Output format specifications
- Domain-level documentation:
  - `INDEX.md`: Complete catalog of all templates organized by category
  - `USAGE-GUIDE.md`: Comprehensive guide for using templates effectively
  - `README.md`: Domain overview (to be populated)
  - Category README files explaining each style category

### Structure
- Templates organized into subdirectories by style category (not subdomains)
- Each template follows consistent format: YAML front-matter + prompt template with config section
- All templates designed for square format (1:1 aspect ratio) image generation

---

## Format

This changelog follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) principles.

### Change types
- **Added**: New templates or features
- **Changed**: Modifications to existing templates
- **Deprecated**: Templates marked for removal
- **Removed**: Deleted templates
- **Fixed**: Bug fixes or corrections
- **Security**: Security-related updates


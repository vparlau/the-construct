# Changelog

All notable changes to this repository are documented here. This file summarizes **root‑level** updates and links to domain‑specific changelogs for detail.

## [Unreleased]

## [2025-01-XX] — Image Style Templates domain registration and standardization

### Added
- Registered `image-style-templates` domain in global `INDEX.md`
- Added YAML front-matter to all 51 prompt templates with standardized metadata:
  - Input schemas (required `subject_description` + optional style parameters)
  - Tags for categorization
  - Safety guidelines and constraints
  - Output format specifications
- Created domain-level documentation:
  - `image-style-templates/README.md`: Domain overview
  - `image-style-templates/USAGE-GUIDE.md`: Comprehensive usage guide
  - `image-style-templates/CHANGELOG.md`: Domain changelog

### Changed
- Updated `README.md` to clarify that subdirectories within domains are organizational categories, not separate domains
- Updated `ops/REPO-CONTEXT.md` to document categories vs subdomains distinction

### Details
See [`image-style-templates/CHANGELOG.md`](./image-style-templates/CHANGELOG.md) for complete domain changelog.

## [2025-11-12] — Repository initialization
### Added
- Root files: `README.md`, `INDEX.md`, `USAGE-GUIDE.md`, `LICENSE`, `DISCLAIMER.md`, `CHANGELOG.md`.
- Established minimal domain layout and cross‑references to `ops/` internals.

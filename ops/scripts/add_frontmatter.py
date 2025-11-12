#!/usr/bin/env python3
"""
Helper script to add YAML front-matter to prompt files.
This script reads prompt files and adds standardized front-matter based on the schema.
"""

import os
import re
from pathlib import Path

def extract_config_params(content):
    """Extract config parameters from the Config section."""
    config_section = re.search(r'# Config:\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if not config_section:
        return []
    
    params = []
    for line in config_section.group(1).strip().split('\n'):
        match = re.match(r'(\w+)\s*=\s*"<.*?>"', line)
        if match:
            param_name = match.group(1)
            # Extract example from the line
            example_match = re.search(r'<(.+?)>', line)
            example = example_match.group(1) if example_match else ""
            params.append((param_name, example))
    return params

def generate_id(filename):
    """Generate ID from filename."""
    # Remove number prefix, _prompt.md suffix, convert underscores to hyphens
    base = filename.replace('_prompt.md', '').replace('.md', '')
    # Remove leading numbers and underscores
    base = re.sub(r'^\d+_?', '', base)
    return base.replace('_', '-')

def get_category_tags(category_dir):
    """Get tags based on category directory."""
    category = category_dir.name
    base_tags = ['image', 'generation', 'plain']
    
    category_tag_map = {
        'photography': ['photography'],
        'illustration': ['illustration'],
        'painting': ['painting'],
        '3d': ['3d'],
        'pixel': ['pixel', 'retro'],
        'graphic_design': ['graphic-design'],
        'mixed_media': ['mixed-media'],
    }
    
    tags = base_tags + category_tag_map.get(category, [category.replace('_', '-')])
    return tags

def generate_frontmatter(filepath, title, config_params, category_dir):
    """Generate YAML front-matter string."""
    filename = filepath.name
    file_id = generate_id(filename)
    tags = get_category_tags(category_dir)
    
    # Build inputs schema
    inputs_schema = {
        'subject_description': {
            'type': 'string',
            'required': True,
            'description': 'Description of the subject to be rendered'
        }
    }
    
    for param_name, example in config_params:
        inputs_schema[param_name] = {
            'type': 'string',
            'required': False,
            'description': f"{param_name.replace('_', ' ').title()} (e.g., {example})" if example else f"{param_name.replace('_', ' ').title()}"
        }
    
    # Format inputs schema as YAML
    inputs_yaml = "  schema:\n"
    for param_name, param_def in inputs_schema.items():
        inputs_yaml += f"    {param_name}:\n"
        inputs_yaml += f"      type: {param_def['type']}\n"
        inputs_yaml += f"      required: {str(param_def['required']).lower()}\n"
        inputs_yaml += f"      description: {param_def['description']}\n"
    
    frontmatter = f"""---
id: {file_id}
title: {title}
domain: image-style-templates
type: prompt
version: 1.0.0
owner: parlau
license: MIT
tags:
"""
    for tag in tags:
        frontmatter += f"  - {tag}\n"
    
    frontmatter += f"""release_status: released
inputs:
{inputs_yaml}output_expectations:
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
"""
    return frontmatter

def process_file(filepath):
    """Process a single prompt file to add front-matter."""
    content = filepath.read_text(encoding='utf-8')
    
    # Check if front-matter already exists
    if content.startswith('---'):
        print(f"Skipping {filepath.name} - already has front-matter")
        return False
    
    # Extract title
    title_match = re.match(r'^# (.+?)\n', content)
    if not title_match:
        print(f"Warning: Could not extract title from {filepath.name}")
        return False
    
    title = title_match.group(1)
    
    # Extract config parameters
    config_params = extract_config_params(content)
    
    # Get category directory
    category_dir = filepath.parent
    
    # Generate front-matter
    frontmatter = generate_frontmatter(filepath, title, config_params, category_dir)
    
    # Insert front-matter after title
    new_content = re.sub(r'^(# .+?\n)', r'\1\n' + frontmatter, content, count=1)
    
    # Write back
    filepath.write_text(new_content, encoding='utf-8')
    print(f"Added front-matter to {filepath.name}")
    return True

def main():
    """Main function to process all prompt files."""
    base_dir = Path('/Users/parlau/Documents/projects/the-construct/image-style-templates')
    
    prompt_files = list(base_dir.rglob('*_prompt.md'))
    
    print(f"Found {len(prompt_files)} prompt files")
    
    processed = 0
    skipped = 0
    
    for filepath in sorted(prompt_files):
        if process_file(filepath):
            processed += 1
        else:
            skipped += 1
    
    print(f"\nProcessed: {processed}, Skipped: {skipped}")

if __name__ == '__main__':
    main()


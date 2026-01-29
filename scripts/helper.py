#!/usr/bin/env python3
"""
Helper utilities for managing Claude Skills.

This module provides functions to:
- Validate skill metadata
- Extract frontmatter from skills
- Generate skill catalogs
- Check skill quality
"""

import os
import re
import yaml
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime


class SkillValidator:
    """Validates Claude Skills for compliance with standards."""
    
    REQUIRED_FIELDS = ['name', 'version', 'description']
    NAME_PATTERN = r'^[a-z0-9]+(-[a-z0-9]+)*$'
    VERSION_PATTERN = r'^\d+\.\d+\.\d+$'
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize validator with optional config."""
        self.config = self._load_config(config_path)
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from file or use defaults."""
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
        return {
            'validation': {
                'require_frontmatter': True,
                'required_fields': self.REQUIRED_FIELDS,
                'naming_pattern': self.NAME_PATTERN,
                'version_pattern': self.VERSION_PATTERN
            }
        }
    
    def validate_skill(self, skill_path: str) -> Dict[str, Any]:
        """
        Validate a skill file.
        
        Args:
            skill_path: Path to the SKILL.md file
            
        Returns:
            Dict with 'valid' boolean and 'errors' list
        """
        errors = []
        
        if not os.path.exists(skill_path):
            return {'valid': False, 'errors': ['File does not exist']}
        
        # Read file content
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract and validate frontmatter
        frontmatter = self.extract_frontmatter(content)
        if not frontmatter:
            if self.config['validation']['require_frontmatter']:
                errors.append('Missing YAML frontmatter')
            return {'valid': False, 'errors': errors}
        
        # Validate required fields
        for field in self.config['validation']['required_fields']:
            if field not in frontmatter:
                errors.append(f'Missing required field: {field}')
        
        # Validate name format
        if 'name' in frontmatter:
            pattern = self.config['validation']['naming_pattern']
            if not re.match(pattern, frontmatter['name']):
                errors.append(f'Invalid name format. Must match: {pattern}')
        
        # Validate version format
        if 'version' in frontmatter:
            pattern = self.config['validation']['version_pattern']
            if not re.match(pattern, frontmatter['version']):
                errors.append(f'Invalid version format. Must match: {pattern}')
        
        # Validate content sections
        content_errors = self._validate_content(content)
        errors.extend(content_errors)
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'metadata': frontmatter
        }
    
    def extract_frontmatter(self, content: str) -> Optional[Dict[str, Any]]:
        """Extract YAML frontmatter from skill content."""
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    
    def _validate_content(self, content: str) -> List[str]:
        """Validate skill content structure."""
        errors = []
        
        # Check for essential sections
        required_sections = ['Overview', 'Instructions', 'Examples']
        for section in required_sections:
            pattern = rf'^##\s+{section}'
            if not re.search(pattern, content, re.MULTILINE):
                errors.append(f'Missing required section: {section}')
        
        return errors


class SkillCatalog:
    """Generate and manage skill catalogs."""
    
    def __init__(self, skills_dir: str):
        """Initialize catalog with skills directory."""
        self.skills_dir = Path(skills_dir)
    
    def generate_catalog(self, output_format: str = 'markdown') -> str:
        """
        Generate a catalog of all skills.
        
        Args:
            output_format: 'markdown', 'json', or 'yaml'
            
        Returns:
            Formatted catalog string
        """
        skills = self._discover_skills()
        
        if output_format == 'json':
            return json.dumps(skills, indent=2)
        elif output_format == 'yaml':
            return yaml.dump(skills, default_flow_style=False)
        else:  # markdown
            return self._format_markdown_catalog(skills)
    
    def _discover_skills(self) -> List[Dict[str, Any]]:
        """Discover all skills in the skills directory."""
        skills = []
        validator = SkillValidator()
        
        for skill_file in self.skills_dir.rglob('SKILL.md'):
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = validator.extract_frontmatter(content)
            if metadata:
                metadata['path'] = str(skill_file.relative_to(self.skills_dir))
                skills.append(metadata)
        
        return sorted(skills, key=lambda x: x.get('name', ''))
    
    def _format_markdown_catalog(self, skills: List[Dict[str, Any]]) -> str:
        """Format skills as markdown catalog."""
        lines = ['# Skills Catalog\n']
        lines.append(f'Generated: {datetime.now().isoformat()}\n')
        lines.append(f'Total Skills: {len(skills)}\n')
        
        # Group by category
        by_category = {}
        for skill in skills:
            category = skill.get('category', 'uncategorized')
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(skill)
        
        for category in sorted(by_category.keys()):
            lines.append(f'\n## {category.title()}\n')
            
            for skill in by_category[category]:
                name = skill.get('name', 'Unknown')
                version = skill.get('version', '0.0.0')
                description = skill.get('description', 'No description')
                path = skill.get('path', '')
                tags = ', '.join(skill.get('tags', []))
                
                lines.append(f'### {name} (v{version})\n')
                lines.append(f'{description}\n')
                lines.append(f'**Tags:** {tags}  \n')
                lines.append(f'**Path:** `{path}`\n')
        
        return '\n'.join(lines)


def validate_skill_file(skill_path: str, config_path: Optional[str] = None) -> None:
    """
    Validate a skill file and print results.
    
    Args:
        skill_path: Path to SKILL.md file
        config_path: Optional path to config.json
    """
    validator = SkillValidator(config_path)
    result = validator.validate_skill(skill_path)
    
    if result['valid']:
        print(f'✓ {skill_path} is valid')
        if 'metadata' in result:
            print(f"  Name: {result['metadata'].get('name')}")
            print(f"  Version: {result['metadata'].get('version')}")
    else:
        print(f'✗ {skill_path} has errors:')
        for error in result['errors']:
            print(f'  - {error}')


def generate_catalog(skills_dir: str, output_format: str = 'markdown') -> None:
    """
    Generate and print skills catalog.
    
    Args:
        skills_dir: Directory containing skills
        output_format: Output format (markdown, json, yaml)
    """
    catalog = SkillCatalog(skills_dir)
    output = catalog.generate_catalog(output_format)
    print(output)


def create_skill_template(
    name: str,
    output_dir: str,
    author: str = '',
    category: str = 'utility'
) -> None:
    """
    Create a new skill from template.
    
    Args:
        name: Skill name (kebab-case)
        output_dir: Directory to create skill in
        author: Author name
        category: Skill category
    """
    # Validate name
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name):
        print(f'Error: Invalid skill name. Use lowercase with hyphens.')
        return
    
    # Create skill directory
    skill_dir = Path(output_dir) / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    # Create SKILL.md from template
    skill_file = skill_dir / 'SKILL.md'
    
    template = f"""---
name: {name}
version: 1.0.0
description: Brief description of {name}
author: {author}
tags: [tag1, tag2, tag3]
category: {category}
license: MIT
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
---

# {name.replace('-', ' ').title()}

## Overview

Brief overview of what this skill does.

## When to Use

- Condition 1
- Condition 2
- Condition 3

## Instructions

### Step 1: [Action Name]

Description of step 1.

### Step 2: [Action Name]

Description of step 2.

### Step 3: [Action Name]

Description of step 3.

## Examples

### Example 1: Basic Usage

**Input:**
```
Example input
```

**Output:**
```
Example output
```

## Best Practices

1. Practice 1
2. Practice 2
3. Practice 3

## Error Handling

- Error Type 1: How to handle
- Error Type 2: How to handle

## Notes

Additional notes and considerations.
"""
    
    with open(skill_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f'✓ Created skill: {skill_file}')
    print(f'  Edit the file to customize your skill.')


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print('Usage:')
        print('  python helper.py validate <skill-path> [config-path]')
        print('  python helper.py catalog <skills-dir> [format]')
        print('  python helper.py create <name> <output-dir> [author] [category]')
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'validate':
        skill_path = sys.argv[2]
        config_path = sys.argv[3] if len(sys.argv) > 3 else None
        validate_skill_file(skill_path, config_path)
    
    elif command == 'catalog':
        skills_dir = sys.argv[2]
        output_format = sys.argv[3] if len(sys.argv) > 3 else 'markdown'
        generate_catalog(skills_dir, output_format)
    
    elif command == 'create':
        if len(sys.argv) < 4:
            print('Error: create requires <name> and <output-dir>')
            sys.exit(1)
        name = sys.argv[2]
        output_dir = sys.argv[3]
        author = sys.argv[4] if len(sys.argv) > 4 else ''
        category = sys.argv[5] if len(sys.argv) > 5 else 'utility'
        create_skill_template(name, output_dir, author, category)
    
    else:
        print(f'Unknown command: {command}')
        sys.exit(1)

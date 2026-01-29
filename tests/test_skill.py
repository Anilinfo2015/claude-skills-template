#!/usr/bin/env python3
"""
Tests for Claude Skills helper utilities.
"""

import unittest
import tempfile
import os
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from helper import SkillValidator, SkillCatalog


class TestSkillValidator(unittest.TestCase):
    """Test cases for SkillValidator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.validator = SkillValidator()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_extract_frontmatter_valid(self):
        """Test extracting valid YAML frontmatter."""
        content = """---
name: test-skill
version: 1.0.0
description: Test skill
---

# Test Skill
"""
        frontmatter = self.validator.extract_frontmatter(content)
        
        self.assertIsNotNone(frontmatter)
        self.assertEqual(frontmatter['name'], 'test-skill')
        self.assertEqual(frontmatter['version'], '1.0.0')
        self.assertEqual(frontmatter['description'], 'Test skill')
    
    def test_extract_frontmatter_missing(self):
        """Test handling missing frontmatter."""
        content = "# Test Skill\n\nNo frontmatter here."
        frontmatter = self.validator.extract_frontmatter(content)
        
        self.assertIsNone(frontmatter)
    
    def test_validate_skill_valid(self):
        """Test validating a valid skill file."""
        skill_content = """---
name: test-skill
version: 1.0.0
description: Test skill for validation
author: Test Author
tags: [test, example]
---

# Test Skill

## Overview

This is a test skill.

## Instructions

### Step 1: Do something

Do the thing.

## Examples

### Example 1: Basic

Input: test
Output: result
"""
        skill_path = os.path.join(self.temp_dir, 'SKILL.md')
        with open(skill_path, 'w') as f:
            f.write(skill_content)
        
        result = self.validator.validate_skill(skill_path)
        
        self.assertTrue(result['valid'])
        self.assertEqual(len(result['errors']), 0)
    
    def test_validate_skill_missing_required_field(self):
        """Test validation fails for missing required fields."""
        skill_content = """---
name: test-skill
version: 1.0.0
---

# Test Skill
"""
        skill_path = os.path.join(self.temp_dir, 'SKILL.md')
        with open(skill_path, 'w') as f:
            f.write(skill_content)
        
        result = self.validator.validate_skill(skill_path)
        
        self.assertFalse(result['valid'])
        self.assertTrue(any('description' in err for err in result['errors']))
    
    def test_validate_skill_invalid_name(self):
        """Test validation fails for invalid name format."""
        skill_content = """---
name: Test_Skill_123
version: 1.0.0
description: Test skill
---

# Test Skill
"""
        skill_path = os.path.join(self.temp_dir, 'SKILL.md')
        with open(skill_path, 'w') as f:
            f.write(skill_content)
        
        result = self.validator.validate_skill(skill_path)
        
        self.assertFalse(result['valid'])
        self.assertTrue(any('name format' in err.lower() for err in result['errors']))
    
    def test_validate_skill_invalid_version(self):
        """Test validation fails for invalid version format."""
        skill_content = """---
name: test-skill
version: 1.0
description: Test skill
---

# Test Skill
"""
        skill_path = os.path.join(self.temp_dir, 'SKILL.md')
        with open(skill_path, 'w') as f:
            f.write(skill_content)
        
        result = self.validator.validate_skill(skill_path)
        
        self.assertFalse(result['valid'])
        self.assertTrue(any('version format' in err.lower() for err in result['errors']))


class TestSkillCatalog(unittest.TestCase):
    """Test cases for SkillCatalog class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.catalog = SkillCatalog(self.temp_dir)
    
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_discover_skills_empty(self):
        """Test discovering skills in empty directory."""
        skills = self.catalog._discover_skills()
        
        self.assertEqual(len(skills), 0)
    
    def test_discover_skills_with_skills(self):
        """Test discovering skills in directory with skill files."""
        # Create test skill
        skill_dir = os.path.join(self.temp_dir, 'test-skill')
        os.makedirs(skill_dir)
        
        skill_content = """---
name: test-skill
version: 1.0.0
description: Test skill
category: test
tags: [test]
---

# Test Skill
"""
        with open(os.path.join(skill_dir, 'SKILL.md'), 'w') as f:
            f.write(skill_content)
        
        skills = self.catalog._discover_skills()
        
        self.assertEqual(len(skills), 1)
        self.assertEqual(skills[0]['name'], 'test-skill')
        self.assertEqual(skills[0]['version'], '1.0.0')
    
    def test_generate_catalog_markdown(self):
        """Test generating catalog in markdown format."""
        # Create test skill
        skill_dir = os.path.join(self.temp_dir, 'test-skill')
        os.makedirs(skill_dir)
        
        skill_content = """---
name: test-skill
version: 1.0.0
description: Test skill
category: development
tags: [test, example]
---

# Test Skill
"""
        with open(os.path.join(skill_dir, 'SKILL.md'), 'w') as f:
            f.write(skill_content)
        
        catalog = self.catalog.generate_catalog('markdown')
        
        self.assertIn('Skills Catalog', catalog)
        self.assertIn('test-skill', catalog)
        self.assertIn('v1.0.0', catalog)
        self.assertIn('Development', catalog)
    
    def test_generate_catalog_json(self):
        """Test generating catalog in JSON format."""
        # Create test skill
        skill_dir = os.path.join(self.temp_dir, 'test-skill')
        os.makedirs(skill_dir)
        
        skill_content = """---
name: test-skill
version: 1.0.0
description: Test skill
---

# Test Skill
"""
        with open(os.path.join(skill_dir, 'SKILL.md'), 'w') as f:
            f.write(skill_content)
        
        catalog = self.catalog.generate_catalog('json')
        
        import json
        data = json.loads(catalog)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'test-skill')


if __name__ == '__main__':
    unittest.main()

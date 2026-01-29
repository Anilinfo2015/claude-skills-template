#!/bin/bash
# Validate Claude Skills for compliance with standards
# Usage: ./validate.sh [skill-path]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
TOTAL=0
PASSED=0
FAILED=0

# Validate a single skill file
validate_skill() {
    local skill_file="$1"
    TOTAL=$((TOTAL + 1))
    
    echo "Validating: $skill_file"
    
    # Check file exists
    if [ ! -f "$skill_file" ]; then
        echo -e "${RED}✗ File does not exist${NC}"
        FAILED=$((FAILED + 1))
        return 1
    fi
    
    # Check for YAML frontmatter
    if ! grep -q "^---" "$skill_file"; then
        echo -e "${RED}✗ Missing YAML frontmatter${NC}"
        FAILED=$((FAILED + 1))
        return 1
    fi
    
    # Extract frontmatter
    local frontmatter=$(awk '/^---$/{i++}i==1' "$skill_file" | tail -n +2 | head -n -1)
    
    # Check required fields
    local required_fields=("name:" "version:" "description:")
    local missing_fields=()
    
    for field in "${required_fields[@]}"; do
        if ! echo "$frontmatter" | grep -q "^$field"; then
            missing_fields+=("$field")
        fi
    done
    
    if [ ${#missing_fields[@]} -gt 0 ]; then
        echo -e "${RED}✗ Missing required fields: ${missing_fields[*]}${NC}"
        FAILED=$((FAILED + 1))
        return 1
    fi
    
    # Validate name format (lowercase with hyphens)
    local name=$(echo "$frontmatter" | grep "^name:" | sed 's/name: *//' | tr -d '"' | tr -d "'")
    if ! echo "$name" | grep -qE '^[a-z0-9]+(-[a-z0-9]+)*$'; then
        echo -e "${RED}✗ Invalid name format: $name (use lowercase with hyphens)${NC}"
        FAILED=$((FAILED + 1))
        return 1
    fi
    
    # Validate version format (semantic versioning)
    local version=$(echo "$frontmatter" | grep "^version:" | sed 's/version: *//' | tr -d '"' | tr -d "'")
    if ! echo "$version" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
        echo -e "${RED}✗ Invalid version format: $version (use semver: X.Y.Z)${NC}"
        FAILED=$((FAILED + 1))
        return 1
    fi
    
    # Check for essential sections
    local sections=("Overview" "Instructions" "Examples")
    local missing_sections=()
    
    for section in "${sections[@]}"; do
        if ! grep -qE "^##\s+$section" "$skill_file"; then
            missing_sections+=("$section")
        fi
    done
    
    if [ ${#missing_sections[@]} -gt 0 ]; then
        echo -e "${YELLOW}⚠ Missing recommended sections: ${missing_sections[*]}${NC}"
    fi
    
    # Check for hardcoded secrets (basic check)
    if grep -qiE '(password|secret|api[_-]?key|token)\s*[:=]\s*["\x27][^"\x27]{8,}["\x27]' "$skill_file"; then
        echo -e "${RED}✗ Possible hardcoded secrets detected${NC}"
        FAILED=$((FAILED + 1))
        return 1
    fi
    
    echo -e "${GREEN}✓ Valid${NC}"
    PASSED=$((PASSED + 1))
    return 0
}

# Main execution
main() {
    echo "Claude Skills Validator"
    echo "======================="
    echo ""
    
    if [ $# -eq 0 ]; then
        # No arguments - validate all SKILL.md files in current directory
        echo "Searching for SKILL.md files..."
        
        # Find all SKILL.md files
        while IFS= read -r -d '' file; do
            validate_skill "$file"
            echo ""
        done < <(find . -name "SKILL.md" -type f -print0)
        
        if [ $TOTAL -eq 0 ]; then
            echo "No SKILL.md files found"
            exit 0
        fi
    else
        # Validate specified file(s)
        for skill_file in "$@"; do
            validate_skill "$skill_file"
            echo ""
        done
    fi
    
    # Print summary
    echo "======================="
    echo "Summary:"
    echo "  Total: $TOTAL"
    echo -e "  ${GREEN}Passed: $PASSED${NC}"
    echo -e "  ${RED}Failed: $FAILED${NC}"
    
    # Exit with error if any failed
    if [ $FAILED -gt 0 ]; then
        exit 1
    fi
    
    exit 0
}

# Run main function
main "$@"

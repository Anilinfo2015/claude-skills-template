# Assets Directory

This directory contains assets used in Claude Skills, such as:

- Diagrams and flowcharts
- Images and screenshots
- Icons and logos
- Templates and samples
- Configuration files

## Organization

Assets should be organized by skill or purpose:

```
assets/
├── images/
│   ├── skill-name/
│   │   ├── diagram1.png
│   │   └── screenshot1.png
│   └── common/
│       └── logo.png
├── diagrams/
│   └── architecture/
│       └── flow.mermaid
└── templates/
    └── config-samples/
        └── example.json
```

## Usage

Reference assets in skills using relative paths:

```markdown
![Architecture Diagram](../../assets/diagrams/architecture/flow.png)
```

## File Formats

Recommended formats:
- **Images**: PNG (preferred), JPEG, SVG
- **Diagrams**: Mermaid, PlantUML, draw.io
- **Documents**: Markdown, PDF
- **Data**: JSON, YAML, CSV

## Naming Conventions

- Use lowercase with hyphens: `user-flow-diagram.png`
- Be descriptive: `api-authentication-sequence.png`
- Include version if needed: `config-v2.json`

## Size Considerations

- Keep images under 1MB when possible
- Optimize images for web use
- Use appropriate resolution (72-150 DPI for screens)
- Consider using external hosting for very large files

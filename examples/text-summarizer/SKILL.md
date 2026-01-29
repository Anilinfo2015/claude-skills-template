---
name: text-summarizer
version: 1.0.0
description: Summarize text to specified length while preserving key information
author: Claude Skills Template
tags: [text-processing, summarization, utility, content]
category: utility
license: MIT
created: 2024-01-01
updated: 2024-01-01
maturity: stable
complexity: low
estimated_time: "2-5 minutes"
---

# Text Summarizer

## Overview

Condense text documents, articles, or content to a specified length while preserving the main ideas, key points, and essential information. The summarization maintains the original tone and intent while removing unnecessary details.

## When to Use

Use this skill when you need to:
- Reduce lengthy documents to digestible summaries
- Create executive summaries for reports
- Generate abstracts for articles or papers
- Extract key points from meeting notes or transcripts
- Condense research findings
- Create TL;DR (Too Long; Didn't Read) versions

## Instructions

### Step 1: Read and Understand Content

Thoroughly read the input text to identify:
- **Main topic or thesis**: The central argument or subject
- **Key supporting points**: 3-5 major ideas that support the main topic
- **Critical data or findings**: Important numbers, conclusions, or results
- **Overall structure**: How the content is organized
- **Tone and intent**: The author's style and purpose

### Step 2: Determine Summary Length

Confirm the desired summary length based on use case:

**Brief (2-3 sentences)**
- Use case: Quick overview, email summary, social media post
- Length: 40-60 words
- Focus: Main point and one supporting detail

**Standard (1 paragraph, 4-6 sentences)**
- Use case: Executive summary, abstract, overview
- Length: 100-150 words
- Focus: Main point, 2-3 supporting ideas, key conclusion

**Extended (2-3 paragraphs)**
- Use case: Detailed summary, comprehensive overview
- Length: 200-300 words
- Focus: Main thesis, major supporting points, methodology (if applicable), conclusions

**Custom**
- Specify word count or percentage of original (e.g., "25% of original length")

### Step 3: Identify Information to Preserve

Prioritize inclusion of:
1. Main thesis or central argument (must include)
2. Key findings or conclusions (must include)
3. Supporting evidence for main points (include if space)
4. Context or background (include if essential)
5. Methodology or approach (include if relevant)

### Step 4: Identify Information to Exclude

Remove:
- Redundant explanations
- Minor details and examples
- Tangential information
- Lengthy quotations (paraphrase instead)
- Excessive attribution or citations
- Flowery or repetitive language

### Step 5: Write the Summary

Create summary following these guidelines:

**Opening sentence:**
- State the main topic or thesis immediately
- Should be clear and self-contained
- Sets context for what follows

**Body:**
- Present key points in logical order
- Use clear, concise language
- Maintain objectivity (don't add opinions)
- Preserve author's original meaning
- Use transitions to connect ideas

**Conclusion (if length allows):**
- Reinforce main point or state significance
- Provide closure

**Style guidelines:**
- Use active voice when possible
- Eliminate unnecessary words
- Prefer simple over complex sentences
- Maintain professional tone
- Avoid jargon unless from original text

### Step 6: Review and Refine

Check that the summary:
- ✓ Accurately represents the original content
- ✓ Preserves key information
- ✓ Meets specified length requirements
- ✓ Is grammatically correct and clear
- ✓ Can stand alone without the original
- ✓ Maintains the original tone and intent

If too long: Remove less critical details, combine sentences, use more concise phrasing
If too short: Add next most important detail or expand key points slightly

## Examples

### Example 1: Brief Summary (Article)

**Input (500 words):**
```
[Long article about the impact of climate change on coastal cities, discussing rising sea levels, 
increased storm intensity, economic implications, case studies from Miami and Venice, proposed 
solutions including sea walls and urban planning changes, cost-benefit analyses, political 
challenges, and timeline projections through 2050]
```

**Brief Summary (50 words):**
```
Climate change poses severe threats to coastal cities through rising sea levels and intensified 
storms. Cities like Miami and Venice face billions in potential damage. Proposed solutions include 
sea walls and revised urban planning, though implementation faces significant political and 
economic challenges requiring immediate action.
```

### Example 2: Standard Summary (Research Paper)

**Input (3000 words):**
```
[Research paper on machine learning applications in medical diagnosis, including literature review, 
methodology using convolutional neural networks, dataset of 10,000 medical images, training process, 
results showing 94% accuracy in detecting early-stage disease, comparison with human doctors, 
limitations, ethical considerations, and future research directions]
```

**Standard Summary (125 words):**
```
This study investigates machine learning applications for medical diagnosis using convolutional 
neural networks. Researchers trained models on 10,000 medical images to detect early-stage disease. 
The system achieved 94% accuracy, matching or exceeding human doctor performance in controlled 
settings.

The methodology employed a deep learning architecture with multiple convolutional layers, trained 
on diverse patient demographics to ensure generalizability. Results demonstrate significant 
potential for AI-assisted diagnosis, particularly in resource-limited settings.

However, limitations include dataset bias, need for larger training sets, and ethical concerns 
about AI decision-making in healthcare. The authors recommend human oversight and suggest future 
research should focus on explainable AI to help doctors understand the model's diagnostic reasoning.
```

### Example 3: Extended Summary (Technical Documentation)

**Input (5000 words):**
```
[Comprehensive API documentation covering authentication, endpoints, request/response formats, 
rate limiting, error codes, webhooks, security best practices, versioning, migration guide, 
code examples in multiple languages, and troubleshooting]
```

**Extended Summary (275 words):**
```
This API documentation provides comprehensive guidance for developers integrating with the platform. 
The REST API uses OAuth 2.0 authentication with token-based access control, supporting both client 
credentials and authorization code flows.

Core endpoints include user management, data operations, and analytics. All requests require HTTPS 
and return JSON responses following a consistent structure with status codes, data payload, and 
error details when applicable. The API implements rate limiting at 1000 requests per hour for 
standard accounts and 10,000 for premium accounts.

Authentication requires obtaining an access token via the /oauth/token endpoint. Tokens expire 
after one hour but can be refreshed without re-authentication. All authenticated requests must 
include the token in the Authorization header as a Bearer token.

The API provides webhooks for real-time event notifications, supporting events like user creation, 
data updates, and system alerts. Webhook endpoints must respond within 5 seconds and use HTTPS. 
Failed deliveries retry with exponential backoff up to 24 hours.

Security best practices include using environment variables for credentials, implementing request 
signing for sensitive operations, and validating webhook signatures to prevent spoofing. The API 
follows semantic versioning with backwards compatibility maintained within major versions.

Error responses use standard HTTP status codes (400 for client errors, 500 for server errors) with 
detailed error messages including error codes and remediation suggestions. Common issues and 
solutions are documented in the troubleshooting section.

Code examples demonstrate integration in Python, JavaScript, and Java, showing authentication, 
basic CRUD operations, and webhook handling. A migration guide helps developers transition from 
version 1.x to 2.0.
```

### Example 4: Meeting Notes Summary

**Input (800 words):**
```
[Meeting transcript discussing Q3 goals, budget allocation, hiring plans, product roadmap changes, 
customer feedback review, action items for each team member, scheduling next meeting, and casual 
conversation]
```

**Standard Summary (100 words):**
```
The Q3 planning meeting focused on three key areas: budget allocation, hiring, and product roadmap. 
The team approved a $50K budget increase for marketing and agreed to hire two engineers by month's 
end. Product roadmap changes include prioritizing mobile app development over desktop features 
based on customer feedback showing 70% mobile usage.

Action items: Sarah to finalize job postings by Friday, Mike to create mobile development timeline, 
Jennifer to present budget details to executive team. Next meeting scheduled for July 15 to review 
progress on hiring and initial mobile development plans.
```

## Best Practices

1. **Stay Objective**: Don't add your own opinions or interpretations
2. **Preserve Meaning**: Ensure the summary accurately represents the original
3. **Use Original Language**: When possible, use key terms from the source
4. **Maintain Proportion**: Give more space to ideas that had more space in original
5. **Be Self-Contained**: Summary should make sense without reading the original
6. **Check Accuracy**: Verify facts, numbers, and conclusions
7. **Respect Context**: Maintain cultural, technical, or domain-specific context

## Common Mistakes to Avoid

❌ **Adding new information** not in the original
❌ **Misrepresenting** the author's position or findings
❌ **Using quotations** without attribution
❌ **Including minor details** while omitting major points
❌ **Copying sentences verbatim** (unless brief quotations)
❌ **Changing the tone** (serious to casual, or vice versa)
❌ **Making it too vague** to be useful

## Error Handling

### Content Too Short to Summarize
- **Issue**: Original is already brief (< 100 words)
- **Solution**: Return original with minimal edits or explain it doesn't need summarizing

### Highly Technical Content
- **Issue**: Specialized jargon or complex concepts
- **Solution**: Preserve essential technical terms with brief context; don't oversimplify to point of inaccuracy

### Multiple Main Topics
- **Issue**: Content covers several unrelated topics
- **Solution**: Briefly cover each topic or focus on the primary topic if one dominates

### Unclear Original Content
- **Issue**: Source material is poorly written or ambiguous
- **Solution**: Summarize what's clear and note any ambiguities

## Performance Tips

For very long documents:
1. Read introduction and conclusion first
2. Skim middle sections for main points
3. Use headers/subheaders as guides
4. Focus on topic sentences of paragraphs
5. Note bolded or emphasized content

## Limitations

- Cannot add information not present in original
- May lose nuance in very brief summaries
- Complex arguments may be oversimplified
- Cultural or contextual subtleties may be reduced
- Does not replace reading the full document when detailed understanding needed

## Related Skills

- **Document Reviewer**: For evaluating document quality before summarizing
- **Text Analyzer**: For deeper content analysis
- **Content Transformer**: For adapting content to different formats

## Version History

- **1.0.0** (2024-01-01): Initial release

## Notes

- The goal is accurate representation, not creative rewriting
- When in doubt, err on the side of including rather than excluding important information
- For academic or professional use, verify summary meets specific style requirements (APA, MLA, etc.)
- Consider the audience when choosing summary length and technical level

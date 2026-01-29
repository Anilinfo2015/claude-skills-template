# Text Summarizer - Additional Examples

More examples demonstrating different summarization scenarios and techniques.

## Example 5: News Article Summary

**Input (600 words - Breaking News):**
```
A major technology company announced today the launch of its latest quantum computing platform, 
representing a significant breakthrough in the field. The system, unveiled at the annual tech 
conference in San Francisco, features 1000 qubits and can perform calculations previously 
thought impossible with current technology.

[Content continues with technical details, expert quotes, market implications, competitor responses, 
timeline, and analysis of impact on various industries including pharmaceuticals, finance, and 
cryptography]
```

**Brief Summary (News Headline + Lede, 40 words):**
```
Major tech company unveils 1000-qubit quantum computer, marking significant industry breakthrough. 
The new platform enables previously impossible calculations, with potential applications in drug 
discovery, financial modeling, and cryptography. Industry experts call it a "transformative moment."
```

## Example 6: Academic Abstract

**Input (4000 words - Journal Article):**
```
[Research paper on the effects of intermittent fasting on metabolic health, including introduction, 
literature review of 50+ studies, methodology with 200 participants over 12 months, control groups, 
statistical analysis, results showing improvements in insulin sensitivity and weight loss, discussion 
of mechanisms, limitations, and implications for clinical practice]
```

**Standard Academic Abstract (150 words):**
```
**Background:** Intermittent fasting (IF) has gained attention as a potential metabolic health 
intervention, but long-term effects remain understudied.

**Methods:** This 12-month randomized controlled trial examined 200 adults (BMI 25-35) assigned to 
either IF (16:8 protocol) or control groups. Primary outcomes measured insulin sensitivity, weight 
change, and metabolic markers.

**Results:** IF participants demonstrated significant improvements in insulin sensitivity (p<0.001) 
and achieved average weight loss of 7.2% compared to 1.1% in controls. Fasting glucose levels 
decreased by 12% (p<0.01). Adherence remained high (84%) throughout the study period.

**Conclusions:** Time-restricted eating shows promise as a sustainable intervention for improving 
metabolic health. Results suggest beneficial effects extend beyond simple caloric restriction, 
possibly through enhanced circadian rhythm alignment and metabolic switching mechanisms.

**Keywords:** intermittent fasting, metabolic health, insulin sensitivity, weight loss, time-restricted eating
```

## Example 7: Business Report Summary

**Input (2000 words - Quarterly Report):**
```
[Detailed Q2 financial report including revenue breakdown by product line, regional performance, 
operating expenses, profit margins, customer acquisition costs, market share changes, new product 
launches, competitive landscape, challenges faced, opportunities identified, and Q3 projections]
```

**Executive Summary (200 words):**
```
**Q2 Performance Highlights**

Revenue reached $45M, up 23% YoY, driven by strong performance in enterprise software (32% growth) 
and cloud services (28% growth). Consumer products remained flat due to increased market competition.

**Regional Performance**
- North America: $28M (62% of revenue), +18% YoY
- Europe: $12M (27% of revenue), +35% YoY  
- Asia Pacific: $5M (11% of revenue), +42% YoY

**Key Metrics**
- Gross margin improved to 68% from 64% in Q1
- Customer acquisition cost decreased 15% through improved marketing efficiency
- Churn rate reduced from 5.2% to 3.8%
- Net Promoter Score increased to 72 from 68

**Challenges**
Supply chain disruptions impacted hardware product delivery, resulting in $2M delayed revenue. 
Increased competition in consumer segment requires strategic repositioning.

**Q3 Outlook**
Projected revenue of $48-52M based on strong pipeline ($85M) and two major product launches scheduled. 
Focus on expanding European operations and addressing supply chain vulnerabilities.

**Strategic Initiatives**
- Launch AI-powered features in September
- Expand sales team by 20%
- Invest $5M in infrastructure improvements
```

## Example 8: Technical Documentation Summary

**Input (1500 words - Feature Documentation):**
```
[Detailed documentation of a new authentication system including architecture, implementation details, 
configuration options, API endpoints, security considerations, migration instructions, testing 
procedures, troubleshooting, and code examples]
```

**Implementation Summary (150 words):**
```
The new OAuth 2.0 authentication system replaces the legacy token-based auth, providing enhanced 
security and standard protocol compliance. Implementation requires three main steps:

1. **Update Dependencies**: Add oauth2-client library v3.2+ and remove legacy-auth module
2. **Configuration**: Set client ID, secret, and authorization server URL in application config
3. **Code Migration**: Replace AuthService calls with OAuth2Client; existing session management 
   remains unchanged

Breaking changes include removal of /auth/token endpoint (replaced by /oauth/authorize) and modified 
token format (JWT instead of opaque tokens). All existing user sessions will remain valid during 
transition period.

Testing requires updating auth test fixtures and adding OAuth flow tests. Migration can be phased 
per environment with feature flags. Complete migration guide with code examples available in 
docs/oauth-migration.md.

Rollback plan: Feature flag allows instant reversion to legacy auth if issues arise.
```

## Example 9: Code Review Comments Summary

**Input (Mixed comments from 15 reviewers):**
```
[Various comments on a pull request including suggestions for refactoring, questions about 
implementation choices, notes on potential bugs, style feedback, performance concerns, test 
coverage suggestions, documentation requests, and approval comments]
```

**Summary for Author (125 words):**
```
**Action Required:**

**Critical Issues (Must Fix):**
1. Null pointer exception in UserService.updateProfile() (line 145) - 3 reviewers noted
2. SQL injection vulnerability in search query (line 203) - security concern

**Important Suggestions (Should Address):**
1. Extract validation logic to separate class for reusability (4 reviewers)
2. Add integration tests for new payment flow (2 reviewers)
3. Update API documentation to reflect new endpoints

**Optional Improvements:**
1. Consider using Optional<> instead of null returns
2. Minor: Rename variable "temp" to more descriptive name (line 87)

**Positive Feedback:**
- Good error handling implementation (3 reviewers)
- Clear commit messages and PR description
- Well-structured code organization

**Status:** 2 approvals pending above fixes, 1 approval with minor comments
```

## Example 10: Email Thread Summary

**Input (12 emails back and forth):**
```
[Email chain discussing project timeline, resource allocation, scope changes, budget concerns, 
stakeholder feedback, technical constraints, and attempts to reach consensus on delivery date]
```

**Thread Summary (100 words):**
```
**Topic:** Project timeline for customer portal redesign

**Key Decisions:**
- Launch date moved from Aug 15 to Sept 1 to accommodate UX feedback
- Budget increased by $15K for additional designer time
- Scope reduced: Analytics dashboard deferred to Phase 2

**Outstanding Issues:**
- Sarah needs confirmation on database migration approach by Wed
- Mike awaiting stakeholder approval on revised mockups
- Budget approval pending from finance (escalated to Director)

**Action Items:**
- Team: Review updated timeline in Monday meeting
- PM: Circulate revised project plan by EOD Friday
- Stakeholders: Provide feedback on mockups by July 20

**Next Steps:** Decision meeting scheduled for July 22
```

## Summarization Strategies by Content Type

### Scientific Papers
**Focus on:**
- Research question/hypothesis
- Methodology (brief)
- Key findings with statistics
- Main conclusions
- Implications

**Omit:**
- Detailed literature review
- Statistical formulas
- Lengthy methodology details
- All citations

### News Articles
**Focus on:**
- Who, what, when, where, why
- Most recent information
- Direct impact
- Key quotes (paraphrased)

**Omit:**
- Historical background
- Extensive quotes
- Speculative content
- Tangential stories

### Technical Documentation
**Focus on:**
- What changed/what it does
- How to use/implement
- Breaking changes
- Critical configuration

**Omit:**
- Detailed code examples
- Every configuration option
- Extensive troubleshooting
- Internal implementation details

### Business Documents
**Focus on:**
- Key metrics and changes
- Decisions made
- Action items
- Financial impact

**Omit:**
- Detailed methodology
- All data points
- Process descriptions
- Historical comparisons

## Multi-Document Summarization

When summarizing multiple related documents:

### Approach 1: Unified Summary
Combine information from all sources into single cohesive summary

**Example:**
```
Based on the three customer feedback reports, users consistently request:
1. Mobile app improvements (mentioned in all three reports)
2. Faster load times (mentioned twice, priority rating 8/10)
3. Better search functionality (mentioned twice)

Implementation of these features would impact approximately 80% of the user base 
and could reduce support tickets by an estimated 30%.
```

### Approach 2: Comparative Summary
Highlight agreements and differences across sources

**Example:**
```
While all three studies found positive effects of the intervention, magnitudes differed:
- Study A: 25% improvement (n=100, 6-month duration)
- Study B: 15% improvement (n=200, 3-month duration)  
- Study C: 35% improvement (n=50, 12-month duration)

Longer study duration correlates with better outcomes, suggesting sustained intervention 
is more effective than short-term application.
```

## Tone Adaptation

Same content, different audiences:

### Technical Audience
```
The API implements OAuth 2.0 authorization code flow with PKCE extension for enhanced 
security. Token refresh uses rotating refresh tokens with 7-day expiry and automatic 
revocation on suspicious activity.
```

### Business Audience
```
The new login system uses industry-standard security (OAuth 2.0) that major platforms 
like Google and Facebook use. User sessions stay active for one week, and the system 
automatically detects and prevents unauthorized access.
```

### General Audience
```
The updated login process is more secure and convenient. You'll stay logged in for up 
to a week on trusted devices, and the system actively protects your account from hackers.
```

## Quality Checklist

Before finalizing a summary, verify:

- [ ] **Accuracy**: All facts are correct and from the source
- [ ] **Completeness**: All major points are covered
- [ ] **Conciseness**: No unnecessary words or details
- [ ] **Clarity**: Understandable without source document
- [ ] **Coherence**: Ideas flow logically
- [ ] **Objectivity**: No added opinions or bias
- [ ] **Tone**: Matches original (formal, casual, technical)
- [ ] **Length**: Meets specified requirements
- [ ] **Stand-alone**: Makes sense independently
- [ ] **Proportionality**: Emphasis matches original

## Advanced Techniques

### Progressive Summarization
Layer summaries for different depth levels:

**Level 1 (Tweet, 20 words):**
```
New quantum computer achieves breakthrough in computing power, enabling calculations 
previously impossible with current technology.
```

**Level 2 (Paragraph, 75 words):**
```
[Standard summary with more details]
```

**Level 3 (Full summary, 200 words):**
```
[Extended summary with methodology, implications]
```

### Extractive vs. Abstractive

**Extractive** (using original sentences):
```
"The system achieved 94% accuracy." "Results demonstrate significant potential 
for AI-assisted diagnosis." "Limitations include dataset bias and need for 
larger training sets."
```

**Abstractive** (rewritten, preferred):
```
The AI diagnostic system's 94% accuracy shows strong potential for clinical use, 
though researchers note current limitations including dataset bias and the need 
for expanded training data.
```

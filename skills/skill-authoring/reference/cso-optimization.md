# CSO Optimization: Claude Search Optimization

## Overview

CSO (Claude Search Optimization) ensures your skill is discoverable. Claude reads metadata from ALL skills at startup, then decides which to load based on description match.

**Critical insight:** The best skill in the world is useless if Claude can't find it.

## Description Formula

```yaml
description: Use when [symptom1, symptom2, symptom3] - [what it does]. [How it helps]. Keywords: X, Y, Z.
```

### Component Breakdown

**1. "Use when" prefix (required)**
- Condition-first discovery optimization
- Triggers Claude's relevance matching
- Examples: "Use when tests are flaky", "Use when working with PDFs"

**2. Specific symptoms (3-5 concrete triggers)**

Include:
- **Error messages:** "command not found", "ENOENT", "timeout", "EAGAIN"
- **Behaviors:** "tests are flaky", "agent skips steps", "build fails intermittently"
- **Contexts:** "working with PDFs", "creating forms", "analyzing spreadsheets"
- **Situations:** "under time pressure", "unclear requirements", "complex workflow"

Avoid:
- Vague triggers: "having problems"
- Generic contexts: "working with files"
- Technology-specific unless necessary: "pytest tests use sleep" → "tests have timing dependencies"

**3. What it does (capability statement)**

Action-oriented verbs:
- "extracts text from PDFs"
- "validates JSON schemas"
- "generates commit messages"
- "enforces TDD discipline"

NOT vague: "helps with documents", "works with data"

**4. How it helps (value proposition)**

Benefit to user:
- "ensuring reliable async tests"
- "preventing data loss"
- "maintaining narrative coherence"
- "catching errors early"

**5. Explicit keywords (critical for search)**

List form:
```yaml
Keywords: keyword1, keyword2, keyword3, synonym1, tool-name, concept
```

Include:
- **Tool names:** pdfplumber, pytest, kubectl, graphviz
- **Concepts:** async, PDF, validation, coherence
- **Synonyms:** timeout/hang/freeze, flaky/inconsistent/unreliable
- **Domain terms:** NCP, Dramatica, Zettelkasten, TDD
- **Error fragments:** "ENOENT", "connection refused", "timeout"

## Examples (Before → After)

### Example 1: Too Vague

❌ **Before:**
```yaml
description: For async testing
```

Problems:
- No "Use when"
- No symptoms/triggers
- No keywords
- No value proposition

✅ **After:**
```yaml
description: Use when tests have race conditions, timing dependencies, or pass/fail inconsistently - replaces arbitrary timeouts with condition polling for reliable async tests. Keywords: flaky, timeout, async, race condition, polling, pytest, jest, testing.
```

### Example 2: First Person

❌ **Before:**
```yaml
description: I can help you with PDF processing and form filling
```

Problems:
- First person (should be third)
- Vague "help"
- No triggers
- No keywords

✅ **After:**
```yaml
description: Use when working with PDF files, form filling, or document extraction - extracts text and tables from PDFs, fills form fields, merges documents using pdfplumber and pypdf. Keywords: PDF, forms, text extraction, tables, pdfplumber, pypdf, document processing.
```

### Example 3: Missing Triggers

❌ **Before:**
```yaml
description: Guides usage of ARCHON framework for narrative coherence
```

Problems:
- No "Use when"
- No specific symptoms
- Missing keywords

✅ **After:**
```yaml
description: Use when working with ARCHON narrative coherence framework, validating NCP schemas, querying knowledge graph (L0-L3), or checking thematic consistency - guides Narrative Context Protocol usage, hierarchical hypergraph traversal, and Narrative Director agent workflows. Keywords: ARCHON, NCP, narrative coherence, knowledge graph, thematic validation, Dramatica, L0-L3, hypergraph.
```

### Example 4: Technology-Specific (Appropriate)

✅ **Good (skill IS tech-specific):**
```yaml
description: Use when using React Router and handling authentication redirects, protected routes, or auth state management - provides patterns for route guards, redirect flows, and session handling in React applications. Keywords: React Router, authentication, protected routes, redirects, route guards, React, auth.
```

The skill IS about React Router, so technology specificity is appropriate.

❌ **Bad (skill is NOT tech-specific):**
```yaml
description: Use when pytest tests use sleep() and are flaky...
```

The underlying issue is timing dependencies, not pytest-specific. Better:

✅ **Good (tech-agnostic):**
```yaml
description: Use when tests have timing dependencies, race conditions, or use sleep/setTimeout - replaces arbitrary delays with condition polling for reliable async tests. Keywords: flaky tests, race conditions, timing, async, pytest, jest, sleep, setTimeout, polling.
```

## Name Optimization

### Pattern

`[verb]-[object]` OR `[verbing]-[object]`

### Good Examples

- `creating-skills` (gerund + object)
- `condition-based-waiting` (adjective + gerund + object)
- `working-with-archon` (gerund + object)
- `testing-async-code` (gerund + object)
- `managing-kubernetes-resources` (gerund + object)

### Avoid

- `skill-creation` (noun phrase, passive)
- `pdf-stuff` (vague object)
- `helper-utils` (generic, meaningless)
- `tool-1` or `helper-2` (numbered, no semantics)
- `awesome-pdf-tool` (marketing language)

### Why Gerunds Work

**Psychological:** Active voice feels actionable
- "creating" → "I am creating"
- "managing" → "I am managing"
- "testing" → "I am testing"

**Search:** Matches user queries
- User thinks: "How do I create skills?"
- Skill name: `creating-skills`
- Strong semantic match

## Keyword Placement Strategy

**Don't just put keywords in description.** Place them throughout SKILL.md:

### 1. Overview Section

Repeat 3-5 key terms naturally:

```markdown
## Overview

This skill guides **async testing** with **condition-based waiting**
to eliminate **flaky tests** caused by **race conditions**.
```

### 2. When to Use Section

Use specific searchable phrases:

```markdown
## When to Use

**Symptoms:**
- Tests fail intermittently with "timeout" errors
- Test suite has race conditions
- Using sleep() or setTimeout() in tests
- Async operations complete at unpredictable times
```

Each symptom is a potential search query.

### 3. Quick Reference Section

Include tool names and command patterns:

```markdown
## Quick Reference

| Task | Command | Tool |
|------|---------|------|
| Extract text | `pdfplumber.open(file)` | pdfplumber |
| Fill form | `fillpdfs.write_fillable_pdf()` | fillpdfs |
```

### 4. Common Mistakes Section

Include error messages verbatim:

```markdown
## Common Mistakes

**Error: "TimeoutError: Waiting for selector..."**
- Problem: Hard-coded timeout too short
- Fix: Use condition-based waiting instead
```

## Technology Agnostic vs. Specific

### Default: Technology Agnostic

**Principle:** Describe the PROBLEM, not the SYMPTOM

❌ **Technology-specific symptom:**
```
Use when pytest tests use time.sleep() and fail randomly
```

✅ **Technology-agnostic problem:**
```
Use when tests have timing dependencies and fail intermittently
```

**Why:** The skill applies regardless of test framework. The problem (timing dependencies) is universal.

### Exception: Skill IS Technology-Specific

**When skill is inherently about specific tech, be explicit:**

✅ **Appropriate specificity:**
```yaml
name: using-react-router-auth
description: Use when using React Router and handling authentication...
```

✅ **Appropriate specificity:**
```yaml
name: kubectl-resource-management
description: Use when managing Kubernetes resources with kubectl...
```

**Test:** If you can't implement the skill without the specific technology, it's technology-specific.

## Length Guidelines

**Description field:** 200-500 characters ideal, 1024 max

Too short (<100 chars):
- Likely missing triggers or keywords
- Poor discoverability

Too long (>700 chars):
- Probably over-explaining
- Token waste at startup (ALL skills' metadata loads)

Sweet spot: 300-500 chars
- Enough for triggers + value prop + keywords
- Fits comfortably in startup context

## Voice and Tone

**Always third person:**

✅ "Extracts text from PDFs"
❌ "I can extract text from PDFs"
❌ "You can extract text from PDFs"

**Why:** Description is injected into system prompt. Inconsistent point-of-view causes confusion.

**Tone:**
- Direct and factual
- Active voice
- Present tense

✅ "Use when working with PDFs - extracts text and fills forms"
❌ "This skill can be used when you might be working with PDFs and need to perhaps extract text or possibly fill forms"

## Validation Checklist

Before finalizing description:

- [ ] Starts with "Use when"
- [ ] Includes 3-5 specific triggers/symptoms
- [ ] Uses third person voice
- [ ] Has explicit keywords list
- [ ] 200-500 characters (check with `wc -c`)
- [ ] Technology-agnostic unless skill IS tech-specific
- [ ] Active, present tense verbs
- [ ] No marketing fluff ("awesome", "powerful", "best")

Name:
- [ ] Format: `verb-object` or `verbing-object`
- [ ] Only letters, numbers, hyphens
- [ ] Semantic meaning (not generic)
- [ ] Matches skill content

## Advanced: Semantic Clustering

**For skill collections, coordinate keywords:**

If you have multiple related skills, ensure they use complementary (not identical) keywords:

**Example: Testing skill collection**

`async-testing`:
```yaml
Keywords: async, race conditions, timing, flaky tests, polling
```

`test-isolation`:
```yaml
Keywords: test pollution, shared state, isolation, cleanup, teardown
```

`fixture-management`:
```yaml
Keywords: fixtures, setup, test data, mocking, stubs
```

**Why:** Prevents all skills from triggering on "testing" query. Specialization improves precision.

## Common CSO Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| No "Use when" prefix | Claude misses relevance signal | Always start with "Use when" |
| Vague triggers | "when working with files" | Specific: "when extracting PDF text", "when parsing JSON" |
| First person voice | "I can help with..." | Third person: "Extracts...", "Validates..." |
| Missing keywords list | Relies only on description text | Explicit: "Keywords: X, Y, Z" |
| Technology-specific by default | "when pytest tests use sleep()" | Agnostic: "when tests have timing dependencies" |
| Marketing language | "awesome tool for amazing..." | Factual: "extracts text from PDFs" |
| No error messages | Generic symptoms | Include verbatim errors in skill body |

## Testing Discoverability

**After creating skill, test:**

1. **Relevance test:**
   - Query: "My tests are flaky and fail randomly"
   - Does Claude load your skill?

2. **Specificity test:**
   - Query: "How do I work with PDFs?"
   - Does Claude load right skill (not all file-related skills)?

3. **Keyword test:**
   - Query using different keyword from your list
   - Does Claude still find skill?

4. **Error message test:**
   - Query with actual error message
   - Does Claude find skill and suggest solution?

If discovery rate <80%, revisit:
- Add more keywords
- Make triggers more specific
- Check name relevance

## Real-World Examples from AEGIS

**For ARCHON skill:**

```yaml
name: working-with-archon
description: Use when working with ARCHON narrative coherence framework, validating NCP schemas, querying knowledge graph (L0-L3), or checking thematic consistency - guides Narrative Context Protocol usage, hierarchical hypergraph traversal, and Narrative Director agent workflows. Keywords: ARCHON, NCP, narrative coherence, knowledge graph, L0-L3, thematic validation, Dramatica, hypergraph, Kohärenz Protokoll.
```

**Why this works:**
- Multiple entry points: "narrative coherence", "NCP", "knowledge graph", "thematic consistency"
- Domain-specific terms: ARCHON, Dramatica, Kohärenz Protokoll
- Technical terms: hypergraph, L0-L3
- Clear value: "guides usage", "validates schemas"

**For Zettelkasten skill:**

```yaml
name: zettelkasten-agent-workflow
description: Use when creating notes, linking concepts, building knowledge graphs, or traversing note networks with Zettelkasten Agent - provides patterns for note creation, concept extraction, bidirectional linking, and knowledge traversal using fast-agents framework. Keywords: Zettelkasten, notes, knowledge graph, linking, concepts, bidirectional links, fast-agents, note-taking, PKM.
```

**Why this works:**
- Common queries: "creating notes", "linking concepts", "knowledge graph"
- Tool-specific: Zettelkasten Agent, fast-agents
- Methods: bidirectional linking, concept extraction
- Domain: PKM (personal knowledge management)

---

**Remember:** CSO is not one-time optimization. Monitor discovery rate and refine based on actual usage patterns.

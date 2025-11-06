# AEGIS Coherence Audit Report

**Date:** [YYYY-MM-DD]
**Auditor:** [Name or "Coherence Enforcer Skill v1.0.0"]
**Scope:** [Full system / Specific component]
**Duration:** [Time spent on audit]

---

## Executive Summary

**Overall Health Score:** [🟢 Good / 🟡 Moderate / 🔴 Needs Work]

| Category | Status | Priority Fixes |
|----------|--------|----------------|
| Code Structure | [🟢/🟡/🔴] | [Number] |
| Documentation | [🟢/🟡/🔴] | [Number] |
| Integration | [🟢/🟡/🔴] | [Number] |
| Dead Code | [🟢/🟡/🔴] | [Number] |

**Summary:** [1-2 sentence overview of findings]

---

## Detailed Findings

### 1. Code Duplication

#### Finding 1.1: [Title]
- **Severity:** [🔴 Critical / 🟡 High / 🟢 Medium / ⚪ Low]
- **Location:** [File paths]
- **Issue:** [Description of duplication]
- **Evidence:**
  ```
  [Code snippet or grep output showing duplication]
  ```
- **Impact:** [Lines duplicated, maintenance burden, user confusion, etc.]
- **Recommendation:** [Specific action to take]
- **Effort:** [Time estimate]
- **Priority:** [P0 / P1 / P2]

#### Finding 1.2: [Title]
[Repeat structure above]

---

### 2. Disconnected Systems

#### Finding 2.1: [Title]
- **Severity:** [🔴 Critical / 🟡 High / 🟢 Medium / ⚪ Low]
- **Components:**
  - Component A: [Path, description]
  - Component B: [Path, description]
- **Issue:** [Why they should integrate but don't]
- **Evidence:**
  ```bash
  # Commands showing disconnection
  grep -r "component_b" component_a/
  # Output: (no results)
  ```
- **Impact:** [Reduced functionality, manual workflows, etc.]
- **Recommendation:** [How to integrate]
- **Effort:** [Time estimate]
- **Priority:** [P0 / P1 / P2]

---

### 3. Documentation Issues

#### Finding 3.1: Documentation Drift
- **Severity:** [🔴 Critical / 🟡 High / 🟢 Medium / ⚪ Low]
- **Document:** [Path to documentation]
- **Claim:** [What documentation says]
- **Reality:** [What code actually does]
- **Impact:** [User confusion, broken workflows, etc.]
- **Recommendation:** [Update docs or implement feature]
- **Effort:** [Time estimate]
- **Priority:** [P0 / P1 / P2]

#### Finding 3.2: Orphaned Documentation
- **Severity:** [🔴 Critical / 🟡 High / 🟢 Medium / ⚪ Low]
- **Document:** [Path to documentation]
- **References:** [What it references that doesn't exist]
- **Impact:** [Confusion, broken links, etc.]
- **Recommendation:** [Remove, update, or implement]
- **Effort:** [Time estimate]
- **Priority:** [P0 / P1 / P2]

#### Finding 3.3: Documentation Fragmentation
- **Severity:** [🔴 Critical / 🟡 High / 🟢 Medium / ⚪ Low]
- **Documents:** [List of overlapping docs]
- **Overlap:** [What concepts are duplicated]
- **Impact:** [Onboarding difficulty, inconsistency, etc.]
- **Recommendation:** [Consolidation strategy]
- **Effort:** [Time estimate]
- **Priority:** [P0 / P1 / P2]

---

### 4. Dead Code Candidates

#### Candidate 4.1: [Filename]
- **Status:** [🟢 Safe to archive / 🟡 Needs verification / 🔴 Still in use]
- **Path:** [Full file path]
- **Last Modified:** [Date from git log]
- **Recent Activity:** [Commits in last 6 months]
- **References:** [Number of imports/references found]
- **Analysis:** [Why it appears dead or why it should be kept]
- **Recommendation:** [Archive / Keep / Investigate further]
- **Effort:** [Time estimate for archival]

---

### 5. Structural Issues

#### Finding 5.1: Directory Organization
- **Severity:** [🔴 Critical / 🟡 High / 🟢 Medium / ⚪ Low]
- **Location:** [Directory path]
- **Issue:** [Unclear purpose, confusing naming, etc.]
- **Impact:** [Navigation difficulty, file placement uncertainty]
- **Recommendation:** [Reorganize, document, or rename]
- **Effort:** [Time estimate]
- **Priority:** [P0 / P1 / P2]

---

## Integration Analysis

### Working Integrations ✅
- [Component A] ↔ [Component B]: [How they integrate]
- [Component C] ↔ [Component D]: [How they integrate]

### Missing Integrations ❌
- [Component E] ⊄ [Component F]: [Should integrate but doesn't]
- [Component G] ⊄ [Component H]: [Should integrate but doesn't]

### Recommendations
1. [Integration priority 1]
2. [Integration priority 2]

---

## Metrics

### Code Health
- **Total files scanned:** [Number]
- **Duplication found:** [Lines or percentage]
- **Dead code candidates:** [Number]
- **Integration gaps:** [Number]

### Documentation Health
- **Total docs scanned:** [Number]
- **Orphaned docs:** [Number]
- **Docs with drift:** [Number]
- **Fragmentation instances:** [Number]

### Test Coverage
- **Tests exist:** [Yes/No or percentage]
- **Tests passing:** [Number/Total]
- **Critical paths covered:** [Yes/No]

---

## Recommendations by Priority

### 🔴 P0: Critical (Do First)

#### Recommendation 1: [Title]
- **Issue:** [Brief description]
- **Impact:** [Why this is critical]
- **Action:** [Specific steps to take]
- **Effort:** [Time estimate]
- **Success criteria:** [How to verify it's fixed]

---

### 🟡 P1: High (Do Soon)

#### Recommendation 2: [Title]
- **Issue:** [Brief description]
- **Impact:** [Why this is important]
- **Action:** [Specific steps to take]
- **Effort:** [Time estimate]
- **Success criteria:** [How to verify it's fixed]

---

### 🟢 P2: Medium (Nice to Have)

#### Recommendation 3: [Title]
- **Issue:** [Brief description]
- **Impact:** [Why this would help]
- **Action:** [Specific steps to take]
- **Effort:** [Time estimate]
- **Success criteria:** [How to verify it's fixed]

---

## Implementation Roadmap

### Week 1
- [ ] [P0 Item 1]
- [ ] [P0 Item 2]
- [ ] Start [P1 Item 1]

### Week 2
- [ ] Complete [P1 Item 1]
- [ ] [P1 Item 2]
- [ ] Start [P1 Item 3]

### Week 3
- [ ] Complete [P1 Item 3]
- [ ] [P2 Items if time allows]

### Week 4
- [ ] Validation and testing
- [ ] Documentation updates
- [ ] Re-audit to verify improvements

---

## Success Criteria

After implementing recommendations, we should achieve:

- ✅ [Metric 1: e.g., "Reduce duplication from 2,000 lines to <100 lines"]
- ✅ [Metric 2: e.g., "Single entry point for learning workflows"]
- ✅ [Metric 3: e.g., "Zero doc drift instances"]
- ✅ [Metric 4: e.g., "All integration gaps closed"]
- ✅ [Metric 5: e.g., "Documentation navigation <5 minutes"]

---

## Validation Plan

Before marking this audit as complete:

1. **Code Validation**
   - [ ] All tests pass after refactoring
   - [ ] No new duplication introduced
   - [ ] Integration points verified

2. **Documentation Validation**
   - [ ] Docs match implementation
   - [ ] All links work
   - [ ] Navigation is clear

3. **User Validation**
   - [ ] Workflows still function
   - [ ] No regressions introduced
   - [ ] User confusion reduced

---

## Next Steps

1. **Review this audit** with stakeholders
2. **Approve P0 items** for implementation
3. **Create feature branch** (if needed): `refactor/[branch-name]`
4. **Assign tasks** from Implementation Roadmap
5. **Begin implementation** following priority order
6. **Re-audit in [timeframe]** to verify improvements

---

## Notes

[Any additional observations, concerns, or context that doesn't fit above categories]

---

## Appendix: Commands Used

```bash
# Duplication detection
[Commands used to find duplication]

# Dead code detection
[Commands used to find dead code]

# Documentation analysis
[Commands used to analyze docs]

# Integration verification
[Commands used to check integration]
```

---

## Appendix: Full File List

### Files Scanned
```
[List of all files included in audit]
```

### Files Excluded
```
[List of files excluded and why]
```

---

**Report prepared by:** [Name]
**Date:** [YYYY-MM-DD]
**Version:** [Report version number]

---

## Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| [YYYY-MM-DD] | 1.0.0 | Initial audit | [Name] |
| [YYYY-MM-DD] | 1.1.0 | [Changes] | [Name] |

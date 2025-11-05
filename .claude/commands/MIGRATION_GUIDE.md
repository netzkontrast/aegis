# Migration Guide: Unified `/learn` Command

**Version:** 2.0
**Date:** 2025-11-05

---

## Summary

The three separate learning commands (`/tapestry`, `/ship-learn-next`, `/zettelkasten-tapestry`) have been unified into a single `/learn` command with a modular architecture.

---

## Quick Migration Reference

| Old Command | New Command | Notes |
|-------------|-------------|-------|
| `/tapestry <URL>` | `/learn <URL>` | Exact same functionality |
| `/ship-learn-next <file>` | `/learn <file>` | Works with existing content files |
| `/zettelkasten-tapestry <URL>` | `/learn <URL> --save` | Adds `--save` flag for Zettelkasten |

---

## What Changed?

### Before: 3 Separate Commands

```
/tapestry <URL>              # Extract content + create plan
/ship-learn-next <file>      # Create plan from content
/zettelkasten-tapestry <URL> # Extract + plan + save to Zettelkasten
```

**Problems:**
- Confusing which command to use
- Code duplication (1,000+ lines)
- Hard to maintain
- No flexibility

### After: 1 Unified Command

```
/learn <URL>                 # Extract + plan
/learn <URL> --save          # Extract + plan + Zettelkasten
/learn <file>                # Plan from existing file
/learn <file> --save         # Plan + Zettelkasten
/learn <URL> --extract-only  # Just extract content
```

**Benefits:**
- Single command to remember
- More flexible (new flags, more options)
- Modular architecture (easy to extend)
- Less code duplication
- Easier to maintain

---

## Detailed Migration Examples

### Example 1: YouTube Video Extraction

**Before:**
```
/tapestry https://youtube.com/watch?v=xxx
```

**After:**
```
/learn https://youtube.com/watch?v=xxx
```

**Result:** Identical functionality

---

### Example 2: Article Extraction

**Before:**
```
/tapestry https://example.com/article
```

**After:**
```
/learn https://example.com/article
```

**Result:** Identical functionality

---

### Example 3: Plan from Existing Content

**Before:**
```
/ship-learn-next article.txt
```

**After:**
```
/learn article.txt
```

**Result:** Identical functionality

---

### Example 4: Full Zettelkasten Workflow

**Before:**
```
/zettelkasten-tapestry https://example.com/article
```

**After:**
```
/learn https://example.com/article --save
```

**Result:** Identical functionality

---

### Example 5: NEW - Just Extract Content

**Not possible before**

**Now:**
```
/learn https://example.com/article --extract-only
```

**Result:** Extracts content without creating a plan

---

### Example 6: NEW - Plan from File + Save to Zettelkasten

**Not possible before**

**Now:**
```
/learn article.txt --save
```

**Result:** Creates plan AND saves to Zettelkasten from existing file

---

## New Capabilities

The unified `/learn` command adds new capabilities that weren't possible before:

### 1. Extract-Only Mode
```
/learn <URL> --extract-only
```
Extract content without creating a plan. Useful when you just want to save the content for later.

### 2. Plan from File + Zettelkasten
```
/learn <file> --save
```
Create a plan from an existing file AND save it to your knowledge vault.

### 3. Shorter Flags
```
/learn <URL> -s         # Short version of --save
```

### 4. Future Extensions (Coming Soon)
- `/learn <URL> --export pdf` - Export plan as PDF
- `/learn <URL> --share` - Generate shareable link
- `/learn <URL> --review` - Review and update existing plan

---

## Architecture Changes

### Modular System

The new `/learn` command is built on three independent modules:

```
.claude/commands/
├── _modules/
│   ├── extract-content.md      # Pure content extraction
│   ├── action-planner.md       # Ship-Learn-Next planning
│   └── knowledge-manager.md    # Zettelkasten management
│
└── learn.md                    # Orchestrator (composes modules)
```

**Benefits:**
- Each module does ONE thing well
- Modules can be used independently
- Easy to test and maintain
- Easy to extend with new modules

---

## Backward Compatibility

### Old Commands Still Work

The old commands (`/tapestry`, `/ship-learn-next`, `/zettelkasten-tapestry`) still work but show a deprecation warning:

```
⚠️ DEPRECATED: Use `/learn` Instead

This command has been replaced by the unified `/learn` command.

Use instead:
  /learn <URL>              # Same functionality

This command still works but will be removed in a future update.

[Original command continues to work...]
```

### Timeline

- **Now - 1 month:** Old commands work with deprecation warnings
- **After 1 month:** Old commands removed (only `/learn` available)

**Recommendation:** Start using `/learn` now to avoid disruption later.

---

## FAQ

### Q: Why consolidate the commands?

**A:** Three reasons:
1. **User experience** - One command is simpler than three
2. **Maintainability** - 1,000+ lines of duplication eliminated
3. **Flexibility** - Easier to add new features

### Q: Will my old workflows break?

**A:** No. Old commands still work and produce identical results. But you'll see deprecation warnings.

### Q: When will old commands be removed?

**A:** After 1 month (early December 2025). This gives time to update habits and scripts.

### Q: Can I still use Zettelkasten?

**A:** Yes! Use `/learn <URL> --save` for the full Zettelkasten workflow.

### Q: What if I have scripts using the old commands?

**A:** Update them to use `/learn` before December 2025. The migration is straightforward - see the reference table above.

### Q: Are there any new features?

**A:** Yes! You can now:
- Extract content without planning (`--extract-only`)
- Plan from files with Zettelkasten (`/learn file.txt --save`)
- More flags coming soon

### Q: What if I find a bug?

**A:** Report it! The new system is thoroughly tested but let us know if you encounter issues.

---

## Support

### Need Help?

1. **Try the new command:** Most migrations are straightforward
2. **Check this guide:** See the examples above
3. **Ask for help:** Create an issue if you're stuck

### Feedback Welcome

We want to hear:
- What works well
- What's confusing
- What features you want next

---

## Summary

**Old way:** Three commands, confusing, hard to maintain
**New way:** One command, modular, flexible

**Action:** Start using `/learn` today. Old commands work for 1 month but will be removed.

**Migration:** Simple - see the reference table at the top.

---

**Welcome to the unified learning system!** 🚀

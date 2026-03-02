import { getNcpData } from "./content";

// Typed helpers for querying the NCP JSON data

type NcpData = Record<string, unknown>;

let cached: NcpData | null = null;

function load(): NcpData {
  if (!cached) {
    cached = getNcpData() || {};
  }
  return cached;
}

export function getMetadata() {
  const data = load();
  return (data.meta as Record<string, unknown>) || null;
}

export function getPhysicsRules() {
  const data = load();
  return (data.physics_rules as Record<string, unknown>) || null;
}

export function getDualKernelTheory() {
  const data = load();
  return (data.dual_kernel_theory as Record<string, unknown>) || null;
}

export function getWorld() {
  const data = load();
  return (data.world as Record<string, unknown>) || null;
}

export function getThroughlines() {
  const data = load();
  return (data.throughlines as Record<string, unknown>) || null;
}

export function getCharacterSystems() {
  const data = load();
  return (data.character_systems as Record<string, unknown>) || null;
}

export function getChapterDesign() {
  const data = load();
  return (data.chapter_design as unknown[]) || null;
}

export function getValidationCriteria() {
  const data = load();
  return (data.validation_criteria as Record<string, unknown>) || null;
}

/** Query a top-level key or dot-path from the NCP data */
export function queryNcp(path: string): unknown {
  const data = load();
  const parts = path.split(".");
  let current: unknown = data;

  for (const part of parts) {
    if (current === null || current === undefined) return null;
    if (typeof current === "object" && !Array.isArray(current)) {
      current = (current as Record<string, unknown>)[part];
    } else if (Array.isArray(current)) {
      const idx = parseInt(part, 10);
      if (isNaN(idx)) return null;
      current = current[idx];
    } else {
      return null;
    }
  }

  return current;
}

/** Get all top-level sections available in the NCP */
export function getNcpSections(): string[] {
  const data = load();
  return Object.keys(data).filter((k) => !k.startsWith("_"));
}

/** Simple prose validator - checks basic constraints */
export interface ValidationIssue {
  severity: "ERROR" | "WARNING" | "INFO";
  category: string;
  message: string;
}

export interface ValidationResult {
  valid: boolean;
  score: number;
  issues: ValidationIssue[];
  wordCount: number;
  checksTotal: number;
  checksPassed: number;
}

export function validateProse(
  text: string,
  chapter: number
): ValidationResult {
  const issues: ValidationIssue[] = [];
  let checksTotal = 0;
  let checksPassed = 0;

  // Word count check
  const words = text.trim().split(/\s+/).length;
  checksTotal++;
  if (words >= 300 && words <= 5000) {
    checksPassed++;
  } else if (words < 300) {
    issues.push({
      severity: "WARNING",
      category: "length",
      message: `Scene is short (${words} words). Aim for 500-3000 words.`,
    });
  } else {
    issues.push({
      severity: "WARNING",
      category: "length",
      message: `Scene is long (${words} words). Consider splitting.`,
    });
  }

  // Physics check: Landauer principle references in suppression scenes
  checksTotal++;
  const hasSuppression = /suppress|erase|delete|remove|eliminate/i.test(text);
  const hasHeatSignal =
    /heat|warm|temperature|shimmer|frost|glow|thermal/i.test(text);
  if (hasSuppression && !hasHeatSignal) {
    issues.push({
      severity: "ERROR",
      category: "physics",
      message:
        "Suppression/erasure occurs without Landauer thermal signal. Suppressing information must produce heat.",
    });
  } else {
    checksPassed++;
  }

  // Style check based on act
  checksTotal++;
  if (chapter <= 13) {
    // Act I: should be fragmented
    const hasFragmentation =
      /\.\.\.|—|–|\(.*\)|fragments?|broken|shatter/i.test(text);
    if (hasFragmentation) {
      checksPassed++;
    } else {
      issues.push({
        severity: "INFO",
        category: "style",
        message:
          "Act I prose should show fragmentation: interruptions, dashes, parenthetical intrusions.",
      });
    }
  } else if (chapter <= 26) {
    checksPassed++;
    issues.push({
      severity: "INFO",
      category: "style",
      message:
        "Act II prose should transition between fragmented and analytical styles.",
    });
  } else {
    // Act III: polyphonic
    const hasPolyphonic = /\bwe\b|together|unified|integration/i.test(text);
    if (hasPolyphonic) {
      checksPassed++;
    } else {
      issues.push({
        severity: "INFO",
        category: "style",
        message:
          'Act III prose should tend toward polyphonic "we" voice showing integration.',
      });
    }
  }

  // Character presence check
  checksTotal++;
  const knownCharacters = [
    "Kael",
    "AEGIS",
    "Lex",
    "Nyx",
    "Kiko",
    "Rhys",
    "Alex",
    "Selene",
    "Argus",
    "Moros",
    "Juna",
    "Lia",
  ];
  const found = knownCharacters.filter((c) =>
    new RegExp(`\\b${c}\\b`, "i").test(text)
  );
  if (found.length > 0) {
    checksPassed++;
  } else {
    issues.push({
      severity: "WARNING",
      category: "characters",
      message: "No known characters detected. Ensure correct character names are used.",
    });
  }

  // Compute score
  const ratio = checksTotal > 0 ? checksPassed / checksTotal : 0;
  const errors = issues.filter((i) => i.severity === "ERROR").length;
  const warnings = issues.filter((i) => i.severity === "WARNING").length;
  const score = Math.max(0, Math.min(10, ratio * 10 - errors * 2 - warnings * 0.5));

  return {
    valid: score >= 7 && errors === 0,
    score: Math.round(score * 10) / 10,
    issues,
    wordCount: words,
    checksTotal,
    checksPassed,
  };
}

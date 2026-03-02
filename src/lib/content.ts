import fs from "fs";
import path from "path";

const ROOT = process.cwd();

/** Read a file relative to the repo root. Returns null if not found. */
function readFile(relativePath: string): string | null {
  const fullPath = path.join(ROOT, relativePath);
  try {
    return fs.readFileSync(fullPath, "utf-8");
  } catch {
    return null;
  }
}

/** Simple markdown to HTML converter for rendering content. */
export function markdownToHtml(md: string): string {
  let html = md;

  // Code blocks (``` ... ```) — must come before inline code
  html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (_match, _lang, code) => {
    return `<pre><code>${escapeHtml(code.trim())}</code></pre>`;
  });

  // Headers
  html = html.replace(/^#### (.+)$/gm, "<h4>$1</h4>");
  html = html.replace(/^### (.+)$/gm, "<h3>$1</h3>");
  html = html.replace(/^## (.+)$/gm, "<h2>$1</h2>");
  html = html.replace(/^# (.+)$/gm, "<h1>$1</h1>");

  // Horizontal rules
  html = html.replace(/^---$/gm, "<hr>");

  // Bold + italic
  html = html.replace(/\*\*\*(.+?)\*\*\*/g, "<strong><em>$1</em></strong>");
  // Bold
  html = html.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  // Italic
  html = html.replace(/\*(.+?)\*/g, "<em>$1</em>");
  // Inline code
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");

  // Links
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

  // Unordered lists (simple, single-level)
  html = html.replace(
    /^(\s*[-*] .+(\n|$))+/gm,
    (block) => {
      const items = block
        .trim()
        .split("\n")
        .map((line) => `<li>${line.replace(/^\s*[-*] /, "")}</li>`)
        .join("\n");
      return `<ul>\n${items}\n</ul>`;
    }
  );

  // Ordered lists
  html = html.replace(
    /^(\s*\d+\. .+(\n|$))+/gm,
    (block) => {
      const items = block
        .trim()
        .split("\n")
        .map((line) => `<li>${line.replace(/^\s*\d+\. /, "")}</li>`)
        .join("\n");
      return `<ol>\n${items}\n</ol>`;
    }
  );

  // Checkbox lists
  html = html.replace(/- \[x\] (.+)/g, '<li class="check done">$1</li>');
  html = html.replace(/- \[ \] (.+)/g, '<li class="check">$1</li>');

  // Blockquotes
  html = html.replace(
    /^(> .+(\n|$))+/gm,
    (block) => {
      const content = block.replace(/^> /gm, "");
      return `<blockquote>${content.trim()}</blockquote>`;
    }
  );

  // Paragraphs: wrap remaining lines that aren't already HTML tags
  html = html
    .split("\n\n")
    .map((block) => {
      const trimmed = block.trim();
      if (!trimmed) return "";
      if (trimmed.startsWith("<")) return trimmed;
      return `<p>${trimmed.replace(/\n/g, "<br>")}</p>`;
    })
    .join("\n");

  return html;
}

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

// --- Chapter loading ---

export interface ChapterSummary {
  number: number;
  slug: string;
  title: string;
  act: string;
  kState: string;
  coreEvent: string;
}

export function getChapters(): ChapterSummary[] {
  const storyDir = path.join(ROOT, "Story");
  const files = fs
    .readdirSync(storyDir)
    .filter((f) => /^Chapter_\d+\.md$/.test(f))
    .sort();

  return files.map((file) => {
    const num = parseInt(file.match(/Chapter_(\d+)/)?.[1] || "0", 10);
    const content = fs.readFileSync(path.join(storyDir, file), "utf-8");
    const titleMatch = content.match(/^# (.+)$/m);
    const actMatch = content.match(/\*\*Act\*\*:\s*(.+)$/m);
    const kStateMatch = content.match(/\*\*K-State\*\*:\s*(.+)$/m);
    const coreEventMatch = content.match(/## Core Event\n(.+)/);

    let act = "Act I";
    if (num >= 14 && num <= 26) act = "Act II";
    else if (num >= 27) act = "Act III";

    return {
      number: num,
      slug: `chapter-${String(num).padStart(2, "0")}`,
      title:
        titleMatch?.[1]?.replace(/^Chapter_\d+:\s*/, "") ||
        `Chapter ${num}`,
      act: actMatch?.[1]?.trim() || act,
      kState: kStateMatch?.[1]?.trim() || "",
      coreEvent: coreEventMatch?.[1]?.trim() || "",
    };
  });
}

export function getChapterContent(chapterNum: number): string | null {
  const file = `Story/Chapter_${String(chapterNum).padStart(2, "0")}.md`;
  return readFile(file);
}

// --- Entity loading ---

export interface EntitySummary {
  slug: string;
  name: string;
  type: string;
  filename: string;
}

export function getEntities(): EntitySummary[] {
  const dir = path.join(ROOT, "Story", "entities");
  try {
    const files = fs.readdirSync(dir).filter((f) => f.endsWith(".md"));
    return files.map((file) => {
      const name = file.replace(/\.md$/, "").replace(/_/g, " ");
      const content = fs.readFileSync(path.join(dir, file), "utf-8");

      let type = "Entity";
      if (file.startsWith("Alter_")) type = "Alter";
      else if (
        file === "Kael_Host.md" ||
        file === "System_Kael.md" ||
        file === "Juna_V.md"
      )
        type = "Protagonist";
      else if (file === "AEGIS.md") type = "Antagonist";
      else if (file === "Factions.md") type = "Faction";
      else if (
        file === "Physics_of_Existence.md" ||
        file === "Core_Worlds.md" ||
        file === "Anomalies.md"
      )
        type = "World";

      return {
        slug: file.replace(/\.md$/, "").toLowerCase(),
        name,
        type,
        filename: file,
      };
    });
  } catch {
    return [];
  }
}

export function getEntityContent(slug: string): string | null {
  const entities = getEntities();
  const entity = entities.find((e) => e.slug === slug);
  if (!entity) return null;
  return readFile(`Story/entities/${entity.filename}`);
}

// --- Quest loading ---

export interface QuestSummary {
  slug: string;
  title: string;
  filename: string;
}

export function getQuests(): QuestSummary[] {
  const dir = path.join(ROOT, "quests");
  try {
    const files = fs
      .readdirSync(dir)
      .filter((f) => f.endsWith(".md") && f !== "README.md");
    return files.map((file) => {
      const content = fs.readFileSync(path.join(dir, file), "utf-8");
      const titleMatch = content.match(/^# (.+)$/m);
      return {
        slug: file.replace(/\.md$/, ""),
        title: titleMatch?.[1] || file.replace(/\.md$/, "").replace(/-/g, " "),
        filename: file,
      };
    });
  } catch {
    return [];
  }
}

export function getQuestContent(slug: string): string | null {
  return readFile(`quests/${slug}.md`);
}

// --- NCP loading ---

export function getNcpData(): Record<string, unknown> | null {
  const content = readFile("aegis/ncp/kohaerenz_protokoll_v2.ncp.json");
  if (!content) return null;
  try {
    return JSON.parse(content);
  } catch {
    return null;
  }
}

import type { Metadata } from "next";

export const metadata: Metadata = { title: "About ARCHON" };

export default function AboutPage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-6 text-[var(--primary)]">
        About ARCHON
      </h1>

      <div className="max-w-4xl">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Framework</h2>
          <p className="text-gray-300 mb-4">
            <strong className="text-[var(--primary)]">ARCHON</strong> (Agentic
            Reasoning & Coherent Hypergraph Orchestration for Narratives) is a
            functional implementation of an AI-assisted narrative coherence
            system.
          </p>
          <p className="text-gray-300">
            It is designed to maintain thematic depth and structural integrity
            across novel-length works through formal systems that enable rather
            than constrain creativity.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-8">
          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <div className="text-4xl mb-3">&#x1F4CB;</div>
            <h3 className="text-xl font-bold mb-2 text-[var(--primary)]">
              NCP
            </h3>
            <p className="text-sm text-gray-400">
              Narrative Context Protocol - Machine-readable thematic structure
              based on Dramatica theory
            </p>
          </div>

          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <div className="text-4xl mb-3">&#x1F578;&#xFE0F;</div>
            <h3 className="text-xl font-bold mb-2 text-[var(--secondary)]">
              Knowledge Graph
            </h3>
            <p className="text-sm text-gray-400">
              Hierarchical memory system (L0-L3) that overcomes LLM context
              limitations
            </p>
          </div>

          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <div className="text-4xl mb-3">&#x1F916;</div>
            <h3 className="text-xl font-bold mb-2 text-[var(--accent)]">
              Narrative Director
            </h3>
            <p className="text-sm text-gray-400">
              Agentic system that generates and validates content against NCP
              constraints
            </p>
          </div>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Core Principles</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--primary)]">
                Integration Over Elimination
              </h3>
              <p className="text-gray-300 text-sm">
                True coherence emerges from integration of contradictions, not
                elimination. This applies to narrative structure, character
                development, and tool design.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--secondary)]">
                Formal Systems Serve Creativity
              </h3>
              <p className="text-gray-300 text-sm">
                ARCHON provides structure to enable, not constrain. The NCP
                defines thematic guardrails, not rigid rules. Tools validate and
                query, not dictate.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--accent)]">
                Recursive Self-Performance
              </h3>
              <p className="text-gray-300 text-sm">
                The project performs its own themes. Repository structure mirrors
                narrative structure. Tools demonstrate principles they enable.
              </p>
            </div>
          </div>
        </div>

        <div className="bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Research Question</h2>
          <p className="text-lg mb-4">
            Can a formal protocol actually help maintain the psychological and
            thematic coherence of a 39-chapter novel about trauma, dissociation,
            and emergence?
          </p>
          <p className="text-sm">
            This project serves as a validation of ARCHON&apos;s principles.
          </p>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Component Status</h2>
          <div className="space-y-3">
            {[
              ["ARCHON NCP", "Complete", "text-green-400"],
              ["ARCHON Tools (Query, Validate)", "Complete", "text-green-400"],
              ["Narrative Director", "Specified", "text-yellow-400"],
              ["Knowledge Graph", "In Development", "text-yellow-400"],
              ["Skill Seeker (299 tests)", "Production Ready", "text-green-400"],
              ["Zettelkasten Agent", "MVP", "text-blue-400"],
              ["Unified Web App", "Active", "text-green-400"],
              ["Kohärenz Protokoll Novel", "Act I Outlined", "text-blue-400"],
            ].map(([name, status, color]) => (
              <div
                key={name}
                className="flex items-center justify-between p-3 bg-black/50 rounded"
              >
                <span>{name}</span>
                <span className={color as string}>{status}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Ecosystem Tools</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-bold mb-2">Skill Seeker</h3>
              <p className="text-sm text-gray-400">
                Documentation-to-Claude-Skills converter. Scrapes docs, GitHub
                repos, and PDFs. 299 passing tests, 15+ preset configs.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-2">Zettelkasten Agent</h3>
              <p className="text-sm text-gray-400">
                AI-powered knowledge management with 4-phase cognitive loop.
                SRC, ZTL, MOC note types with MCP integration.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-2">
                NCP Tools (Query, Validate, Assist)
              </h3>
              <p className="text-sm text-gray-400">
                Python CLI tools for querying scene requirements, validating
                prose against constraints, and generating writing prompts.
              </p>
            </div>
          </div>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Get Involved</h2>
          <p className="text-gray-300 mb-4">
            AEGIS is an open research and creative project.
          </p>
          <a
            href="https://github.com/netzkontrast/aegis"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block px-6 py-3 bg-[var(--primary)] text-black font-bold rounded hover:bg-opacity-80 transition-all"
          >
            Visit GitHub Repository &rarr;
          </a>
        </div>
      </div>
    </div>
  );
}

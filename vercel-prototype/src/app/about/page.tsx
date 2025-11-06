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
            <strong className="text-[var(--primary)]">ARCHON</strong> (Agentic Reasoning & Coherent
            Hypergraph Orchestration for Narratives) is a functional implementation of an AI-assisted
            narrative coherence system.
          </p>
          <p className="text-gray-300">
            It is designed to maintain thematic depth and structural integrity across novel-length
            works through formal systems that enable rather than constrain creativity.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-8">
          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <div className="text-4xl mb-3">📋</div>
            <h3 className="text-xl font-bold mb-2 text-[var(--primary)]">NCP</h3>
            <p className="text-sm text-gray-400">
              Narrative Context Protocol - Machine-readable thematic structure based on Dramatica theory
            </p>
          </div>

          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <div className="text-4xl mb-3">🕸️</div>
            <h3 className="text-xl font-bold mb-2 text-[var(--secondary)]">Knowledge Graph</h3>
            <p className="text-sm text-gray-400">
              Hierarchical memory system (L0-L3) that overcomes LLM context limitations
            </p>
          </div>

          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <div className="text-4xl mb-3">🤖</div>
            <h3 className="text-xl font-bold mb-2 text-[var(--accent)]">Narrative Director</h3>
            <p className="text-sm text-gray-400">
              Agentic system that generates and validates content against NCP constraints
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
                True coherence emerges from integration of contradictions, not elimination.
                This applies to narrative structure, character development, and tool design.
              </p>
            </div>

            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--secondary)]">
                Formal Systems Serve Creativity
              </h3>
              <p className="text-gray-300 text-sm">
                ARCHON provides structure to enable, not constrain. The NCP defines thematic
                guardrails, not rigid rules. Tools validate and query, not dictate.
              </p>
            </div>

            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--accent)]">
                Recursive Self-Performance
              </h3>
              <p className="text-gray-300 text-sm">
                The project performs its own themes. Repository structure mirrors narrative structure.
                Tools demonstrate principles they enable. Development validates research questions.
              </p>
            </div>
          </div>
        </div>

        <div className="bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Research Question</h2>
          <p className="text-lg mb-4">
            Can a formal protocol actually help maintain the psychological and thematic coherence
            of a 39-chapter novel about trauma, dissociation, and emergence?
          </p>
          <p className="text-sm">
            This project serves as a validation of ARCHON&apos;s principles. The development
            process itself is research data, documenting both successes and failures of the framework.
          </p>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Component Status</h2>
          <div className="space-y-3">
            <div className="flex items-center justify-between p-3 bg-black/50 rounded">
              <span>ARCHON NCP</span>
              <span className="text-green-400">✅ Complete</span>
            </div>
            <div className="flex items-center justify-between p-3 bg-black/50 rounded">
              <span>ARCHON Tools (Query, Validate)</span>
              <span className="text-green-400">✅ Complete</span>
            </div>
            <div className="flex items-center justify-between p-3 bg-black/50 rounded">
              <span>Narrative Director</span>
              <span className="text-yellow-400">📋 Specified</span>
            </div>
            <div className="flex items-center justify-between p-3 bg-black/50 rounded">
              <span>Knowledge Graph</span>
              <span className="text-yellow-400">📋 Planned</span>
            </div>
            <div className="flex items-center justify-between p-3 bg-black/50 rounded">
              <span>Kohärenz Protokoll Novel</span>
              <span className="text-blue-400">🔜 Early (Act I outlined)</span>
            </div>
          </div>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Additional Tools</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-bold mb-2">Skill Seeker</h3>
              <p className="text-sm text-gray-400">
                Documentation-to-Claude-Skills converter. Automatically scrapes documentation,
                GitHub repos, and PDFs to create AI skills. Production-ready with 299 passing tests.
              </p>
            </div>

            <div>
              <h3 className="text-lg font-bold mb-2">Zettelkasten Agent</h3>
              <p className="text-sm text-gray-400">
                AI-powered knowledge management system implementing the Zettelkasten method
                with automatic synthesis and linking.
              </p>
            </div>

            <div>
              <h3 className="text-lg font-bold mb-2">Skills Library</h3>
              <p className="text-sm text-gray-400">
                Reusable Claude AI skills including skill authoring framework and
                zettelkasten-tapestry integration for progressive learning.
              </p>
            </div>
          </div>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Get Involved</h2>
          <p className="text-gray-300 mb-4">
            AEGIS is an open research and creative project. You can:
          </p>
          <ul className="list-disc list-inside space-y-2 text-gray-400 ml-4 mb-6">
            <li>Report bugs or suggest improvements</li>
            <li>Provide feedback on narrative or prose</li>
            <li>Contribute research or analysis</li>
            <li>Implement planned features</li>
            <li>Add tests or improve documentation</li>
          </ul>
          <a
            href="https://github.com/netzkontrast/aegis"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block px-6 py-3 bg-[var(--primary)] text-black font-bold rounded hover:bg-opacity-80 transition-all"
          >
            Visit GitHub Repository →
          </a>
        </div>
      </div>
    </div>
  );
}

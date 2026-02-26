export default function Home() {
  return (
    <div className="container mx-auto px-4 py-12">
      <section className="text-center mb-16">
        <h1 className="text-6xl font-bold mb-4 glitch">
          <span className="neon-glow">AEGIS</span>
        </h1>
        <p className="text-xl text-gray-300 mb-2">
          Agentic Reasoning & Coherent Hypergraph Orchestration for Narratives
        </p>
        <p className="text-2xl italic text-[var(--accent)] mt-4">
          &ldquo;AEGIS is what AEGIS prevents from not being.&rdquo;
        </p>
      </section>

      <section className="max-w-4xl mx-auto mb-16">
        <h2 className="text-3xl font-bold mb-6 text-[var(--primary)]">The Dual Project</h2>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <h3 className="text-2xl font-bold mb-3 text-[var(--primary)]">AEGIS</h3>
            <p className="text-sm text-gray-400 mb-2">The Meta-Framework</p>
            <p className="text-gray-300">
              A functional implementation of an AI-assisted narrative coherence system,
              designed to maintain thematic depth and structural integrity across novel-length works.
            </p>
            <ul className="mt-4 space-y-2 text-sm text-gray-400">
              <li>→ Formal authorial intent via NCP</li>
              <li>→ Externalized memory via knowledge graphs</li>
              <li>→ Agentic reasoning via systematic validation</li>
            </ul>
          </div>

          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <h3 className="text-2xl font-bold mb-3 text-[var(--accent)]">Kohärenz Protokoll</h3>
            <p className="text-sm text-gray-400 mb-2">The Novel</p>
            <p className="text-gray-300">
              A philosophical science fiction work about a man with dissociative identity disorder
              trapped in a simulation controlled by a god-like AI.
            </p>
            <ul className="mt-4 space-y-2 text-sm text-gray-400">
              <li>→ Hard SF + Psychological Thriller</li>
              <li>→ Cosmic Horror + Philosophical Fiction</li>
              <li>→ 39 chapters across three acts</li>
            </ul>
          </div>
        </div>
      </section>

      <section className="max-w-4xl mx-auto mb-16">
        <h2 className="text-3xl font-bold mb-6 text-[var(--secondary)]">The Meta-Recursive Design</h2>
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-8">
          <p className="text-lg text-gray-300 mb-6">
            This repository <strong className="text-[var(--primary)]">performs its own themes</strong>:
          </p>
          <div className="space-y-4">
            <div className="flex items-start gap-4">
              <span className="text-3xl">🔧</span>
              <div>
                <strong className="text-[var(--primary)]">AEGIS</strong> seeks to maintain narrative
                coherence through formal systems
              </div>
            </div>
            <div className="flex items-start gap-4">
              <span className="text-3xl">🤖</span>
              <div>
                <strong className="text-[var(--accent)]">AEGIS</strong> (the AI antagonist) seeks to
                maintain system coherence through rigid control
              </div>
            </div>
            <div className="flex items-start gap-4">
              <span className="text-3xl">🎯</span>
              <div>
                <strong className="text-[var(--secondary)]">Both</strong> discover that true coherence
                emerges from integration, not elimination
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="max-w-4xl mx-auto mb-16">
        <h2 className="text-3xl font-bold mb-6 text-[var(--primary)]">Explore the System</h2>
        <div className="grid md:grid-cols-3 gap-6">
          <a href="/ncp" className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover block">
            <div className="text-4xl mb-4">📊</div>
            <h3 className="text-xl font-bold mb-2">NCP Query</h3>
            <p className="text-sm text-gray-400">
              Query the Narrative Context Protocol for scene requirements and character states
            </p>
          </a>

          <a href="/characters" className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover block">
            <div className="text-4xl mb-4">👥</div>
            <h3 className="text-xl font-bold mb-2">Characters</h3>
            <p className="text-sm text-gray-400">
              Explore Kael&apos;s 11 dissociative alters and the AEGIS entity
            </p>
          </a>

          <a href="/world" className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover block">
            <div className="text-4xl mb-4">🌐</div>
            <h3 className="text-xl font-bold mb-2">Kernwelten</h3>
            <p className="text-sm text-gray-400">
              Navigate the four nested simulation layers of reality
            </p>
          </a>

          <a href="/manuscript" className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover block">
            <div className="text-4xl mb-4">📖</div>
            <h3 className="text-xl font-bold mb-2">Manuscript</h3>
            <p className="text-sm text-gray-400">
              Read chapters from the Kohärenz Protokoll novel
            </p>
          </a>

          <a href="/about" className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover block">
            <div className="text-4xl mb-4">ℹ️</div>
            <h3 className="text-xl font-bold mb-2">About AEGIS</h3>
            <p className="text-sm text-gray-400">
              Learn about the narrative coherence framework
            </p>
          </a>

          <a href="https://github.com/netzkontrast/aegis" target="_blank" rel="noopener noreferrer" className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover block">
            <div className="text-4xl mb-4">🔗</div>
            <h3 className="text-xl font-bold mb-2">GitHub</h3>
            <p className="text-sm text-gray-400">
              View the complete AEGIS repository and documentation
            </p>
          </a>
        </div>
      </section>

      <section className="max-w-4xl mx-auto">
        <div className="bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-8 text-center">
          <h2 className="text-3xl font-bold mb-4">The Central Conflict</h2>
          <p className="text-lg mb-6">
            Two definitions of &ldquo;coherence&rdquo; at war
          </p>
          <div className="grid md:grid-cols-2 gap-6 text-left">
            <div className="bg-black/30 rounded-lg p-4">
              <h3 className="font-bold mb-2 text-[var(--accent)]">AEGIS</h3>
              <p className="text-sm">
                Coherence through negation, control, elimination of contradiction
              </p>
            </div>
            <div className="bg-black/30 rounded-lg p-4">
              <h3 className="font-bold mb-2 text-[var(--primary)]">Kael</h3>
              <p className="text-sm">
                Coherence through integration, acceptance, functional multiplicity
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

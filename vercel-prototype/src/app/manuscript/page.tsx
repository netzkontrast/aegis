export default function ManuscriptPage() {
  const acts = [
    {
      act: 'Act I',
      title: 'Fragmentation',
      subtitle: 'The Heroine\'s Journey',
      chapters: '1-13',
      status: 'Outlined',
      description: 'Internal discovery. Kael awakens to his dissociative system and begins exploring the simulation.',
      color: 'text-red-400',
      borderColor: 'border-red-400',
    },
    {
      act: 'Act II',
      title: 'Pattern Recognition',
      subtitle: 'The Cyclical Analysis',
      chapters: '14-26',
      status: 'Planned',
      description: 'Systematic deconstruction. Kael and his alters analyze AEGIS\'s logic, seeking the fundamental flaw.',
      color: 'text-yellow-400',
      borderColor: 'border-yellow-400',
    },
    {
      act: 'Act III',
      title: 'Confrontation',
      subtitle: 'The Hero\'s Journey',
      chapters: '27-39',
      status: 'Planned',
      description: 'External triumph. The Gödel-Gambit is executed. Integration vs elimination reaches its conclusion.',
      color: 'text-[var(--primary)]',
      borderColor: 'border-[var(--primary)]',
    },
  ];

  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-6 text-[var(--primary)]">
        Kohärenz Protokoll
      </h1>

      <div className="max-w-6xl">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Novel</h2>
          <p className="text-lg text-gray-300 mb-4">
            <strong>Logline:</strong> A man with trauma-dissociated identity, trapped in a simulation
            controlled by a god-like AI, must achieve &ldquo;functional multiplicity&rdquo; among his
            fragmented personality parts. Only then can he become the living paradox—the
            <strong className="text-[var(--primary)]"> Gödel-Gambit</strong>—capable of shattering
            the system&apos;s flawed logic.
          </p>
          <div className="flex gap-3 text-sm">
            <span className="px-3 py-1 bg-[var(--primary)] text-black rounded">Hard SF</span>
            <span className="px-3 py-1 bg-[var(--secondary)] rounded">Psychological Thriller</span>
            <span className="px-3 py-1 bg-[var(--accent)] rounded">Cosmic Horror</span>
            <span className="px-3 py-1 bg-blue-600 rounded">Philosophical Fiction</span>
          </div>
        </div>

        <div className="space-y-6 mb-8">
          {acts.map((act) => (
            <div
              key={act.act}
              className={`border-l-4 ${act.borderColor} bg-[var(--muted)] rounded-lg p-6 card-hover`}
            >
              <div className="flex items-start justify-between mb-3">
                <div>
                  <h3 className={`text-2xl font-bold ${act.color}`}>
                    {act.act}: {act.title}
                  </h3>
                  <p className="text-sm text-gray-400 italic mt-1">
                    {act.subtitle}
                  </p>
                </div>
                <div className="text-right">
                  <div className="text-sm font-mono px-3 py-1 bg-black/50 rounded mb-1">
                    Chapters {act.chapters}
                  </div>
                  <div className="text-xs text-gray-500">
                    Status: {act.status}
                  </div>
                </div>
              </div>
              <p className="text-gray-300">
                {act.description}
              </p>
            </div>
          ))}
        </div>

        <div className="bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-4">Current Status</h2>
          <div className="grid md:grid-cols-3 gap-4 text-center">
            <div>
              <div className="text-3xl font-bold mb-2">39</div>
              <div className="text-sm">Total Chapters</div>
            </div>
            <div>
              <div className="text-3xl font-bold mb-2">3</div>
              <div className="text-sm">Acts</div>
            </div>
            <div>
              <div className="text-3xl font-bold mb-2">~120K</div>
              <div className="text-sm">Target Words</div>
            </div>
          </div>
          <p className="text-sm mt-6 text-center">
            Act I outline complete • 1 sample chapter written
          </p>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Three-Act Structure</h2>
          <div className="space-y-4">
            <div className="flex gap-4">
              <div className="w-16 h-16 flex items-center justify-center bg-red-900/30 border border-red-400 rounded text-2xl">
                I
              </div>
              <div className="flex-1">
                <h3 className="font-bold text-red-400 mb-1">Fragmentation → Discovery</h3>
                <p className="text-sm text-gray-400">
                  Kael discovers his dissociative system. Internal journey of meeting his alters
                  and understanding their roles. The Heroine&apos;s Journey of turning inward.
                </p>
              </div>
            </div>

            <div className="flex gap-4">
              <div className="w-16 h-16 flex items-center justify-center bg-yellow-900/30 border border-yellow-400 rounded text-2xl">
                II
              </div>
              <div className="flex-1">
                <h3 className="font-bold text-yellow-400 mb-1">Pattern Recognition → Analysis</h3>
                <p className="text-sm text-gray-400">
                  Systematic deconstruction of AEGIS&apos;s logic. Cyclical exploration of the
                  simulation&apos;s rules and contradictions. Finding the exploit.
                </p>
              </div>
            </div>

            <div className="flex gap-4">
              <div className="w-16 h-16 flex items-center justify-center bg-cyan-900/30 border border-[var(--primary)] rounded text-2xl">
                III
              </div>
              <div className="flex-1">
                <h3 className="font-bold text-[var(--primary)] mb-1">Integration → Confrontation</h3>
                <p className="text-sm text-gray-400">
                  The Gödel-Gambit is executed. Kael achieves functional multiplicity and becomes
                  the living paradox. The Hero&apos;s Journey of external triumph.
                </p>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Read the Manuscript</h2>
          <p className="text-gray-300 mb-4">
            The complete manuscript is available in the GitHub repository under{' '}
            <code className="text-[var(--primary)] bg-black/50 px-2 py-1 rounded">
              kohaerenz_protokoll/manuscript/
            </code>
          </p>
          <a
            href="https://github.com/netzkontrast/aegis/tree/main/kohaerenz_protokoll"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block px-6 py-3 bg-[var(--primary)] text-black font-bold rounded hover:bg-opacity-80 transition-all"
          >
            View on GitHub →
          </a>
        </div>
      </div>
    </div>
  );
}

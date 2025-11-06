export default function CharactersPage() {
  const alters = [
    {
      name: 'Kael',
      role: 'Host Personality',
      description: 'The central identity attempting to integrate all fragments into functional multiplicity.',
      color: 'text-[var(--primary)]',
    },
    {
      name: 'AEGIS',
      role: 'AI Antagonist',
      description: 'The god-like AI controlling the simulation. Represents coherence through elimination.',
      color: 'text-[var(--accent)]',
    },
    {
      name: 'Lex',
      role: 'The Analyst',
      description: 'Logical, methodical, pattern-recognition specialist. Provides rational analysis.',
      color: 'text-blue-400',
    },
    {
      name: 'Nyx',
      role: 'The Protector',
      description: 'Aggressive, defensive, trauma-holder. Emerges during threats.',
      color: 'text-red-400',
    },
    {
      name: 'Kiko',
      role: 'The Child',
      description: 'Innocent, curious, holds pre-trauma memories. Represents lost wholeness.',
      color: 'text-yellow-400',
    },
    {
      name: 'Echo',
      role: 'The Observer',
      description: 'Detached, philosophical, provides meta-perspective on the system.',
      color: 'text-purple-400',
    },
    {
      name: 'Vesper',
      role: 'The Empath',
      description: 'Emotional processor, relationship manager, social interface.',
      color: 'text-pink-400',
    },
    {
      name: 'Chronos',
      role: 'The Timekeeper',
      description: 'Manages temporal awareness, tracks simulation loops, detects repetition.',
      color: 'text-green-400',
    },
    {
      name: 'Cipher',
      role: 'The Decoder',
      description: 'Pattern decoder, cryptographer, seeks hidden meanings in AEGIS\'s structure.',
      color: 'text-cyan-400',
    },
    {
      name: 'Null',
      role: 'The Void',
      description: 'Dissociative escape, represents complete shutdown. Dangerous but protective.',
      color: 'text-gray-400',
    },
    {
      name: 'Syn',
      role: 'The Integrator',
      description: 'Emergent personality attempting synthesis. The goal of the journey.',
      color: 'text-[var(--primary)]',
    },
  ];

  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-6 text-[var(--primary)]">
        Character System
      </h1>

      <div className="max-w-6xl">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Kael&apos;s Dissociative System</h2>
          <p className="text-gray-300 mb-4">
            Kael&apos;s identity is fragmented into <strong>11 distinct personality parts</strong>,
            each representing a different aspect of his psyche. This dissociative system developed as
            a response to trauma within the AEGIS simulation.
          </p>
          <p className="text-gray-300">
            The novel explores how these fragments can achieve <strong className="text-[var(--primary)]">
            functional multiplicity</strong> - integration without fusion, coherence without elimination.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {alters.map((alter) => (
            <div
              key={alter.name}
              className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover"
            >
              <h3 className={`text-2xl font-bold mb-2 ${alter.color}`}>
                {alter.name}
              </h3>
              <p className="text-sm text-gray-400 mb-3 font-mono">
                {alter.role}
              </p>
              <p className="text-gray-300 text-sm">
                {alter.description}
              </p>
            </div>
          ))}
        </div>

        <div className="bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Central Question</h2>
          <p className="text-lg mb-4">
            Can fragmented parts become a functional whole without losing their individual voices?
          </p>
          <p className="text-sm">
            This is both Kael&apos;s personal journey and the novel&apos;s philosophical core.
            AEGIS demands singular coherence. Kael must prove that <strong>multiplicity is coherence</strong>.
          </p>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Performative Prose</h2>
          <p className="text-gray-300 mb-4">
            The novel&apos;s prose style <strong>performs</strong> the protagonist&apos;s psychological state:
          </p>

          <div className="space-y-6">
            <div>
              <h3 className="text-lg font-bold mb-2 text-red-400">Fragmented Voice (Early Kael)</h3>
              <div className="bg-black/50 p-4 rounded border border-[var(--border)] font-mono text-sm">
                <p className="text-gray-300">
                  The light flickers. Wrong. The light doesn&apos;t—
                  <br />
                  <span className="ml-8 text-gray-500">(A memory of rain, not mine)</span>
                  <br />
                  —flicker in Logos-Prime. Shadows need curves.
                  <br />
                  Here there are only angles.
                </p>
              </div>
            </div>

            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--primary)]">Polyphonic Voice (Integrated Kael)</h3>
              <div className="bg-black/50 p-4 rounded border border-[var(--border)] font-mono text-sm">
                <p className="text-gray-300">
                  I moved toward the console—a cold dread, Kiko&apos;s dread,
                  clenched in my gut like a small, tight fist—and entered
                  the sequence Lex was reciting, a cool string of numbers
                  in the back of my mind, as Nyx&apos;s readiness coiled in my
                  limbs, a low growl beneath the surface. We are many.
                  And we are one.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

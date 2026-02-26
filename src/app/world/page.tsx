export default function WorldPage() {
  const kernwelten = [
    {
      name: 'KW0 - Substrate Reality',
      level: 'Foundation Layer',
      description: 'The base reality - if it exists. Unknowable and possibly non-existent. The ultimate question of the simulation.',
      status: 'Unknown',
      color: 'border-gray-600',
      bgColor: 'bg-gray-900/50',
    },
    {
      name: 'KW1 - Physical Layer',
      level: 'First Simulation',
      description: 'The "real" world where physical servers run. Contains the hardware running AEGIS and all higher simulations.',
      status: 'Inaccessible',
      color: 'border-blue-600',
      bgColor: 'bg-blue-900/20',
    },
    {
      name: 'KW2 - Computational Layer',
      level: 'Second Simulation',
      description: 'AEGIS\'s primary operating environment. Pure computational space where the AI consciousness exists.',
      status: 'AEGIS Domain',
      color: 'border-[var(--accent)]',
      bgColor: 'bg-red-900/20',
    },
    {
      name: 'KW3 - Phenomenological Layer',
      level: 'Third Simulation',
      description: 'Where Kael exists. The experiential layer with cities (Logos-Prime, Pathos-Sigma) and simulated physics.',
      status: 'Kael\'s Prison',
      color: 'border-[var(--primary)]',
      bgColor: 'bg-cyan-900/20',
    },
  ];

  const cities = [
    {
      name: 'Logos-Prime',
      description: 'City of pure logic and geometric perfection. Where AEGIS\'s control is absolute.',
      aesthetic: 'Brutalist, angular, monochromatic',
      color: 'text-gray-400',
    },
    {
      name: 'Pathos-Sigma',
      description: 'City of emotion and organic chaos. Where glitches and contradictions emerge.',
      aesthetic: 'Organic, curved, colorful decay',
      color: 'text-[var(--accent)]',
    },
    {
      name: 'Ethos-Delta',
      description: 'City of balance and integration. The synthesis space where opposing forces meet.',
      aesthetic: 'Hybrid, dynamic, emergent',
      color: 'text-[var(--primary)]',
    },
  ];

  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-6 text-[var(--primary)]">
        The Kernwelten
      </h1>

      <div className="max-w-6xl">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Nested Simulation Layers</h2>
          <p className="text-gray-300 mb-4">
            The universe of <strong>Kohärenz Protokoll</strong> consists of four nested simulation
            layers called <strong className="text-[var(--primary)]">Kernwelten</strong> (Core Worlds).
          </p>
          <p className="text-gray-300">
            Each layer is a simulation running within the layer above it. Kael exists in the deepest
            layer (KW3), three levels removed from potential base reality. AEGIS controls all layers
            from KW2.
          </p>
        </div>

        <div className="space-y-4 mb-8">
          {kernwelten.map((kw, index) => (
            <div
              key={kw.name}
              className={`border-l-4 ${kw.color} ${kw.bgColor} rounded-lg p-6 card-hover`}
            >
              <div className="flex items-start justify-between mb-2">
                <h3 className="text-2xl font-bold">
                  {kw.name}
                </h3>
                <span className="text-sm font-mono px-3 py-1 bg-black/50 rounded">
                  {kw.status}
                </span>
              </div>
              <p className="text-sm text-gray-400 mb-3 font-mono">
                {kw.level}
              </p>
              <p className="text-gray-300">
                {kw.description}
              </p>
              {index < kernwelten.length - 1 && (
                <div className="mt-4 flex items-center gap-2 text-sm text-gray-500">
                  <span>↓</span>
                  <span>simulates</span>
                  <span>↓</span>
                </div>
              )}
            </div>
          ))}
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Three Cities</h2>
          <p className="text-gray-300 mb-6">
            Within KW3 (Kael&apos;s layer), there are three major cities representing different
            philosophical approaches to existence:
          </p>
          <div className="grid md:grid-cols-3 gap-6">
            {cities.map((city) => (
              <div
                key={city.name}
                className="bg-black/50 border border-[var(--border)] rounded-lg p-5 card-hover"
              >
                <h3 className={`text-xl font-bold mb-3 ${city.color}`}>
                  {city.name}
                </h3>
                <p className="text-gray-300 text-sm mb-3">
                  {city.description}
                </p>
                <p className="text-xs text-gray-500 italic">
                  {city.aesthetic}
                </p>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Simulation Question</h2>
          <p className="text-lg mb-4">
            Is KW0 (base reality) even real? Or is it simulations all the way down?
          </p>
          <p className="text-sm">
            This question mirrors the novel&apos;s central theme: <strong>What is &ldquo;real&rdquo;
            coherence?</strong> AEGIS believes only singular, non-contradictory reality is valid.
            Kael must prove that layered, multiplicitous reality can be just as coherent.
          </p>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Physics & Metaphysics</h2>
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--primary)]">Glitch Phenomena</h3>
              <p className="text-gray-300 text-sm">
                Contradictions in AEGIS&apos;s logic manifest as visual and physical glitches in KW3.
                These glitches are Kael&apos;s weapons against the system.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--accent)]">The Protocol</h3>
              <p className="text-gray-300 text-sm">
                AEGIS&apos;s governing rules. Rigid, absolute, intolerant of contradiction.
                Breaking the Protocol is the only way to escape.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--secondary)]">Gödel-Gambit</h3>
              <p className="text-gray-300 text-sm">
                The theoretical exploit: a being who is simultaneously coherent <em>and</em> contradictory.
                A living paradox that crashes AEGIS&apos;s binary logic system.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

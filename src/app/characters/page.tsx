import type { Metadata } from "next";

export const metadata: Metadata = { title: "Characters" };

const alters = [
  {
    name: "Kael",
    role: "Host Personality",
    description:
      "The central identity attempting to integrate all fragments into functional multiplicity.",
    color: "text-[var(--primary)]",
  },
  {
    name: "AEGIS",
    role: "AI Antagonist",
    description:
      "The god-like AI controlling the simulation. Represents coherence through elimination.",
    color: "text-[var(--accent)]",
  },
  {
    name: "Lex",
    role: "The Analyst",
    description:
      "Logical, methodical, pattern-recognition specialist. Provides rational analysis.",
    color: "text-blue-400",
  },
  {
    name: "Nyx",
    role: "The Protector",
    description:
      "Aggressive, defensive, trauma-holder. Emerges during threats.",
    color: "text-red-400",
  },
  {
    name: "Kiko",
    role: "The Child",
    description:
      "Innocent, curious, holds pre-trauma memories. Represents lost wholeness.",
    color: "text-yellow-400",
  },
  {
    name: "Rhys",
    role: "The Caregiver",
    description:
      "Gentle, empathetic, warm. Handles emotional processing and connection.",
    color: "text-green-400",
  },
  {
    name: "Alex",
    role: "The Strategist",
    description:
      "Adaptive, diplomatic, crisis manager. Maintains facades and navigates social dynamics.",
    color: "text-orange-400",
  },
  {
    name: "Selene",
    role: "Internal Self Helper",
    description:
      "The ISH - mediates between alters, maintains internal system awareness and navigation.",
    color: "text-indigo-400",
  },
  {
    name: "Lia",
    role: "The Connector",
    description:
      "Attachment-seeking, connection-oriented. Bridges between internal parts and external world.",
    color: "text-pink-400",
  },
  {
    name: "Argus",
    role: "The Observer",
    description:
      "Detached, meta-cognitive. Provides bird's-eye perspective on the system.",
    color: "text-purple-400",
  },
  {
    name: "Moros",
    role: "The Void",
    description:
      "Existential collapse, dissociative escape. The dangerous shutdown state.",
    color: "text-gray-400",
  },
];

export default function CharactersPage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-6 text-[var(--primary)]">
        Character System
      </h1>

      <div className="max-w-6xl">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">
            Kael&apos;s Dissociative System
          </h2>
          <p className="text-gray-300 mb-4">
            Kael&apos;s identity is fragmented into{" "}
            <strong>11 distinct personality parts</strong>, each representing a
            different aspect of his psyche. This dissociative system developed as
            a response to trauma within the AEGIS simulation.
          </p>
          <p className="text-gray-300">
            The novel explores how these fragments can achieve{" "}
            <strong className="text-[var(--primary)]">
              functional multiplicity
            </strong>{" "}
            - integration without fusion, coherence without elimination.
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
              <p className="text-gray-300 text-sm">{alter.description}</p>
            </div>
          ))}
        </div>

        <div className="bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-4">The Central Question</h2>
          <p className="text-lg mb-4">
            Can fragmented parts become a functional whole without losing their
            individual voices?
          </p>
          <p className="text-sm">
            This is both Kael&apos;s personal journey and the novel&apos;s
            philosophical core. AEGIS demands singular coherence. Kael must prove
            that <strong>multiplicity is coherence</strong>.
          </p>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Performative Prose</h2>
          <p className="text-gray-300 mb-4">
            The novel&apos;s prose style <strong>performs</strong> the
            protagonist&apos;s psychological state:
          </p>
          <div className="space-y-6">
            <div>
              <h3 className="text-lg font-bold mb-2 text-red-400">
                Fragmented Voice (Early Kael)
              </h3>
              <div className="bg-black/50 p-4 rounded border border-[var(--border)] font-mono text-sm">
                <p className="text-gray-300">
                  The light flickers. Wrong. The light doesn&apos;t&mdash;
                  <br />
                  <span className="ml-8 text-gray-500">
                    (A memory of rain, not mine)
                  </span>
                  <br />
                  &mdash;flicker in Logos-Prime. Shadows need curves.
                  <br />
                  Here there are only angles.
                </p>
              </div>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-2 text-[var(--primary)]">
                Polyphonic Voice (Integrated Kael)
              </h3>
              <div className="bg-black/50 p-4 rounded border border-[var(--border)] font-mono text-sm">
                <p className="text-gray-300">
                  I moved toward the console&mdash;a cold dread, Kiko&apos;s
                  dread, clenched in my gut like a small, tight fist&mdash;and
                  entered the sequence Lex was reciting, a cool string of
                  numbers in the back of my mind, as Nyx&apos;s readiness coiled
                  in my limbs, a low growl beneath the surface. We are many. And
                  we are one.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

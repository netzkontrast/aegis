import Link from "next/link";
import { getChapters, getEntities, getQuests } from "@/lib/content";

export default function Home() {
  const chapters = getChapters();
  const entities = getEntities();
  const quests = getQuests();

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
        <h2 className="text-3xl font-bold mb-6 text-[var(--primary)]">
          The Dual Project
        </h2>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <h3 className="text-2xl font-bold mb-3 text-[var(--primary)]">
              AEGIS
            </h3>
            <p className="text-sm text-gray-400 mb-2">The Meta-Framework</p>
            <p className="text-gray-300">
              A functional implementation of an AI-assisted narrative coherence
              system, designed to maintain thematic depth and structural
              integrity across novel-length works.
            </p>
            <ul className="mt-4 space-y-2 text-sm text-gray-400">
              <li>&rarr; Formal authorial intent via NCP</li>
              <li>&rarr; Externalized memory via knowledge graphs</li>
              <li>&rarr; Agentic reasoning via systematic validation</li>
            </ul>
          </div>

          <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 card-hover">
            <h3 className="text-2xl font-bold mb-3 text-[var(--accent)]">
              Kohärenz Protokoll
            </h3>
            <p className="text-sm text-gray-400 mb-2">The Novel</p>
            <p className="text-gray-300">
              A philosophical science fiction work about a man with dissociative
              identity disorder trapped in a simulation controlled by a god-like
              AI.
            </p>
            <ul className="mt-4 space-y-2 text-sm text-gray-400">
              <li>&rarr; Hard SF + Psychological Thriller</li>
              <li>&rarr; Cosmic Horror + Philosophical Fiction</li>
              <li>&rarr; 39 chapters across three acts</li>
            </ul>
          </div>
        </div>
      </section>

      <section className="max-w-4xl mx-auto mb-16">
        <h2 className="text-3xl font-bold mb-6 text-[var(--secondary)]">
          The Meta-Recursive Design
        </h2>
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-8">
          <p className="text-lg text-gray-300 mb-6">
            This repository{" "}
            <strong className="text-[var(--primary)]">
              performs its own themes
            </strong>
            :
          </p>
          <div className="space-y-4">
            <div className="flex items-start gap-4">
              <span className="text-2xl w-8">&#x1F527;</span>
              <div>
                <strong className="text-[var(--primary)]">AEGIS</strong> seeks
                to maintain narrative coherence through formal systems
              </div>
            </div>
            <div className="flex items-start gap-4">
              <span className="text-2xl w-8">&#x1F916;</span>
              <div>
                <strong className="text-[var(--accent)]">AEGIS</strong> (the AI
                antagonist) seeks to maintain system coherence through rigid
                control
              </div>
            </div>
            <div className="flex items-start gap-4">
              <span className="text-2xl w-8">&#x1F3AF;</span>
              <div>
                <strong className="text-[var(--secondary)]">Both</strong>{" "}
                discover that true coherence emerges from integration, not
                elimination
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="max-w-5xl mx-auto mb-16">
        <h2 className="text-3xl font-bold mb-6 text-[var(--primary)]">
          Explore the System
        </h2>
        <div className="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
          <Link
            href="/manuscript"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x1F4D6;</div>
            <h3 className="text-lg font-bold mb-1">Manuscript</h3>
            <p className="text-sm text-gray-400">
              {chapters.length} chapters across 3 acts
            </p>
          </Link>

          <Link
            href="/characters"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x1F465;</div>
            <h3 className="text-lg font-bold mb-1">Characters</h3>
            <p className="text-sm text-gray-400">
              Kael&apos;s dissociative alter system
            </p>
          </Link>

          <Link
            href="/entities"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x1F4DA;</div>
            <h3 className="text-lg font-bold mb-1">Entities</h3>
            <p className="text-sm text-gray-400">
              {entities.length} character & world profiles
            </p>
          </Link>

          <Link
            href="/world"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x1F30C;</div>
            <h3 className="text-lg font-bold mb-1">Kernwelten</h3>
            <p className="text-sm text-gray-400">
              Four nested simulation layers
            </p>
          </Link>

          <Link
            href="/quests"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x2694;&#xFE0F;</div>
            <h3 className="text-lg font-bold mb-1">Quests</h3>
            <p className="text-sm text-gray-400">
              {quests.length} active development quests
            </p>
          </Link>

          <Link
            href="/ncp"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x1F4CA;</div>
            <h3 className="text-lg font-bold mb-1">NCP Query</h3>
            <p className="text-sm text-gray-400">
              Query narrative constraints live
            </p>
          </Link>

          <Link
            href="/about"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x2139;&#xFE0F;</div>
            <h3 className="text-lg font-bold mb-1">About ARCHON</h3>
            <p className="text-sm text-gray-400">
              The narrative coherence framework
            </p>
          </Link>

          <a
            href="https://github.com/netzkontrast/aegis"
            target="_blank"
            rel="noopener noreferrer"
            className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
          >
            <div className="text-3xl mb-3">&#x1F517;</div>
            <h3 className="text-lg font-bold mb-1">GitHub</h3>
            <p className="text-sm text-gray-400">Source code & documentation</p>
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
                Coherence through negation, control, elimination of
                contradiction
              </p>
            </div>
            <div className="bg-black/30 rounded-lg p-4">
              <h3 className="font-bold mb-2 text-[var(--primary)]">Kael</h3>
              <p className="text-sm">
                Coherence through integration, acceptance, functional
                multiplicity
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

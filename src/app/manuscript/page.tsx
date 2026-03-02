import type { Metadata } from "next";
import Link from "next/link";
import { getChapters } from "@/lib/content";

export const metadata: Metadata = { title: "Manuscript" };

export default function ManuscriptPage() {
  const chapters = getChapters();

  const acts = [
    {
      num: "I",
      title: "Die Innere Reise",
      subtitle: "Fragmentation & Awakening",
      range: [1, 13],
      color: "text-red-400",
      border: "border-red-400",
      bg: "bg-red-900/20",
    },
    {
      num: "II",
      title: "Die Dekodierung",
      subtitle: "Pattern Recognition & Failure of Control",
      range: [14, 26],
      color: "text-yellow-400",
      border: "border-yellow-400",
      bg: "bg-yellow-900/20",
    },
    {
      num: "III",
      title: "Die Transzendenz",
      subtitle: "Integration & Confrontation",
      range: [27, 39],
      color: "text-[var(--primary)]",
      border: "border-[var(--primary)]",
      bg: "bg-cyan-900/20",
    },
  ];

  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-2 text-[var(--primary)]">
        Kohärenz Protokoll
      </h1>
      <p className="text-gray-400 mb-8">
        {chapters.length} chapters &middot; 3 acts &middot; ~130K target words
      </p>

      <div className="max-w-4xl mb-12">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <p className="text-lg text-gray-300">
            <strong>Logline:</strong> A man with trauma-dissociated identity,
            trapped in a simulation controlled by a god-like AI, must achieve
            &ldquo;functional multiplicity&rdquo; among his fragmented
            personality parts to become the living paradox&mdash;the{" "}
            <strong className="text-[var(--primary)]">
              G&ouml;del-Gambit
            </strong>
            &mdash;capable of shattering the system&apos;s flawed logic.
          </p>
          <div className="flex gap-3 mt-4 text-sm flex-wrap">
            <span className="px-3 py-1 bg-[var(--primary)] text-black rounded">
              Hard SF
            </span>
            <span className="px-3 py-1 bg-[var(--secondary)] rounded">
              Psychological Thriller
            </span>
            <span className="px-3 py-1 bg-[var(--accent)] rounded">
              Cosmic Horror
            </span>
            <span className="px-3 py-1 bg-blue-600 rounded">
              Philosophical Fiction
            </span>
          </div>
        </div>
      </div>

      {acts.map((act) => {
        const actChapters = chapters.filter(
          (c) => c.number >= act.range[0] && c.number <= act.range[1]
        );

        return (
          <div key={act.num} className="max-w-4xl mb-10">
            <div
              className={`border-l-4 ${act.border} ${act.bg} rounded-lg p-5 mb-4`}
            >
              <h2 className={`text-2xl font-bold ${act.color}`}>
                Act {act.num}: {act.title}
              </h2>
              <p className="text-sm text-gray-400 italic">{act.subtitle}</p>
              <p className="text-xs text-gray-500 mt-1">
                Chapters {act.range[0]}&ndash;{act.range[1]} &middot;{" "}
                {actChapters.length} chapters
              </p>
            </div>

            <div className="space-y-2">
              {actChapters.map((ch) => (
                <Link
                  key={ch.number}
                  href={`/manuscript/${ch.slug}`}
                  className="block bg-[var(--muted)] border border-[var(--border)] rounded-lg p-4 card-hover"
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <span className="text-sm text-gray-500 font-mono mr-3">
                        {String(ch.number).padStart(2, "0")}
                      </span>
                      <span className="font-semibold">{ch.title}</span>
                    </div>
                    {ch.kState && (
                      <span className="text-xs text-gray-500 font-mono">
                        {ch.kState}
                      </span>
                    )}
                  </div>
                  {ch.coreEvent && (
                    <p className="text-sm text-gray-400 mt-1 ml-9">
                      {ch.coreEvent}
                    </p>
                  )}
                </Link>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}

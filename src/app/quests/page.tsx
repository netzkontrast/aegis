import type { Metadata } from "next";
import Link from "next/link";
import { getQuests } from "@/lib/content";

export const metadata: Metadata = { title: "Quests" };

export default function QuestsPage() {
  const quests = getQuests();

  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-2 text-[var(--primary)]">
        Quest Dashboard
      </h1>
      <p className="text-gray-400 mb-8">
        {quests.length} active development quests driving the AEGIS project
        forward
      </p>

      <div className="max-w-4xl">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-xl font-bold mb-3">About Quests</h2>
          <p className="text-gray-300 text-sm">
            Quests are the primary development methodology for AEGIS.
            Each quest focuses on a specific domain &mdash; narrative structure,
            character systems, world physics, tool implementation, and more.
            They track consolidated knowledge, verification steps, and next
            actions.
          </p>
        </div>

        <div className="space-y-3">
          {quests.map((quest) => (
            <Link
              key={quest.slug}
              href={`/quests/${quest.slug}`}
              className="block bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover"
            >
              <div className="flex items-center justify-between">
                <h3 className="text-lg font-bold">{quest.title}</h3>
                <span className="text-xs text-gray-500 font-mono">
                  {quest.filename}
                </span>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}

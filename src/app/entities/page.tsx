import type { Metadata } from "next";
import Link from "next/link";
import { getEntities } from "@/lib/content";

export const metadata: Metadata = { title: "Entities" };

const typeColors: Record<string, string> = {
  Protagonist: "bg-[var(--primary)] text-black",
  Antagonist: "bg-[var(--accent)]",
  Alter: "bg-[var(--secondary)]",
  World: "bg-blue-600",
  Faction: "bg-orange-600",
  Entity: "bg-gray-600",
};

export default function EntitiesPage() {
  const entities = getEntities();

  const grouped = {
    Protagonist: entities.filter((e) => e.type === "Protagonist"),
    Antagonist: entities.filter((e) => e.type === "Antagonist"),
    Alter: entities.filter((e) => e.type === "Alter"),
    World: entities.filter((e) => e.type === "World"),
    Faction: entities.filter((e) => e.type === "Faction"),
  };

  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-2 text-[var(--primary)]">
        Entity Codex
      </h1>
      <p className="text-gray-400 mb-8">
        {entities.length} character profiles, world systems, and factions
      </p>

      {Object.entries(grouped).map(
        ([type, items]) =>
          items.length > 0 && (
            <div key={type} className="max-w-4xl mb-10">
              <h2 className="text-2xl font-bold mb-4 text-gray-300">{type}s</h2>
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                {items.map((entity) => (
                  <Link
                    key={entity.slug}
                    href={`/entities/${entity.slug}`}
                    className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-5 card-hover block"
                  >
                    <div className="flex items-start justify-between mb-2">
                      <h3 className="text-lg font-bold">{entity.name}</h3>
                      <span
                        className={`text-xs px-2 py-0.5 rounded ${
                          typeColors[entity.type] || "bg-gray-600"
                        }`}
                      >
                        {entity.type}
                      </span>
                    </div>
                    <p className="text-sm text-gray-500 font-mono">
                      {entity.filename}
                    </p>
                  </Link>
                ))}
              </div>
            </div>
          )
      )}
    </div>
  );
}

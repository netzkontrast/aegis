import type { Metadata } from "next";
import Link from "next/link";
import {
  getEntities,
  getEntityContent,
  markdownToHtml,
} from "@/lib/content";
import { notFound } from "next/navigation";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getEntities().map((e) => ({ slug: e.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const entity = getEntities().find((e) => e.slug === slug);
  return { title: entity?.name || "Entity" };
}

export default async function EntityPage({ params }: Props) {
  const { slug } = await params;
  const entities = getEntities();
  const entity = entities.find((e) => e.slug === slug);

  if (!entity) notFound();

  const content = getEntityContent(slug);
  if (!content) notFound();

  const html = markdownToHtml(content);

  const typeColors: Record<string, string> = {
    Protagonist: "bg-[var(--primary)] text-black",
    Antagonist: "bg-[var(--accent)]",
    Alter: "bg-[var(--secondary)]",
    World: "bg-blue-600",
    Faction: "bg-orange-600",
    Entity: "bg-gray-600",
  };

  return (
    <div className="container mx-auto px-4 py-12 max-w-4xl">
      <div className="mb-6">
        <Link
          href="/entities"
          className="text-sm text-gray-400 hover:text-[var(--primary)] transition-colors"
        >
          &larr; All Entities
        </Link>
      </div>

      <div className="mb-8 flex items-start justify-between">
        <div>
          <h1 className="text-3xl font-bold text-[var(--primary)]">
            {entity.name}
          </h1>
          <p className="text-sm text-gray-500 font-mono mt-1">
            {entity.filename}
          </p>
        </div>
        <span
          className={`text-sm px-3 py-1 rounded ${
            typeColors[entity.type] || "bg-gray-600"
          }`}
        >
          {entity.type}
        </span>
      </div>

      <article
        className="prose-aegis"
        dangerouslySetInnerHTML={{ __html: html }}
      />
    </div>
  );
}

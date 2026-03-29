import type { Metadata } from "next";
import Link from "next/link";
import { getQuests, getQuestContent, markdownToHtml } from "@/lib/content";
import { notFound } from "next/navigation";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getQuests().map((q) => ({ slug: q.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const quest = getQuests().find((q) => q.slug === slug);
  return { title: quest?.title || "Quest" };
}

export default async function QuestPage({ params }: Props) {
  const { slug } = await params;
  const quests = getQuests();
  const quest = quests.find((q) => q.slug === slug);

  if (!quest) notFound();

  const content = getQuestContent(slug);
  if (!content) notFound();

  const html = markdownToHtml(content);

  return (
    <div className="container mx-auto px-4 py-12 max-w-4xl">
      <div className="mb-6">
        <Link
          href="/quests"
          className="text-sm text-gray-400 hover:text-[var(--primary)] transition-colors"
        >
          &larr; All Quests
        </Link>
      </div>

      <div className="mb-8">
        <h1 className="text-3xl font-bold text-[var(--primary)]">
          {quest.title}
        </h1>
        <p className="text-sm text-gray-500 font-mono mt-1">
          {quest.filename}
        </p>
      </div>

      <article
        className="prose-aegis"
        dangerouslySetInnerHTML={{ __html: html }}
      />
    </div>
  );
}

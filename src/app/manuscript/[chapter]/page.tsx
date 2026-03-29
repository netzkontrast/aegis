import type { Metadata } from "next";
import Link from "next/link";
import { getChapters, getChapterContent, markdownToHtml } from "@/lib/content";
import { notFound } from "next/navigation";

interface Props {
  params: Promise<{ chapter: string }>;
}

export async function generateStaticParams() {
  return getChapters().map((ch) => ({ chapter: ch.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { chapter } = await params;
  const chapters = getChapters();
  const ch = chapters.find((c) => c.slug === chapter);
  return { title: ch ? `Ch ${ch.number}: ${ch.title}` : "Chapter" };
}

export default async function ChapterPage({ params }: Props) {
  const { chapter } = await params;
  const chapters = getChapters();
  const chapterInfo = chapters.find((c) => c.slug === chapter);

  if (!chapterInfo) notFound();

  const content = getChapterContent(chapterInfo.number);
  if (!content) notFound();

  const html = markdownToHtml(content);

  const currentIdx = chapters.findIndex((c) => c.slug === chapter);
  const prev = currentIdx > 0 ? chapters[currentIdx - 1] : null;
  const next =
    currentIdx < chapters.length - 1 ? chapters[currentIdx + 1] : null;

  return (
    <div className="container mx-auto px-4 py-12 max-w-4xl">
      <div className="mb-6">
        <Link
          href="/manuscript"
          className="text-sm text-gray-400 hover:text-[var(--primary)] transition-colors"
        >
          &larr; All Chapters
        </Link>
      </div>

      <div className="mb-8">
        <p className="text-sm text-gray-500 font-mono mb-1">
          Chapter {chapterInfo.number} &middot; {chapterInfo.act}
        </p>
        <h1 className="text-3xl font-bold text-[var(--primary)]">
          {chapterInfo.title}
        </h1>
        {chapterInfo.kState && (
          <p className="text-sm text-gray-400 mt-2 font-mono">
            {chapterInfo.kState}
          </p>
        )}
      </div>

      <article
        className="prose-aegis"
        dangerouslySetInnerHTML={{ __html: html }}
      />

      <div className="flex justify-between mt-12 pt-6 border-t border-[var(--border)]">
        {prev ? (
          <Link
            href={`/manuscript/${prev.slug}`}
            className="text-sm text-gray-400 hover:text-[var(--primary)] transition-colors"
          >
            &larr; Ch {prev.number}: {prev.title}
          </Link>
        ) : (
          <span />
        )}
        {next ? (
          <Link
            href={`/manuscript/${next.slug}`}
            className="text-sm text-gray-400 hover:text-[var(--primary)] transition-colors"
          >
            Ch {next.number}: {next.title} &rarr;
          </Link>
        ) : (
          <span />
        )}
      </div>
    </div>
  );
}

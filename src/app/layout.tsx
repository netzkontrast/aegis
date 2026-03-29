import type { Metadata } from "next";
import "./globals.css";
import { Navigation } from "@/components/navigation";

export const metadata: Metadata = {
  title: {
    default: "AEGIS - Narrative Coherence Framework",
    template: "%s | AEGIS",
  },
  description:
    "Agentic Reasoning & Coherent Hypergraph Orchestration for Narratives. A unified platform for the ARCHON framework and Kohärenz Protokoll novel.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        <div className="min-h-screen flex flex-col">
          <Navigation />
          <main className="flex-1">{children}</main>
          <footer className="border-t border-[var(--border)] bg-[var(--muted)] py-6">
            <div className="container mx-auto px-4 text-center text-sm text-gray-400">
              <p>
                <span className="text-[var(--primary)]">AEGIS</span> - Agentic
                Reasoning & Coherent Hypergraph Orchestration for Narratives
              </p>
              <p className="mt-2">
                Built at the intersection of system and story, where coherence
                emerges from contradiction.
              </p>
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}

import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AEGIS - Narrative Coherence Framework",
  description: "Agentic Reasoning & Coherent Hypergraph Orchestration for Narratives",
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
          <header className="border-b border-[var(--border)] bg-[var(--muted)] sticky top-0 z-50">
            <nav className="container mx-auto px-4 py-4">
              <div className="flex items-center justify-between">
                <a href="/" className="text-2xl font-bold neon-glow">
                  AEGIS
                </a>
                <div className="flex gap-6">
                  <a href="/" className="hover:text-[var(--primary)] transition-colors">
                    Home
                  </a>
                  <a href="/ncp" className="hover:text-[var(--primary)] transition-colors">
                    NCP Query
                  </a>
                  <a href="/characters" className="hover:text-[var(--primary)] transition-colors">
                    Characters
                  </a>
                  <a href="/world" className="hover:text-[var(--primary)] transition-colors">
                    World
                  </a>
                  <a href="/manuscript" className="hover:text-[var(--primary)] transition-colors">
                    Manuscript
                  </a>
                  <a href="/about" className="hover:text-[var(--primary)] transition-colors">
                    About
                  </a>
                </div>
              </div>
            </nav>
          </header>
          <main className="flex-1">
            {children}
          </main>
          <footer className="border-t border-[var(--border)] bg-[var(--muted)] py-6">
            <div className="container mx-auto px-4 text-center text-sm text-gray-400">
              <p>
                <span className="text-[var(--primary)]">AEGIS</span> - Agentic Reasoning & Coherent Hypergraph Orchestration for Narratives
              </p>
              <p className="mt-2">
                Built at the intersection of system and story, where coherence emerges from contradiction.
              </p>
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}

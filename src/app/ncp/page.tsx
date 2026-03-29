"use client";

import { useState } from "react";
import Link from "next/link";

export default function NCPQueryPage() {
  const [path, setPath] = useState("");
  const [results, setResults] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [sections, setSections] = useState<string[]>([]);

  const fetchSections = async () => {
    const res = await fetch("/api/ncp/query?path=_sections");
    const data = await res.json();
    setSections(data.sections || []);
  };

  const handleQuery = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!path.trim()) return;
    setLoading(true);
    try {
      const res = await fetch(
        `/api/ncp/query?path=${encodeURIComponent(path.trim())}`
      );
      const data = await res.json();
      setResults(JSON.stringify(data.result, null, 2));
    } catch (err) {
      setResults(`Error: ${err}`);
    }
    setLoading(false);
  };

  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-6 text-[var(--primary)]">
        NCP Query Interface
      </h1>

      <div className="max-w-4xl">
        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">About the NCP</h2>
          <p className="text-gray-300 mb-4">
            The <strong>Narrative Context Protocol (NCP)</strong> is a
            machine-readable JSON schema encoding the deep thematic structure of
            the Kohärenz Protokoll based on Dramatica theory.
          </p>
          <ul className="list-disc list-inside space-y-2 text-gray-400 ml-4">
            <li>Physics rules (Landauer, Gödel, Bekenstein)</li>
            <li>Dual Kernel Theory (K₁ Ordnungskernel, K₀ Entropiekernel)</li>
            <li>Ontological world layers</li>
            <li>Character systems and throughlines</li>
            <li>Chapter design and validation criteria</li>
          </ul>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Query the Protocol</h2>
          <p className="text-sm text-gray-400 mb-4">
            Enter a dot-separated path to query NCP data. For example:{" "}
            <code className="text-[var(--primary)]">physics_rules</code>,{" "}
            <code className="text-[var(--primary)]">
              meta.thematic_statement
            </code>
            , or{" "}
            <code className="text-[var(--primary)]">
              dual_kernel_theory.K1
            </code>
          </p>
          <form onSubmit={handleQuery} className="space-y-4">
            <input
              type="text"
              value={path}
              onChange={(e) => setPath(e.target.value)}
              placeholder="e.g. physics_rules.landauer_principle"
              className="w-full px-4 py-2 bg-black border border-[var(--border)] rounded focus:outline-none focus:border-[var(--primary)] text-gray-100 font-mono"
            />
            <button
              type="submit"
              disabled={loading || !path.trim()}
              className="px-6 py-2 bg-[var(--primary)] text-black font-bold rounded hover:bg-opacity-80 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? "Querying..." : "Query NCP"}
            </button>
          </form>
        </div>

        {results && (
          <div className="bg-[var(--muted)] border border-[var(--primary)] rounded-lg p-6 mb-8">
            <h3 className="text-xl font-bold mb-4 text-[var(--primary)]">
              Results
            </h3>
            <pre className="text-sm text-gray-300 whitespace-pre-wrap font-mono overflow-x-auto max-h-[600px] overflow-y-auto">
              {results}
            </pre>
          </div>
        )}

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Quick Queries</h2>
          <div className="space-y-3">
            {[
              ["meta", "Project metadata & logline"],
              ["physics_rules", "Hard narrative physics laws"],
              ["physics_rules.landauer_principle", "Landauer Principle details"],
              ["physics_rules.goedel_incompleteness", "Gödel Incompleteness"],
              ["dual_kernel_theory", "K₁/K₀ Dual Kernel Theory"],
              ["world.ontological_layers", "Simulation layers"],
              ["character_systems", "Character system definitions"],
              ["validation_criteria", "Prose validation rules"],
            ].map(([p, label]) => (
              <button
                key={p}
                onClick={() => {
                  setPath(p);
                  setLoading(true);
                  fetch(`/api/ncp/query?path=${encodeURIComponent(p)}`)
                    .then((r) => r.json())
                    .then((d) =>
                      setResults(JSON.stringify(d.result, null, 2))
                    )
                    .finally(() => setLoading(false));
                }}
                className="block w-full text-left px-4 py-2 bg-black border border-[var(--border)] rounded hover:border-[var(--primary)] transition-colors text-gray-300"
              >
                <code className="text-[var(--primary)] mr-3">{p}</code>
                <span className="text-sm text-gray-500">{label}</span>
              </button>
            ))}
          </div>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Validate Prose</h2>
          <p className="text-gray-300 mb-4">
            Use the{" "}
            <Link
              href="/api/ncp/validate"
              className="text-[var(--primary)] underline"
            >
              /api/ncp/validate
            </Link>{" "}
            API to validate prose against NCP constraints. Send a POST with:
          </p>
          <pre className="bg-black/50 p-4 rounded border border-[var(--border)] text-sm font-mono text-gray-300">
            {`POST /api/ncp/validate
Content-Type: application/json

{
  "text": "Your prose here...",
  "chapter": 1
}`}
          </pre>
        </div>
      </div>
    </div>
  );
}

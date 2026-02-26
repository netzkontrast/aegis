'use client';

import { useState } from 'react';

export default function NCPQueryPage() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleQuery = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    // Simulate API call
    setTimeout(() => {
      setResults(`Query results for: "${query}"

This is a prototype interface for the Narrative Context Protocol (NCP).
In production, this would query the NCP JSON schema to retrieve:
- Scene-level thematic requirements
- Character state constraints
- Throughline checkpoints
- Structural validation criteria

The actual NCP implementation is available in the aegis/ncp/ directory.`);
      setLoading(false);
    }, 1000);
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
            The <strong>Narrative Context Protocol (NCP)</strong> is a machine-readable JSON schema
            that encodes the deep thematic structure of a story based on Dramatica theory.
          </p>
          <p className="text-gray-300 mb-4">
            It defines:
          </p>
          <ul className="list-disc list-inside space-y-2 text-gray-400 ml-4">
            <li>Four throughlines: Objective Story, Main Character, Impact Character, Subjective Story</li>
            <li>Character systems: Kael&apos;s 11 dissociative alters, their relationships and growth arcs</li>
            <li>Thematic checkpoints: Scene-level validation criteria for narrative coherence</li>
            <li>Structural constraints: The &ldquo;thematic guardrails&rdquo; that preserve authorial intent</li>
          </ul>
        </div>

        <div className="bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">Query the Protocol</h2>
          <form onSubmit={handleQuery} className="space-y-4">
            <div>
              <label htmlFor="query" className="block text-sm font-medium mb-2">
                Enter your query
              </label>
              <input
                type="text"
                id="query"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="e.g., 'What are the requirements for Chapter 4?'"
                className="w-full px-4 py-2 bg-black border border-[var(--border)] rounded focus:outline-none focus:border-[var(--primary)] text-gray-100"
              />
            </div>
            <button
              type="submit"
              disabled={loading || !query}
              className="px-6 py-2 bg-[var(--primary)] text-black font-bold rounded hover:bg-opacity-80 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? 'Querying...' : 'Query NCP'}
            </button>
          </form>
        </div>

        {results && (
          <div className="bg-[var(--muted)] border border-[var(--primary)] rounded-lg p-6">
            <h3 className="text-xl font-bold mb-4 text-[var(--primary)]">Results</h3>
            <pre className="text-sm text-gray-300 whitespace-pre-wrap font-mono">
              {results}
            </pre>
          </div>
        )}

        <div className="mt-8 bg-[var(--muted)] border border-[var(--border)] rounded-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Example Queries</h2>
          <div className="space-y-3">
            <button
              onClick={() => setQuery('What are the thematic requirements for Act I?')}
              className="block w-full text-left px-4 py-2 bg-black border border-[var(--border)] rounded hover:border-[var(--primary)] transition-colors text-gray-300"
            >
              What are the thematic requirements for Act I?
            </button>
            <button
              onClick={() => setQuery('Show me Kael\'s character state in Chapter 7')}
              className="block w-full text-left px-4 py-2 bg-black border border-[var(--border)] rounded hover:border-[var(--primary)] transition-colors text-gray-300"
            >
              Show me Kael&apos;s character state in Chapter 7
            </button>
            <button
              onClick={() => setQuery('What validation constraints apply to AEGIS dialogue?')}
              className="block w-full text-left px-4 py-2 bg-black border border-[var(--border)] rounded hover:border-[var(--primary)] transition-colors text-gray-300"
            >
              What validation constraints apply to AEGIS dialogue?
            </button>
          </div>
        </div>

        <div className="mt-8 bg-gradient-to-r from-[var(--secondary)] to-[var(--accent)] rounded-lg p-6">
          <h2 className="text-xl font-bold mb-2">Implementation Status</h2>
          <p className="text-sm mb-4">
            This is a prototype interface. The actual NCP tools are available via CLI:
          </p>
          <code className="block bg-black/50 p-3 rounded text-sm font-mono">
            python aegis/tools/ncp_query.py --chapter 4 --verbose
            <br />
            python aegis/tools/ncp_validate.py manuscript/chapter_01.md
          </code>
        </div>
      </div>
    </div>
  );
}

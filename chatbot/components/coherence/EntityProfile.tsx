import React from 'react';
import { cn } from '../../lib/utils';

export interface EntityProfileProps {
  entity_id: string; // "Kael", "Selene", "Nyx", "Lia", "Alex", "Lost One"
  tsdp_type: string; // "ANP", "EP", "Unknown"
  current_burden: string; // Description of their role/trauma
  dominance: boolean; // Is this alter currently fronting?
}

const entityColors: Record<string, string> = {
  'Kael': 'text-zinc-500 border-zinc-500',
  'Selene': 'text-crystal-sky border-crystal-sky',
  'Nyx': 'text-shadow-fire border-shadow-fire',
  'Lia': 'text-hope-yellow border-hope-yellow',
  'Alex': 'text-alex-rust border-alex-rust',
  'Lost One': 'text-trauma-yellow border-trauma-yellow',
  'Moros': 'text-trauma-yellow border-trauma-yellow',
  'Kiko': 'text-hope-yellow border-hope-yellow',
};

const entityBgs: Record<string, string> = {
  'Kael': 'bg-zinc-100',
  'Selene': 'bg-crystal-sky/10',
  'Nyx': 'bg-shadow-fire/10',
  'Lia': 'bg-hope-yellow/10',
  'Alex': 'bg-alex-rust/10',
  'Lost One': 'bg-trauma-yellow/10',
  'Moros': 'bg-trauma-yellow/10',
  'Kiko': 'bg-hope-yellow/10',
};

export function EntityProfile({ entity_id, tsdp_type, current_burden, dominance }: EntityProfileProps) {
  const colorClass = entityColors[entity_id] || 'text-zinc-800 border-zinc-800';
  const bgClass = entityBgs[entity_id] || 'bg-zinc-50';

  return (
    <div className={cn(
      "relative p-6 max-w-sm mx-auto my-4 overflow-hidden transition-all duration-300",
      "border-2 border-shaky bg-rough-paper shadow-lg",
      colorClass,
      dominance ? "scale-105 ring-2 ring-offset-2 ring-zinc-200" : "opacity-80 grayscale-[0.3]"
    )}>
      {/* Background Noise/Texture Overlay specific to entity */}
      <div className={cn("absolute inset-0 pointer-events-none opacity-30 mix-blend-multiply", bgClass)} />

      <div className="relative z-10 flex flex-col items-center text-center">
        {/* Abstract Silhouette */}
        <div className={cn("w-24 h-24 rounded-full border-2 mb-4 flex items-center justify-center bg-white/50 backdrop-blur-sm", colorClass)}>
           <svg viewBox="0 0 24 24" fill="currentColor" className="w-16 h-16 opacity-80">
             <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
           </svg>
        </div>

        <h3 className="text-2xl font-serif font-bold tracking-tight mb-1">{entity_id}</h3>

        <div className="flex items-center gap-2 mb-4">
          <span className="px-2 py-0.5 text-xs font-mono font-bold border rounded-full bg-white/80 uppercase tracking-widest">
            {tsdp_type}
          </span>
          {dominance && (
             <span className="px-2 py-0.5 text-xs font-mono font-bold bg-zinc-900 text-white border border-zinc-900 rounded-full uppercase tracking-widest animate-pulse">
               Fronting
             </span>
          )}
        </div>

        <p className="text-sm font-serif italic leading-relaxed text-zinc-700 max-w-[90%]">
          "{current_burden}"
        </p>
      </div>

      {/* Decorative elements */}
      <div className="absolute top-2 right-2 opacity-20">
        <svg width="40" height="40" viewBox="0 0 100 100">
           <circle cx="50" cy="50" r="40" stroke="currentColor" strokeWidth="1" fill="none" strokeDasharray="4 4" />
        </svg>
      </div>
    </div>
  );
}

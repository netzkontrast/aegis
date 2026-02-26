import React from 'react';
import { cn } from '../../lib/utils';

export interface CoreWorldViewProps {
  world_id: string; // e.g., "KW1", "KW4"
  stability_index: number; // 0-100
  active_logic: string; // "Classical Logic", "Paraconsistent Logic"
}

export function CoreWorldView({ world_id, stability_index, active_logic }: CoreWorldViewProps) {
  // Determine color based on stability
  let statusColor = "text-emerald-700";
  let statusBg = "bg-emerald-600";

  if (stability_index < 40) {
    statusColor = "text-trauma-yellow"; // #9C963B
    statusBg = "bg-trauma-yellow";
  } else if (stability_index < 80) {
    statusColor = "text-nostalgia-yellow"; // #D9A922
    statusBg = "bg-nostalgia-yellow";
  }

  return (
    <div className="p-6 bg-rough-paper border-shaky border-zinc-800 shadow-sm my-4 font-mono transition-all duration-500">
      <div className="flex justify-between items-center mb-4 border-b border-dashed border-zinc-400 pb-2">
        <h3 className="text-xl font-bold uppercase tracking-widest text-zinc-900 font-sans">Core World Monitor</h3>
        <span className="text-xs text-zinc-500 font-mono">SYS.KW.{world_id.replace('KW', '')}</span>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="p-4 border border-zinc-300 rounded-sm bg-white/50 backdrop-blur-sm shadow-inner">
          <p className="text-xs uppercase text-zinc-500 mb-1 tracking-wider">Current Reality</p>
          <p className="text-2xl font-bold text-zinc-800 font-serif">{world_id}</p>
        </div>

        <div className="p-4 border border-zinc-300 rounded-sm bg-white/50 backdrop-blur-sm shadow-inner">
          <p className="text-xs uppercase text-zinc-500 mb-1 tracking-wider">Active Logic</p>
          <p className="text-sm font-medium text-zinc-700 italic">{active_logic}</p>
        </div>
      </div>

      <div className="mt-6">
        <div className="flex justify-between text-xs mb-1 font-bold tracking-widest text-zinc-600">
          <span>STABILITY INDEX</span>
          <span className={statusColor}>{stability_index}%</span>
        </div>
        <div className="w-full h-2 bg-zinc-200 rounded-full overflow-hidden border border-zinc-300 relative">
          <div
            className={cn("h-full transition-all duration-500 relative overflow-hidden", statusBg)}
            style={{ width: `${stability_index}%` }}
          >
             {/* Add a subtle shimmer/noise overlay inside the bar */}
             <div className="absolute inset-0 bg-white/20 animate-pulse" />
          </div>
        </div>
      </div>

      {/* Decorative corners for "tech" feel */}
      <div className="absolute top-0 left-0 w-2 h-2 border-t-2 border-l-2 border-zinc-900 -mt-1 -ml-1" />
      <div className="absolute bottom-0 right-0 w-2 h-2 border-b-2 border-r-2 border-zinc-900 -mb-1 -mr-1" />
    </div>
  );
}

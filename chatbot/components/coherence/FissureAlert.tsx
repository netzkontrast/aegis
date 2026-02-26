import React from 'react';
import { cn } from '../../lib/utils';
import { TriangleAlert, Activity } from 'lucide-react'; // Assuming lucide-react is available (standard in shadcn)

export interface FissureAlertProps {
  severity_color: 'trauma-yellow' | 'signal-yellow' | 'shadow-fire';
  intruding_element: string; // The concept breaking through (e.g., "The Void")
  analysis_text: string; // "Logic failure detected in sector 7"
}

export function FissureAlert({ severity_color, intruding_element, analysis_text }: FissureAlertProps) {

  const colorMap = {
    'trauma-yellow': 'text-trauma-yellow border-trauma-yellow bg-trauma-yellow/10',
    'signal-yellow': 'text-signal-yellow border-signal-yellow bg-signal-yellow/10',
    'shadow-fire': 'text-shadow-fire border-shadow-fire bg-shadow-fire/10',
  };

  const activeColor = colorMap[severity_color] || colorMap['signal-yellow'];

  return (
    <div className={cn(
      "relative p-4 my-6 border-l-4 font-mono overflow-hidden",
      "border-shaky bg-rough-paper shadow-md",
      activeColor
    )}>
      {/* Glitch Overlay */}
      <div className="absolute inset-0 bg-white/5 opacity-20 pointer-events-none animate-pulse" />

      <div className="flex items-start gap-3 relative z-10">
        <div className="p-2 bg-white/80 rounded-full shadow-sm animate-bounce">
          <TriangleAlert className="w-6 h-6 stroke-2" />
        </div>

        <div className="flex-1">
          <h4 className="text-sm font-bold uppercase tracking-widest mb-1 flex items-center gap-2">
            <Activity className="w-3 h-3" />
            System Fissure Detected
          </h4>

          <div className="bg-white/60 p-2 rounded-sm mb-2 backdrop-blur-sm border border-current/20">
             <span className="text-xs font-bold uppercase block mb-0.5 opacity-70">Intrusion:</span>
             <p className="font-serif text-lg font-bold italic leading-tight">
               "{intruding_element}"
             </p>
          </div>

          <p className="text-xs font-medium leading-relaxed opacity-90 border-t border-dashed border-current/30 pt-2">
            Analysis: {analysis_text}
          </p>
        </div>
      </div>

      {/* Visual Tears/Rips */}
      <div className="absolute top-0 right-0 w-16 h-16 bg-gradient-to-bl from-white/40 to-transparent transform rotate-45 translate-x-8 -translate-y-8" />
    </div>
  );
}

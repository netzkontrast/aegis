"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Home" },
  { href: "/manuscript", label: "Manuscript" },
  { href: "/characters", label: "Characters" },
  { href: "/entities", label: "Entities" },
  { href: "/world", label: "World" },
  { href: "/quests", label: "Quests" },
  { href: "/ncp", label: "NCP" },
  { href: "/about", label: "About" },
];

export function Navigation() {
  const pathname = usePathname();

  return (
    <header className="border-b border-[var(--border)] bg-[var(--muted)] sticky top-0 z-50">
      <nav className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link href="/" className="text-2xl font-bold neon-glow">
            AEGIS
          </Link>
          <div className="flex gap-4 text-sm md:text-base md:gap-6 overflow-x-auto">
            {links.map((link) => {
              const isActive =
                link.href === "/"
                  ? pathname === "/"
                  : pathname.startsWith(link.href);
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  className={`whitespace-nowrap transition-colors ${
                    isActive
                      ? "text-[var(--primary)] border-b-2 border-[var(--primary)] pb-0.5"
                      : "hover:text-[var(--primary)]"
                  }`}
                >
                  {link.label}
                </Link>
              );
            })}
          </div>
        </div>
      </nav>
    </header>
  );
}

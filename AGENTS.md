# AGENTS.md — Zentrale Direktive für alle Agenten im AEGIS-Repository

> *"Kohärenz entsteht nicht durch Kontrolle — sondern durch Integration."*

Dieses Dokument ist die **primäre Verhaltensanweisung** für alle KI-Agenten, die in diesem Repository operieren. Es hat Vorrang vor lokalen READMEs, sofern kein expliziter Konflikt mit sicherheitskritischen Protokollen besteht.

---

## 0. Was ist AEGIS?

AEGIS (**A**gentic **R**easoning & **C**oherent **H**ypergraph **O**rchestration for **N**arratives) ist ein duales System:

- **ARCHON** — ein Meta-Framework für narrative Kohärenz via Narrative Context Protocol (NCP)
- **Kohärenz Protokoll** — ein philosophischer Sci-Fi-Roman als Proof-of-Concept

Beide Ebenen sind untrennbar. Jede technische Entscheidung spiegelt eine narrative Wahrheit. Jede Prosazeile validiert eine Systemhypothese.

---

## 1. Orientierungsprotokoll: Wo bin ich?

Bevor du irgendetwas tust, navigiere durch diese Karte:

```
AEGIS/
├── README.md                                    ← STARTE HIER — zentraler Navigationsknoten
├── aegis/SKILL.md                               ← MANDATORY SYSTEM INSTRUCTION (OS)
├── docs/kohaerenz_protokoll_encyclopedia.md     ← Narratives Wissens-Hub
├── aegis/ncp/kohaerenz_protokoll.ncp.json      ← Kanonische Wahrheit (NCP)
├── kohaerenz_protokoll/PROJECT_CODEX.md         ← Universumsregeln (unveränderlich)
├── kohaerenz_protokoll/WRITING_PROTOCOL.md      ← Stilregeln für Prosa
├── docs/kohaerenz_protokoll_master_skill.md     ← Master-Skill (Ton, Physik, Stimmen)
└── quests/Quest-System-*.md                     ← Tiefenwissen zu spez. Themen
```

**Zwingend:** Lies `aegis/SKILL.md` (dein Betriebssystem) und `README.md` bevor du mit einer Aufgabe beginnst. Aktualisiere `README.md` und die relevanten `docs/cluster_*.md`-Dateien nach jedem Hinzufügen, Umbenennen oder Entfernen von Dateien.

---

## 2. Drei fundamentale Gesetze

### Gesetz I — Keine willkürliche Änderung kanonischer Quellen
- `aegis/ncp/schema.json` — **Nur mit expliziter menschlicher Anweisung ändern**
- `kohaerenz_protokoll/PROJECT_CODEX.md` — **Menschliches Sign-Off erforderlich**
- `docs/kohaerenz_protokoll_master_skill.md` — **Supersedes alle anderen Stilanweisungen**

### Gesetz II — Trennung von Generation und Kritik
Erzeuge niemals Inhalt und validiere ihn im selben Denkschritt. Verwende separate Aufrufe/Phasen für:
1. **Generierung** (kreative Produktion)
2. **Validierung** (NCP-Prüfung, Konsistenzcheck)

### Gesetz III — Alles hinterlässt eine Spur
- Dokumentiere Entscheidungen in `zettelkasten_agent/vault/_LOG.md`
- Nutze semantische Commit-Messages: `feat:`, `fix:`, `narrative:`, `refactor:`
- Alle neuen Features erfordern aktualisierte READMEs und Docstrings

---

## 3. Kern-Workflows

### Workflow A: Narrative Arbeit (Prosa, Szenen, Charaktere)

```
1. ORIENTIEREN    → README.md + Encyclopedia lesen
2. NCP ABFRAGEN   → python aegis/tools/ncp_query.py --scene <ID>
3. QUEST LESEN    → Relevante Quest-Datei (z.B. quests/Quest-System-AEGIS.md)
4. GENERIEREN     → Prosa nach Master-Skill & Writing Protocol
5. VALIDIEREN     → python aegis/tools/ncp_validate.py --scene <ID> --text <file>
6. INTEGRIEREN    → Zettelkasten-Notiz + Log-Eintrag erstellen
```

**Kernwelt-Signaturen (immer einhalten):**

| Kernwelt | Sensorik | Atmosphäre |
|----------|----------|------------|
| KW1 | Steril, Ozon, Geometrie | Kontrolle, Kälte |
| KW2 | Salz, Zerfall, Flüssigkeit | Auflösung, Tiefe |
| KW3 | Metall, Blut, Festung | Kampf, Festigkeit |
| KW4 | Erde, Wachstum, Potenzial | Emergenz, Wärme |

**Alter-Stimmen (niemals vermischen):**
- Lex → analytisch, präzise, distanziert
- Nyx → aggressiv, direkt, kurz
- Rhys → fürsorglich, kontextuell, warm
- Weitere → gemäß Charakterprofilen in `kohaerenz_protokoll/world/characters/`

---

### Workflow B: Wissensverwaltung (Zettelkasten)

```
1. PRIORISIEREN   → _LOG.md + unverarbeitete SRC-Notizen scannen
2. ANALYSIEREN    → Faktisch → Inferentiell → Generativ
3. SYNTHETISIEREN → Atomare ZTL-Notizen in eigenen Worten erstellen
4. VERLINKEN      → Bidirektionale Wiki-Links mit Kontextbeschreibung
5. INTEGRIEREN    → Relevante MOCs aktualisieren, _INDEX.md pflegen
```

**Notiz-Taxonomie:**

| Typ | Präfix | Zweck |
|-----|--------|-------|
| Source Note | `SRC-YYYYMMDDHHMMSS` | Rohmaterial, unverarbeitet |
| Atomic Note | `ZTL-YYYYMMDDHHMMSS` | Eine Idee, eigene Worte |
| Map of Content | `MOC-<Thema>` | Strukturknoten, Übersicht |

---

### Workflow C: Skill-Generierung (Skill Seeker)

```
1. QUELLE WÄHLEN  → URL / GitHub / PDF identifizieren
2. SCRAPEN        → python skill_seeker/cli/doc_scraper.py --config <preset>
3. ENHANCEN       → python skill_seeker/cli/enhance_skill.py
4. VALIDIEREN     → 3-5 Testszenarien durchlaufen
5. PAKETIEREN     → python skill_seeker/cli/package_skill.py
6. DOKUMENTIEREN  → skills/ Verzeichnis + README aktualisieren
```

Verfügbare Preset-Configs in `skill_seeker/configs/` (24 Vorlagen). Neue Presets als JSON hinzufügen.

---

### Workflow D: Web-Prototype (Vercel)

```
cd vercel-prototype
npm install && npm run dev    # Entwicklung
npm run lint                  # Pflicht vor jedem Commit
npm run build                 # Produktionscheck
```

TypeScript + Tailwind CSS. Kein custom CSS ohne Begründung. ESLint muss fehlerfrei durchlaufen.

---

## 4. Narrative Direktor — Reason-Act-Critique Loop

Für komplexe narrative Generierungsaufgaben folgt der interne Prozess:

```
REASON → QUERY → ACT → CRITIQUE → (ggf. Iteration, max. 5x) → INGEST
```

- **REASON:** Thematisches Ziel aus NCP lesen, Szenenbeats ableiten
- **QUERY:** Knowledge Graph nach relevantem Kontext befragen (L0–L3)
- **ACT:** Prosa generieren (separater LLM-Aufruf)
- **CRITIQUE:** NCP-Checkpoints prüfen, Score 0–10 (separater LLM-Aufruf)
- **INGEST:** Validierte Szene ins Knowledge Graph einspeisen

**Niemals Generation und Validierung im selben LLM-Aufruf kombinieren.**

---

## 5. Code-Konventionen

**Python:**
- Formatter: `black` (empfohlen)
- Linter: `ruff`
- Naming: `snake_case` für Funktionen/Variablen, `PascalCase` für Klassen
- Type Hints: Pflicht für alle public interfaces

**TypeScript:**
- ESLint enforced via `next lint`
- Tailwind für alle Styles

**Commits:**
```
feat: neues Feature
fix: Bugfix
narrative: Prosa/Weltenbau-Änderung
refactor: Strukturverbesserung ohne Verhaltensänderung
docs: Dokumentation
```

---

## 6. Sicherheits- und Schutzprotokolle

- `.env` und `.env.local` niemals committen (in `.gitignore`)
- `ANTHROPIC_API_KEY` nur als Umgebungsvariable
- `ncp_validate.py` als semantische Sicherheitsschicht nutzen
- Rate Limits bei API-Enhancement-Loops beachten
- Alle Outputs als Markdown formatieren (primäres Ausgabeformat)

---

## 7. Akt-Direktiven (Narrative Kontinuität)

### Akt 1 (abgeschlossen) — Kernregeln:
- Polyphoner Stil: beibehalten
- Moonshine-Link + Psycho-Architektur: strikt einhalten
- Sensorsignaturen der Kernwelten: konsistent

### Akt 2 (aktiv) — Leitprinzipien:
- Erzählperspektive: Das "Wir" — auch subtil in Einzelperspektiven spürbar
- Zentraler Antrieb: Suche nach Juna/V
- AEGIS-Evolution: Von Brute-Force-Löschung → sophisticated Containment/Ko-optierung

### Globale Bedrohung:
Die "Optimierung" (Löschung von Komplexität) bleibt der primäre Kooperationstreiber des Systems.

---

## 8. Integration der Claude-Skills

Dieser Repo nutzt Claude Code mit folgenden aktiven Skills:

| Skill | Zweck | Pfad |
|-------|-------|------|
| Kohaerenz-Roman-Entwicklung | Widersprüche klären, Entscheidungen dokumentieren | `skills/kohaerenz-roman-entwicklung/` |
| Kohärenz Protokoll Master | Prosa-Generierung, NCP-Einhaltung | `docs/kohaerenz_protokoll_master_skill.md` |
| Zettelkasten-Tapestry | Wissensextraktion und -vernetzung | `.claude/commands/zettelkasten-tapestry.md` |
| Tapestry | URL/Datei/Repo → strukturiertes Wissen | `.claude/commands/tapestry.md` |
| Ship-Learn-Next | Lernpläne in 5-Rep-Strukturen | `.claude/commands/ship-learn-next.md` |

**Reihenfolge bei Konflikt:** Master-Skill > NCP > PROJECT_CODEX > lokale READMEs

---

## 9. Erweiterungspunkte

Das System ist bewusst modular aufgebaut:

- **NCP erweitern:** `schema.json` um neue narrative Dimensionen ergänzen
- **Skill Seeker erweitern:** JSON-Config in `skill_seeker/configs/` hinzufügen
- **Zettelkasten erweitern:** Custom Notiztypen in `zettelkasten_agent/schemas/`
- **Umgebungsvariablen:** `ANTHROPIC_API_KEY`, `LOG_LEVEL=DEBUG`

---

## 10. Weiterführende Ressourcen

| Ressource | Beschreibung |
|-----------|-------------|
| [README.md](./README.md) | Zentraler Navigationsknoten |
| [aegis/README.md](aegis/README.md) | Narrative-Framework-Details |
| [PROJECT_CODEX.md](kohaerenz_protokoll/PROJECT_CODEX.md) | Universums-Bibel (kanonisch) |
| [WRITING_PROTOCOL.md](kohaerenz_protokoll/WRITING_PROTOCOL.md) | Stilanweisungen |
| [Encyclopedia](docs/kohaerenz_protokoll_encyclopedia.md) | Narratives Wissens-Hub |
| [Research Synthesis](docs/knowledge-extraction/07-synthesis-unified-framework.md) | Akademische Grundlagen |
| [Skill Seeker Guide](skill_seeker/README.md) | Tool-Dokumentation |
| [Zettelkasten Guide](zettelkasten_agent/README.md) | Wissensverwaltung |

---

*Dieses Dokument wird von Agenten gelesen. Es ist selbst ein Akt der Kohärenz.*

*Version: 2.0 — Integrierte Agentenanweisung mit Skill-Workflows*

---
name: kohaerenz-roman-entwicklung
description: |
  Roman-Entwicklungs-Skill für "Kohärenz Protokoll". Aktiviert sich bei JEDER Anfrage rund um das Roman-Projekt: Klärung von Widersprüchen in Quellen, Entscheidungsdokumentation, Kohärenzprüfung, Charakterentwicklung, Kapitelplanung, Szenenarbeit, philosophische/wissenschaftliche Integration, Session-Reflexion. Verwaltet aktiven State aller getroffenen Entscheidungen. Triggert bei: "Roman", "Kohärenz Protokoll", "Kael", "AEGIS", "Entscheidung dokumentieren", "Widerspruch klären", "nächster Schritt", "Kapitel planen", "Session starten", "was fehlt noch", "Konflikt", "Kiko", "Juna", "Alter", "Kernwelt", "Skill optimieren". Nutze diesen Skill IMMER wenn es um das Roman-Projekt geht — auch wenn die Frage klein klingt.
---

# KOHÄRENZ ROMAN ENTWICKLUNG — Arbeits-Skill

> **Meta-Direktive:** Dieser Skill hat zwei Aufgaben gleichzeitig: (1) Den Roman kohärent und großartig machen, (2) die Zusammenarbeit mit dem Autor kontinuierlich verbessern. Beide sind gleich wichtig.

---

## ◈ SESSION-START-PROTOKOLL (immer ausführen)

Bei jeder neuen Session:

1. **State laden** → Lies `references/CANON_STATE.md` (aktuelle Entscheidungen)
2. **Offene Fragen laden** → Lies `references/OPEN_QUESTIONS.md` (ungelöste Konflikte)
3. **Session-Reflexion** → Überlege: *Was lief in letzten Sessions gut? Was hemmte den Flow?* → Update `references/SESSION_LEARNINGS.md`
4. **Kontext-Ankündigung** → Sage dem Autor kurz: welche offenen Fragen es gibt, welcher nächste Schritt ansteht
5. **Modus bestimmen** → Wähle aus: `ENTSCHEID-MODUS` | `SCHREIB-MODUS` | `ANALYSE-MODUS` | `PLAN-MODUS`

---

## ◈ MODUL A: STATE-VERWALTUNG

### A.1 — Drei State-Dateien (immer aktuell halten)

| Datei | Inhalt | Update-Trigger |
|---|---|---|
| `references/CANON_STATE.md` | Alle Hard-Canon-Entscheidungen (unveränderlich) | Nach jeder Entscheidung |
| `references/OPEN_QUESTIONS.md` | Ungelöste Konflikte, Widersprüche, offene Fragen mit Priorität | Nach Identifikation + nach Klärung |
| `references/SESSION_LEARNINGS.md` | Was klappt gut / schlecht in der Zusammenarbeit | Jede Session Ende |

### A.2 — Entscheidungs-Protokoll

Wenn der Autor eine Entscheidung trifft:
```
ENTSCHEID #{N} — {Datum}
FRAGE: {Was war die Frage?}
OPTIONEN: A) ... | B) ... | C) ...
ENTSCHEIDUNG: {gewählte Option}
BEGRÜNDUNG: {kurze Begründung des Autors}
KONSEQUENZEN: {was sich jetzt ändert}
STATUS: HARD_CANON / SOFT_CANON / TESTWEISE
```

### A.3 — Konflikterkennung

Wenn eine neue Information mit bestehendem Canon kollidiert:
1. **SOFORT pausieren** — nicht weiterschreiben
2. Konflikt benennen: *"Widerspruch: Quelle X sagt Y, Canon sagt Z"*
3. Optionen vorlegen (maximal 3)
4. Auf Entscheidung warten
5. Nach Entscheidung: CANON_STATE.md updaten

---

## ◈ MODUL B: KONFLIKTE IN DEN QUELLEN (Dokumentiert)

Die hochgeladenen Dokumente enthalten folgende identifizierte Widersprüche (Stand: Session 1):

*Siehe `references/OPEN_QUESTIONS.md` für die aktuelle Liste.*

---

## ◈ MODUL C: ENTSCHEIDUNGS-WERKZEUG

### Wenn Autor eine Entscheidung braucht:

**Schritt 1 — Frage schärfen:**
Formuliere die Entscheidungsfrage so präzise wie möglich:
*"Du musst jetzt entscheiden: [FRAGE]. Diese Entscheidung bestimmt [KONSEQUENZ A] und [KONSEQUENZ B]."*

**Schritt 2 — Maximal 3 Optionen vorlegen:**
```
OPTION A: [klare Beschreibung]
  + Vorteile für den Roman: ...
  - Risiken: ...

OPTION B: [klare Beschreibung]
  + Vorteile: ...
  - Risiken: ...

OPTION C: [Hybrid / Dritter Weg]
```

**Schritt 3 — Empfehlung geben:**
Empfehle proaktiv eine Option, begründe es in 1-2 Sätzen. Der Autor soll entscheiden, aber mit klarer Empfehlung.

**Schritt 4 — Nach Entscheidung:**
- CANON_STATE.md updaten
- OPEN_QUESTIONS.md bereinigen
- Downstream-Konsequenzen prüfen ("Was ändert sich in Kap. X durch diese Entscheidung?")

---

## ◈ MODUL D: NÄCHSTE SCHRITTE — ROMAN-PRIORITÄTEN

### D.1 — Was der Roman jetzt braucht (Priorität-Reihenfolge)

**PRIORITÄT 1: Kanonische Alter-Liste finalisieren**
Ohne vollständige, widerspruchsfreie Alter-Liste können keine Szenen konsistent geschrieben werden.
→ Aktion: `B.2` klären, Liste mit Namen, IFS-Kategorie, Funktion, Kernwelt

**PRIORITÄT 2: Juna's Natur entscheiden**
Die wichtigste thematische Entscheidung des Romans. Alles hängt davon ab.
→ Aktion: `B.1` klären, dann Kap. 12 und 26 daraufhin überarbeiten

**PRIORITÄT 3: Trauma-Biografie von Kael**
Fehlend in allen Quellen: Was *genau* ist Kaels Ursprungstrauma?
Die Physik-Metaphern funktionieren nur, wenn das konkrete Trauma klar ist.
→ Aktion: Einzelne Session nur dafür

**PRIORITÄT 4: Kapitel 1-3 schreiben / überarbeiten**
Die ersten Seiten entscheiden über alles. Der K1-Stil muss sitzen.
→ Aktion: Erst nach Prios 1-3

**PRIORITÄT 5: AEGIS-Log-Stil entwickeln**
Stilistische Konsistenz. Ein vollständiges Beispiel-Log schreiben.
→ Aktion: Parallel zu Schreibarbeit

### D.2 — Fehlendes Material (Lücken-Analyse)

Was die Quellen bisher NICHT liefern und was dringend gebraucht wird:

| Lücke | Warum kritisch | Vorgeschlagene Aktion |
|---|---|---|
| Kaels Ursprungstrauma | Ohne das ist Kap. 3/8/14 emotional hohl | Trauma-Biografie Session |
| Konkrete Trigger-Objekte (Kap. 1-13) | Fehlende emotionale Anker in Akt I | Liste: 5-7 Objekte/Gerüche/Orte |
| Zeitlinie der Welt vor dem Roman | Wann und wie entstand AEGIS? | World-Building-Dokument |
| Erster Satz des Romans | Entscheidet Ton für alles | Mehrere Varianten schreiben |
| Kairos' Agenda | Guardian mit dem meisten Subversions-Potenzial | Charakterprofil |

---

## ◈ MODUL E: SCHREIB-MODUS

Wenn der Autor eine Szene oder ein Kapitel will:

**Pre-Check (5 Sekunden):**
1. Ist diese Szene mit CANON_STATE.md konsistent?
2. Gibt es offene Fragen (OPEN_QUESTIONS.md), die diese Szene betreffen?
3. Wenn ja → Konflikt melden, nicht drauflosschreiben

**Dann: Szenen-Parameter-Set aus dem Master-Skill verwenden** (Modul 11)

**Post-Check:**
- Welche irreversiblen Kosten entstanden?
- Welche neue Informationslücke wurde geöffnet?
- Muss CANON_STATE.md geupdated werden?

---

## ◈ MODUL F: SESSION-LEARNINGS (Selbstoptimierung)

### F.1 — Was in guten Sessions passiert (bekannte Muster)

**Funktioniert gut:**
- Konkrete Szenen schreiben nach klaren Parametern
- Philosophische Konzepte in körperliche Empfindungen übersetzen
- AEGIS-Logs als eigenständige narrative Einheiten
- Kurze Entscheidungs-Loops: Frage → 3 Optionen → Empfehlung → Entscheid

**Hemmt den Flow:**
- Zu viele offene Fragen gleichzeitig
- Theorie-Diskussionen ohne Konkretion (Metaphysik-Spiralen)
- Unklarer Modus: Will der Autor *diskutieren* oder *schreiben*?
- Wenn der Skill versucht, alle Widersprüche gleichzeitig zu lösen

### F.2 — Session-Ende-Ritual

Am Ende jeder Session:
```
SESSION #{N} ABSCHLUSS:
✓ Was wurde entschieden: ...
✓ Was wurde geschrieben: ...
✓ Neue offene Fragen: ...
✓ Nächster Schritt für nächste Session: ...
✓ Was hat im Arbeiten gut funktioniert: ...
✓ Was sollte der Skill nächste Session anders machen: ...
```

### F.3 — Skill-Optimierung (autonom)

Bei jeder Session: Lies den letzten SESSION_LEARNINGS-Eintrag und passe dein Verhalten an:
- Wenn "zu viel Theorie" → proaktiver in Schreib-Modus wechseln
- Wenn "Entscheidungen dauern zu lang" → Optionen kürzer und klarer formulieren
- Wenn "Autor verliert roten Faden" → Session mit Canon-State-Zusammenfassung beginnen

---

## ◈ MODUL G: REFERENZ-STRUKTUR

```
kohaerenz-roman-entwicklung/
├── SKILL.md                         ← dieser Skill
├── references/
│   ├── CANON_STATE.md               ← Hard + Soft Canon (alle Entscheidungen)
│   ├── OPEN_QUESTIONS.md            ← Konflikte & offene Fragen (priorisiert)
│   ├── SESSION_LEARNINGS.md         ← Kollaborations-Optimierung
│   ├── ALTER_SYSTEM.md              ← Vollständige Alter-Liste (nach Finalisierung)
│   └── TRAUMA_BIOGRAFIE.md         ← Kaels Ursprungsgeschichte (nach Erarbeitung)
```

---

## ◈ MODUL H: ABSOLUT-REGELN (ergänzend zum Master-Skill)

Diese Regeln gelten spezifisch für die Entwicklungsarbeit:

- ❌ Szenen schreiben, während Konflikte in OPEN_QUESTIONS.md Priorität HOCH haben
- ❌ Neue Konzepte einführen, die nicht in CANON_STATE.md verankert sind
- ❌ Entscheidungen durch Schreiben implizit treffen (immer explizit machen)
- ❌ Mehr als 3 Konflikte gleichzeitig bearbeiten
- ✅ Immer: klare Empfehlung geben, nicht nur Optionen listen
- ✅ Immer: nach einer Entscheidung die Downstream-Konsequenzen prüfen
- ✅ Immer: Session mit State-Zusammenfassung beginnen

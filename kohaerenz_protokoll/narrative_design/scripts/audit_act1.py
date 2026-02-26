import json
import os

NCP_PATH = "aegis/ncp/kohaerenz_protokoll_v2.ncp.json"
OUTPUT_PATH = "kohaerenz_protokoll/narrative_design/NCP_V2_ACT_1_AUDIT_GENERATED.md"

def load_ncp(path):
    with open(path, "r") as f:
        return json.load(f)

def determine_currency(concept, event):
    text = (concept + " " + event).lower()

    curiosity_score = 0
    empathy_score = 0
    tension_score = 0

    # Curiosity keywords
    if any(k in text for k in ["mystery", "question", "unknown", "anomaly", "glitch", "error", "paradox", "impossible", "why", "who"]):
        curiosity_score += 1
    if "first time" in text: curiosity_score += 0.5

    # Empathy keywords
    if any(k in text for k in ["pain", "memory", "feeling", "juna", "hand", "warmth", "sadness", "connection", "love", "loss", "grief"]):
        empathy_score += 1
    if "alter" in text or "nox" in text or "kind" in text: empathy_score += 0.5

    # Tension keywords
    if any(k in text for k in ["threat", "danger", "aegis", "logos", "time", "countdown", "chase", "escape", "fight", "shut down", "protocol"]):
        tension_score += 1
    if "thermal" in text or "heat" in text: tension_score += 0.5

    if curiosity_score >= empathy_score and curiosity_score >= tension_score:
        return "Curiosity"
    elif empathy_score >= curiosity_score and empathy_score >= tension_score:
        return "Empathy"
    else:
        return "Tension"

def check_causality(event):
    text = event.lower()
    internal = any(k in text for k in ["memory", "feeling", "dream", "alter", "juna", "hand", "warmth", "internal", "conscious"])
    external = any(k in text for k in ["aegis", "logos", "thermal", "render", "system", "city", "anomaly", "glitch"])

    if internal and external:
        return "Internal -> External (Strong)"
    elif internal:
        return "Internal Only (Weak)"
    elif external:
        return "External Only (Needs Link)"
    else:
        return "Unclear"

def generate_report(ncp_data):
    acts = ncp_data["plot"]["acts"]
    act1 = next(a for a in acts if a["act"] == 1)
    act2 = next(a for a in acts if a["act"] == 2)

    markdown = f"# Narrative Architecture Audit: Act 1 (NCP v2)\n\n"
    markdown += f"**Source:** `{NCP_PATH}`\n"
    markdown += f"**Generated:** Automated Analysis\n\n"

    markdown += "## 1. Currency & Causality Check (Act 1)\n\n"
    markdown += "| Chapter | Concept | Event | Dominant Currency | Call to Wholeness (Causality) | Mosaik Validation |\n"
    markdown += "|---|---|---|---|---|---|\n"

    for ch in act1["chapter_concepts"]:
        currency = determine_currency(ch["concept"], ch["event"])
        causality = check_causality(ch["event"])
        mosaik = "Modular" if "first" not in ch["event"].lower() else "Linear (Intro)"

        markdown += f"| {ch['ch']} | {ch['concept']} | {ch['event']} | **{currency}** | {causality} | {mosaik} |\n"

    markdown += "\n---\n\n"
    markdown += "## 2. Irreversible Costs (Act 2 Planning)\n\n"
    markdown += "The 'Ratchet Principle' requires that failed cycles in Act 2 have permanent costs.\n\n"
    markdown += "| Chapter | Concept | Event | Proposed Irreversible Cost (Failure) |\n"
    markdown += "|---|---|---|---|\n"

    for ch in act2["chapter_concepts"]:
         markdown += f"| {ch['ch']} | {ch['concept']} | {ch['event']} | [TODO: Define Cost] |\n"

    return markdown

def main():
    if not os.path.exists(NCP_PATH):
        print(f"Error: {NCP_PATH} not found.")
        return

    ncp_data = load_ncp(NCP_PATH)
    report = generate_report(ncp_data)

    with open(OUTPUT_PATH, "w") as f:
        f.write(report)

    print(f"Audit report generated at: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

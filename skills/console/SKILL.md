# SKILL: AEGIS Console (Interface Definition)

**Version:** 0.1.0
**Status:** Design Phase
**Owner:** Jules (Agent)

## 🎯 Purpose
This skill defines the high-level specification for the AEGIS Console web application (`vercel-prototype`). It acts as the "Root Configuration" for the frontend, detailing the layout, theme, and initial capabilities available to users.

## 🛠️ Specification (`console.json`)

The console is configured via a JSON object derived from repository state:

```json
{
  "theme": "cyberpunk-dark",
  "layout": {
    "header": {
      "title": "AEGIS :: Console",
      "links": [
        {"label": "Repo State", "href": "/repo-state"},
        {"label": "Quests", "href": "/quests"}
      ]
    },
    "sidebar": {
      "modules": [
        "quest-tracker",
        "system-status"
      ]
    },
    "main": {
      "defaultView": "terminal",
      "availableViews": ["terminal", "knowledge-graph", "manuscript-editor"]
    }
  },
  "modules": {
    "quest-tracker": {
      "source": "quests/README.md",
      "refreshRate": 60
    },
    "system-status": {
      "source": "REPO_STATE.md",
      "refreshRate": 300
    }
  }
}
```

## 🔗 Integration
- **Frontend Skill:** Generates the dynamic command list injected into the Console.
- **Gemini:** Provides natural language understanding for the "Terminal" view.
- **Next.js:** Renders the interface based on this configuration.

## 📝 Usage
Use this skill to modify the *behavior* and *appearance* of the Console without altering the underlying Next.js code directly. Update `specs/console.json` to change the layout or active modules.

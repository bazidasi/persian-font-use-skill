# Persian Font Use Skill - Installation Guide

## Platform Installation

### Claude Code
```bash
# Via marketplace
/plugin marketplace add YOUR_USERNAME/persian-font-use-skill
/plugin install persian-font-use@persian-font-use-skill

# Or manual
cp -r .opencode/skill/persian-font-use ~/.claude/skills/persian-font-use
```

### Cursor
```bash
cp -r .opencode/skill/persian-font-use ~/.cursor/skills/persian-font-use
```

### Windsurf
```bash
cp -r .opencode/skill/persian-font-use ~/.windsurf/skills/persian-font-use
```

### VS Code
```bash
cp -r .opencode/skill/persian-font-use ~/.vscode/skills/persian-font-use
```

### OpenCode
```bash
cp -r .opencode/skill/persian-font-use ~/.config/opencode/skill/persian-font-use
```

### GitHub Copilot
```bash
cp -r .opencode/skill/persian-font-use ~/.copilot/skills/persian-font-use
```

### Continue
```bash
cp -r .opencode/skill/persian-font-use ~/.continue/skills/persian-font-use
```

### Antigravity
```bash
cp -r .opencode/skill/persian-font-use ~/.agents/skills/persian-font-use
```

---

## Global Installation (All Projects)

For system-wide availability:

```bash
# Create global skills directory
mkdir -p ~/.local/share/ai-skills/persian-font-use

# Copy skill
cp -r .opencode/skill/persian-font-use/* ~/.local/share/ai-skills/persian-font-use/
```

Then add to your AI tool config:

**Claude Code**: Add to `~/.claude/settings.json`
```json
{
  "skills": {
    "persian-font-use": "~/.local/share/ai-skills/persian-font-use"
  }
}
```

---

## Verify Installation

Test the skill is working:

```bash
# Test search script
python3 ~/.local/share/ai-skills/persian-font-use/scripts/search_fonts.py "vazirmatn"

# Test design system generation
python3 ~/.local/share/ai-skills/persian-font-use/scripts/search_fonts.py --design-system -p "MyApp" "ui"
```

---

## Uninstall

```bash
# Local project
rm -rf .opencode/skill/persian-font-use

# Global
rm -rf ~/.local/share/ai-skills/persian-font-use
```

---

## Troubleshooting

**Python not found**: Install Python 3.x from python.org

**Permission denied**: Use `chmod +x scripts/*.py`

**Module not found**: Install dependencies `pip install pyyaml`

**Skill not activating**: Check AI tool's skill directory path
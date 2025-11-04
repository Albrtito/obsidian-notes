# AGENTS.md - Coding Guidelines for Obsidian Vault

## Build/Lint/Test Commands
- **Run Python script**: `cd 99-meta/02-scripts && python buscar_dudas.py`
- **Single test**: No formal test suite; manually verify script output
- **Lint Python**: `python -m flake8 99-meta/02-scripts/buscar_dudas.py` (if flake8 installed)

## Code Style Guidelines
- **Python**: Follow PEP 8; use pathlib for paths, yaml.safe_load for frontmatter
- **Imports**: Standard library first, then third-party; one import per line
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Error handling**: Use try/except with specific exceptions; avoid bare except
- **Types**: No type hints currently used; consider adding for complex functions

## Note-Taking Conventions - CRITICAL: ALWAYS USE noteTemplate.md
- **File naming**: `unixTimestamp-title.md` (e.g., 1761239003-returnvsrewardinreinforcementlearning.md)
- **Aliases**: REQUIRED - Use original title as alias (e.g., "Return vs reward in reinforcement learning")
- **Tags**: All lowercase in frontmatter YAML; #Duda for questions needing answers
- **Template**: ⚠️ MANDATORY: Check 99-meta/01-templ/noteTemplate.md before EVERY note creation
- **Structure**: Keep notes atomic and concise; link related concepts

## AI-Generated Notes Rules  
- **⛔ CRITICAL**: NEVER modify files in 02-atomic, 01-areas, or any folder except 98-ai
- **Location**: ALL AI notes MUST go in `98-ai` folder - NO EXCEPTIONS
- **Tag**: Include 'artificial' tag to mark as AI-generated
- **Format**: MUST follow noteTemplate.md exactly - intro callout, Up/Down sections required
- **Dictionary**: Use `> [!example] Dictionary` callout with **term->** Definition format
- **Properties**: Use `> [!important]` callout with **property:** Definition format
- **Best practice**: Create multiple small atomic notes, then one joining note
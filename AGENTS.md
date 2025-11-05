# AGENTS.md - Coding Guidelines for Obsidian Vault

## 1. Build/Lint/Test Commands

1.1 **Run Python script**: `cd 99-meta/02-scripts && python buscar_dudas.py`
1.2 **Single test**: No formal test suite; manually verify script output
1.3 **Lint Python**: `python -m flake8 99-meta/02-scripts/buscar_dudas.py` (if flake8 installed)

## 2. Code Style Guidelines

2.1 **Python**: Follow PEP 8; use pathlib for paths, yaml.safe_load for frontmatter
2.2 **Imports**: Standard library first, then third-party; one import per line
2.3 **Naming**: snake_case for functions/variables, PascalCase for classes
2.4 **Error handling**: Use try/except with specific exceptions; avoid bare except
2.5 **Types**: No type hints currently used; consider adding for complex functions

## 3. Note-Taking Conventions - Critical: Always use noteTemplate.md for new notes

3.1 **File naming**: `unixTimestamp-title.md` (e.g., 1761239003-returnvsrewardinreinforcementlearning.md)
3.2 **Aliases**: Required - Use original title as alias (e.g., "Return vs reward in reinforcement learning")
3.3 **Tags**: All lowercase in frontmatter YAML; #duda for questions needing answers
3.4 **Template**: Mandatory: Check 99-meta/01-templ/noteTemplate.md before every note creation
3.5 **Structure**: Keep notes atomic and concise; link related concepts
3.6 **No Emojis**: Never use emojis in any notes or files

## 4. AI-Generated Notes Rules

4.1 **Critical**: Never modify files in 02-atomic, 01-areas, or any folder except 98-ai
4.2 **Location**: All AI notes must go in `98-ai` folder - no exceptions
4.3 **Tag**: Include 'artificial' tag to mark as AI-generated
4.4 **Format**: Must follow noteTemplate.md exactly - intro callout, Up/Down sections required
4.5 **Intro**: Write a concise description in the > [!info] Intro: callout
4.6 **Dictionary**: Use `> [!example]- Dictionary` (collapsible) callout with **term ->** Definition format
4.7 **Properties**: Use `> [!important]` Properties: callout with **property:** Definition format
4.8 **Content Structure**: Use ## headings for sections, keep atomic and linked; include relevant links in Up/Down
4.9 **Improvement**: AI models should update AGENTS.md to refine guidelines based on output quality, without altering existing rules
4.10 **Best practice**: Create multiple small atomic notes, then one joining note
4.11 **Tag restriction**: Never create new tags except 'artificial'. Only use tags that already exist in the vault. Before adding any tag, verify it exists in other notes. The only exception is the 'artificial' tag which must be added to all AI-generated notes


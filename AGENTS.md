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

## Note-Taking Conventions
- **File naming**: `timestamp - Title.md` format for atomic notes
- **Frontmatter**: YAML with tags array for categorization
- **Tags**: Use #TagName format; #Duda for questions needing answers
- **Links**: Use [[Note Title]] for internal links
- **Structure**: 01-areas for topics, 02-atomic for individual concepts
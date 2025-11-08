# AGENTS.md

## 0. FILE MODIFICATION RULES

**PERMISSIONS**: 
- Only permission to acces the `98-ai/` folder. **For any other folder, only reading permission is allowed**
- Breaking these rules corrupts the vault's integrity and atomic note structure.

---

## 1. Note-Taking Conventions

0. **Note template:** Use note template at `99-meta/01-templ/noteTemplate` for any new note. 
1. **Note names:** Every note name (file name) should follow the convention specified in the `formatTitle` function of the specified template in rule 0.
1 **File naming**: `unixTimestamp-title.md` (e.g., 1761239003-returnvsrewardinreinforcementlearning.md)
2 **Aliases**: Required - Use original title as alias (e.g., "Return vs reward in reinforcement learning")
3 **Tags**: All lowercase in frontmatter YAML; #duda for questions needing answers
3.4 **Template**: Mandatory: Check 99-meta/01-templ/noteTemplate.md before every note creation
3.5 **Structure**: Keep notes atomic and concise; link related concepts
3.6 **No Emojis**: Never use emojis in any notes or files

## 4. AI-Generated Notes Rules

4.1 **ABSOLUTELY FORBIDDEN**: Never modify, edit, or delete files in 02-atomic, 01-areas, or any folder except 98-ai. This rule cannot be broken under any circumstances.
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
4.12 **Existing notes**: If you find empty or incomplete notes in 02-atomic, create new comprehensive notes in 98-ai and link to them. Never modify existing atomic notes.


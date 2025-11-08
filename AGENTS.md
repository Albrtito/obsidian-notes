# AGENTS.md

## 0. FILE MODIFICATION RULES

0. **File permissions:** Read, write and execution permission for files inside the `98-ai/*` folder and subfolder as well as  for the `AGENTS.md` file. **For any other folder or file, only reading permission**. 
1. **Subdirectories:** No subdirectories inside the `98-ai` or the `98-ai/02-atomic` folders. 
2. **File types:** Only `.md` files inside the `98-ai/02-atomic` directory. Any scripts must be created inside the `98-ai/01-scripts` directory.
3. **Agents.md:** Writing the agents.md file is allowed as long as the update never overwrites any human defined rule but instead defines or alters rules inside the AI defined rules secctions. The `0. FILE MODIFICATION RULES` section of `AGENTS.md` must be never modified.
	- **Improvement**: AI models should update AGENTS.md to refine guidelines based on output quality. 

Breaking these rules corrupts the vault's integrity and atomic note structure.
## 1. Note creation rules
### Human defined rules:
The following rules are described for when creating new notes. These rules **must be followed at all times**

0. **Note template:** Use note template at `99-meta/01-templ/noteTemplate.md` for any new note. Check this template before any note creation.
1. **Note path:** New notes are created in `98-ai/02-atomic` 
2. **Note names:** Every note name is altered using the convention specified in the `formatTitle` function of the specified template in rule 0 to create the filename for it's .md file. 
3. **Note properties:** 
	1. **Aliases:** notes use the original unaltered name as an alias.
	2. **Tags:** **DO NOT CREATE NEW TAGS**. All notes must have **ONLY** the #artificial tag.
4. **Best practice**: Create multiple atomic notes describing concepts, then one joining note. Following the **Zettlekasten method**
### AI defined rules:
0. **Build/Test Commands:** No package.json or build system detected - this is a pure Markdown Obsidian vault
1. **Python Scripts:** Run scripts from `98-ai/01-scripts/` using `python3 script_name.py` 
2. **Single Script Test:** No specific test scripts found - create test scripts in `98-ai/01-scripts/` if needed
3. **File Naming:** Use Unix timestamp + hyphen + formatted title (lowercase, no special chars, no spaces)
4. **Frontmatter Format:** Include aliases (original title), tags (subject-specific + #artificial for AI notes), id field with timestamp
5. **Content Structure:** Use callouts for definitions ([!info] Intro:), intro sections, and organize with Up/Down link sections
6. **Vault Structure:** Strict directory separation - scripts in `98-ai/01-scripts/`, notes in `98-ai/02-atomic/`, templates in `99-meta/01-templ/`
7. **Existing Note Links:** When linking to existing notes, use format `[[timestamp - title|display text]]` for atomic note references
8. **Spaced Repetition:** Existing notes may include sr-due, sr-ease, sr-interval fields for spaced repetition - preserve these when editing
9. **Note Structure:** Follow existing patterns - use ## for sections, maintain subject-specific tags from existing vault taxonomy

## 2. Note formatting:
### Human defined rules:

0. **Callouts:** Use the Intro, Dictionary and Properties callouts to define: An introduction to the note's concept, the dictionary of terms used for the current node, properties of the current note's concept.
1. **Links:** Link to related concepts (in text) if the linked note concept is directly mentioned. If not link them in the up/down section. **Only link to existing notes**
2. **No Emojis:** Never use emojis in any notes or files
3. **Language:** Use english for all notes

### AI defined rules:
0. **Code Style:** Follow existing patterns - use YAML frontmatter, callout syntax, double-bracket links
1. **Import/Link Style:** Use `[[timestamp - title|display text]]` for internal links, maintain atomic note relationships  
2. **Error Handling:** Python scripts use try/except for YAML parsing, graceful file handling with encoding='utf-8'
3. **Naming Conventions:** Variables in snake_case (Python), file operations use pathlib.Path for cross-platform compatibility
4. **Type Safety:** No explicit typing detected, but use descriptive variable names and clear function signatures
5. **Template Usage:** Always reference the `noteTemplate.md` which includes Templater plugin syntax for dynamic content generation
6. **Markdown Standards:** Use standard markdown with Obsidian extensions (callouts, wikilinks, YAML frontmatter)
7. **Content Language:** Existing vault contains Spanish content - respect language consistency when editing existing notes
8. **Subject Tags:** Preserve existing subject tags like #cripto, #empresa, avoid creating new tag hierarchies
9. **Virtual Environment:** Python development uses venv in `99-meta/02-scripts/.venv` - activate before running scripts



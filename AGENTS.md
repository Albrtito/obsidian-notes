# AGENTS.md

## 0. FILE MODIFICATION RULES

0. **Permissions:** Read, write and execution permissions inside the `98-ai/` folder and for the `AGENTS.md` file. **For any other folder or file, only reading permission is allowed**
1. **File types:** Only `.md` files inside the `98-ai/` directory. Any scripts must be created inside the `98-ai/01-scripts` directory.
2. **Agents.md:** Writing the agents.md file is allowed as long as the updated 
	- **Improvement**: AI models should update AGENTS.md to refine guidelines based on output quality. This update must never overwrite any human defined rule but instead define or alter rules inside the AI defined rules secctions. 

Breaking these rules corrupts the vault's integrity and atomic note structure.
## 1. Note creation rules
### Human defined rules:
The following rules are described for when creating new notes. These rules **must be followed at all times**

0. **Note template:** Use note template at `99-meta/01-templ/noteTemplate` for any new note. Check this template before any note creation.
1. **Note names:** Every note name is altered using the convention specified in the `formatTitle` function of the specified template in rule 0 to create the filname for its .md file. 
2. **Note properties:** 
	1. **Aliases:** notes use the original unaltered name as an alias.
	2. **Tags:** **No permission to create new tags**. All generated notes must have at least the #artificial tag.
3. **Best practice**: Create multiple atomic notes describing concepts, then one joining note. Following the **Zettlekasten method**
### AI defined rules:
0. **Build/Test Commands:** No package.json or build system detected - this is a pure Markdown Obsidian vault
1. **Python Scripts:** Run scripts from `99-meta/02-scripts/` using `python3 script_name.py` 
2. **Single Script Test:** Run `python3 99-meta/02-scripts/buscar_dudas.py` to test the dudas analyzer
3. **File Naming:** Use Unix timestamp + hyphen + formatted title (lowercase, no special chars, no spaces)
4. **Frontmatter Format:** Include aliases (original title), tags (subject-specific + #artificial for AI notes), References, cssclasses
5. **Content Structure:** Use callouts for definitions ([!NOTE]), intro sections, and organize with Up/Down link sections

## 2. Note formatting:
### Human defined rules:

0.  **Callouts:** Use the Intro, Dictionary and Properties callouts to define: An introduction to the note's concept, the dictionary of terms used for the current node, properties of the current note's concept.
1. **Links:** Link to related concepts in text if the linked note is directly mentioned. If not link them in the up/down section.
2. **No Emojis:** Never use emojis in any notes or files

### AI defined rules:
0. ...



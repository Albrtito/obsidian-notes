# AGENTS.md

## 0. FILE MODIFICATION RULES

**PERMISSIONS**: 
- Read, write and execution permissions inside the `98-ai/` folder and for the `AGENTS.md` file. **For any other folder or file, only reading permission is allowed**
- Breaking these rules corrupts the vault's integrity and atomic note structure.


## 1. Note creation rules
The following rules are described for when creating new notes. These rules **must be followed at all times**

0. **Note template:** Use note template at `99-meta/01-templ/noteTemplate` for any new note. Check this template before any note creation.
1. **Note names:** Every note name is altered using the convention specified in the `formatTitle` function of the specified template in rule 0 to create the filname for its .md file. 
2. **Note properties:** 
	1. **Aliases:** notes use the original unaltered name as an alias.
	2. **Tags:** **No permission to create new tags**. All generated notes must have at least the #artificial tag.
3. **Best practice**: Create multiple atomic notes describing concepts, then one joining note. Following the **Zettlekasten method**



## 2. Note formatting:

0.  **Callouts:** Use the Intro, Dictionary and Properties callouts to define: An introduction to the note's concep
1. 
3.5 **Structure**: Keep notes atomic and concise; link related concepts
3.6 **No Emojis**: Never use emojis in any notes or files
4.6 **Dictionary**: Use `> [!example]- Dictionary` (collapsible) callout with **term ->** Definition format
4.7 **Properties**: Use `> [!important]` Properties: callout with **property:** Definition format


4.8 **Content Structure**: Use ## headings for sections, keep atomic and linked; include relevant links in Up/Down
4.9 **Improvement**: AI models should update AGENTS.md to refine guidelines based on output quality, without altering existing rules
4.10 


<%*
// Prompt the user for a title to append
let userTitle = await tp.system.prompt("Enter title");
// Get the current file title
let currentTitle = tp.file.title;
// Append the user's input to the current title
let newTitle = userTitle ? `${currentTitle} ${userTitle}` : `${currentTitle} - Untitled Suffix`;
// Rename the file
await tp.file.rename(newTitle);

// Get a list of all folders in the vault
let folders = app.vault.getAllFolders().map(folder => folder.path);

// Prompt the user to select a folder
let selectedFolder = await tp.system.suggester(folders, folders, "Select a folder (or enter a new folder path)");

// If the selected folder doesn't exist, create it
if (!app.vault.getAbstractFileByPath(selectedFolder)) {
  let newFolder = await app.vault.createFolder(selectedFolder);
}

// Move the file to the selected folder
await tp.file.move(`${selectedFolder}/${newTitle}`);
%>
---
aliases:
  - <%userTitle%>
tags:
  - incomplete 
---
# <%userTitle%>
<% tp.file.cursor(10) %>
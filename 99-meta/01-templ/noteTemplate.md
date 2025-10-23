<%* 
// Prompt the user for a title
let userTitle = await tp.system.prompt("Enter title");
// Prompt for tags
let tags= await tp.system.prompt("Enter tag");

// Get the current file title to use as prefix
let currentTitle = tp.file.title;

// Function to format the title like Obsidian plugin for nvim
function formatTitle(title) {
    return title
        .toLowerCase()                    // Convert to lowercase
        .replace(/[^a-z0-9\s]/g, '')     // Remove special characters, keep letters, numbers, and spaces
        .replace(/\s+/g, '')             // Remove all spaces
        .trim();                         // Trim any remaining whitespace
}

// Format the user's input
let formattedTitle = userTitle ? formatTitle(userTitle) : "untitledsuffix";

// Create the new title with current title as prefix
let newTitle = `${currentTitle}-${formattedTitle}`;

// Rename the file
await tp.file.rename(newTitle);
-%>
---
aliases:
- <% userTitle %>
tags:
- <%tags%>
---
# <% userTitle %>
> [!NOTE] Intro: 
> <% tp.file.cursor(10) %>




***
### Up
### Down
***
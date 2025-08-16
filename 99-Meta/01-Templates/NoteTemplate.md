<%* 
// Prompt the user for a title
let userTitle = await tp.system.prompt("Enter title");

// Define your prefix here
let prefix = "prefix"; // Change this to whatever prefix you want

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

// Create the new title with prefix
let newTitle = `${prefix}-${formattedTitle}`;

// Rename the file
await tp.file.rename(newTitle);
-%>
---
aliases:
  - <% userTitle %>
tags:
References:
cssclasses:
---
# <% userTitle %>
> [!NOTE] Intro: 
> <% tp.file.cursor(10) %>

***

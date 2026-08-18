// ==========================================
// 1. STATE MANAGEMENT (SINGLE SOURCE OF TRUTH)
// ==========================================
// Holds all shopping items. Each item will be an object like: { id: 123, name: "Teff", done: false }
let items = [];

// ==========================================
// 2. DOM ELEMENT SELECTION
// ==========================================
// Select HTML elements by their CSS selectors so JS can interact with them
const form = document.querySelector("#add-form");       // The form element
const nameInput = document.querySelector("#name");      // Input text box
const list = document.querySelector("#list");           // The <ul> list container
const count = document.querySelector("#count");         // The item counter paragraph

// ==========================================
// 3. RENDER FUNCTION (UPDATES SCREEN FROM STATE)
// ==========================================
function render() {
  // Clear all current items inside <ul> to start clean
  list.innerHTML = "";

  // Loop through every item object inside the items array
  items.forEach(item => {
    // Step A: Create dynamic list item node in memory
    const li = document.createElement("li");
    li.textContent = item.name; // Insert name into li
    
    // Store unique ID in element dataset (e.g. data-id="169000...") for lookup later
    li.dataset.id = item.id;

    // If item status is marked done, add CSS class "done" to cross it out
    if (item.done) {
      li.classList.add("done");
    }

    // Step B: Create a delete button for this specific item
    const delBtn = document.createElement("button");
    delBtn.textContent = "X";
    delBtn.className = "del"; // Assign CSS class for styling

    // Step C: Assemble and place elements in the tree
    li.append(delBtn); // Put delete button inside <li>
    list.append(li);   // Put <li> inside the main <ul> list
  });

  // Update item counter text
  count.textContent = `${items.length} items`;
}

// ==========================================
// 4. ADD ITEM HANDLER (FORM SUBMISSION)
// ==========================================
form.addEventListener("submit", (e) => {
  // Prevent default behavior (which reloads the whole web browser page)
  e.preventDefault();

  // Read input value and remove trailing white spaces
  const name = nameInput.value.trim();

  // Basic validation: stop if input string is empty
  if (!name) return;

  // Create a new item object
  const newItem = {
    id: Date.now(), // Generate unique ID using current timestamp
    name: name,     // Item name entered by user
    done: false     // Default status
  };

  // Push new item into state array
  items.push(newItem);

  // Reset form input box to empty
  nameInput.value = "";

  // Re-render UI to display updated array
  render();
});

// ==========================================
// 5. EVENT DELEGATION (HANDLE TOGGLE & DELETE)
// ==========================================
// Instead of adding click listeners to every single row, add ONE listener to parent list
list.addEventListener("click", (e) => {
  // Find closest parent <li> of clicked target element
  const li = e.target.closest("li");
  
  // Exit if click happened outside any item row
  if (!li) return;

  // Retrieve item ID stored in dataset attribute (converted to number)
  const id = Number(li.dataset.id);

  // Case A: User clicked on Delete button ("X")
  if (e.target.matches(".del")) {
    // Filter out item with matching ID (removes it from items array)
    items = items.filter(item => item.id !== id);
  } 
  // Case B: User clicked anywhere else on item row
  else {
    // Find item object in items array
    const item = items.find(item => item.id === id);
    if (item) {
      // Toggle state status boolean (true -> false or false -> true)
      item.done = !item.done;
    }
  }

  // Redraw page state
  render();
});
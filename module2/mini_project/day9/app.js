// ==========================================
// 1. DOM Element Cache (Cached ONCE at top)
// ==========================================
const itemForm = document.getElementById('item-form');
const nameInput = document.getElementById('item-name');
const priceInput = document.getElementById('item-price');
const itemList = document.getElementById('item-list');
const totalDisplay = document.getElementById('total-display');

// Application State
let runningTotal = 0;

// ==========================================
// 2. Helper Functions
// ==========================================
function updateTotal(amountChange) {
    runningTotal += amountChange;
    // Guard against tiny precision floating-point errors
    if (runningTotal < 0.001) runningTotal = 0;
    totalDisplay.textContent = runningTotal.toFixed(2);
}

// ==========================================
// 3. Form Submit Handler
// ==========================================
itemForm.addEventListener('submit', (e) => {
    // Prevent page refresh on submit
    e.preventDefault();

    const name = nameInput.value.trim();
    const price = parseFloat(priceInput.value);

    // Validation check
    if (!name || isNaN(price) || price < 0) {
        alert('Please provide a valid item name and positive ETB price.');
        return;
    }

    // Create DOM elements (Without rebuilding entire list)
    const li = document.createElement('li');
    li.className = 'item-row';
    li.dataset.price = price; // Attach price to row element dataset

    const infoSpan = document.createElement('span');
    infoSpan.className = 'item-info';
    infoSpan.textContent = `${name} — ${price.toFixed(2)} ETB`;

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.textContent = 'Delete';

    // Append children to list item, then append list item to container
    li.append(infoSpan, deleteBtn);
    itemList.append(li);

    // Update total
    updateTotal(price);

    // Reset inputs
    itemForm.reset();
    nameInput.focus();
});

// ==========================================
// 4. Delegated Event Listener on Parent List
// ==========================================
itemList.addEventListener('click', (e) => {
    const target = e.target;
    const row = target.closest('.item-row');

    // Guard clause if click happened outside an item row
    if (!row) return;

    // Check if click was on the Delete Button
    if (target.classList.contains('delete-btn')) {
        const itemPrice = parseFloat(row.dataset.price);
        updateTotal(-itemPrice);
        row.remove();
        return;
    }

    // Otherwise, toggle the "bought" state class on the row
    row.classList.toggle('bought');
});
// ==========================================
// 1. APPLICATION STATE
// ==========================================
// Array of order objects (Single Source of Truth)
let orderState = [];

// ==========================================
// 2. DOM ELEMENT SELECTION (querySelector)
// ==========================================
const orderForm = document.querySelector('#order-form');
const dishInput = document.querySelector('#dish-name');
const quantityInput = document.querySelector('#quantity');
const spiceInput = document.querySelector('#spice-level');
const orderList = document.querySelector('#order-list');
const totalCountEl = document.querySelector('#total-count');

// ==========================================
// 3. RENDER FUNCTION (Updates DOM from State)
// ==========================================
function renderOrder() {
  // Clear existing items in the DOM
  orderList.innerHTML = '';

  // Calculate total items count
  let totalQuantity = 0;

  if (orderState.length === 0) {
    orderList.innerHTML = '<li style="color: #888; text-align: center;">No items added yet.</li>';
  } else {
    // Re-render each element based on state
    orderState.forEach((item) => {
      totalQuantity += item.quantity;

      // Create elements dynamically
      const li = document.createElement('li');
      li.className = 'order-item';

      li.innerHTML = `
        <div class="order-info">
          <span class="order-title">${item.quantity}x ${item.dish}</span>
          <span class="order-details">Spice Level: ${item.spice}</span>
        </div>
        <button class="delete-btn" data-id="${item.id}">Remove</button>
      `;

      orderList.appendChild(li);
    });
  }

  // Update total count on the DOM
  totalCountEl.textContent = totalQuantity;
}

// ==========================================
// 4. FORM SUBMISSION (e.preventDefault & Inputs)
// ==========================================
orderForm.addEventListener('submit', (e) => {
  // Prevent browser from refreshing page
  e.preventDefault();

  // Read input values
  const dish = dishInput.value;
  const quantity = Number(quantityInput.value);
  const spice = spiceInput.value;

  // Create new state object
  const newItem = {
    id: Date.now(), // unique timestamp ID
    dish: dish,
    quantity: quantity,
    spice: spice
  };

  // Update application state
  orderState.push(newItem);

  // Reset inputs
  orderForm.reset();

  // Re-render UI
  renderOrder();
});

// ==========================================
// 5. EVENT DELEGATION (Handling dynamic deletes)
// ==========================================
// Listen on the parent <ul> container instead of individual buttons
orderList.addEventListener('click', (e) => {
  // Check if clicked target is a delete button
  if (e.target.matches('.delete-btn')) {
    // Read dataset ID from attribute
    const idToDelete = Number(e.target.dataset.id);

    // Update state by removing item
    orderState = orderState.filter(item => item.id !== idToDelete);

    // Re-render UI
    renderOrder();
  }
});

// Initial Render
renderOrder();
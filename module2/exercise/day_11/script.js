const form = document.getElementById('signupForm');
const nameInput = document.getElementById('name');
const phoneInput = document.getElementById('phone');
const messageArea = document.getElementById('messageArea');
const counterDisplay = document.getElementById('counter');
const tableBody = document.getElementById('signupsTableBody');

const ethioPhoneRegex = /^(?:\+251|251|0)?(9|7)\d{8}$/;
const STORAGE_KEY = 'signups';

// Load array safely with try...catch
function getSignups() {
  try {
    const rawData = localStorage.getItem(STORAGE_KEY);
    if (!rawData) return [];
    const parsed = JSON.parse(rawData);
    return Array.isArray(parsed) ? parsed : [];
  } catch (e) {
    console.error("Corrupted local storage data. Resetting...", e);
    localStorage.removeItem(STORAGE_KEY);
    return [];
  }
}

// Save helper
function saveSignups(dataArray) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(dataArray));
  } catch (e) {
    console.error("Failed to save to localStorage:", e);
  }
}

// Render table and count badge
function renderUI() {
  const signups = getSignups();
  
  // 1. Update counter
  counterDisplay.textContent = `Total Signups: ${signups.length}`;

  // 2. Render table rows
  tableBody.innerHTML = '';

  if (signups.length === 0) {
    tableBody.innerHTML = '<tr><td colspan="3">No registered signups found.</td></tr>';
    return;
  }

  signups.forEach((entry, index) => {
    const row = document.createElement('tr');

    const nameCell = document.createElement('td');
    nameCell.textContent = entry.name;
    row.appendChild(nameCell);

    const phoneCell = document.createElement('td');
    phoneCell.textContent = entry.phone;
    row.appendChild(phoneCell);

    const actionCell = document.createElement('td');
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.className = 'delete-btn';
    deleteBtn.addEventListener('click', () => deleteSignup(index));
    actionCell.appendChild(deleteBtn);
    row.appendChild(actionCell);

    tableBody.appendChild(row);
  });
}

// Delete item by index
function deleteSignup(index) {
  const signups = getSignups();
  signups.splice(index, 1);
  saveSignups(signups);
  renderUI();
}

// Submit handler with validation and duplicate prevention
form.addEventListener('submit', (event) => {
  event.preventDefault();
  messageArea.textContent = '';
  messageArea.className = '';

  const trimmedName = nameInput.value.trim();
  const trimmedPhone = phoneInput.value.trim();

  // Validate Name Length
  if (trimmedName.length < 2) {
    messageArea.textContent = 'Name must be at least 2 characters long.';
    messageArea.className = 'error';
    return;
  }

  // Validate Ethiopian Phone Regex
  if (!ethioPhoneRegex.test(trimmedPhone)) {
    messageArea.textContent = 'Please enter a valid Ethiopian phone number (e.g., 0912345678).';
    messageArea.className = 'error';
    return;
  }

  // Duplicate Phone Check
  const existingSignups = getSignups();
  const isDuplicate = existingSignups.some(entry => entry.phone === trimmedPhone);
  
  if (isDuplicate) {
    messageArea.textContent = 'This phone number has already been registered.';
    messageArea.className = 'error';
    return;
  }

  // Save new record
  existingSignups.push({ name: trimmedName, phone: trimmedPhone });
  saveSignups(existingSignups);

  // Update UI & reset inputs
  messageArea.textContent = 'Signup successfully recorded!';
  messageArea.className = 'success';
  form.reset();
  renderUI();
});

// Initial run on script initialization
renderUI();
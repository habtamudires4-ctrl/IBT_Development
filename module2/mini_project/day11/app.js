// DOM Element References
const form = document.getElementById('signupForm');
const nameInput = document.getElementById('name');
const phoneInput = document.getElementById('phone');
const messageArea = document.getElementById('messageArea');
const counterDisplay = document.getElementById('counter');
const entriesList = document.getElementById('entriesList');

// Regex for Ethiopian phone numbers as specified in requirements
const ETHIO_PHONE_REGEX = /^(?:\+251|0)9\d{8}$/;

// LocalStorage key
const STORAGE_KEY = 'day11_signups';

/**
 * Safely restores signups from localStorage.
 * Handles missing key (null), non-array types, and corrupt JSON strings using try...catch.
 * @returns {Array} Array of user records
 */
function loadSignups() {
  try {
    const rawData = localStorage.getItem(STORAGE_KEY);
    if (!rawData) {
      return [];
    }
    const parsedData = JSON.parse(rawData);
    if (!Array.isArray(parsedData)) {
      console.warn("Stored data is not an array. Resetting storage...");
      localStorage.removeItem(STORAGE_KEY);
      return [];
    }
    return parsedData;
  } catch (error) {
    console.error("Corrupted JSON detected in localStorage. Clearing key...", error);
    localStorage.removeItem(STORAGE_KEY);
    return [];
  }
}

/**
 * Stringifies and saves signups array to localStorage.
 * @param {Array} signupsArray - List of valid user entries
 */
function saveSignups(signupsArray) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(signupsArray));
  } catch (error) {
    console.error("Failed to write to localStorage:", error);
    showMessage("Storage limit reached or permission denied. Could not save entry.", "error");
  }
}

/**
 * Displays feedback messages strictly using textContent (prevents XSS).
 * @param {string} text - Message text
 * @param {'error'|'success'} type - Message status type
 */
function showMessage(text, type) {
  messageArea.textContent = text;
  messageArea.className = `message-area ${type}`;
}

/**
 * Clears status message area.
 */
function clearMessage() {
  messageArea.textContent = '';
  messageArea.className = 'message-area';
}

/**
 * Updates UI counter and renders stored entries.
 */
function updateUI() {
  const signups = loadSignups();

  // Update total count display
  counterDisplay.textContent = `Total Signups: ${signups.length}`;

  // Clear existing list elements
  entriesList.innerHTML = '';

  if (signups.length === 0) {
    const emptyLi = document.createElement('li');
    emptyLi.textContent = 'No registered signups yet.';
    emptyLi.className = 'empty-state';
    entriesList.appendChild(emptyLi);
    return;
  }

  // Render each saved entry safely
  signups.forEach((entry) => {
    const li = document.createElement('li');

    const nameSpan = document.createElement('span');
    nameSpan.textContent = entry.name; // Secure insertion via textContent

    const phoneSpan = document.createElement('span');
    phoneSpan.textContent = entry.phone; // Secure insertion via textContent
    phoneSpan.className = 'phone-text';

    li.appendChild(nameSpan);
    li.appendChild(phoneSpan);
    entriesList.appendChild(li);
  });
}

/**
 * Handles Form Submission Event
 */
form.addEventListener('submit', (event) => {
  // Prevent page refresh / submission default behavior
  event.preventDefault();
  clearMessage();

  // Read and trim input values
  const trimmedName = nameInput.value.trim();
  const trimmedPhone = phoneInput.value.trim();

  // 1. Validate Name Length
  if (trimmedName.length < 2) {
    showMessage("Name must be at least 2 characters long.", "error");
    nameInput.focus();
    return; // Halt on first error
  }

  // 2. Validate Phone against Ethiopian Regex
  if (!ETHIO_PHONE_REGEX.test(trimmedPhone)) {
    showMessage("Please enter a valid Ethiopian phone number starting with 09... or +2519... (10 or 13 digits total).", "error");
    phoneInput.focus();
    return; // Halt on first error
  }

  // Load existing records and append new valid entry
  const signups = loadSignups();
  signups.push({
    name: trimmedName,
    phone: trimmedPhone
  });

  // Save updated records array to localStorage as JSON string
  saveSignups(signups);

  // Clear form inputs
  form.reset();

  // Show success feedback
  showMessage("Signup successfully saved!", "success");

  // Re-render counter and list
  updateUI();
});

// Initial load execution when page loads
document.addEventListener('DOMContentLoaded', updateUI);
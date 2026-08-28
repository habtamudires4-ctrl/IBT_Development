// --- Step 1: DOM Elements & Global State ---
const statusArea = document.getElementById('statusArea');
const convertForm = document.getElementById('convertForm');
const amountInput = document.getElementById('amountInput');
const currencySelect = document.getElementById('currencySelect');
const resultArea = document.getElementById('resultArea');
const addToWatchlistBtn = document.getElementById('addToWatchlistBtn');
const watchlistContainer = document.getElementById('watchlistContainer');

const STORAGE_KEY = 'day12_watchlist';
const API_URL = 'https://open.er-api.com/v6/latest/ETB'; // Base currency ETB

// Central Application State
const state = {
  rates: {},
  watchlist: []
};

// --- Step 6: LocalStorage Helpers ---
function saveWatchlist() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state.watchlist));
  } catch (err) {
    console.error("Failed to save watchlist to localStorage:", err);
  }
}

function loadWatchlist() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch (err) {
    console.error("Corrupt data found in localStorage. Resetting...", err);
    localStorage.removeItem(STORAGE_KEY);
    return [];
  }
}

// Helper to show visual messages in UI
function setStatus(message, type = 'info') {
  statusArea.textContent = message;
  statusArea.className = `status-area ${type}`;
}

// --- Step 2 & 5: Rendering UI ---
function renderSelectOptions() {
  currencySelect.innerHTML = '';
  const currencies = Object.keys(state.rates);

  currencies.forEach((code) => {
    const option = document.createElement('option');
    option.value = code;
    option.textContent = `${code} (Rate: ${state.rates[code]})`;
    currencySelect.appendChild(option);
  });
}

function renderWatchlist() {
  watchlistContainer.innerHTML = '';

  if (state.watchlist.length === 0) {
    const emptyLi = document.createElement('li');
    emptyLi.textContent = 'No currencies in watchlist.';
    watchlistContainer.appendChild(emptyLi);
    return;
  }

  state.watchlist.forEach((currencyCode) => {
    const rate = state.rates[currencyCode] || 'N/A';

    const li = document.createElement('li');
    li.className = 'watchlist-item';

    const infoSpan = document.createElement('span');
    infoSpan.textContent = `1 ETB = ${rate} ${currencyCode}`;

    // Delete button with data-c attribute for delegation
    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'Remove';
    removeBtn.className = 'remove-btn';
    removeBtn.setAttribute('data-c', currencyCode);

    li.appendChild(infoSpan);
    li.appendChild(removeBtn);
    watchlistContainer.appendChild(li);
  });
}

// --- Step 3: Fetching Live Exchange Rates ---
async function loadRates() {
  setStatus('Loading live exchange rates...', 'info');

  try {
    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }

    const data = await response.json();

    if (!data.rates) {
      throw new Error('Invalid rate data format received.');
    }

    // Save rates into central state
    state.rates = data.rates;

    setStatus('', ''); // Clear loading message
    renderSelectOptions();
    renderWatchlist(); // Re-render watchlist once rates are fetched
  } catch (err) {
    console.error('Fetch error:', err);
    setStatus('Failed to load exchange rates. Check network connection.', 'error');
  }
}

// --- Step 4: Convert Form Handling ---
convertForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const rawAmount = amountInput.value.trim();
  const numericAmount = Number(rawAmount);

  // Validation
  if (!rawAmount || isNaN(numericAmount) || numericAmount <= 0) {
    resultArea.textContent = 'Please enter a valid amount greater than 0.';
    resultArea.style.color = '#e74c3c';
    return;
  }

  const selectedCurrency = currencySelect.value;
  const rate = state.rates[selectedCurrency];

  if (!rate) {
    resultArea.textContent = 'Selected currency rate unavailable.';
    return;
  }

  // Calculate & format
  const convertedTotal = (numericAmount * rate).toFixed(2);
  resultArea.style.color = '#2c3e50';
  resultArea.textContent = `${numericAmount} ETB = ${convertedTotal} ${selectedCurrency}`;
});

// --- Step 5: Add to Watchlist & Event Delegation ---
addToWatchlistBtn.addEventListener('click', () => {
  const selectedCurrency = currencySelect.value;

  if (!selectedCurrency) return;

  // Guard against duplicate additions
  if (state.watchlist.includes(selectedCurrency)) {
    alert(`${selectedCurrency} is already in your watchlist!`);
    return;
  }

  // Update state & persist
  state.watchlist.push(selectedCurrency);
  saveWatchlist();
  renderWatchlist();
});

// Delegated click listener to remove currency items from watchlist
watchlistContainer.addEventListener('click', (event) => {
  const target = event.target;

  // Check if click was on a button with data-c attribute
  if (target.tagName === 'BUTTON' && target.hasAttribute('data-c')) {
    const currencyToRemove = target.getAttribute('data-c');

    // Filter out target item
    state.watchlist = state.watchlist.filter(code => code !== currencyToRemove);

    saveWatchlist();
    renderWatchlist();
  }
});

// --- Step 6: Initialization ---
function init() {
  // Load persisted watchlist state on page load
  state.watchlist = loadWatchlist();
  
  // Fetch live exchange rates
  loadRates();
}

// Execute app initialization when script loads
init();
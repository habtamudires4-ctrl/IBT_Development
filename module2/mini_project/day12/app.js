const API_URL = "https://open.er-api.com/v6/latest/ETB";
const STORAGE_KEY = "birrWatchState";

const state = {
    rates: {},
    watchlist: [],
    currency: "USD",
    amount: 1,
    loading: true,
    error: null
};

// Cache DOM elements
const els = {
    status: document.querySelector("#status"),
    statusContainer: document.querySelector("#status-container"),
    mainContent: document.querySelector("#main-content"),
    select: document.querySelector("#currency"),
    result: document.querySelector("#result"),
    watchlist: document.querySelector("#watchlist"),
    form: document.querySelector("#convert-form"),
    amountInput: document.querySelector("#amount"),
    watchBtn: document.querySelector("#watch-btn")
};

function init() {
    loadState();
    setupListeners();
    fetchRates();
}

async function fetchRates() {
    state.loading = true;
    state.error = null;
    renderStatus();

    try {
        const res = await fetch(API_URL);
        if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);
        
        const data = await res.json();
        if (!data.rates) throw new Error("Invalid rate data received.");

        state.rates = data.rates;
        state.loading = false;
        
        populateDropdown();
        renderStatus();
        render();
    } catch (err) {
        state.error = "Could not load live rates. Please try again later.";
        state.loading = false;
        renderStatus();
    }
}

function renderStatus() {
    if (state.loading) {
        els.status.textContent = "Loading rates...";
        els.status.className = "status-message";
        els.statusContainer.style.display = "block";
        els.mainContent.style.display = "none";
    } else if (state.error) {
        els.status.textContent = state.error;
        els.status.className = "status-message error";
        els.statusContainer.style.display = "block";
        els.mainContent.style.display = "none";
    } else {
        els.statusContainer.style.display = "none";
        els.mainContent.style.display = "block";
    }
}

function populateDropdown() {
    const fragment = document.createDocumentFragment();
    
    Object.keys(state.rates).forEach(code => {
        const option = document.createElement("option");
        option.value = code;
        option.textContent = code;
        fragment.appendChild(option);
    });

    els.select.replaceChildren(fragment);
}

function render() {
    els.select.value = state.currency;
    els.amountInput.value = state.amount;

    calculateResult();
    renderWatchlist();
}

function calculateResult() {
    if (isNaN(state.amount) || state.amount <= 0) {
        els.result.textContent = "Invalid amount";
        return;
    }

    const rate = state.rates[state.currency] ?? 1.0;
    const converted = (state.amount * rate).toFixed(2);
    
    els.result.textContent = `${state.amount} ETB = ${converted} ${state.currency}`;
}

function renderWatchlist() {
    if (state.watchlist.length === 0) {
        els.watchlist.innerHTML = `<li class="empty-watchlist">No currencies in your watchlist.</li>`;
        return;
    }

    els.watchlist.innerHTML = state.watchlist
        .map(currency => {
            const rate = state.rates[currency] ?? 1.0;
            const converted = (state.amount * rate).toFixed(2);

            return `
                <li class="watchlist-item">
                    <div class="watchlist-item-left">
                        <span>${state.amount} ETB</span>
                        <span class="arrow">&rarr;</span>
                    </div>
                    <div class="watchlist-item-right">
                        <span class="watchlist-item-val">${converted}</span>
                        <span class="watchlist-item-curr">${currency}</span>
                        <button type="button" class="remove-btn" data-currency="${currency}" title="Remove">&times;</button>
                    </div>
                </li>
            `;
        })
        .join("");
}

function setupListeners() {
    // Form input live conversion
    els.form.addEventListener("submit", (e) => {
        e.preventDefault();
        updateConversion();
    });

    els.select.addEventListener("change", () => {
        state.currency = els.select.value;
        saveState();
        calculateResult();
    });

    els.amountInput.addEventListener("input", () => {
        const num = parseFloat(els.amountInput.value);
        if (!isNaN(num) && num > 0) {
            state.amount = num;
            calculateResult();
            renderWatchlist();
        }
    });

    // Add to Watchlist
    els.watchBtn?.addEventListener("click", () => {
        const selectedCurrency = els.select.value;
        if (!selectedCurrency) return;

        if (!state.watchlist.includes(selectedCurrency)) {
            state.watchlist.push(selectedCurrency);
            saveState();
            renderWatchlist();
        } else {
            alert(`${selectedCurrency} is already in your watchlist!`);
        }
    });

    // Watchlist item deletion (Event Delegation)
    els.watchlist.addEventListener("click", (e) => {
        const removeBtn = e.target.closest(".remove-btn");
        if (!removeBtn) return;

        const currencyToRemove = removeBtn.dataset.currency;
        state.watchlist = state.watchlist.filter(c => c !== currencyToRemove);
        saveState();
        renderWatchlist();
    });
}

function updateConversion() {
    const num = parseFloat(els.amountInput.value);
    if (!isNaN(num) && num > 0) {
        state.amount = num;
        state.currency = els.select.value;
        saveState();
        render();
    } else {
        alert("Please enter a valid amount greater than 0");
    }
}

function saveState() {
    const dataToSave = {
        currency: state.currency,
        watchlist: state.watchlist
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(dataToSave));
}

function loadState() {
    const savedStr = localStorage.getItem(STORAGE_KEY);
    if (!savedStr) return;

    try {
        const savedData = JSON.parse(savedStr);
        if (savedData.currency) state.currency = savedData.currency;
        if (Array.isArray(savedData.watchlist)) state.watchlist = savedData.watchlist;
    } catch (e) {
        console.error("Failed to parse local storage state:", e);
    }
}

// Initialize Application
init();
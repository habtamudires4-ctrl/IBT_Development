// ==========================================
// 1. SELECT DOM ELEMENTS
// ==========================================
const searchForm = document.querySelector('#search-form');
const countryInput = document.querySelector('#country-input');
const factsContainer = document.querySelector('#facts');

// ==========================================
// 2. HELPER FUNCTION (Create DOM Fact Rows)
// ==========================================
function appendFactRow(parent, labelText, valueText) {
  const row = document.createElement('div');
  row.className = 'fact-item';

  const label = document.createElement('span');
  label.className = 'fact-label';
  label.textContent = labelText;

  const value = document.createElement('span');
  value.textContent = valueText;

  row.appendChild(label);
  row.appendChild(value);
  parent.appendChild(row);
}

// ==========================================
// 3. MAIN ASYNC FETCH & RENDER FUNCTION
// ==========================================
async function showCountry(name) {
  // STATE 1: LOADING
  factsContainer.innerHTML = '<p class="state-text">Loading...</p>';

  try {
    // Fetch data from public API
    const res = await fetch(`https://restcountries.com/v3.1/name/${encodeURIComponent(name)}`);

    // HTTP ERROR HANDLING (res.ok check)
    if (!res.ok) {
      if (res.status === 404) {
        throw new Error('Country not found');
      }
      throw new Error(`HTTP Error Status: ${res.status}`);
    }

    const data = await res.json();
    const country = data[0]; // Extract first matched result

    // Clear loading state
    factsContainer.innerHTML = '';

    // Render Flag using createElement
    if (country.flags && country.flags.png) {
      const flagImg = document.createElement('img');
      flagImg.src = country.flags.png;
      flagImg.alt = country.flags.alt || `Flag of ${country.name.common}`;
      flagImg.className = 'flag-img';
      factsContainer.appendChild(flagImg);
    }

    // Safely extract and format values
    const capital = country.capital ? country.capital[0] : 'N/A';
    const population = country.population ? country.population.toLocaleString() : 'N/A';
    const region = country.region || 'N/A';

    // Parse currencies object dynamically
    let currencyList = 'N/A';
    if (country.currencies) {
      currencyList = Object.values(country.currencies)
        .map(c => `${c.name} (${c.symbol || ''})`)
        .join(', ');
    }

    // STATE 2: SUCCESS (Render facts to DOM)
    appendFactRow(factsContainer, 'Country', country.name.common);
    appendFactRow(factsContainer, 'Capital', capital);
    appendFactRow(factsContainer, 'Population', population);
    appendFactRow(factsContainer, 'Region', region);
    appendFactRow(factsContainer, 'Currencies', currencyList);

  } catch (err) {
    // STATE 3: ERROR
    factsContainer.innerHTML = `<p class="state-text error-text">${err.message}</p>`;
  }
}

// ==========================================
// 4. EVENT LISTENERS
// ==========================================
searchForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const query = countryInput.value.trim();
  if (query) {
    showCountry(query);
  }
});

// DEFAULT ON INITIAL LOAD: Ethiopia (Addis Ababa)
showCountry('ethiopia');
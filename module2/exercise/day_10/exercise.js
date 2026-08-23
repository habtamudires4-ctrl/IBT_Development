// ============================================================================
// EXERCISE 1: Async function fetching USD to ETB exchange rate
// ============================================================================
async function getUsdToEtbRate() {
  const res = await fetch('https://open.er-api.com/v6/latest/USD');
  if (!res.ok) {
    throw new Error(`HTTP Error Status: ${res.status}`);
  }
  const data = await res.json();
  const rate = data.rates.ETB;
  return rate;
}

// Run Exercise 1
getUsdToEtbRate()
  .then(rate => console.log('Exercise 1 - USD to ETB Rate:', rate))
  .catch(err => console.error('Exercise 1 Error:', err.message));


// ============================================================================
// EXERCISE 2: Rewrite .then chain as async/await with try/catch
// ============================================================================
async function fetchAndRenderData() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    if (!res.ok) throw new Error(`HTTP Error Status: ${res.status}`);
    
    const data = await res.json();
    console.log('Exercise 2 - Fetched Post Title:', data.title);
  } catch (err) {
    console.error('Exercise 2 Error:', err.message);
  }
}

// Run Exercise 2
fetchAndRenderData();


// ============================================================================
// EXERCISE 3: Wrong URL (Network error) vs Real 404 URL (HTTP error)
// ============================================================================
async function testErrorHandling() {
  // Part A: Wrong domain (Fails network connection -> catch block triggers)
  try {
    await fetch('https://domain-that-does-not-exist-xyz123.com');
  } catch (err) {
    console.log('Exercise 3A (Network Error caught):', err.message);
  }

  // Part B: Real domain but 404 endpoint (Fetch succeeds, but res.ok is false)
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/invalid-page-404');
    console.log('Exercise 3B - Did fetch reject on 404? No. res.ok value is:', res.ok);

    if (!res.ok) {
      throw new Error(`Custom 404 Error! Status: ${res.status}`);
    }
  } catch (err) {
    console.log('Exercise 3B (HTTP 404 Error caught):', err.message);
  }
}

// Run Exercise 3
testErrorHandling();


// ============================================================================
// EXERCISE 4: Parallel fetches using Promise.all
// ============================================================================
async function fetchTopTwoItemsInParallel() {
  try {
    const listRes = await fetch('https://jsonplaceholder.typicode.com/posts');
    if (!listRes.ok) throw new Error('Failed to load item list');
    const posts = await listRes.json();

    // Fetch details for the first two items in parallel
    const [item1Res, item2Res] = await Promise.all([
      fetch(`https://jsonplaceholder.typicode.com/posts/${posts[0].id}`),
      fetch(`https://jsonplaceholder.typicode.com/posts/${posts[1].id}`)
    ]);

    if (!item1Res.ok || !item2Res.ok) throw new Error('Failed parallel item fetch');

    const [item1, item2] = await Promise.all([
      item1Res.json(),
      item2Res.json()
    ]);

    console.log('Exercise 4 - Parallel Items Fetched:', { item1, item2 });
  } catch (err) {
    console.error('Exercise 4 Error:', err.message);
  }
}

// Run Exercise 4
fetchTopTwoItemsInParallel();


// ============================================================================
// EXERCISE 5: 3-State Page (Loading, Success, Error)
// ============================================================================
const display = document.querySelector('#status-display');
const btn = document.querySelector('#load-btn');

btn.addEventListener('click', async () => {
  // STATE 1: LOADING
  display.textContent = 'Loading...';
  display.style.color = 'blue';

  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    
    if (!res.ok) {
      throw new Error(`HTTP Status Error: ${res.status}`);
    }

    const data = await res.json();

    // STATE 2: SUCCESS
    display.textContent = `Success! Data: "${data.title}"`;
    display.style.color = 'green';
  } catch (err) {
    // STATE 3: ERROR (Trigger by turning off Wi-Fi or going Offline in DevTools)
    display.textContent = `Error: ${err.message}`;
    display.style.color = 'red';
  }
});
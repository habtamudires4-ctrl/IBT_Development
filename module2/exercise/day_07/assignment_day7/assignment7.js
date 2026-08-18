// ==========================================
// 1. VAT Function with Default Parameter
// ==========================================
console.log("--- Question 1 ---");

// Standard function declaration with default parameter
function vat(amount, rate = 0.15) {
  return amount * rate;
}

// Arrow function with implicit return
const vatArrow = (amount, rate = 0.15) => amount * rate;

// Verifying outputs
console.log("Standard VAT (Default 15%):", vat(1000));         // Output: 150
console.log("Arrow VAT (Default 15%):", vatArrow(1000));       // Output: 150
console.log("Arrow VAT (Custom 10%):", vatArrow(1000, 0.10));  // Output: 100
console.log("\n");


// ==========================================
// 2. Private Counter with Closure
// ==========================================
console.log("--- Question 2 ---");

function makeCounter() {
  let count = 0; // Private state residing in lexical scope
  return function() {
    count++;
    return count;
  };
}

const counter = makeCounter();

console.log("Counter call 1:", counter()); // Output: 1
console.log("Counter call 2:", counter()); // Output: 2
console.log("Counter call 3:", counter()); // Output: 3

/* 
EXPLANATION OF PRIVACY:
The `count` variable remains private because it is scoped exclusively inside `makeCounter()`.
External scripts cannot access or modify `count` directly (e.g., `counter.count` returns `undefined`).
However, because the inner function forms a Closure over its outer lexical environment, 
it retains access to `count` across multiple calls while preserving its state safely.
*/
console.log("\n");


// ==========================================
// 3. Discount Factory
// ==========================================
console.log("--- Question 3 ---");

// Function factory returning a customized discount function
const discountBy = (rate) => (price) => price * (1 - rate);

// Creating specialized member and sale discount functions
const memberPrice = discountBy(0.10); // 10% discount
const salePrice = discountBy(0.30);   // 30% discount

const basePrice = 1000; // 1000 ETB

console.log(`Base Price: ${basePrice} ETB`);
console.log(`Member Price (10% off): ${memberPrice(basePrice)} ETB`); // Output: 900 ETB
console.log(`Sale Price (30% off): ${salePrice(basePrice)} ETB`);     // Output: 700 ETB
console.log("\n");


// ==========================================
// 4. Custom Higher-Order Function (applyToAll)
// ==========================================
console.log("--- Question 4 ---");

// Custom Higher-Order Function
function applyToAll(list, fn) {
  const result = [];
  for (let i = 0; i < list.length; i++) {
    result.push(fn(list[i]));
  }
  return result;
}

// Data array of raw prices in ETB
const rawPrices = [200, 500, 1000, 1500];

// Callback function adding 15% VAT
const addVat = (price) => price + (price * 0.15);

// Running applyToAll over rawPrices
const pricesWithVat = applyToAll(rawPrices, addVat);

console.log("Raw Prices:", rawPrices);
console.log("Prices with 15% VAT:", pricesWithVat); // Output: [230, 575, 1150, 1725]
console.log("\n");


// ==========================================
// 5. Iterating Array with forEach
// ==========================================
console.log("--- Question 5 ---");

const ethiopianCities = ['Addis Ababa', 'Gondar', 'Hawassa', 'Mekelle', 'Dire Dawa'];

// Iterating using forEach callback with index
ethiopianCities.forEach((city, index) => {
  console.log(`${index + 1}. ${city}`);
});
// ========================================================
// Demo Script for TeleBirr Loyalty Points Module
// ========================================================

import { createLoyalityAccount, standardEarnRule, holidayEarnRule } from './loyaltyModule.js';

console.log("================================================");
console.log("   TELEBIRR SHOP - LOYALTY POINTS DEMO          ");
console.log("================================================\n");

// 1. Create a primary customer loyalty card
const customerA = createLoyaltyAccount();

console.log("--- 1. Initial State & Privacy Verification ---");
console.log(`Customer A Balance: ${customerA.balance()} points`);
console.log(`Direct Access Check (customerA.points): ${customerA.points}`); // Output: undefined
console.log("\n");

// 2. Earn points using the Standard Rule (1 pt / 10 ETB)
console.log("--- 2. Earning Points (Standard Rule) ---");
const spentETB1 = 250; // Spent 250 ETB
const earned1 = customerA.earn(spentETB1, standardEarnRule);
console.log(`Spent: ${spentETB1} ETB | Points Earned: ${earned1}`);
console.log(`Updated Balance: ${customerA.balance()} points\n`);

// 3. Earning points using the Swappable Holiday Rule (Double Points)
console.log("--- 3. Earning Points (Holiday Double-Points Rule) ---");
const spentETB2 = 250; // Spent 250 ETB during promotion
const earned2 = customerA.earn(spentETB2, holidayEarnRule);
console.log(`Spent: ${spentETB2} ETB | Points Earned: ${earned2} (Holiday Bonus!)`);
console.log(`Updated Balance: ${customerA.balance()} points\n`);

// 4. Redeeming Points & Insufficient Funds Guard
console.log("--- 4. Redeeming Points ---");
console.log("Attempting to redeem 30 points...");
const success1 = customerA.redeem(30);
console.log(`Redemption Successful? ${success1}`);
console.log(`Remaining Balance: ${customerA.balance()} points\n`);

console.log("Attempting to redeem 500 points (Exceeding Balance)...");
const success2 = customerA.redeem(500);
console.log(`Redemption Successful? ${success2 ? "YES" : "NO (Prevented negative balance)"}`);
console.log(`Remaining Balance: ${customerA.balance()} points\n`);

// 5. Independent State Verification (Customer B)
console.log("--- 5. Independent Accounts Verification ---");
const customerB = createLoyaltyAccount(100); // Customer B starts with 100 bonus points
console.log(`Customer A Balance: ${customerA.balance()} points`);
console.log(`Customer B Balance: ${customerB.balance()} points`);
console.log("Are account balances completely independent?", customerA.balance() !== customerB.balance() ? "YES (Pass)" : "NO");

console.log("\n================================================");
// ==========================================
// 1. DATA STORE & IMMUTABILITY HANDLER
// ==========================================
const transactions = [
  { id: 101, customer: "Abebe Bikila", amount: 1500, type: "credit" },
  { id: 102, customer: "Tigist Assefa", amount: 450, type: "debit" },
  { id: 103, customer: "Mulugeta Seraw", amount: 2300, type: "credit" },
  { id: 104, customer: "Frehiwot Dado", amount: 120, type: "debit" },
  { id: 105, customer: "Biniam Girmay", amount: 800, type: "credit" }
];

// Pure function using the spread operator (...) for non-mutating updates
const updateTransactionAmount = (originalTx, newAmount) => ({
  ...originalTx,
  amount: newAmount
});

// ==========================================
// 2. REPORT CALCULATION FUNCTIONS (HOFs)
// ==========================================

// Filter & Reduce
const getTotalByType = (txList, txType) =>
  txList
    .filter(({ type }) => type === txType)
    .reduce((total, { amount }) => total + amount, 0);

// Map with Parameter Destructuring
const generateReceipts = (txList) =>
  txList.map(({ customer, amount, type }) => {
    const action = type === "credit" ? "[RECEIVED]" : "[PAID]";
    return {
      text: `Receipt: ${action} ${amount} ETB - ${customer}`,
      type
    };
  });

const generateReport = (txList) => ({
  totalCredits: getTotalByType(txList, "credit"),
  totalDebits: getTotalByType(txList, "debit"),
  netBalance: getTotalByType(txList, "credit") - getTotalByType(txList, "debit"),
  receipts: generateReceipts(txList)
});

// ==========================================
// 3. EXECUTION & DOM RENDERING
// ==========================================

// Perform immutability check
const originalTx = transactions[1]; // Tigist Assefa (450 ETB)
const updatedTx = updateTransactionAmount(originalTx, 500); // Corrected to 500 ETB

// Update log box in UI
const logBox = document.querySelector('#immutability-log');
logBox.innerHTML = `
  <strong>Immutability Check:</strong><br/>
  • Original Tx (Unchanged): ${originalTx.amount} ETB<br/>
  • Updated Copy (New Object): ${updatedTx.amount} ETB<br/>
  • Different References? <strong>${originalTx !== updatedTx ? "YES (Pass)" : "NO"}</strong>
`;

// Create updated list without mutating raw array
const activeTransactions = transactions.map(tx => tx.id === updatedTx.id ? updatedTx : tx);

// Generate calculations
const report = generateReport(activeTransactions);

// Update HTML metric elements
document.querySelector('#total-credits').textContent = `${report.totalCredits} ETB`;
document.querySelector('#total-debits').textContent = `${report.totalDebits} ETB`;
document.querySelector('#net-balance').textContent = `${report.netBalance} ETB`;

// Populate DOM receipt list items
const receiptsList = document.querySelector('#receipts-list');
report.receipts.forEach(({ text, type }) => {
  const li = document.createElement('li');
  li.textContent = text;
  li.classList.add(type);
  receiptsList.appendChild(li);
});
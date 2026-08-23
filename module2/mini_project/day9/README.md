# ETB Item Tracker & Shopping List

A web application built with vanilla JavaScript, HTML, and CSS to track items and their prices in Ethiopian Birr (ETB).

## Description
This project allows users to manage a list of items with real-time total price calculation. It incorporates optimized DOM manipulation techniques such as element caching, incremental DOM building, and event delegation.

## Features
- **Form Submission**: Add items by providing a name and ETB price without page reloading.
- **Form Validation**: Ensures both fields are correctly populated before insertion.
- **Incremental Rendering**: Appends elements individually using `document.createElement()` and `.append()`.
- **Bought Toggle**: Click any item row to toggle its "bought" state (styles visually via CSS class).
- **Single Delegated Delete Listener**: Delete items efficiently via a single listener attached to the parent `<ul>`.
- **Live Total**: Automatically updates the running total ETB price when items are added or removed.

## How to Open and Run
1. Clone or download this repository.
2. Open `index.html` directly in any standard web browser (or use the VS Code **Live Server** extension).
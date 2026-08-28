# Day 11 Mini Project 1: Ethiopian Signup Form & LocalStorage

This mini project is a client-side JavaScript signup form that demonstrates input validation using Regular Expressions (Regex), event handling, safe DOM manipulation with `textContent`, and local data persistence via `localStorage` and `JSON`.

---

## 🚀 Features

- **Form Validation**:
  - Name input requires at least 2 characters.
  - Phone input is checked against the regex `/^(?:\+251|0)9\d{8}$/` (supports `09...` and `+2519...`).
  - Inputs are trimmed before evaluation.
- **Security & Safe Rendering**:
  - Direct text updates using `textContent` to prevent Cross-Site Scripting (XSS).
- **Data Persistence**:
  - Converts records into JSON strings for storage in `localStorage`.
  - Automatically loads and displays total signups and previous entries upon page reload.
- **Resilient Data Loading**:
  - Guarded with `try...catch` blocks to seamlessly recover from `null`, invalid JSON, or corrupt local storage entries without throwing unhandled errors.

---

## ⚡ One Step to Open and Run

1. **Open `index.html` in any web browser.**  
   *(Double-click `index.html` or drag it directly into your web browser tab—no server setup or installation required).*

---

## 📁 Repository Structure

```text
├── index.html   # Main HTML structure with semantic elements & accessibility attributes
├── style.css    # Responsive styles and layout styling
├── app.js       # Core logic: Regex validation, DOM manipulation, JSON parsing, & LocalStorage handlers
└── README.md    # Documentation and setup instructions
# Ethio Telecom Customer Portal Dashboard

A reconstructed layout of the **Ethio Telecom Customer Portal Dashboard** built using CSS Grid for structural layout and Flexbox for nested UI components.

---

## 🛠️ Layout Architecture

* **CSS Grid (`grid-template-areas`)**: Used to construct the primary page skeleton (`header`, `sidebar`, `main`, and `footer`).
* **Flexbox Components**:
  * **Header & User Navigation**: Aligned horizontally using `justify-content: space-between`.
  * **Sidebar Menu**: Stacked vertically using `flex-direction: column`.
  * **Toolbar & Actions**: Structured using Flexbox alignment.
* **Responsive Card Grid**: Built using `repeat(auto-fit, minmax(220px, 1fr))` to reflow stat cards automatically without requiring media queries.
* **Sticky Navigation**: `.app-header` stays pinned at `top: 0` using `position: sticky`.
* **Anchored Badges**: `.status-badge` items are pinned absolutely (`position: absolute`) inside `.stat-card` parents (`position: relative`).
* **Mobile Breakpoint**: A single `@media (max-width: 700px)` query collapses the 2-column Grid layout into a single vertical layout.
# Country Facts Explorer

A single-page application built with vanilla JavaScript that fetches live data from the REST Countries API and renders country details dynamically.

## Features
- **Default Load:** Automatically fetches and displays facts for Ethiopia on initial launch.
- **Search Functionality:** Enables searching for any world country.
- **State Management:** Fully displays Loading, Success, and Friendly Error states.
- **Data Formatting:** Formats population numbers using `toLocaleString()`.
- **Error Handling:** Validates HTTP responses using `res.ok` to handle 404 errors gracefully.

## API Used
- **REST Countries API v3.1**: `https://restcountries.com/v3.1/name/{country}`

## How to Run
1. Download or clone this project repository.
2. Open `index.html` in any browser.
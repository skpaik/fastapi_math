# 📊 Number Analyzer API

A **FastAPI** project that analyzes a list of integers and returns useful statistics such as sum, even sum, odd sum, average, median, mode, and more.

---

## 🚀 Features

- Accepts a raw JSON array of integers (e.g., `[1, 2, 3, 4, 5]`)
- Returns:
    - Total sum, even sum, odd sum
    - Average, min, max
    - Median, mode, standard deviation
    - Count of numbers
- Fully type-safe using **Pydantic models**
- **Validation included**: returns `422` if input is empty or invalid
- OpenAPI/Swagger documentation at `/docs`

---

## 📂 Project Structure

```shell

app/
├── main.py # Entry point
├── api/ # Routers
│ └── numbers.py
├── models/ # Pydantic models
│ └── numbers.py
├── services/ # Business logic
│ └── numbers_service.py
├── core/ # Config, logging
│ └── config.py
└── tests/ # Unit tests
  └── test_numbers.py


```


---

## 🛠️ Setup

Clone the repository and run the setup script:

```bash
git clone <your-repo-url>
cd <your-repo-name>

# Install dependencies & set up environment
./after_clone.sh


# Run
./run.sh
```


Open the URL in browser
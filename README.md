# Insurance Premium Prediction

A machine learning application that predicts insurance premium categories — **Low**, **Medium**, or **High** — based on a user's demographics, lifestyle, and financial profile.

Built with **FastAPI** (REST API) and **Streamlit** (web UI), backed by a pre-trained **scikit-learn** classifier.

---

## Architecture

```
┌─────────────────────┐        HTTP POST /predict        ┌──────────────────────┐
│  Streamlit Frontend │ ───────────────────────────────► │  FastAPI Backend     │
│  (frontend.py)      │ ◄───────────────────────────────  │  (app.py)            │
└─────────────────────┘       JSON PredictResponse        └──────────┬───────────┘
                                                                      │
                                                          ┌───────────▼───────────┐
                                                          │  model/predict.py     │
                                                          │  (scikit-learn .pkl)  │
                                                          └───────────────────────┘
```

### Derived features computed server-side

| Field | Source |
|---|---|
| `bmi` | `weight / height²` |
| `age_group` | young / adult / middle_aged / senior |
| `lifestyle_risk` | low / medium / high (BMI + smoker status) |
| `city_tier` | 1 / 2 / 3 (from city name lookup) |

---

## Tech Stack

| Layer | Technology |
|---|---|
| REST API | FastAPI 0.135 + Uvicorn |
| Frontend | Streamlit 1.57 |
| Validation | Pydantic v2 |
| ML inference | scikit-learn 1.6 |
| Data handling | pandas 3.0 + numpy 2.4 |

---

## Prerequisites

- Python **3.12+**
- pip

---

## Quick Start

```bash
# 1. Clone the repository
git clone <repo-url>
cd insurance-premium-prediction

# 2. Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate          # Linux / macOS
# myenv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirement.txt

# 4. Configure environment
cp .env.example .env               # edit .env if needed

# 5. Start the API (terminal 1)
make api
# or: uvicorn app:app --reload

# 6. Start the frontend (terminal 2)
make frontend
# or: streamlit run frontend.py
```

Open **http://localhost:8501** for the UI or **http://localhost:8000/docs** for the interactive API docs.

---

## API Reference

### `GET /`
Health greeting.

### `GET /health`
```json
{
  "status": "ok",
  "model_version": "1.0.0",
  "model_loaded": true
}
```

### `POST /predict`

**Request body:**

| Field | Type | Description |
|---|---|---|
| `age` | int | 1 – 119 |
| `weight` | float | kg, > 0 |
| `height` | float | metres, > 0 |
| `income_lpa` | float | Annual income in LPA, > 0 |
| `smoker` | bool | true / false |
| `city` | string | City name (used for tier lookup) |
| `occupation` | string | One of: `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job` |

**Example request:**
```json
{
  "age": 35,
  "weight": 75.0,
  "height": 1.75,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Example response:**
```json
{
  "predicted_category": "Medium",
  "confidence": 0.7812,
  "class_probabilities": {
    "High": 0.1023,
    "Low": 0.1165,
    "Medium": 0.7812
  }
}
```

---

## Project Structure

```
.
├── app.py                  # FastAPI application
├── frontend.py             # Streamlit UI
├── requirement.txt         # Python dependencies
├── Makefile                # Dev shortcuts
├── .env.example            # Environment variable template
├── .env                    # Local environment (not committed)
├── .gitignore
├── README.md
├── config/
│   └── city_tier.py        # Tier 1 / Tier 2 city lists
├── model/
│   ├── model.pkl           # Pre-trained scikit-learn model
│   └── predict.py          # Inference logic
└── schema/
    ├── user_input.py       # Pydantic input model + derived fields
    └── prediction_response.py  # Pydantic response model
```

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `API_URL` | `http://localhost:8000/predict` | FastAPI endpoint used by the frontend |
| `MODEL_PATH` | `model/model.pkl` | Path to the serialised model file |
| `MODEL_VERSION` | `1.0.0` | Version string returned by `/health` |

---

## Contributing

1. Fork the repository and create a feature branch.
2. Follow PEP 8. Run `make lint` before committing.
3. Open a pull request with a clear description of the change.

---

## License

MIT

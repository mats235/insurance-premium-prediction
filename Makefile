.PHONY: install api frontend run lint clean

install:
	pip install -r requirement.txt

api:
	uvicorn app:app --host 0.0.0.0 --port 8000 --reload

frontend:
	streamlit run frontend.py

run:
	@echo "Start the API in one terminal:  make api"
	@echo "Start the frontend in another:  make frontend"

lint:
	python -m py_compile app.py model/predict.py schema/user_input.py schema/prediction_response.py frontend.py config/city_tier.py
	@echo "Syntax check passed."

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete

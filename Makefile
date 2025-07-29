.PHONY: *


# --- SERVICE ---

run.app:
	uvicorn src.app:create_app --host 0.0.0.0 --port 80


# --- DOCKER ---

run:
	docker compose up --build

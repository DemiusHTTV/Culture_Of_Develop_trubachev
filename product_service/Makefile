.PHONY: create-structure run

PORT ?= 8001
export PRODUCT_SERVICE_URL ?= http://localhost:$(PORT)

create-structure:
	mkdir -p src docs tests
	touch README.md requirements.txt setup.py
	touch src/.gitkeep tests/.gitkeep docs/DOMAIN.md

run:
	poetry run uvicorn src.app.main:app --host 0.0.0.0 --port $(PORT)

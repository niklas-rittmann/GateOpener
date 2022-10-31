.DEFAULT_GOAL := help
TAG := 0.0.1

run-server: # Run the server locally using uvicorn
	uvicorn opener.main:app --reload

install-requirements: # Install all python deps
	poetry install

export-requirements: install-requirements # Export the app requirements to ci/
	poetry export --without-hashes -o ci/backend/requirements.txt

build-backend: # Build the backend image
	docker build -t  gate_opener:${TAG} -f ci/backend/Dockerfile .

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
 

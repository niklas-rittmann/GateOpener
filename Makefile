.DEFAULT_GOAL := help
TAG := 0.0.1

run-server: # Run the server locally using uvicorn
	uvicorn opener.main:app --reload

install-requirements: # Install all python deps
	poetry install

export-requirements: install-requirements # Export the app requirements to ci/
	poetry export --without-hashes -o ci/backend/requirements.txt

dev-requirements: install-requirements # Export the app requirements to ci/
	poetry export --without-hashes --dev -o ci/backend/dev-requirements.txt

build-backend: # Build the backend image
	docker buildx build --platform linux/arm/v7 -t gate_opener:${TAG} -f ci/backend/Dockerfile .

tests: # Run test and calc coverage
	coverage run -m pytest test
	coverage report -m --skip-covered --ignore-errors

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

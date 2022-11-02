.DEFAULT_GOAL := help
TAG ?= 0.0.1
TARGET ?= base

run-server: # Run the server locally using uvicorn
	uvicorn opener.main:app --reload

install-requirements: # Install all python deps
	poetry install

export-requirements: install-requirements # Export the app requirements to ci/
	poetry export --without-hashes -o ci/backend/requirements.txt

dev-requirements: install-requirements # Export the app requirements to ci/
	poetry export --without-hashes --dev -o ci/backend/dev-requirements.txt

login: # Loginto docker registry
	echo ${DOCKER_PWD} | docker login -u ${DOCKER_USER} --password-stdin

push: login # Build and push image to registry
	docker buildx build --push --platform=linux/arm/v7,linux/amd64 --target ${TARGET} -t ${DOCKER_USER}/gate_opener:${TAG} -f ci/backend/Dockerfile .

tests: # Run test and calc coverage
	coverage run -m pytest test
	coverage report -m --skip-covered --ignore-errors

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

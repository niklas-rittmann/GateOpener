.DEFAULT_GOAL := help
TAG := 0.0.1
TARGET := testing

run-server: # Run the server locally using uvicorn
	uvicorn opener.main:app --reload

install-requirements: # Install all python deps
	poetry install

export-requirements: install-requirements # Export the app requirements to ci/
	poetry export --without-hashes -o ci/backend/requirements.txt

dev-requirements: install-requirements # Export the app requirements to ci/
	poetry export --without-hashes --dev -o ci/backend/dev-requirements.txt

build-backend: # Build the backend image
	docker buildx build --platform=linux/arm/v7,linux/amd64 --target ${TARGET} -t gate_opener:${TAG} -f ci/backend/Dockerfile .

login: build-backend # Login to docker
	echo ${{ secrets.DOCKER_PWD }} | docker login -u ${{ secrets.DOCKER_USER }} --password-stdin

push: login # Push to docker registry
	docker tag gate_opener:${TAG} ${ secrets.DOCKER_USER }/gate_opener:${TAG}
	docker push ${{ secrets.DOCKER_USER }}/gate_opener:${TAG}

tests: # Run test and calc coverage
	coverage run -m pytest test
	coverage report -m --skip-covered --ignore-errors

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

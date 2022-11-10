FROM python:3.10.8-slim-buster as base

WORKDIR /opt/gate

# Install installation requirements
RUN apt-get update && apt-get install -y build-essential

# Copy over requirements
COPY ci/backend/requirements.txt ./requirements.txt
COPY ci/backend/gunicorn_conf.py ./gunicorn_conf.py
COPY ci/backend/startup.sh ./startup.sh

# Create venv and install requirements
RUN python -m venv venv \
&& venv/bin/pip install -r requirements.txt \
&& venv/bin/pip install gunicorn

# Copy over source code
COPY ./opener ./opener

# Run guincorn
CMD ["./startup.sh"]

FROM base as testing

# Set env to have access to coverage
ENV PATH="/opt/gate/venv/bin:${PATH}" \
    PYTHONPATH="/opt/gate"

# Install aditional test requs
COPY ./test ./test
COPY ./ci/backend/dev-requirements.txt ./Makefile ./pyproject.toml ./

# Install dev requirements
RUN apt-get install make -y \
&& venv/bin/pip install -r dev-requirements.txt

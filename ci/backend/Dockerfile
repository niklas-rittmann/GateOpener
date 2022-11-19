FROM python:3.10.8-slim-buster as base

WORKDIR /opt/gate

# Install installation requirements
RUN apt-get update \
  && apt-get install -y build-essential libffi-dev curl libssl-dev

# Set env for rust
ARG PATH="/root/.cargo/bin:${PATH}"

# Copy over requirements
COPY ci/backend/requirements.txt ./requirements.txt
COPY ci/backend/gunicorn_conf.py ./gunicorn_conf.py
COPY ci/backend/startup.sh ./startup.sh

# Create venv and install requirements
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y \
  && python -m venv venv \
  && venv/bin/pip install --upgrade pip \
  && venv/bin/pip install -r requirements.txt \
  && venv/bin/pip install gunicorn \
  && rustup self uninstall \
  && rm -rf /root/.cargo

# Copy over source code
COPY ./opener ./opener
ENV PYTHONPATH="/opt/gate"

FROM base as prod

# Add non-root user to run webserver
RUN groupadd -g 1001 server \
  && useradd -m -u 1500 -s /bin/bash -g server webserver

# Run guincorn
CMD ["./startup.sh"]

FROM base as testing

# Set env to have access to coverage
ENV PATH="/opt/gate/venv/bin:${PATH}"

# Install aditional test requs
COPY ./test ./test
COPY ./ci/backend/dev-requirements.txt ./Makefile ./pyproject.toml ./

# Install dev requirements
RUN apt-get install make -y \
&& venv/bin/pip install -r dev-requirements.txt

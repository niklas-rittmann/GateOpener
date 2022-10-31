FROM python:3.10.8-slim-buster

WORKDIR /opt/gate

# Copy over requirements
COPY ci/backend/requirements.txt ./requirements.txt
COPY ci/backend/gunicorn_conf.py ./gunicorn_conf.py

# Create venv and install requirements
RUN python -m venv venv \
&& venv/bin/pip install -r requirements.txt \
&& venv/bin/pip install gunicorn

# Copy over source code
COPY ./opener ./opener

# Run guincorn
CMD ["venv/bin/gunicorn", "opener.main:app", "-c", "gunicorn_conf.py"]

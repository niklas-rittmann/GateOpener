import os

PORT = os.getenv("BACKEND_PORT", "8000")

worker_class = "uvicorn.workers.UvicornWorker"
bind = f"0.0.0.0:{PORT}"

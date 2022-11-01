from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from opener.internal.env import STATIC_DIR
from opener.routes import actions

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)
app.include_router(actions.router)

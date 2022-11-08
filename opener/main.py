from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from opener.internal.database import Base, engine
from opener.internal.env import STATIC_DIR
from opener.routes import actions, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)
app.include_router(actions.router)
app.include_router(auth.router)

from enum import Enum

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from opener.internal.auth import check_current_user
from opener.internal.env import TEMPLATES_DIR
from opener.internal.logic import trigger_gate


class Actions(Enum):
    trigger = "trigger"


class Action(BaseModel):
    action: Actions


class TriggerResp(BaseModel):
    action: Actions
    success: bool


router = APIRouter(
    tags=["actions"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def index(
    request: Request,
):
    return TEMPLATES_DIR.TemplateResponse("index.html", {"request": request})


@router.post("/", response_model=TriggerResp)
async def actions(action: Action, _=Depends(check_current_user)) -> TriggerResp:
    """Perform selected operation"""
    trigger_gate()
    return TriggerResp(action=action.action, success=True)

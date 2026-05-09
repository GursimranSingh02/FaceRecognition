from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home/index.html",
        context={},
    )


@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register/index.html",
        context={},
    )


@router.get("/detect")
async def detect_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="detect/index.html",
        context={},
    )

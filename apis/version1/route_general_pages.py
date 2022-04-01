from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html",
                                      {"request":request})


# routers/home.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize the router
router = APIRouter()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Define a route for the home page


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello, World!"})

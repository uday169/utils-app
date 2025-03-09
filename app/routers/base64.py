# routers/about.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize the router
router = APIRouter()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Define a route for the about page


@router.get("/base64-converter", response_class=HTMLResponse)
async def base64_converter(request: Request):
    return templates.TemplateResponse("base64.html", {"request": request, "message": "About Us"})

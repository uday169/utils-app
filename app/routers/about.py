# routers/about.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize the router
router = APIRouter()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Define a route for the about page


@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "message": "About Us"})

# main.py
from fastapi import FastAPI
from app.routers import home_router, about_router, base64_router
from fastapi.staticfiles import StaticFiles

# Initialize the FastAPI app
app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(home_router)
app.include_router(about_router)
app.include_router(base64_router)

# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

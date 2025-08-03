from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS - CRUCIAL for frontend-backend communication
# Adjust origins if your React app runs on a different port/domain
origins = [
    "http://localhost:3000",  # Default port for Create React App
    # You can add other origins here if needed, e.g., for production deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],    # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],    # Allow all headers
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI Backend!"}

@app.get("/status")
async def get_status():
    return {"status": "Backend is running", "version": "1.0.0"}
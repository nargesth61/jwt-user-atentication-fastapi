from fastapi import FastAPI
from app.routes import auth,profile

# Create FastAPI
app = FastAPI(
    title="User Management API",
    description="An API for user registration, login, email verification, and profile management",
    version="1.0.0",
)

app.include_router(auth.router, prefix="/user", tags=["auth"])
app.include_router(profile.router, prefix="/profile", tags=["profile"])


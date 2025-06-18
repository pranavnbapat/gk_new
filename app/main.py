# main.py

import os
import subprocess

from app.auth.routes import router as auth_router
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run Alembic migrations before the app starts
    print("Running Alembic migrations...")
    try:
        subprocess.run(
            ["alembic", "upgrade", "head"],
            cwd=os.path.dirname(__file__) + "/..",
            check=True
        )
        print("✅ Alembic migration successful.")
    except subprocess.CalledProcessError:
        print("❌ Alembic migration failed")

    yield  # App startup continues
    # Optional: shutdown logic here

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router, prefix="/api")

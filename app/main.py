import os
from fastapi import FastAPI
from routers import user, project
from fastapi.middleware.cors import CORSMiddleware

if os.getenv("ENV") == "production":  # Solo en producción
    from run_migrations import run_migrations
    run_migrations()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # URL de producción del frontend en Vercel
        "https://music-app-frontend-pc8g.vercel.app",
        "https://music-app-frontend-pc8g-5x5jpup4y-omars-projects-b5a3697e.vercel.app",
        "https://music-gen-demo-omars-projects-b5a3697e.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])


@app.get("/")
async def root():
    return {"message": "Welcome to the music app API!"}

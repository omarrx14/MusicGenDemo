import os
from alembic.config import Config
from alembic import command
from fastapi import FastAPI
from routers import user, project
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@app.lifespan("startup")
async def startup_event():
    run_migrations()


app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=[
        "https://music-app-frontend-pc8g.vercel.app",
        "https://music-app-frontend-pc8g-5x5jpup4y-omars-projects-b5a3697e.vercel.app",
        "https://music-gen-demo-omars-projects-b5a3697e.vercel.app"
    ],
)

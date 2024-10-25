import os
from alembic.config import Config
from alembic import command
from fastapi import FastAPI
from routers import user, project
from starlette.middleware.cors import CORSMiddleware

# Añadir la ruta de la raíz del proyecto para permitir importaciones relativas

os.environ["DATABASE_URL"] = "postgres://default:MbpU67rvGqKg@ep-green-credit-a4beru5o.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

config = Config()
config.set_main_option("sqlalchemy.url", os.environ["DATABASE_URL"])
config.set_section_option("alembic", "script_location", "alembic")
app = FastAPI()


app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])

origins = [
    "https://music-app-frontend-pc8g.vercel.app",
    "https://music-app-frontend-pc8g-5x5jpup4y-omars-projects-b5a3697e.vercel.app",
    "https://music-gen-demo-omars-projects-b5a3697e.vercel.app"
    # Agrega aquí cualquier otra variación necesaria
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

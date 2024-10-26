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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def add_cors_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,OPTIONS,PATCH,DELETE,POST,PUT"
    response.headers["Access-Control-Allow-Headers"] = "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
    return response

app.middleware('http')(add_cors_headers_middleware)

app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])

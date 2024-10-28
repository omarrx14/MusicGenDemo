import os
from fastapi import FastAPI, Request
from routers import user, project
from fastapi.middleware.cors import CORSMiddleware

# Configuración de la URL de la base de datos
os.environ["DATABASE_URL"] = "postgres://default:MbpU67rvGqKg@ep-green-credit-a4beru5o.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    # Permite cualquier subdominio de Vercel
    allow_origin_regex="https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)

# Middleware adicional para agregar encabezados CORS manualmente


@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "https://music-app-frontend-pc8g.vercel.app"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

# Middleware para logs de solicitudes y respuestas (opcional para depuración)


@app.middleware("http")
async def log_request(request: Request, call_next):
    print(f"Request method: {request.method}, path: {request.url.path}")
    response = await call_next(request)
    print(f"Response headers: {response.headers}")
    return response

# Rutas de la aplicación
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])


@app.get("/")
async def read_root():
    return {"message": "API is running"}

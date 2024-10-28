import os
from fastapi import FastAPI, Request
from app.routers import user, project
from fastapi.middleware.cors import CORSMiddleware

# Configuración de la URL de la base de datos

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    # URL exacta del frontend
    allow_origins=["music-app-frontend-pc8g.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)


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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

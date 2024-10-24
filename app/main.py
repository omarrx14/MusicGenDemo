from fastapi import FastAPI
from routers import user, project
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Permite solo tu origen de desarrollo
    allow_origins=[
        "http://localhost:5173",  # En desarrollo local
        # Dominio principal en producción (Vercel)
        "https://music-app-frontend-pc8g.vercel.app",
        "https://music-app-frontend-pc8g-3zhtbk91n-omars-projects-b5a3697e.vercel.app",
        "https://music-gen-demo-omarrx14.replit.app/"  # Subdominio temporal en Vercel
    ],
    allow_credentials=True,
    # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_methods=["*"],
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])


@app.get("/")
async def root():
    return {"message": "Welcome to the music app API!"}

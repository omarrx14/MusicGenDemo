from fastapi import FastAPI
from routers import user, project
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    # Permite cualquier origen, puedes restringir a ["http://127.0.0.1:5173"] o tu frontend específico
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])

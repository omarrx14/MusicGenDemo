from fastapi import FastAPI
from routers import user, project
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Permite solo tu origen de desarrollo
    allowed_origins=[
        "http://localhost:5173",
        "https://music-app-frontend-pc8g.vercel.app",
        "https://music-gen-demo.vercel.app",
        "https://music-app-frontend-pc8g-ciautrm86-omars-projects-b5a3697e.vercel.app"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user.router, prefix="/api/users", tags=["users"])
    app.include_router(
        project.router, prefix="/api/projects", tags=["projects"])


@ app.get("/")
async def root():
    return {"message": "Welcome to the music app API!"}

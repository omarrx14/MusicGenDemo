from fastapi import FastAPI
from routers import user, project

app = FastAPI()

app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(project.router, prefix="/api/projects", tags=["projects"])

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import User
from dependencies import get_current_user, get_db
from crud.project import create_project, get_projects_by_user
from schemas.project import ProjectCreate, Project
from typing import List
from models.project import Project as ProjectModel
from schemas.project import ProjectCreate

router = APIRouter()


# @router.post("/projects/", response_model=Project)
# def create_new_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return create_project(db=db, project=project, user_id=current_user.id)


# @router.get("/projects/", response_model=List[Project])
# def read_user_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     projects = get_projects_by_user(db=db, user_id=current_user.id)
#     if not projects:
#         raise HTTPException(status_code=404, detail="Projects not found")
#     return projects


@router.post("/", response_model=Project)
def create_new_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_project(db=db, project=project, user_id=current_user.id)


@router.get("/", response_model=List[Project])
def read_user_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    projects = get_projects_by_user(db=db, user_id=current_user.id)
    return projects


def update_project(db: Session, project_id: int, project_data: ProjectCreate):
    project = db.query(ProjectModel).filter(
        ProjectModel.id == project_id).first()
    if project:
        project.name = project_data.name
        project.project_data = project_data.project_data
        db.commit()
        db.refresh(project)
    return project

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import User
from dependencies import get_current_user, get_db
from crud.project import create_project, get_projects_by_user
from schemas.project import ProjectCreate, Project
from typing import List
from models.project import Project as ProjectModel

router = APIRouter()

# Crear un nuevo proyecto


@router.post("/", response_model=Project)
def create_new_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_project = Project(
        name=project.name,
        description=project.description,  # Nuevo campo agregado
        user_id=current_user.id,
        project_data=project.project_data  # Opcional
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


# Leer todos los proyectos del usuario actual


@router.get("/", response_model=List[Project])
def read_user_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    projects = db.query(ProjectModel).filter(
        ProjectModel.user_id == current_user.id).all()
    return projects

# Leer un proyecto específico por ID


@router.get("/{project_id}", response_model=Project)
def read_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(ProjectModel).filter(
        ProjectModel.id == project_id, ProjectModel.user_id == current_user.id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# Actualizar un proyecto existente


@router.put("/{project_id}", response_model=Project)
def update_project(project_id: int, updated_project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(ProjectModel).filter(
        ProjectModel.id == project_id, ProjectModel.user_id == current_user.id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    project.name = updated_project.name
    project.description = updated_project.description
    db.commit()
    db.refresh(project)
    return project

# Eliminar un proyecto existente


@router.delete("/{project_id}", response_model=Project)
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(ProjectModel).filter(
        ProjectModel.id == project_id, ProjectModel.user_id == current_user.id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()
    return project

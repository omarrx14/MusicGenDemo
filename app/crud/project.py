from sqlalchemy.orm import Session
from models.project import Project
from schemas.project import ProjectCreate


def create_project(db: Session, project: ProjectCreate, user_id: int):
    db_project = Project(name=project.name, user_id=user_id,
                         project_data=project.project_data)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_projects_by_user(db: Session, user_id: int):
    return db.query(Project).filter(Project.user_id == user_id).all()

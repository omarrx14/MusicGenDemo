from pydantic import BaseModel
from typing import Any, Optional


class ProjectBase(BaseModel):
    name: str
    project_data: Any


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None  # Descripción opcional
    # Datos adicionales del proyecto opcionales
    project_data: Optional[Any] = None

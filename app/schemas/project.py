from pydantic import BaseModel
from typing import Any


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

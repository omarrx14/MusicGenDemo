from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_data = Column(JSON)  # Aquí almacenaríamos las notas, efectos, etc.
    # Añadí el campo `description` si se espera en el esquema `ProjectCreate`
    description = Column(String, nullable=True)

    user = relationship("User", back_populates="projects")

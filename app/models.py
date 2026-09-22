from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.database import Base


def utcnow():
    return datetime.now(timezone.utc)


class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, default="")
    completada = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, default=utcnow)

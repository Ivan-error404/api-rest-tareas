from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TareaBase(BaseModel):
    titulo: str
    descripcion: str = ""


class TareaCreate(TareaBase):
    pass


class TareaUpdate(BaseModel):
    titulo: str | None = None
    descripcion: str | None = None
    completada: bool | None = None


class TareaOut(TareaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    completada: bool
    fecha_creacion: datetime

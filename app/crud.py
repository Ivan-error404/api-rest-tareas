from sqlalchemy.orm import Session

from app import models, schemas


def obtener_tareas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarea).offset(skip).limit(limit).all()


def obtener_tarea(db: Session, tarea_id: int):
    return db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()


def crear_tarea(db: Session, tarea: schemas.TareaCreate):
    db_tarea = models.Tarea(**tarea.model_dump())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea


def actualizar_tarea(db: Session, tarea: models.Tarea, datos: schemas.TareaUpdate):
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(tarea, campo, valor)
    db.commit()
    db.refresh(tarea)
    return tarea


def eliminar_tarea(db: Session, tarea: models.Tarea):
    db.delete(tarea)
    db.commit()

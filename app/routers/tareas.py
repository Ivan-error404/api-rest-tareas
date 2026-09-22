from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.TareaOut])
def listar_tareas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.obtener_tareas(db, skip=skip, limit=limit)


@router.post("", response_model=schemas.TareaOut, status_code=201)
def crear_tarea(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    return crud.crear_tarea(db, tarea)


@router.get("/{tarea_id}", response_model=schemas.TareaOut)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = crud.obtener_tarea(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@router.put("/{tarea_id}", response_model=schemas.TareaOut)
def actualizar_tarea(
    tarea_id: int, datos: schemas.TareaUpdate, db: Session = Depends(get_db)
):
    tarea = crud.obtener_tarea(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return crud.actualizar_tarea(db, tarea, datos)


@router.delete("/{tarea_id}", status_code=204)
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = crud.obtener_tarea(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    crud.eliminar_tarea(db, tarea)

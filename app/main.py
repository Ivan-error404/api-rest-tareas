from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import tareas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Tareas",
    description="API REST para gestionar tareas personales.",
    version="1.0.0",
    contact={"name": "Ivan", "url": "https://github.com/Ivan-error404"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tareas.router, prefix="/tareas", tags=["tareas"])


@app.get("/", tags=["root"])
def raiz():
    return {"mensaje": "API de Tareas", "docs": "/docs", "health": "/health"}


@app.get("/health", tags=["root"])
def health():
    return {"estado": "ok"}

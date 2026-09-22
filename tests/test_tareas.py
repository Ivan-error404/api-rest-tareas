from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=False,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_listar_tareas_vacia():
    respuesta = client.get("/tareas")
    assert respuesta.status_code == 200
    assert respuesta.json() == []


def test_crear_y_obtener_tarea():
    respuesta = client.post("/tareas", json={"titulo": "Estudiar DAM"})
    assert respuesta.status_code == 201
    tarea_id = respuesta.json()["id"]

    respuesta = client.get(f"/tareas/{tarea_id}")
    assert respuesta.status_code == 200
    assert respuesta.json()["titulo"] == "Estudiar DAM"


def test_actualizar_tarea():
    creada = client.post(
        "/tareas", json={"titulo": "Hacer ejercicio", "descripcion": "30 min"}
    ).json()
    respuesta = client.put(
        f"/tareas/{creada['id']}", json={"completada": True}
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["completada"] is True


def test_eliminar_tarea():
    creada = client.post("/tareas", json={"titulo": "Tarea temporal"}).json()
    respuesta = client.delete(f"/tareas/{creada['id']}")
    assert respuesta.status_code == 204

    respuesta = client.get(f"/tareas/{creada['id']}")
    assert respuesta.status_code == 404


def test_tarea_inexistente():
    respuesta = client.get("/tareas/9999")
    assert respuesta.status_code == 404

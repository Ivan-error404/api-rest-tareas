# API de Tareas

API REST profesional para gestionar tareas personales, desarrollada con **FastAPI**, **SQLAlchemy** y **SQLite**. Incluye documentación interactiva automática con Swagger UI.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## Características

- CRUD completo de tareas (crear, leer, actualizar, eliminar)
- Base de datos SQLite con SQLAlchemy (ORM)
- Documentación interactiva en `/docs` (Swagger UI) y `/redoc`
- Validación de datos con Pydantic v2
- Pruebas automáticas con pytest
- CORS habilitado para consumir desde cualquier frontend

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Servidor disponible en `http://localhost:8000`.

## Endpoints

| Método | Ruta          | Descripción                    |
|--------|---------------|--------------------------------|
| GET    | `/`           | Información de la API          |
| GET    | `/health`     | Estado del servicio            |
| GET    | `/tareas`     | Listar tareas                  |
| POST   | `/tareas`     | Crear una tarea                |
| GET    | `/tareas/{id}`| Obtener una tarea              |
| PUT    | `/tareas/{id}`| Actualizar una tarea           |
| DELETE | `/tareas/{id}`| Eliminar una tarea             |

## Ejemplo con curl

```bash
# Crear
curl -X POST http://localhost:8000/tareas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Aprender FastAPI", "descripcion": "Curso + practicas"}'

# Listar
curl http://localhost:8000/tareas
```

## Tests

```bash
pytest -v
```

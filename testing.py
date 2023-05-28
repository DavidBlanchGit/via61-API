import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from main import app
from conexion import SessionLocal
from tablas.models import Model_User

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_obtener_usuarios(test_client, SessionLocal):
    # Insertar algunos datos de prueba en la base de datos
    user1 = Model_User(
        txto_protonmail="usuario1@ejemplo.com",
        txto_psswrd="contraseña1",
        foto_perfil="ruta/imagen1.jpg",
        txto_nick="usuario1",
        cdgo_rango=1
    )
    user2 = Model_User(
        txto_protonmail="usuario2@ejemplo.com",
        txto_psswrd="contraseña2",
        foto_perfil="ruta/imagen2.jpg",
        txto_nick="usuario2",
        cdgo_rango=2
    )
    db.add(user1)
    db.add(user2)
    db.commit()

    # Realizar una solicitud GET a la ruta '/getUsers'
    response = test_client.get("/getUsers")

    # Verificar el código de respuesta
    assert response.status_code == 200

    # Verificar que la respuesta sea una lista de usuarios
    assert isinstance(response.json(), list)

    # Verificar que se hayan devuelto los usuarios esperados
    assert len(response.json()) == 2

    # Verificar que los usuarios devueltos coincidan con los datos de prueba
    assert response.json()[0]["txto_protonmail"] == "usuario1@ejemplo.com"
    assert response.json()[0]["txto_psswrd"] == "contraseña1"
    assert response.json()[0]["foto_perfil"] == "ruta/imagen1.jpg"
    assert response.json()[0]["txto_nick"] == "usuario1"
    assert response.json()[0]["cdgo_rango"] == 1

    assert response.json()[1]["txto_protonmail"] == "usuario2@ejemplo.com"
    assert response.json()[1]["txto_psswrd"] == "contraseña2"
    assert response.json()[1]["foto_perfil"] == "ruta/imagen2.jpg"
    assert response.json()[1]["txto_nick"] == "usuario2"
    assert response.json()[1]["cdgo_rango"] == 2

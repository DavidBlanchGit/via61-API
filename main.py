from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from tablas.models import Model_User
from tablas.schema import Schema_User, Schema_User_Update, Schema_Foto_Update, Exit_Code
from starlette.responses import RedirectResponse
from conexion import SessionLocal
from sqlalchemy.orm import Session
from typing import List
import hashlib
import uvicorn

# Crear la aplicacion de FastAPI
app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Redirecciona a docs
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
    
# Devuelve todos los usuarios
@app.get('/getUsers', response_model=List[Schema_User])
def obtener_usuarios(db: Session = Depends(get_db)):
    users = db.query(Model_User).all()
    return users

# Devuelve los usuarios por id
@app.get('/getUser/id/{user_id}', response_model=Schema_User)
def obtener_id_usuario(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Model_User).filter_by(nmro_id=user_id).first()
    return user

# Devuelve los usuarios por protonmail
@app.get('/getUser/protonmail/{protonmail}', response_model=Schema_User)
def obtener_protonmail(protonmail: str, db: Session = Depends(get_db)):
    user = db.query(Model_User).filter_by(txto_protonmail=protonmail).first()
    return user

# Crear usuarios
@app.post('/setUsers', response_model=Schema_User)
def insertar_usuarios(entrada:Schema_User, db: Session = Depends(get_db)):
    password = b'{entrada.txto_psswrd}'
    hashed_password = hashlib.sha256(password).hexdigest()
    user = Model_User(txto_protonmail = entrada.txto_protonmail, txto_psswrd = hashed_password,  txto_nick = entrada.txto_nick, cdgo_rango = 0)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Cambiar el nombre de usuario
@app.put('/changeUser/name/{user_id}', response_model=Schema_User)
def modificar_nombre_usuario(user_id: int,entrada:Schema_User_Update, db: Session = Depends(get_db)):
    user = db.query(Model_User).filter_by(nmro_id=user_id).first()
    user.txto_nick = entrada.txto_nick
    db.commit()
    db.refresh(user)
    return user

# Cambiar la foto de perfil
@app.put('/changeUser/foto/{user_id}', response_model=Schema_User)
def modificar_foto(user_id: int,entrada:Schema_Foto_Update, db: Session = Depends(get_db)):
    user = db.query(Model_User).filter_by(nmro_id=user_id).first()
    user.foto_perfil = entrada.foto_perfil
    db.commit()
    db.refresh(user)
    return user

# Sumar rango por personas con las que hables
@app.put('/changeUser/rango/{user_id}', response_model=Schema_User)
def mas_rango(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Model_User).filter_by(nmro_id=user_id).first()
    user.cdgo_rango = user.cdgo_rango+1
    db.commit()
    db.refresh(user)
    return user

# Borrar un usuario
@app.delete('/delUsers/{user_id}', response_model=Exit_Code)
def borrar_usuarios(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Model_User).filter_by(nmro_id=user_id).first()
    db.delete(user)
    db.commit()
    mensaje = Exit_Code(mensaje=0)
    return mensaje

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
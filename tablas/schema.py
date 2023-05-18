from typing import Optional
from pydantic import BaseModel

# Esquema del modelo de la base de datos
class Schema_User(BaseModel):
    nmro_id: int
    txto_protonmail: str
    txto_psswrd: str
    foto_perfil: str = None
    txto_nick: str
    cdgo_rango: int

    class Config:
        orm_mode = True

# Esquema para cambiar el nick  
class Schema_User_Update(BaseModel):
    txto_nick: str

    class Config:
        orm_mode = True

# Esquema para cambiar la foto
class Schema_Foto_Update(BaseModel):
    foto_perfil: str

    class Config:
        orm_mode = True

# Esquema de error
class Exit_Code(BaseModel):
    exit: int

    class Config:
        orm_mode = True
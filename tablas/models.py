from sqlalchemy import Column, Integer, String, LargeBinary
from conexion import Base

#Modelo de la base de datos
class Model_User(Base):
    __tablename__ = 'via_users'

    nmro_id = Column(Integer, primary_key=True, autoincrement=True)
    txto_protonmail = Column(String(120), nullable=False)
    txto_psswrd = Column(String(50), nullable=False)
    foto_perfil = Column(String(500), nullable=False)
    txto_nick = Column(String(50), nullable=False)
    cdgo_rango = Column(Integer, nullable=False)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# String de conexión a la base de datos MySQL
DATA_BASE = "mysql+mysqlconnector://root:root@localhost/via61"
# Crear un objeto de SQLAlchemy
engine = create_engine(DATA_BASE, echo=True)
# Definir una clase de modelo
Base = declarative_base()
# Crear una clase de sesión
SessionLocal = sessionmaker(bind=engine)
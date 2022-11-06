from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from .declarative_base import Base
from .gasto import Gasto


class Viajero(Base):
    # Tabla
    __tablename__ = 'viajero'

    # Columnas
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

    # Relaciones
    gastos = relationship(Gasto)
    actividades = relationship('Actividad', secondary='actividad_viajero', backref='Viajero')

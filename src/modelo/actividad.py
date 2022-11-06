from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Actividad(Base):
    # Tabla
    __tablename__ = 'actividad'

    # Columnas
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    # Relaciones
    viajeros = relationship('Viajero', secondary='actividad_viajero', backref='Actividad')
    gastos = relationship('Gasto')


class ActividadViajero(Base):
    # Tabla
    __tablename__ = 'actividad_viajero'

    # Columnas
    id = Column(Integer, primary_key=True)
    # actividad_id = Column(Integer, ForeignKey('actividad.id'))
    # viajero_id = Column(Integer, ForeignKey('viajero.id'))
    actividad_id = Column(Integer, ForeignKey('actividad.id'), primary_key=True)
    viajero_id = Column(Integer, ForeignKey('viajero.id'), primary_key=True)

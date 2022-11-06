from sqlalchemy import Column, String, Date, Float, Integer, ForeignKey

from .declarative_base import Base


class Gasto(Base):
    # Tabla
    __tablename__ = 'gasto'

    # Columnas
    id = Column(Integer, primary_key=True)
    concepto = Column(String)
    fecha = Column(Date)
    valor = Column(Float)
    viajero = Column(Integer, ForeignKey('viajero.id'))  # Relacion con Viajero
    actividad = Column(Integer, ForeignKey('actividad.id'))  # Relacion con Actividad

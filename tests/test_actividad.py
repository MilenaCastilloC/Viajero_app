import unittest

from faker import Faker

from src.logica.control_aplicacion import ControlAplicacion
from src.modelo.declarative_base import Session


class ActividadTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.control_app = ControlAplicacion()
        self.data_factory = Faker()

    def tearDown(self):
        self.session = Session()

    def test_listar_actividades(self):
        actividades = self.control_app.listar_actividades()
        self.assertIsNotNone(actividades)

    def test_obtener_gastos_de_actividad(self):
        id_actividad = self.data_factory.random_digit_not_null()
        gastos_actividad = self.control_app.obtener_gastos_actividad(id_actividad)
        self.assertIsNotNone(gastos_actividad)

    def test_obtener_reporte_de_compensacion(self):
        id_actividad = self.data_factory.random_digit_not_null()
        reporte_compensacion = self.control_app.obtener_reporte_compensacion(id_actividad)
        self.assertIsNotNone(reporte_compensacion)

# def test_test(self):
# Actividades
# actividad_01 = Actividad(nombre='Actividad 01')
# actividad_02 = Actividad(nombre='Actividad 02')
# self.session.add(actividad_01)
# self.session.add(actividad_02)

# Viajeros
# nombre_01 = self.data_factory.first_name()
# apellido_01 = self.data_factory.last_name()
# nombre_02 = self.data_factory.first_name()
# apellido_02 = self.data_factory.last_name()
# nombre_03 = self.data_factory.first_name()
# apellido_03 = self.data_factory.last_name()
# viajero_01 = Viajero(nombre=nombre_01, apellido=apellido_01)
# viajero_02 = Viajero(nombre=nombre_02, apellido=apellido_02)
# viajero_03 = Viajero(nombre=nombre_03, apellido=apellido_03)
# self.session.add(viajero_01)
# self.session.add(viajero_02)
# self.session.add(viajero_03)

# Gastos
# fecha_01 = self.data_factory.date_object(end_datetime=None)
# gasto_01 = Gasto(concepto="Launch", fecha=fecha_01, valor=10000, viajero=1, actividad=1)

# gasto_02 = Gasto(concepto="Dinner", fecha=fecha_01, valor=20000, viajero=1, actividad=1)
# gasto_03 = Gasto(concepto="Toll", fecha=fecha_01, valor=15000, viajero=2, actividad=1)
# gasto_04 = Gasto(concepto="Launch", fecha=fecha_01, valor=30000, viajero=1, actividad=2)
# gasto_05 = Gasto(concepto="Launch", fecha=fecha_01, valor=40000, viajero=3, actividad=1)
# self.session.add(gasto_01)
# self.session.add(gasto_02)
# self.session.add(gasto_03)
# self.session.add(gasto_04)
# self.session.add(gasto_05)

# Commit
# self.session.commit()

# id_actividad = self.data_factory.random_digit_not_null()

# id_actividad = 1
# gastos_actividad = self.control_app.obtener_gastos_actividad(id_actividad)
# reporte_compensacion = self.control_app.obtener_reporte_compensacion(id_actividad)
# self.assertIsNotNone(reporte_compensacion)

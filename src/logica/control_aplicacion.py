import numpy

from src.modelo import Gasto
from src.modelo.actividad import Actividad
from src.modelo.declarative_base import Base, engine, session


class ControlAplicacion():

    def __init__(self):
        Base.metadata.create_all(engine)

    def listar_actividades(self):
        actividades = [elem.__dict__ for elem in
                       session.query(Actividad).all()]
        return actividades

    def obtener_gastos_actividad(self, id_actividad):
        gastos_actividad = [elem.__dict__ for elem in
                            session.query(Gasto).filter_by(actividad=id_actividad).all()]
        return gastos_actividad

    def obtener_reporte_compensacion(self, id_actividad):
        total_gastos_actividad = 0
        gastos_actividad = self.obtener_gastos_actividad(id_actividad)
        for gasto in gastos_actividad:
            total_gastos_actividad = gasto["valor"] + total_gastos_actividad

        viajeros = session.query(Gasto.viajero).filter_by(actividad=id_actividad).distinct().all()
        cantidad_viajeros = session.query(Gasto.viajero).filter_by(actividad=id_actividad).distinct().count()
        if cantidad_viajeros > 0:
            gasto_maximo_por_viajero = total_gastos_actividad / cantidad_viajeros
        else:
            gasto_maximo_por_viajero = 0

        # Calcular valores a compensar
        compensar = []
        for viajero in viajeros:
            gastos_un_viajero = session.query(Gasto.valor).filter_by(actividad=id_actividad, viajero=viajero[0]).all()
            valor_total_gastado_viajero = 0
            for gasto in gastos_un_viajero:
                valor_total_gastado_viajero += gasto[0]
            compensar.append([gasto_maximo_por_viajero - valor_total_gastado_viajero, 0])
        # print("compensar")
        # print(compensar)

        # Generar reporte de compensación
        reporte_compensacion = numpy.zeros((cantidad_viajeros, cantidad_viajeros))
        for fila in range(cantidad_viajeros):
            for col in range(cantidad_viajeros):
                if fila != col:
                    cantidad_a_compensar = compensar[fila][0]
                    cantidad_compensada = compensar[fila][1]
                    if cantidad_a_compensar > 0:
                        # Compensar a los otros viajeros
                        # print("Compensar a los otros viajeros")
                        for index in range(col + 1, cantidad_viajeros):
                            cantidad = compensar[index][0]
                            if cantidad < 0:
                                valor = -cantidad
                                if valor >= cantidad_a_compensar:
                                    compensar[index][0] = cantidad + cantidad_a_compensar
                                    compensar[fila][0] = 0
                                    reporte_compensacion[fila][col] = cantidad + cantidad_a_compensar
                                else:
                                    compensar[index][0] = 0
                                    compensar[fila][0] = cantidad_a_compensar - valor
                                    reporte_compensacion[fila][col] = cantidad_a_compensar - valor
                    # elif cantidad_a_compensar < 0:
                    # Es compensado por otros viajeros
                    # print("Es compensado por otros viajeros")

        # print("reporte_compensacion")
        # print(reporte_compensacion)

        # print("-------------------------------------------------------------------------------------------------------")
        # print("total_gastos_actividad")
        # print(total_gastos_actividad)
        # print("cantidad_viajeros")
        # print(cantidad_viajeros)
        # print("gasto_maximo_por_viajero")
        # print(gasto_maximo_por_viajero)
        # print("-------------------------------------------------------------------------------------------------------")
        return reporte_compensacion

from model.servicio import Servicio
from exceptions.excepciones import (
    ServicioNoDisponibleError
)

class ReservaSala(Servicio):

    def __init__(
        self,
        nombre,
        tarifa_base,
        capacidad
    ):
        
        super().__init__(
            nombre,
            tarifa_base
        )

        self.capacidad = capacidad

    # ==========================================
    # CAPACIDAD
    # ==========================================

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):

        if not isinstance(valor, int):
            raise ServicioNoDisponibleError(
                "La capacidad debe ser un número entero"
            )

        if valor <= 0:
            raise ServicioNoDisponibleError(
                "La capacidad debe ser mayor a cero"
            )

        self._capacidad = valor

    # ==========================================
    # CALCULAR COSTO
    # ==========================================

    def calcular_costo(self, horas, descuento=0, incluir_impuesto=False):

        if not isinstance(horas, (int, float)):
            raise ServicioNoDisponibleError(
                "Las horas deben ser numéricas"
            )

        if horas <= 0:
            raise ServicioNoDisponibleError(
                "Las horas deben ser mayores a cero"
            )

        if descuento < 0 or descuento > 1:
            raise ServicioNoDisponibleError(
                "El descuento debe estar entre 0 y 1"
            )

        total = self.tarifa_base * horas

        # Aplicar descuento
        if descuento > 0:
            total -= total * descuento

        # Impuesto IVA
        if incluir_impuesto:
            total *= 1.19

        return round(total, 2)
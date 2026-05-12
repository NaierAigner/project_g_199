from model.servicio import Servicio
from exceptions.excepciones import (
    ServicioNoDisponibleError
)

class AlquilerEquipo(Servicio):
    def __init__(
        self,
        nombre,
        tarifa_base,
        tipo_equipo
    ):  
        super().__init__(
            nombre,
            tarifa_base
        )

        self.tipo_equipo = tipo_equipo

    @property
    def tipo_equipo(self):
        return self._tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, valor):
        if not valor:
            raise ServicioNoDisponibleError(
                "Debe indicar un tipo de equipo"
            )
        valor = valor.strip()
        if len(valor) < 3:
            raise ServicioNoDisponibleError(
                "Tipo de equipo inválido"
            )
        self._tipo_equipo = valor.title()

    def calcular_costo(self, horas, descuento=0, incluir_impuesto=True):
        if not isinstance(horas, (int, float)):
            raise ServicioNoDisponibleError(
                "Las horas deben ser numéricas"
            )
        if horas <= 0:
            raise ServicioNoDisponibleError(
                "Las horas deben ser válidas"
            )
        if descuento < 0 or descuento > 1:
            raise ServicioNoDisponibleError(
                "El descuento debe estar entre 0 y 1"
            )
        subtotal = self.tarifa_base * horas
        # Descuento adicional
        if descuento > 0:
            subtotal -= subtotal * descuento
        # Impuesto IVA
        if incluir_impuesto:
            subtotal *= 1.19
        return round(subtotal, 2)
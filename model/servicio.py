from abc import ABC, abstractmethod
from exceptions.excepciones import (
    ServicioNoDisponibleError
)

class Servicio(ABC):
    """
    Clase abstracta base para todos
    los servicios del sistema.
    """
    def __init__(self, nombre, tarifa_base):

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    # ==========================================
    # NOMBRE
    # ==========================================

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor:
            raise ServicioNoDisponibleError(
                "El nombre del servicio no puede estar vacío"
            )

        valor = valor.strip()

        if len(valor) < 3:
            raise ServicioNoDisponibleError(
                "El nombre del servicio es inválido"
            )

        self._nombre = valor.title()

    # ==========================================
    # TARIFA BASE
    # ==========================================

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):

        if not isinstance(valor, (int, float)):
            raise ServicioNoDisponibleError(
                "La tarifa debe ser numérica"
            )

        if valor <= 0:
            raise ServicioNoDisponibleError(
                "La tarifa debe ser mayor a cero"
            )

        self._tarifa_base = valor

    # ==========================================
    # METODOS ABSTRACTOS
    # ==========================================

    @abstractmethod
    def calcular_costo(self, horas, descuento=0, incluir_impuesto=False):
        pass
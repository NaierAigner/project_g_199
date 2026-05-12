from model.servicio import Servicio
from exceptions.excepciones import (
    ServicioNoDisponibleError
)

class AsesoriaEspecializada(Servicio):
    def __init__(
        self,
        nombre,
        tarifa_base,
        especialidad
    ):
        super().__init__(
            nombre,
            tarifa_base
        )
        self.especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad
    
    @especialidad.setter
    def especialidad(self, valor):

        if not valor:
            raise ServicioNoDisponibleError(
                "La especialidad no puede estar vacía"
            )
        valor = valor.strip()

        if len(valor) < 3:
            raise ServicioNoDisponibleError(
                "Especialidad inválida"
            )
        self._especialidad = valor.title()

    def calcular_costo(self, horas, descuento=0, incluir_impuesto=False):

        """
        Calcula el costo de la asesoría con parámetros opcionales.
        Incluye recargo profesional fijo.
        
        Args:
            horas: Duración de la asesoría
            descuento: Porcentaje de descuento (0-1)
            incluir_impuesto: Si se aplica IVA
            
        Returns:
            Costo total calculado
        """

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
        RECARGO_PROFESIONAL = 50000
        total = (
            self.tarifa_base * horas
        ) + RECARGO_PROFESIONAL
        # Descuento adicional
        if descuento > 0:
            total -= total * descuento
        # Impuesto IVA
        if incluir_impuesto:
            total *= 1.19
        return round(total, 2)
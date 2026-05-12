from exceptions.excepciones import (
    ReservaError
)

class Reserva:

    ESTADOS_VALIDOS = [
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Procesada"
    ]

    def __init__(
        self,
        cliente,
        servicio,
        horas
    ):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas

        self._estado = "Pendiente"

    # ==========================================
    # CLIENTE
    # ==========================================

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):

        if valor is None:
            raise ReservaError(
                "Debe existir un cliente válido"
            )

        self._cliente = valor

    # ==========================================
    # SERVICIO
    # ==========================================

    @property
    def servicio(self):
        return self._servicio

    @servicio.setter
    def servicio(self, valor):

        if valor is None:
            raise ReservaError(
                "Debe existir un servicio válido"
            )

        self._servicio = valor

    # ==========================================
    # HORAS
    # ==========================================

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):

        if not isinstance(valor, (int, float)):
            raise ReservaError(
                "Las horas deben ser numéricas"
            )

        if valor <= 0:
            raise ReservaError(
                "Las horas deben ser mayores a cero"
            )

        self._horas = valor

    # ==========================================
    # ESTADO
    # ==========================================

    @property
    def estado(self):
        return self._estado

    def cambiar_estado(self, nuevo_estado):

        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ReservaError(
                "Estado de reserva inválido"
            )

        self._estado = nuevo_estado

    # ==========================================
    # CONFIRMAR
    # ==========================================

    def confirmar(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "No se puede confirmar "
                    "una reserva cancelada"
                )

            if self.estado == "Confirmada":
                raise ReservaError(
                    "La reserva ya fue confirmada"
                )

            costo = self.servicio.calcular_costo(
                self.horas
            )

            if costo <= 0:
                raise ReservaError(
                    "El costo calculado es inválido"
                )

            self.cambiar_estado(
                "Confirmada"
            )

            return costo

        except Exception as e:

            raise ReservaError(
                "Error al confirmar la reserva"
            ) from e

    # ==========================================
    # CANCELAR
    # ==========================================

    def cancelar(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "La reserva ya está cancelada"
                )

            if self.estado == "Procesada":
                raise ReservaError(
                    "No se puede cancelar "
                    "una reserva procesada"
                )

            self.cambiar_estado(
                "Cancelada"
            )

            return True

        except Exception as e:

            raise ReservaError(
                "Error al cancelar la reserva"
            ) from e

    # ==========================================
    # INFORMACION
    # ==========================================

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado}"
        )

    # ==========================================
    # STR
    # ==========================================

    def __str__(self):

        return (
            f"Reserva("
            f"{self.cliente.nombre}, "
            f"{self.servicio.nombre}, "
            f"{self.estado}"
            f")"
        )
# controller/sistema_controller.py

from model.cliente import Cliente
from model.reserva import Reserva
from model.reserva_sala import ReservaSala
from model.alquiler_equipo import AlquilerEquipo
from model.asesoria_especializada import AsesoriaEspecializada

from utils.logger import (
    registrar_info,
    registrar_warning,
    registrar_error,
    registrar_critico
)


class SistemaController:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(
        self,
        identificador,
        nombre,
        correo,
        telefono
    ):

        try:
            cliente = Cliente(
                identificador,
                nombre,
                correo,
                telefono
            )

            self.clientes.append(cliente)

            registrar_info(
                f"Cliente registrado: {cliente.nombre}"
            )

            return cliente

        except Exception as e:
            registrar_error(
                f"Error registrando cliente: {e}"
            )
            raise

    def crear_servicio_sala(
        self,
        nombre,
        tarifa,
        capacidad
    ):

        try:
            servicio = ReservaSala(
                nombre,
                tarifa,
                capacidad
            )

            self.servicios.append(servicio)

            registrar_info(
                f"Servicio de sala creado: {nombre}"
            )

            return servicio

        except Exception as e:
            registrar_error(
                f"Error creando sala: {e}"
            )
            raise

    def crear_servicio_alquiler(
        self,
        nombre,
        tarifa,
        tipo_equipo
    ):

        try:
            servicio = AlquilerEquipo(
                nombre,
                tarifa,
                tipo_equipo
            )

            self.servicios.append(servicio)

            registrar_info(
                f"Servicio de alquiler creado: {nombre}"
            )

            return servicio

        except Exception as e:
            registrar_error(
                f"Error creando alquiler: {e}"
            )
            raise

    def crear_servicio_asesoria(
        self,
        nombre,
        tarifa,
        especialidad
    ):

        try:
            servicio = AsesoriaEspecializada(
                nombre,
                tarifa,
                especialidad
            )

            self.servicios.append(servicio)

            registrar_info(
                f"Asesoría creada: {nombre}"
            )

            return servicio

        except Exception as e:
            registrar_error(
                f"Error creando asesoría: {e}"
            )
            raise

    def crear_reserva(
        self,
        cliente,
        servicio,
        horas
    ):

        try:
            reserva = Reserva(
                cliente,
                servicio,
                horas
            )

            costo = reserva.confirmar()

            self.reservas.append(reserva)

            registrar_info(
                f"Reserva confirmada para {cliente.nombre}"
            )

            return reserva

        except Exception as e:
            registrar_error(
                f"Error creando reserva: {e}"
            )
            raise

    def cancelar_reserva(self, reserva):

        try:
            reserva.cancelar()

            registrar_info(
                "Reserva cancelada correctamente"
            )

        except Exception as e:
            registrar_error(
                f"Error cancelando reserva: {e}"
            )
            raise
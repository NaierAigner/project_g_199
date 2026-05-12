import re
from model.entidad import Entidad
from exceptions.excepciones import (
    ClienteInvalidoError
)

class Cliente(Entidad):
    def __init__(
        self,
        identificador,
        nombre,
        correo,
        telefono
    ):
        super().__init__(identificador)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # ==========================================
    # NOMBRE
    # ==========================================

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor:
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío"
            )

        valor = valor.strip()

        if len(valor) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener mínimo 3 caracteres"
            )

        # ==========================================
        # VALIDAR FORMATO DEL NOMBRE
        # ==========================================
        if not re.fullmatch(

            r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+",

            valor

        ):

            raise ClienteInvalidoError(

                "El nombre solo puede contener letras"

            )

        self._nombre = valor.title()

    # ==========================================
    # CORREO
    # ==========================================

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        if not valor:
            raise ClienteInvalidoError(
                "El correo no puede estar vacío"
            )

        valor = valor.strip().lower()

        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(patron, valor):
            raise ClienteInvalidoError(
                "El correo electrónico es inválido"
            )

        self._correo = valor

    # ==========================================
    # TELEFONO
    # ==========================================

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor:
            raise ClienteInvalidoError(
                "El teléfono no puede estar vacío"
            )

        valor = valor.strip()

        if not valor.isdigit():
            raise ClienteInvalidoError(
                "El teléfono debe contener solo números"
            )

        if len(valor) < 7 or len(valor) > 15:
            raise ClienteInvalidoError(
                "El teléfono debe tener entre 7 y 15 dígitos"
            )

        self._telefono = valor

    # ==========================================
    # METODOS
    # ==========================================

    def mostrar_datos(self):

        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )

    def __str__(self):

        return (
            f"{self.nombre} "
            f"({self.correo})"
        )
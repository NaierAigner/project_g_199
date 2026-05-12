from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, identificador):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador
    @abstractmethod
    def mostrar_datos(self):
        pass
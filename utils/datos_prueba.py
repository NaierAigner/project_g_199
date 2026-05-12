# ==========================================
# IMPORTACIONES
# ==========================================

from model.cliente import Cliente

from model.reserva_sala import ReservaSala
from model.alquiler_equipo import AlquilerEquipo
from model.asesoria_especializada import (
    AsesoriaEspecializada
)

# ==========================================
# FUNCION PRINCIPAL
# ==========================================

def cargar_datos_prueba(controller):

    # ==========================================
    # CLIENTES
    # ==========================================

    clientes = [

        Cliente(
            "10203040",
            "Carlos Ramirez",
            "carlos@gmail.com",
            "3104567890"
        ),

        Cliente(
            "99887766",
            "Laura Martinez",
            "laura@gmail.com",
            "3201112233"
        ),

        Cliente(
            "88776655",
            "Andres Torres",
            "andres@gmail.com",
            "3159876543"
        ),

        Cliente(
            "55443322",
            "Sofia Herrera",
            "sofia@gmail.com",
            "3124445566"
        ),

        Cliente(
            "11223344",
            "Nicolas Becerra",
            "nicolas@gmail.com",
            "3015556677"
        )

    ]

    for cliente in clientes:

        controller.clientes.append(
            cliente
        )

    # ==========================================
    # SALAS
    # ==========================================

    salas = [

        ReservaSala(
            "Sala Premium",
            150000,
            20
        ),

        ReservaSala(
            "Sala Gaming",
            90000,
            10
        ),

        ReservaSala(
            "Sala Conferencias",
            250000,
            50
        )

    ]

    # ==========================================
    # EQUIPOS
    # ==========================================

    equipos = [

        AlquilerEquipo(
            "Camara Sony A7III",
            45000,
            "Camara"
        ),

        AlquilerEquipo(
            "Microfono HyperX",
            20000,
            "Audio"
        ),

        AlquilerEquipo(
            "PC Gamer RTX",
            80000,
            "Computador"
        )

    ]

    # ==========================================
    # ASESORIAS
    # ==========================================

    asesorias = [

        AsesoriaEspecializada(
            "Juan Perez",
            120000,
            "Marketing"
        ),

        AsesoriaEspecializada(
            "Maria Lopez",
            95000,
            "Programación"
        ),

        AsesoriaEspecializada(
            "Camilo Ruiz",
            110000,
            "Finanzas"
        )

    ]

    # ==========================================
    # AGREGAR SERVICIOS
    # ==========================================

    for sala in salas:

        controller.servicios.append(
            sala
        )

    for equipo in equipos:

        controller.servicios.append(
            equipo
        )

    for asesoria in asesorias:

        controller.servicios.append(
            asesoria
        )
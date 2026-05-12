import logging
import os

# ==========================================
# RUTA PRINCIPAL DEL PROYECTO
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# ==========================================
# RUTA DEL ARCHIVO DE LOGS
# ==========================================

RUTA_LOGS = os.path.join(
    BASE_DIR,
    "logs.txt"
)

# ==========================================
# CONFIGURACION GLOBAL DEL LOGGER
# ==========================================

logging.basicConfig(

    # Archivo donde se guardaran los logs
    filename=RUTA_LOGS,

    # Nivel minimo de eventos registrados
    level=logging.INFO,

    # Formato del registro
    format=(
        "[%(asctime)s] "
        "[%(levelname)s] "
        "%(message)s"
    ),

    # Formato de fecha y hora
    datefmt="%Y-%m-%d %H:%M:%S",

    # Codificacion UTF-8
    encoding="utf-8"
)

# ==========================================
# LOGGER PRINCIPAL DEL SISTEMA
# ==========================================

logger = logging.getLogger(
    "SistemaReservas"
)

def registrar_info(mensaje):

    logger.info(mensaje)

def registrar_warning(mensaje):

    logger.warning(mensaje)

def registrar_error(mensaje):

    logger.error(mensaje)

def registrar_critico(mensaje):

    logger.critical(mensaje)

# ==========================================
# REGISTRO AUTOMATICO DE INICIO
# ==========================================

registrar_info(
    "Sistema de logs inicializado correctamente"
)
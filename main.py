
import tkinter as tk
from controller.sistema_controller import (
    SistemaController
)
from view.interfaz import SistemaGUI
# ==========================================
# DATOS DE PRUEBA
# ==========================================
from utils.datos_prueba import (
    cargar_datos_prueba
)

def main():
    root = tk.Tk()
    controller = SistemaController()
    # ==========================================
    # CARGAR DATOS AUTOMATICOS DE PRUEBA
    # =========================================
    cargar_datos_prueba(controller)
    app = SistemaGUI(
        root,
        controller
    )
    root.mainloop()
if __name__ == "__main__":
    main()
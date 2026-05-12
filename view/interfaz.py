# views/interfaz_grafica.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.logger import (
    registrar_info,
    registrar_error,
    registrar_warning
)

class SistemaGUI:

    def __init__(self, root, controller):

        self.root = root
        self.root.title(
            "Software FJ - Sistema de Reservas"
        )

        self.root.geometry("1000x650")
        self.root.configure(bg="#1e1e2f")

        self.controller = controller

        self.crear_estilos()
        self.crear_componentes()

    def crear_estilos(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "TLabel",
            background="#1e1e2f",
            foreground="white",
            font=("Segoe UI", 11)
        )

        style.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=10
        )

        style.configure(
            "TEntry",
            padding=5
        )

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=28
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

    def _crear_ventana_modal(self, titulo, ancho=450, alto=650):
       
        ventana = tk.Toplevel(self.root)
        ventana.transient(self.root)
        ventana.grab_set()
        ventana.focus_force()
        ventana.attributes("-topmost", True)
        ventana.after(200, lambda: ventana.attributes("-topmost", False))
        ventana.title(titulo)
        ventana.geometry(f"{ancho}x{alto}")
        ventana.configure(bg="#2b2b3d")
        return ventana

    def crear_componentes(self):

        titulo = tk.Label(
            self.root,
            text="Sistema Integral de Reservas",
            bg="#1e1e2f",
            fg="white",
            font=("Segoe UI", 22, "bold")
        )

        titulo.pack(pady=20)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=20, pady=10)

        self.tab_clientes = tk.Frame(
            notebook,
            bg="#2b2b3d"
        )

        self.tab_servicios = tk.Frame(
            notebook,
            bg="#2b2b3d"
        )

        self.tab_reservas = tk.Frame(
            notebook,
            bg="#2b2b3d"
        )

        notebook.add(
            self.tab_clientes,
            text="Clientes"
        )

        notebook.add(
            self.tab_servicios,
            text="Servicios"
        )

        notebook.add(
            self.tab_reservas,
            text="Reservas"
        )

        self.crear_tab_clientes()
        self.crear_tab_servicios()
        self.crear_tab_reservas()

    # ==========================================
    # CLIENTES
    # ==========================================

    def crear_tab_clientes(self):

        frame = tk.Frame(
            self.tab_clientes,
            bg="#2b2b3d"
        )

        frame.pack(pady=20)

        tk.Label(
            frame,
            text="Nombre",
            bg="#2b2b3d",
            fg="white"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = ttk.Entry(frame, width=30)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(
            frame,
            text="Correo",
            bg="#2b2b3d",
            fg="white"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.entry_correo = ttk.Entry(frame, width=30)
        self.entry_correo.grid(row=1, column=1)

        tk.Label(
            frame,
            text="Teléfono",
            bg="#2b2b3d",
            fg="white"
        ).grid(row=2, column=0, padx=10, pady=10)

        self.entry_telefono = ttk.Entry(frame, width=30)
        self.entry_telefono.grid(row=2, column=1)

        boton = ttk.Button(
            frame,
            text="Registrar Cliente",
            command=self.registrar_cliente
        )

        boton.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )

        self.tabla_clientes = ttk.Treeview(
            self.tab_clientes,
            columns=("Identificador", "Nombre", "Correo", "Telefono"),
            show="headings",
            height=10
        )

        self.tabla_clientes.heading(
            "Identificador",
            text="Identificador"
        )

        self.tabla_clientes.heading(
            "Nombre",
            text="Nombre"
        )

        self.tabla_clientes.heading(
            "Correo",
            text="Correo"
        )

        self.tabla_clientes.heading(
            "Telefono",
            text="Teléfono"
        )

        self.tabla_clientes.pack(
            fill="x",
            padx=20,
            pady=20
        )

        for clientes in self.controller.clientes:

            self.tabla_clientes.insert(

                "",

                "end",

                values=(

                    clientes.identificador,
                    clientes.nombre,
                    clientes.correo,
                    clientes.telefono
                )
            )

    def registrar_cliente(self):

        try:

            nombre = self.entry_nombre.get()
            correo = self.entry_correo.get()
            telefono = self.entry_telefono.get()

            cliente = self.controller.registrar_cliente(
                len(self.controller.clientes) + 1,
                nombre,
                correo,
                telefono
            )

            self.tabla_clientes.insert(
                "",
                "end",
                values=(
                    cliente.identificador,
                    cliente.nombre,
                    cliente.correo,
                    cliente.telefono
                )
            )

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================================
    # SERVICIOS
    # ==========================================

    def crear_tab_servicios(self):

        titulo = tk.Label(
            self.tab_servicios,
            text="Servicios Disponibles",
            bg="#2b2b3d",
            fg="white",
            font=("Segoe UI", 16, "bold")
        )

        titulo.pack(pady=20)

        frame_botones = tk.Frame(
            self.tab_servicios,
            bg="#2b2b3d"
        )

        frame_botones.pack()

        ttk.Button(
            frame_botones,
            text="Agregar Sala",
            command=self.agregar_sala
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            frame_botones,
            text="Agregar Alquiler",
            command=self.agregar_alquiler
        ).grid(row=0, column=1, padx=10)

        ttk.Button(
            frame_botones,
            text="Agregar Asesoría",
            command=self.agregar_asesoria
        ).grid(row=0, column=2, padx=10)

        self.tabla_servicios = ttk.Treeview(

            self.tab_servicios,

            columns=(
                "Nombre",
                "Tipo",
                "Precio",
                "Detalles"
            ),

            show="headings",
            height=15
        )

        # ==========================================
        # ENCABEZADOS
        # ==========================================

        self.tabla_servicios.heading(
            "Nombre",
            text="Nombre"
        )

        self.tabla_servicios.heading(
            "Tipo",
            text="Tipo"
        )

        self.tabla_servicios.heading(
            "Precio",
            text="Precio/Hora"
        )

        self.tabla_servicios.heading(
            "Detalles",
            text="Detalles"
        )

        # ==========================================
        # TAMAÑOS
        # ==========================================

        self.tabla_servicios.column(
            "Nombre",
            width=180
        )

        self.tabla_servicios.column(
            "Tipo",
            width=120
        )

        self.tabla_servicios.column(
            "Precio",
            width=100
        )

        self.tabla_servicios.column(
            "Detalles",
            width=250
        )

        self.tabla_servicios.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        for servicio in self.controller.servicios:

            self.tabla_servicios.insert(

                "",

                "end",

                values=(

                    servicio.nombre,

                    type(servicio).__name__,

                    servicio.tarifa_base
                )
            )

    def agregar_sala(self):

        ventana = self._crear_ventana_modal("Agregar Sala")

        # ==========================================
        # VARIABLES
        # ==========================================

        nombre_var = tk.StringVar()
        capacidad_var = tk.StringVar()
        tarifa_var = tk.StringVar()
        equipos_var = tk.StringVar()
        ubicacion_var = tk.StringVar()

        # ==========================================
        # TITULO
        # ==========================================

        titulo = tk.Label(
            ventana,
            text="Registrar Nueva Sala",
            bg="#2b2b3d",
            fg="white",
            font=("Segoe UI", 16, "bold")
        )

        titulo.pack(pady=20)

        # ==========================================
        # FORMULARIO
        # ==========================================

        campos = [

            ("Nombre Sala", nombre_var),
            ("Capacidad", capacidad_var),
            ("Tarifa por Hora", tarifa_var),
            ("Equipos", equipos_var),
            ("Ubicación", ubicacion_var)

        ]

        for texto, variable in campos:

            tk.Label(
                ventana,
                text=texto,
                bg="#2b2b3d",
                fg="white"
            ).pack(pady=5)

            ttk.Entry(
                ventana,
                textvariable=variable,
                width=40
            ).pack()

        # ==========================================
        # GUARDAR
        # ==========================================

        def guardar_sala():

            try:

                nombre = nombre_var.get().strip()
                equipos = equipos_var.get().strip()
                ubicacion = ubicacion_var.get().strip()

                # ==========================================
                # VALIDACIONES
                # ==========================================

                if not nombre:
                    raise ValueError(
                        "Debe ingresar el nombre de la sala"
                    )

                if not capacidad_var.get().isdigit():
                    raise ValueError(
                        "La capacidad debe ser numérica"
                    )

                try:
                    tarifa = float(
                        tarifa_var.get()
                    )
                except:
                    raise ValueError(
                        "La tarifa debe ser numérica"
                    )

                capacidad = int(
                    capacidad_var.get()
                )

                if capacidad <= 0:
                    raise ValueError(
                        "La capacidad debe ser mayor a cero"
                    )

                if tarifa <= 0:
                    raise ValueError(
                        "La tarifa debe ser mayor a cero"
                    )

                # ==========================================
                # CREAR SERVICIO
                # ==========================================

                servicio = self.controller.crear_servicio_sala(
                    nombre,
                    tarifa,
                    capacidad
                )

                self.tabla_servicios.insert(
                    "",
                    "end",
                    values=(
                        nombre,
                        "Sala",
                        f"${tarifa}",
                        (
                            f"Capacidad: {capacidad} | "
                            f"Equipos: {equipos} | "
                            f"Ubicación: {ubicacion}"
                        )
                    )
                )

                registrar_info(
                    f"Sala registrada: {nombre}"
                )

                messagebox.showinfo(
                    "Éxito",
                    "Sala registrada correctamente"
                )

                ventana.destroy()

            except ValueError as e:

                registrar_warning(
                    f"Validación fallida en sala: {e}"
                )

                messagebox.showwarning(
                    "Validación",
                    str(e)
                )

            except Exception as e:

                registrar_error(
                    f"Error registrando sala: {e}"
                )

                messagebox.showerror(
                    "Error",
                    "Ocurrió un error inesperado"
                )
        ttk.Button(
            ventana,
            text="Guardar Sala",
            command=guardar_sala
        ).pack(pady=20)

    def agregar_alquiler(self):

        ventana = tk.Toplevel(self.root)
        # Mantener ventana encima
        ventana.transient(self.root)

        # Bloquear interacción con ventana principal
        ventana.grab_set()

        # Forzar foco
        ventana.focus_force()

        # Mantener arriba temporalmente
        ventana.attributes("-topmost", True)

        # Quitar topmost después de abrir
        ventana.after(
            200,
            lambda: ventana.attributes("-topmost", False)
        )
        ventana.title("Agregar Equipo")
        ventana.geometry("450x650")
        ventana.configure(bg="#2b2b3d")

        nombre_var = tk.StringVar()
        tipo_var = tk.StringVar()
        marca_var = tk.StringVar()
        tarifa_var = tk.StringVar()
        stock_var = tk.StringVar()

        titulo = tk.Label(
            ventana,
            text="Registrar Equipo",
            bg="#2b2b3d",
            fg="white",
            font=("Segoe UI", 16, "bold")
        )

        titulo.pack(pady=20)

        campos = [

            ("Nombre Equipo", nombre_var),
            ("Tipo", tipo_var),
            ("Marca", marca_var),
            ("Tarifa por Hora", tarifa_var),
            ("Stock", stock_var)

        ]

        for texto, variable in campos:

            tk.Label(
                ventana,
                text=texto,
                bg="#2b2b3d",
                fg="white"
            ).pack(pady=5)

            ttk.Entry(
                ventana,
                textvariable=variable,
                width=40
            ).pack()

        def guardar_equipo():

            try:

                nombre = nombre_var.get().strip()
                tipo = tipo_var.get().strip()
                marca = marca_var.get().strip()

                if not nombre:
                    raise ValueError(
                        "Debe ingresar el nombre del equipo"
                    )

                if not tipo:
                    raise ValueError(
                        "Debe ingresar el tipo de equipo"
                    )

                if not marca:
                    raise ValueError(
                        "Debe ingresar la marca"
                    )

                if not stock_var.get().isdigit():
                    raise ValueError(
                        "El stock debe ser numérico"
                    )

                try:
                    tarifa = float(
                        tarifa_var.get()
                    )
                except:
                    raise ValueError(
                        "La tarifa debe ser numérica"
                    )

                stock = int(
                    stock_var.get()
                )

                if stock <= 0:
                    raise ValueError(
                        "El stock debe ser mayor a cero"
                    )

                if tarifa <= 0:
                    raise ValueError(
                        "La tarifa debe ser mayor a cero"
                    )

                servicio = self.controller.crear_servicio_alquiler(
                    nombre,
                    tarifa,
                    tipo
                )

                self.tabla_servicios.insert(
                    "",
                    "end",
                    values=(
                        nombre,
                        "Alquiler",
                        f"${tarifa}",
                        (
                            f"Tipo: {tipo} | "
                            f"Marca: {marca} | "
                            f"Stock: {stock}"
                        )
                    )
                )

                registrar_info(
                    f"Equipo registrado: {nombre}"
                )

                messagebox.showinfo(
                    "Éxito",
                    "Equipo registrado correctamente"
                )

                ventana.destroy()

            except ValueError as e:

                registrar_warning(
                    f"Validación fallida en equipo: {e}"
                )

                messagebox.showwarning(
                    "Validación",
                    str(e)
                )

            except Exception as e:

                registrar_error(
                    f"Error registrando equipo: {e}"
                )

                messagebox.showerror(
                    "Error",
                    "Ocurrió un error inesperado"
                )
        ttk.Button(
            ventana,
            text="Guardar Equipo",
            command=guardar_equipo
        ).pack(pady=20)        

    def agregar_asesoria(self):

        ventana = tk.Toplevel(self.root)
        # Mantener ventana encima
        ventana.transient(self.root)

        # Bloquear interacción con ventana principal
        ventana.grab_set()

        # Forzar foco
        ventana.focus_force()

        # Mantener arriba temporalmente
        ventana.attributes("-topmost", True)

        # Quitar topmost después de abrir
        ventana.after(
            200,
            lambda: ventana.attributes("-topmost", False)
        )
        ventana.title("Agregar Asesoría")
        ventana.geometry("450x650")
        ventana.configure(bg="#2b2b3d")

        nombre_var = tk.StringVar()
        especialidad_var = tk.StringVar()
        experiencia_var = tk.StringVar()
        horario_var = tk.StringVar()
        tarifa_var = tk.StringVar()

        titulo = tk.Label(
            ventana,
            text="Registrar Asesor",
            bg="#2b2b3d",
            fg="white",
            font=("Segoe UI", 16, "bold")
        )

        titulo.pack(pady=20)

        campos = [

            ("Nombre Asesor", nombre_var),
            ("Especialidad", especialidad_var),
            ("Años de Experiencia", experiencia_var),
            ("Horario Disponible", horario_var),
            ("Tarifa por Hora", tarifa_var)

        ]

        for texto, variable in campos:

            tk.Label(
                ventana,
                text=texto,
                bg="#2b2b3d",
                fg="white"
            ).pack(pady=5)

            ttk.Entry(
                ventana,
                textvariable=variable,
                width=40
            ).pack()

        def guardar_asesoria():

            try:

                nombre = nombre_var.get().strip()

                especialidad = (
                    especialidad_var.get().strip()
                )

                horario = horario_var.get().strip()

                if not nombre:
                    raise ValueError(
                        "Debe ingresar el nombre del asesor"
                    )

                if not especialidad:
                    raise ValueError(
                        "Debe ingresar la especialidad"
                    )

                if not horario:
                    raise ValueError(
                        "Debe ingresar el horario"
                    )

                if not experiencia_var.get().isdigit():
                    raise ValueError(
                        "La experiencia debe ser numérica"
                    )

                experiencia = int(
                    experiencia_var.get()
                )

                if experiencia < 0:
                    raise ValueError(
                        "La experiencia es inválida"
                    )

                try:
                    tarifa = float(
                        tarifa_var.get()
                    )
                except:
                    raise ValueError(
                        "La tarifa debe ser numérica"
                    )

                if tarifa <= 0:
                    raise ValueError(
                        "La tarifa debe ser mayor a cero"
                    )

                servicio = self.controller.crear_servicio_asesoria(
                    nombre,
                    tarifa,
                    especialidad
                )

                self.tabla_servicios.insert(
                    "",
                    "end",
                    values=(
                        nombre,
                        "Asesoría",
                        f"${tarifa}",
                        (
                            f"Especialidad: {especialidad} | "
                            f"Experiencia: {experiencia} años | "
                            f"Horario: {horario}"
                        )
                    )
                )

                registrar_info(
                    f"Asesoría registrada: {nombre}"
                )

                messagebox.showinfo(
                    "Éxito",
                    "Asesoría registrada correctamente"
                )

                ventana.destroy()

            except ValueError as e:

                registrar_warning(
                    f"Validación fallida en asesoría: {e}"
                )

                messagebox.showwarning(
                    "Validación",
                    str(e)
                )

            except Exception as e:

                registrar_error(
                    f"Error registrando asesoría: {e}"
                )

                messagebox.showerror(
                    "Error",
                    "Ocurrió un error inesperado"
                )
        ttk.Button(
            ventana,
            text="Guardar Asesoría",
            command=guardar_asesoria
        ).pack(pady=20)        

    # ==========================================
    # RESERVAS
    # ==========================================

    def crear_tab_reservas(self):

        titulo = tk.Label(
            self.tab_reservas,
            text="Reservas",
            bg="#2b2b3d",
            fg="white",
            font=("Segoe UI", 16, "bold")
        )

        titulo.pack(pady=20)

        boton = ttk.Button(
            self.tab_reservas,
            text="Crear Reserva",
            command=self.crear_reserva
        )

        boton.pack(pady=20)

        self.tabla_reservas = ttk.Treeview(
            self.tab_reservas,
            columns=("Cliente", "Servicio", "Estado"),
            show="headings",
            height=12
        )

        self.tabla_reservas.heading(
            "Cliente",
            text="Cliente"
        )

        self.tabla_reservas.heading(
            "Servicio",
            text="Servicio"
        )

        self.tabla_reservas.heading(
            "Estado",
            text="Estado"
        )

        self.tabla_reservas.pack(
            fill="x",
            padx=20,
            pady=20
        )
    def crear_reserva(self):

        # ==========================================
        # VENTANA
        # ==========================================

        ventana = tk.Toplevel(self.root)

        ventana.title("Crear Reserva")
        ventana.geometry("500x650")

        ventana.configure(bg="#2b2b3d")

        ventana.transient(self.root)
        ventana.grab_set()
        ventana.focus_force()

        # ==========================================
        # TITULO
        # ==========================================

        titulo = tk.Label(

            ventana,

            text="Nueva Reserva",

            bg="#2b2b3d",
            fg="white",

            font=("Segoe UI", 16, "bold")
        )

        titulo.pack(pady=20)

        # ==========================================
        # CLIENTES
        # ==========================================

        tk.Label(

            ventana,

            text="Cliente",

            bg="#2b2b3d",
            fg="white"

        ).pack(pady=5)

        clientes = [
            cliente.nombre
            for cliente in self.controller.clientes
        ]

        cliente_var = tk.StringVar()

        combo_clientes = ttk.Combobox(

            ventana,

            textvariable=cliente_var,

            values=clientes,

            state="readonly",
            width=40
        )

        combo_clientes.pack()

        # ==========================================
        # TIPO SERVICIO
        # ==========================================

        tk.Label(

            ventana,

            text="Tipo de Servicio",

            bg="#2b2b3d",
            fg="white"

        ).pack(pady=5)

        tipo_var = tk.StringVar()

        combo_tipo = ttk.Combobox(

            ventana,

            textvariable=tipo_var,

            values=[
                "Sala",
                "Alquiler",
                "Asesoría"
            ],

            state="readonly",
            width=40
        )

        combo_tipo.pack()

        # ==========================================
        # SERVICIOS DISPONIBLES
        # ==========================================

        tk.Label(

            ventana,

            text="Servicio Disponible",

            bg="#2b2b3d",
            fg="white"

        ).pack(pady=5)

        servicio_var = tk.StringVar()

        combo_servicios = ttk.Combobox(

            ventana,

            textvariable=servicio_var,

            state="readonly",
            width=40
        )

        combo_servicios.pack()

        # ==========================================
        # ACTUALIZAR SERVICIOS
        # ==========================================

        def actualizar_servicios(event=None):

            tipo = tipo_var.get()

            servicios_filtrados = []

            for servicio in self.controller.servicios:

                nombre_clase = type(
                    servicio
                ).__name__

                if (
                    tipo == "Sala"
                    and nombre_clase == "ReservaSala"
                ):

                    servicios_filtrados.append(
                        servicio.nombre
                    )

                elif (
                    tipo == "Alquiler"
                    and nombre_clase == "AlquilerEquipo"
                ):

                    servicios_filtrados.append(
                        servicio.nombre
                    )

                elif (
                    tipo == "Asesoría"
                    and nombre_clase == "AsesoriaEspecializada"
                ):

                    servicios_filtrados.append(
                        servicio.nombre
                    )

            combo_servicios["values"] = (
                servicios_filtrados
            )

        combo_tipo.bind(
            "<<ComboboxSelected>>",
            actualizar_servicios
        )

        # ==========================================
        # HORAS
        # ==========================================

        tk.Label(

            ventana,

            text="Horas",

            bg="#2b2b3d",
            fg="white"

        ).pack(pady=5)

        horas_var = tk.StringVar()

        ttk.Entry(

            ventana,

            textvariable=horas_var,
            width=42

        ).pack()

        # ==========================================
        # DESCUENTO (OPCIONAL)
        # ==========================================

        tk.Label(

            ventana,

            text="Descuento % (0-100, opcional)",

            bg="#2b2b3d",
            fg="white",
            font=("Segoe UI", 9)

        ).pack(pady=5)

        descuento_var = tk.StringVar(value="0")

        ttk.Entry(

            ventana,

            textvariable=descuento_var,
            width=42

        ).pack()

        # ==========================================
        # IMPUESTO IVA
        # ==========================================

        impuesto_var = tk.BooleanVar(value=False)

        tk.Checkbutton(

            ventana,

            text="Aplicar IVA (19%)",

            variable=impuesto_var,

            bg="#2b2b3d",
            fg="white",

            selectcolor="#2b2b3d"

        ).pack(pady=10)

        # ==========================================
        # GUARDAR RESERVA
        # ==========================================

        def guardar_reserva():
            try:
                if not cliente_var.get():

                    raise ValueError(
                        "Debe seleccionar un cliente"
                    )

                if not servicio_var.get():

                    raise ValueError(
                        "Debe seleccionar un servicio"
                    )

                try:

                    horas = float(
                        horas_var.get()
                    )

                except:

                    raise ValueError(
                        "Las horas deben ser numéricas"
                    )

                try:

                    descuento_porcentaje = float(
                        descuento_var.get()
                    )

                    if descuento_porcentaje < 0 or descuento_porcentaje > 100:
                        raise ValueError(
                            "El descuento debe estar entre 0 y 100"
                        )

                    descuento = descuento_porcentaje / 100

                except ValueError as e:

                    if "must be" in str(e):
                        raise ValueError(
                            "El descuento debe ser un número"
                        )
                    raise

                # ==========================================
                # BUSCAR CLIENTE
                # ==========================================

                cliente_obj = None

                for cliente in self.controller.clientes:

                    if (
                        cliente.nombre
                        == cliente_var.get()
                    ):

                        cliente_obj = cliente
                        break

                # ==========================================
                # BUSCAR SERVICIO
                # ==========================================

                servicio_obj = None

                for servicio in self.controller.servicios:

                    if (
                        servicio.nombre
                        == servicio_var.get()
                    ):

                        servicio_obj = servicio
                        break

                # ==========================================
                # CREAR RESERVA
                # ==========================================

                reserva = self.controller.crear_reserva(
                    cliente_obj,
                    servicio_obj,
                    horas
                )

                costo = servicio_obj.calcular_costo(
                    horas,
                    descuento=descuento,
                    incluir_impuesto=impuesto_var.get()
                )

                # ==========================================
                # INSERTAR TABLA
                # ==========================================

                self.tabla_reservas.insert(

                    "",

                    "end",

                    values=(

                        cliente_obj.nombre,

                        servicio_obj.nombre,

                        f"Confirmada | ${costo}"

                    )
                )

                registrar_info(
                    f"Reserva creada: "
                    f"{cliente_obj.nombre}"
                )

                messagebox.showinfo(

                    "Éxito",

                    f"Reserva creada correctamente\n"
                    f"Costo total: ${costo}"

                )

                ventana.destroy()

            except ValueError as e:

                registrar_warning(
                    f"Validación reserva: {e}"
                )

                messagebox.showwarning(
                    "Validación",
                    str(e)
                )

                ventana.lift()
                ventana.focus_force()

            except Exception as e:

                registrar_error(
                    f"Error reserva: {e}"
                )

                messagebox.showerror(
                    "Error",
                    str(e)
                )

                ventana.lift()
                ventana.focus_force()

        # ==========================================
        # BOTON PARA GUARDAR
        # ==========================================

        ttk.Button(

            ventana,

            text="Guardar Reserva",

            command=guardar_reserva

        ).pack(pady=25)
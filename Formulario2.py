import  flet as ft
def main(page: ft.Page):
    # Configuración de la página
    page.title = "Formulario de Registro"
    page.padding = 30
    page.bgcolor = "#FDFBE3"
    page.scroll = "auto"
    
    # --- CONTROLES ---
    
    txt_nombre = ft.TextField(
        label="Nombre",
        border_color="#4D2A32",
        hint_text="Ingresa tu nombre completo",
        keyboard_type=ft.KeyboardType.NAME,
        autofocus=True,
    )
    
    txt_num_control = ft.TextField(
        label="Número de control",
        border_color="#4D2A32",
        hint_text="Ingresa tu número de control",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    
    txt_email = ft.TextField(
        label="Email",
        border_color="#4D2A32",
        hint_text="correo@ejemplo.com",
        keyboard_type=ft.KeyboardType.EMAIL,
    )
    
    # CAMBIO: Dropdown para carrera en lugar de TextField
    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#4D2A32",
        hint_text="Selecciona tu carrera",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas Computacionales"),
            ft.dropdown.Option("Ingeniería Industrial"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Mecánica"),

        ]
    )
    
    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#4D2A32",
        hint_text="Selecciona",
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("9"),
        ]
    )
    
    # Radio buttons para género
    rg_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="masculino", label="Masculino"),
            ft.Radio(value="femenino", label="Femenino"),
        ]),
    )
    
    # Contenedor para mensajes
    mensaje = ft.Text("", color="red", size=14)
    
    # NUEVO: Función para cerrar el diálogo de datos
    def cerrar_dialogo(e):
        dialogo_datos.open = False
        page.update()
    
    # NUEVO: Diálogo para mostrar los datos
    dialogo_datos = ft.AlertDialog(
        modal=True,
        title=ft.Text(
            "📋 Datos Registrados",
            size=22,
            weight=ft.FontWeight.BOLD,
            color="#075E54",
        ),
        content=ft.Column([], tight=True, spacing=10),
        actions=[
            ft.ElevatedButton(
                content=ft.Text("Cerrar", color="white"),
                bgcolor="#075E54",
                on_click=cerrar_dialogo,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    # Función de validación
    def enviar_datos(e):
        mensaje.value = ""
        mensaje.color = "red"
        
        # Validaciones
        if not txt_nombre.value or txt_nombre.value.strip() == "":
            mensaje.value = "❌ El nombre es obligatorio"
            page.update()
            return
        
        if not txt_num_control.value or txt_num_control.value.strip() == "":
            mensaje.value = "❌ El número de control es obligatorio"
            page.update()
            return
        
        if not txt_email.value or "@" not in txt_email.value:
            mensaje.value = "❌ Ingresa un email válido"
            page.update()
            return
        
        if not dd_carrera.value:
            mensaje.value = "❌ Debes seleccionar una carrera"
            page.update()
            return
        
        if not dd_semestre.value:
            mensaje.value = "❌ Debes seleccionar un semestre"
            page.update()
            return
        
        if not rg_genero.value:
            mensaje.value = "❌ Debes seleccionar un género"
            page.update()
            return
        
        # Si todo está correcto, mostrar datos en ventana emergente
        mensaje.color = "green"
        mensaje.value = "✅ Datos validados correctamente"
        
        # Preparar contenido del diálogo con los datos
        dialogo_datos.content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.PERSON, color="#075E54", size=20),
                        ft.Text("Nombre:", weight=ft.FontWeight.BOLD, size=14),
                    ], spacing=5),
                    ft.Text(txt_nombre.value, size=14, color="#333333"),
                ], spacing=5),
                padding=10,
                bgcolor="#F0F0F0",
                border_radius=5,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.NUMBERS, color="#075E54", size=20),
                        ft.Text("Número de Control:", weight=ft.FontWeight.BOLD, size=14),
                    ], spacing=5),
                    ft.Text(txt_num_control.value, size=14, color="#333333"),
                ], spacing=5),
                padding=10,
                bgcolor="#F0F0F0",
                border_radius=5,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.EMAIL, color="#075E54", size=20),
                        ft.Text("Email:", weight=ft.FontWeight.BOLD, size=14),
                    ], spacing=5),
                    ft.Text(txt_email.value, size=14, color="#333333"),
                ], spacing=5),
                padding=10,
                bgcolor="#F0F0F0",
                border_radius=5,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.SCHOOL, color="#075E54", size=20),
                        ft.Text("Carrera:", weight=ft.FontWeight.BOLD, size=14),
                    ], spacing=5),
                    ft.Text(dd_carrera.value, size=14, color="#333333"),
                ], spacing=5),
                padding=10,
                bgcolor="#F0F0F0",
                border_radius=5,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.CALENDAR_TODAY, color="#075E54", size=20),
                        ft.Text("Semestre:", weight=ft.FontWeight.BOLD, size=14),
                    ], spacing=5),
                    ft.Text(f"{dd_semestre.value}° Semestre", size=14, color="#333333"),
                ], spacing=5),
                padding=10,
                bgcolor="#F0F0F0",
                border_radius=5,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.PERSON_OUTLINE, color="#075E54", size=20),
                        ft.Text("Género:", weight=ft.FontWeight.BOLD, size=14),
                    ], spacing=5),
                    ft.Text(rg_genero.value.capitalize(), size=14, color="#333333"),
                ], spacing=5),
                padding=10,
                bgcolor="#F0F0F0",
                border_radius=5,
            ),
        ], spacing=10, tight=True, scroll=ft.ScrollMode.AUTO)
        
        # Mostrar el diálogo
        dialogo_datos.open = True
        page.update()
    
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="white"),
        bgcolor="#8B7D7D",
        width=None,
        expand=True,
        on_click=enviar_datos,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
        )
    )
    
    # --- ESTRUCTURA ---
    page.add(
        ft.Container(
            content=ft.Column([
                txt_nombre,
                txt_num_control,
                txt_email,
                ft.Row([dd_carrera, dd_semestre], spacing=10),
                ft.Row([
                    ft.Text("Género:", size=16, color="#4D2A32", weight=ft.FontWeight.W_500),
                    rg_genero,
                ], spacing=20, alignment=ft.MainAxisAlignment.START),
                btn_enviar,
                mensaje,
            ], 
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
            width=600,
            padding=30,
            border_radius=10,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color="rgba(0,0,0,0.1)",
            )
        )
    )
    
    # Agregar el diálogo al overlay
    page.overlay.append(dialogo_datos)
    page.update()

# Ejecución
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
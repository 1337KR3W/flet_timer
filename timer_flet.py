import flet as ft
import time

def main(page: ft.Page):

    # Parámetros de la ventana principal
    page.title = "Timer using Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 475
    page.window_height = 240
    page.window_max_width = 475
    page.window_max_height = 240
    page.window_min_width = 475
    page.window_min_height = 240
    page.window_maximizable = False
    page.window_resizable = False
    # Sonidos
    start_sound = ft.Audio(src="resources/sounds/tic-tac.wav", volume=1)
    end_sound = ft.Audio(src="resources/sounds/end_timer.wav", volume=1)
    page.overlay.append(start_sound)
    page.overlay.append(end_sound)

    # Función para el efecto del texto del campo de texto
    def textbox_changed(e):
        text.value = e.control.value
        page.update()
    
    # Función del switch para cambiar de tema oscuro a claro
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        switch.label = (
            "Light" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark"
        )
        page.update()
    page.theme_mode = ft.ThemeMode.DARK
    switch = ft.Switch(label="Dark", on_change=theme_changed)
    

    # Display para mostrar el tiempo del cronómetro
    only_digits_filter = ft.InputFilter('^[0-9]*') # Filtro para solo permitir dígitos en el temporizador
    hours = ft.TextField(input_filter=only_digits_filter, 
                         label="hours", 
                         on_change=textbox_changed, 
                         text_align=ft.TextAlign.CENTER, 
                         width=100, 
                         max_length=2, 
                         counter_text=" ", 
                         border_color=ft.colors.DEEP_PURPLE_400, 
                         text_size=25)
    












    minutes = ft.TextField(input_filter=only_digits_filter, label="minutes", on_change=textbox_changed,text_align=ft.TextAlign.CENTER, width=100, max_length=2, counter_text=" ", border_color=ft.colors.DEEP_PURPLE_400, text_size=25)
    seconds = ft.TextField(input_filter=only_digits_filter, label="seconds", on_change=textbox_changed,text_align=ft.TextAlign.CENTER, width=100, max_length=2, counter_text=" ", border_color=ft.colors.DEEP_PURPLE_400, text_size=25)
    text = ft.Text()

    github = ft.IconButton(url="https://github.com/tric0ma", content=ft.Image(src="resources/icons/github-mark.png", width=35, height=30))
    
    def bigger_display(e):
        hours.text_size = 39
        minutes.text_size = 39
        seconds.text_size = 39
        page.update()

    # Funcion para obtener el número de los TextFields, o un 0 si no se especifica ninguno
    def get_int_value(text_field):
        try:
            return int(text_field.value.split(" ")[0])
        except ValueError:
            return 0
    # Función de inicio del temporizador
    def start_timer(e):
        
        seconds.read_only = True
        minutes.read_only = True
        hours.read_only = True
        secs_val = get_int_value(seconds)
        mins_val = get_int_value(minutes)
        hrs_val = get_int_value(hours)
        start_btn.visible = False
        is_running = True
        start_sound.play()
        bigger_display(e)
        while is_running == True:
            
            time.sleep(1)
            if hrs_val == 0 and mins_val == 0 and secs_val == 0:
                end_sound.play()
                secs_val == 0
                is_running == False
                update_display(hrs_val, mins_val, secs_val)
                start_btn.visible = True
                seconds.read_only = False
                minutes.read_only = False
                hours.read_only = False
                page.update()
                break
            if secs_val > 0:
                secs_val -= 1
            elif mins_val > 0:
                secs_val = 59
                mins_val -= 1
            elif hrs_val > 0:
                secs_val = 59
                mins_val = 59
                hrs_val -= 1
            update_display(hrs_val, mins_val, secs_val)     

    # Función que actualiza el display cada segundo
    def update_display(hrs_val, mins_val, secs_val):  
      
        hours.value = "{:02d}".format(hrs_val)    
        minutes.value = "{:02d}".format(mins_val)
        seconds.value = "{:02d}".format(secs_val)    

        if hrs_val == 0 and mins_val ==0 and secs_val == 0:
            hours.value = "".format(hrs_val)    
            minutes.value = "".format(mins_val)
            seconds.value = "".format(secs_val) 
        page.update()

    # Botones del cronómetro
    start_btn = ft.ElevatedButton(text="Start", on_click=start_timer, icon=ft.icons.PLAY_ARROW)
    # Fila con los botones
    buttons = ft.Row(
        [
            start_btn,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    social = ft.Row(
        [
            github,switch
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    # Grid a través de una columna principal con filas; una fila del display y otra de los botones
    page.add(
        ft.Column(
            [
                ft.Row(
                  [
                    hours,minutes,seconds
                  ],
                  alignment=ft.MainAxisAlignment.CENTER,
              ),
                buttons,social,
            ]
        )
    )

if __name__ == '__main__':

    ft.app(target=main)

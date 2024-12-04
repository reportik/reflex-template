"""The overview page of the app."""

import reflex as rx
from .. import styles
from ..templates import template
from ..views.stats_cards import stats_cards
from ..views.stats_cards import stats_cards2
from ..views.stats_cards import titulo_con_icono
from ..views.charts import (
    users_chart,
    revenue_chart,
    orders_chart,
    area_toggle,
    pie_chart,
    timeframe_select,
    StatsState,
)
from ..views.adquisition_view import adquisition
from ..components.notification import notification
from ..components.card import card
from .profile import ProfileState
from .login_page import LoginState

import datetime

def UserInfo()-> rx.Component:
    user = ""
    return rx.text( f"Bienvenido {LoginState.username}!")    

def _time_data() -> rx.Component:
    return rx.hstack(
        rx.tooltip(
            rx.icon("info", size=20),
            content=f"{(datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%b %d, %Y')} - {datetime.datetime.now().strftime('%b %d, %Y')}",
        ),
        rx.text("Last 30 days", size="4", weight="medium"),
        align="center",
        spacing="2",
        display=["none", "none", "flex"],
    )

def tab_content_header() -> rx.Component:
    return rx.hstack(
        _time_data(),
        area_toggle(),
        align="center",
        width="100%",
        spacing="4",
    )
def tarjeta(image_base64, title, description) -> rx.Component:
    # Crear la data URI (asumiendo una imagen PNG, puedes cambiar 'png' según corresponda)
    image_data_uri = f"data:image/png;base64,{image_base64}"
    
    return rx.card(
        rx.flex(
            rx.box(
                rx.image(src=image_data_uri, style={"width": "30%", "height": "30%", "border-radius": "8px 8px 0 0"}),
                rx.box(
                    rx.heading(title, style={"font-size": "1.5em", "margin": "16px 0 8px"}),
                    # rx.text(description, style={"font-size": "1em", "color": "#555"}),
                    style={"padding": "16px"}
                )
            ),
            spacing="2",
        ),
        as_child=True,
        spacing="2",
    )
def select_intro():
    return rx.center(
        
        rx.html('<label  class="form-label">Selecciona tu Tela:</label>'),
        rx.select(
            
            color_scheme='green',
            radius='large',
            size='3',
            items=ProfileState.select_tela_items,
            id='sel_tela',
            #value="pear",
            #default_value="Bruno Coel Vol 1 Color 2 Hueso",
            on_change=ProfileState.select_elige_tela,
            spacing="2",
            class_name="form-select"
        ),
        
        tarjeta(ProfileState.card_image_base64, ProfileState.select_tela_value, ""),
        spacing="2",
    
    )
@template(route="/", title="Inicio")
def index() -> rx.Component:
    cards_1 = [
            {"opcion_radio": "Muro Interior", "image": "im1.png"},
            {"opcion_radio": "Muro Exterior", "image": "im2.png"},
            {"opcion_radio": "Techo Interior", "image": "im3.png"},
            {"opcion_radio": "Techo Exterior", "image": "im4.png"},
            {"opcion_radio": "Escuadra", "image": "im5.png"}
        ]
    cards_2 = [
            {"opcion_radio": "Tradicional", "image": "IMG6.jpg"},
            {"opcion_radio": "Ripplefold", "image": "IMG7.jpg"},
            {"opcion_radio": "Ojillos", "image": "IMG8.jpg"}
        ]
    cards_3 = [
            {"opcion_radio": "Blackout", "image": "img9.PNG"},
            {"opcion_radio": "Sheer", "image": "img10.PNG"}
            #{"opcion_radio": "Decorativa", "image": "img11.PNG"}
        ]
    #Aqui llenar las listas por cada tipo de tela, que serian las de card_3
    #los datos ver si los podemos traer de odoo. la idea es invocar una funcion de ProfileState
    #ver el tema de las imagenes
    
        
    return rx.vstack(
        UserInfo(),
        # Aqui puede ir el codigo NUM_1
        titulo_con_icono(f"1.- SELECCIONA EL ESPACIO DONDE UBICARÁS TU CORTINA", f""),
        stats_cards(cards_1, "radio_espacio_cortina"),             
        titulo_con_icono(f"2.- ELIGE EL SISTEMA DE CONFECCIÓN QUE DESEAS", f""),
        stats_cards(cards_2, "radio_sistema_confeccion"),            
        titulo_con_icono(f"3.- ELIGE EL TIPO DE TELA EN QUE DESEES CONFECCIONAR TU CORTINA",
                         f"PUEDES SELECCIONAR DE 1 A 2 OPCIONES, SEGÚN LAS CAPAS QUE LLEVARÁ TU CORTINA"),
        stats_cards(cards_3, "radio_tipo_tela"), 
        titulo_con_icono(f"4.- ELIGE LA TELA QUE DESEES UTILIZAR", f""),
        select_intro(), 
        
    
        spacing="5",
        width="100%",
        
    )

# codigo NUM_1
# rx.flex(
             
        #     rx.flex(
        #         notification("user", "cyan", 12),
        #         notification("message-square-text", "plum", 6),
        #         spacing="4",
        #         width="100%",
        #         wrap="nowrap",
        #         justify="end",
        #     ),
        #     justify="between",
        #     align="center",
        #     width="100%",
        # ),
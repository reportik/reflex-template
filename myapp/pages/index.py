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

#from ..auth import authenticate_user

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
            {"opcion_check": "Blackout", "image": "img9.PNG"},
            {"opcion_check": "Sheer", "image": "img10.PNG"},
            {"opcion_check": "Decorativa", "image": "img11.PNG"}
        ]
    return rx.vstack(
        UserInfo(),
        # Aqui puede ir el codigo NUM_1
        titulo_con_icono(f"1.- SELECCIONA EL ESPACIO DONDE UBICARÁS TU CORTINA", f""),
        stats_cards(cards_1, "radio_espacio_cortina"),             
        titulo_con_icono(f"2.- ELIGE EL SISTEMA DE CONFECCIÓN QUE DESEAS", f""),
        stats_cards(cards_2, "radio_sistema_confeccion"),            
        titulo_con_icono(f"3.- ELIGE EL TIPO DE TELA EN QUE DESEES CONFECCIONAR TU CORTINA",
                         f"PUEDES SELECCIONAR DE 1 A 2 OPCIONES, SEGÚN LAS CAPAS QUE LLEVARÁ TU CORTINA"),
        stats_cards2(cards_3, "radio_tipo_tela"),            
                    
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
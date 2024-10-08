"""The overview page of the app."""

import reflex as rx
from .. import styles
from ..templates import template
from ..views.stats_cards import stats_cards
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
    return rx.vstack(
        UserInfo(),
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
        rx.hstack(

            rx.icon_button(
                rx.icon("square-check-big"),
                #padding="0.5rem",
                radius="full",
                variant="soft",
                color_scheme="green",
                size="4",
            ),
            rx.heading(f"1.- SELECCIONA EL ESPACIO DONDE UBICARÁS TU CORTINA", size="3", padding_top="0.5rem"),

        ),
        

        # Llamada a la función
        stats_cards(cards_1),
        rx.hstack(

            rx.icon_button(
                rx.icon("square-check-big"),
                #padding="0.5rem",
                radius="full",
                variant="soft",
                color_scheme="green",
                size="4",
            ),
            rx.heading(f"1.- SELECCIONA EL TIPO DE CORTINA", size="3", padding_top="0.5rem"),

        ),
        

        # Llamada a la función
        stats_cards(cards_2),
                        
        spacing="5",
        width="100%",
    )

from rxconfig import config
import reflex as rx
import xmlrpc.client
from typing import List
docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

# Add state and page to the app.
class State(rx.State):
    # The app state
    pass
   


def index() -> rx.Component:
    url = 'https://comeritk.odoo.com'
    db = 'comeritk'
    username = 'eduardo.macias@iteknia.com'
    password = 'iteknia2023'
    
    
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    x = common.version()
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
    socios = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
    
    table_data = []
    for socio in socios:
        table_data.append(
           [socio["id"],socio["name"]]
        )
    type(table_data)
    columns: List[str] = ["Codigo Cliente", "Nombre Cliente"]
    return rx.fragment(
        rx.chakra.color_mode_button(rx.chakra.color_mode_icon(), float="right"),
        rx.chakra.vstack(
            rx.chakra.heading("Bienvenido a Invtek!", font_size="2em"),
            rx.chakra.box("Empecemos editando ", rx.chakra.code(filename, font_size="1em")),
            rx.data_table(
                data=table_data,
                columns=columns,
                pagination=True,
                search=True,
                sort=True,
                filter_text="Filtro",  # Texto del filtro
                info_text="{0} a {1} de {2} registros",  # Texto de la etiqueta de información
                previous_text="Anterior",  # Texto del botón "previous"
                next_text="Siguiente"  # Texto del botón "next"
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )

def health() -> rx.Component:
    return rx.chakra.text("healthy")

def not_found(page_text) -> rx.Component:
    return rx.fragment(
        rx.chakra.color_mode_button(rx.chakra.color_mode_icon(), float="right"),
        rx.chakra.vstack(
            rx.chakra.heading(page_text, font_size="2em"),
            spacing="1.5em",
            padding_top="10%",
        ),
    )
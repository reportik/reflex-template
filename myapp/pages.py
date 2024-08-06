from rxconfig import config
import reflex as rx
import xmlrpc.client
from typing import List
#from gridjs.l10n import frFR

#rx.script("from gridjs.l10n import frFR")

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

def index() -> rx.Component:
    url = 'https://comeritk.odoo.com'
    db = 'comeritk'
    username = 'eduardo.macias@iteknia.com'
    password = 'iteknia2023'
    
    
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    #x = common.version()
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [[['write_uid', '=', 23]]], {'fields': ['name', 'id'], 'limit': 1})
    #socios = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [[['write_uid', '=', 23]]], {'attributes': ['string', 'help', 'type']})
    ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['write_uid', '=', 23]]], { 'limit': 1})
    socios = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'id']})
    table_data = []
    for socio in socios:
        table_data.append(
           [socio["id"],socio["name"]]
        )
    print(uid, socios)
    columns: List[str] = ["Codigo Cliente", "Nombre Cliente"]
    return rx.fragment(
        rx.chakra.color_mode_button(rx.chakra.color_mode_icon(), float="right"),
        rx.chakra.vstack(
            rx.chakra.heading("Bienvenido a Invtek!", font_size="2em"),
            rx.chakra.box("Editando ", rx.chakra.code(filename, font_size="1em")),
            rx.data_table(
                data=table_data,
                columns=columns,
                pagination=True,
                search=True,
                sort=True,
                #custom_attrs={"language": "frFR"}                
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )

def not_found(page_text) -> rx.Component:
    return rx.fragment(
        rx.chakra.color_mode_button(rx.chakra.color_mode_icon(), float="right"),
        rx.chakra.vstack(
            rx.chakra.heading(page_text, font_size="2em"),
            spacing="1.5em",
            padding_top="10%",
        ),
    )
"""The profile page."""

from ..templates import template
from ..components.profile_input import profile_input
from ..key import *
#from ..auth import authenticate_user
from ..model.o_products import OProducts
import reflex as rx

class Profile(rx.Base):
    name: str = ""
    email: str = ""
    notifications: bool = True
    
def odoo_tela_items() -> list[str] :
    # Ejemplo de uso
    url = ODOO_URL
    db = ODOO_DB
    
    username = ADMIN_USER
    password = ADMIN_PASS  

    oproducts = OProducts(url, db, username, password)
    productos_filtrados = oproducts.get_products_by_category('CORTINAS/SHADES/TELAS')

    return [producto['name'] for producto in productos_filtrados]

class ProfileState(rx.State):
    profile: Profile = Profile(name="Invitado", email="", notifications=True)
    radio_tipo_tela_value: str =""
    select_tela_items: list[str] = odoo_tela_items() #Aqui hay que cargar la lista de telas Blackout de Odoo 
    select_tela_value: str = select_tela_items[0]
    
    def handle_submit(self, form_data: dict):
        self.profile = Profile(**form_data)
        return rx.toast.success(
            "Profile updated successfully", position="top-center"
        )

    def toggle_notifications(self):
        self.profile.notifications = not self.profile.notifications

    def select_elige_tela(self, value: str):
        self.select_tela_value = value
    def radio_elige_tipo_tela(self, value: str):
        print(f"Radio button seleccionado: {value}")
        #print(f"Radio button seleccionado ID: {id}")
        #if id == 'rg_radio_tipo_tela':
        self.radio_tipo_tela_value = value
        match value:
            case 'Blackout':
                self.select_tela_items = ['Blackout 1', 'Blackout 2']
            case 'Sheer':
                self.select_tela_items = ['Sheer 1', 'Sheer 2']
            case 'Decorativa':
                self.select_tela_items = ['Decorativa 1', 'Decorativa 2']
                    
# @template(route="/profile", title="Profile")
# def profile() -> rx.Component:
#     """The profile page.

#     Returns:
#         The UI for the account page.
#     """
#     return rx.vstack(
#         rx.flex(
#             rx.vstack(
#                 rx.hstack(
#                     rx.icon("square-user-round"),
#                     rx.heading("Personal information", size="5"),
#                     align="center",
#                 ),
#                 rx.text("Update your personal information.", size="3"),
#                 width="100%",
#             ),
#             rx.form.root(
#                 rx.vstack(
#                     profile_input(
#                         "Name",
#                         "name",
#                         "Admin",
#                         "text",
#                         "user",
#                         ProfileState.profile.name,
#                     ),
#                     profile_input(
#                         "Email",
#                         "email",
#                         "user@reflex.dev",
#                         "email",
#                         "mail",
#                         ProfileState.profile.email,
#                     ),
#                     rx.button("Update", type="submit", width="100%"),
#                     width="100%",
#                     spacing="5",
#                 ),
#                 on_submit=ProfileState.handle_submit,
#                 reset_on_submit=True,
#                 width="100%",
#                 max_width="325px",
#             ),
#             width="100%",
#             spacing="4",
#             flex_direction=["column", "column", "row"],
#         ),
#         rx.divider(),
#         rx.flex(
#             rx.vstack(
#                 rx.hstack(
#                     rx.icon("bell"),
#                     rx.heading("Notifications", size="5"),
#                     align="center",
#                 ),
#                 rx.text("Manage your notification settings.", size="3"),
#             ),
#             rx.checkbox(
#                 "Receive product updates",
#                 size="3",
#                 checked=ProfileState.profile.notifications,
#                 on_change=ProfileState.toggle_notifications(),
#             ),
#             width="100%",
#             spacing="4",
#             justify="between",
#             flex_direction=["column", "column", "row"],
#         ),
#         spacing="6",
#         width="100%",
#         max_width="800px",
#     )

"""The profile page."""

from ..templates import template
from ..components.profile_input import profile_input
from ..key import *
#from ..auth import authenticate_user
from ..model.o_products import OProducts
import reflex as rx
from . import * 
class Profile(rx.Base):
    name: str = ""
    email: str = ""
    notifications: bool = True
    
def odoo_tela_items(path: str) -> list[str] :
    # Ejemplo de uso
    url = ODOO_URL
    db = ODOO_DB
    
    username = ADMIN_USER
    password = ADMIN_PASS  

    oproducts = OProducts(url, db, username, password)
    productos_filtrados = oproducts.get_products_by_category('CORTINAS/SHADES/TELAS/'+path)
    return productos_filtrados
    #ProfileState.products = productos_filtrados
def getNombresTelas(productos_filtrados: list[OProducts]):
    return [producto['name'] for producto in productos_filtrados]

class ProfileState(rx.State):
    search_list = 'BLACKOUT'
    products = odoo_tela_items(search_list)
    profile: Profile = Profile(name="Invitado", email="", notifications=True)
    radio_tipo_tela_value: str =""
    select_tela_items: list[str] = getNombresTelas(products) #Aqui hay que cargar la lista de telas Blackout de Odoo 
    select_tela_value: str = products[0]['name']
    card_image_base64: str = products[0]['image']
    
    
    def handle_submit(self, form_data: dict):
        self.profile = Profile(**form_data)
        return rx.toast.success(
            "Profile updated successfully", position="top-center"
        )

    def toggle_notifications(self):
        self.profile.notifications = not self.profile.notifications

    def select_elige_tela(self, value: str):
        self.select_tela_value = value
        # Busca el producto con el nombre igual al valor seleccionado
        for product in self.products:
            if product['name'] == value:
                self.card_image_base64 = product['image']
                break  # Termina la búsqueda una vez encontrado el producto
        else:
            # Si no se encuentra el producto, se asigna None o un valor por defecto
            self.card_image_base64 = None
        
        
    def radio_elige_tipo_tela(self, value: str):
        print(f"Radio button seleccionado: {value}")
        #print(f"Radio button seleccionado ID: {id}")
        #if id == 'rg_radio_tipo_tela':        
        self.radio_tipo_tela_value = value
        match value:
            case 'Blackout':                
                self.search_list = 'BLACKOUT'                
            case 'Sheer':
                self.search_list = 'SHEER'
                
        self.select_tela_items = odoo_tela_items(self.search_list)
        self.select_tela_value = self.products[0]['name']
        self.card_image_base64 = self.products[0]['image']
                    
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

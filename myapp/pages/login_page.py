import reflex as rx
import re
import asyncio
#from ..service.auth_service import auth_user
from ..components.form_components import field_form_component,field_form_component_general
from ..components.notify_component import notify_component
from ..pages.profile import ProfileState
import xmlrpc.client
from ..key import ADMIN_USER # 
from ..key import ADMIN_PASS # 

class LoginState(rx.State):
    username: str = 'example@mail.com'
    password: str
    loader: bool = False
    error_create_user: str = ''

    
    def auth_user(self, data: dict):
        try:
            url = 'https://comeritk-odoo-dev-14432757.dev.odoo.com'
            db = 'comeritk-odoo-dev-14432757'
            
            admin_username = ADMIN_USER
            admin_password = ADMIN_PASS                
            
            username = data['username']    
            password = data['password']    
            
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))    
            print(username)
            print(password)
            
            uid = common.authenticate(db, username, password, {})
            admin_uid = common.authenticate(db, admin_username, admin_password, {})
            print(uid)
                                
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
            #email_normalized email                
            #ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['write_uid', '=', uid]]], { 'limit': 1})                                                                                    
            socios = models.execute_kw(db, admin_uid, admin_password, 'res.users', 'read', [uid], {})
            
            #print(socios[0])
            temp_user = ""+socios[0]["name"]+""
            self.username = temp_user
            
            self.loader = False
            return rx.redirect('/')
        except ValueError:
            
            self.loader = False
            print("BaseException")
            
        #await self.handleNotify()

    async def handleNotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error_create_user = ''

    @rx.var
    def user_invalid(self)->bool:
        return not (re.match(r"[^@]+@[^@]+.[^@]+", self.username) and "example@mail.com")
    
    @rx.var
    def user_empty(self)->bool:
        return not self.username.strip()

    @rx.var
    def password_empty(self)->bool:
        return not (self.password.strip())

    @rx.var
    def validate_fields(self) -> bool:
        return (
            self.user_empty
            or self.user_invalid
            or self.password_empty
        )
    

@rx.page(route='/login', title='Login')
def login_page() -> rx.Component:
    return rx.section(
        rx.flex(
            rx.image(src='/logo.jpg', width="300px", border_radius="15px 50px"),
            rx.heading('Inicio de sesión'),
            rx.form.root(
                rx.flex(
                    field_form_component_general("Usuario", "Ingrese su correo", "Ingrese un correo valido", "username",
                                                     LoginState.set_username, LoginState.user_invalid),

                    field_form_component("Contraseña", "Ingrese su contraseña", "password", 
                                             LoginState.set_password, "password"),
                    
                    rx.form.submit(
                            rx.cond(
                                LoginState.loader,
                                rx.chakra.spinner(color="red", size="xs"),
                                rx.button(
                                    "Iniciar sesión",
                                    disabled=LoginState.validate_fields,
                                    width="30vw"
                                ),
                            ),
                            as_child=True,  
                        ),
                        direction="column",
                        justify="center",
                        align="center",
                        spacing="2",
                ),
                on_submit=LoginState.auth_user,
                reset_on_submit=False,
                width="80%",
            ),
            width="100%",
            direction="column",
            align="center",
            justify="center",
        ),
        rx.cond(
                LoginState.error_create_user != '',
                notify_component(LoginState.error_create_user, 'shield-alert', 'yellow'),
                ),
        style=style_section,
        justify="center",
        width="100%",
    )

style_section = {
    "height": "90vh",
    "width": "80%",
    "margin": "auto",
}
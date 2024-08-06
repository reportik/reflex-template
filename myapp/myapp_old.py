# Welcome to Reflex! This file outlines the steps to create a basic app

import reflex as rx

from .pages import index
from .pages import health
from .pages import not_found
#from .modules import login_page
from .api import root

app = rx.App()

app.add_page(index)
app.add_page(health)
#app.add_page(login_page)
app.api.add_api_route(
    path="/",
    endpoint=root
)


not_found_text = "La página no existe"

app.add_custom_404_page(
    title="404 - Page Not Found", 
    description=not_found_text,
    component=not_found(not_found_text)
)

app._compile()

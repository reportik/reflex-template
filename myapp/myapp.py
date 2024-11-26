

# Import all the pages.
from . import styles
from .pages import *
import reflex as rx

from .pages.profile import ProfileState

# Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets
    
)
not_found_text = "Pagina no Encontrada"
app.add_custom_404_page(
    title="404 - Page Not Found", 
    description=not_found_text,
    #component=not_found(not_found_text)
)


app._compile()
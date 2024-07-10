from rxconfig import config
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

# Add state and page to the app.

class State(rx.State):
    # The app state
    pass

def index() -> rx.Component:
    return rx.fragment(
        rx.chakra.color_mode_button(rx.chakra.color_mode_icon(), float="right"),
        rx.chakra.vstack(
            rx.chakra.heading("Bienvenido a Invtek!", font_size="2em"),
            rx.chakra.box("Empecemos editando ", rx.chakra.code(filename, font_size="1em")),
            rx.chakra.link(
                "Echale un ojo a la documentación!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
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
import reflex as rx
from .. import styles
from myapp.pages.profile import ProfileState
from reflex.components.radix.themes.base import LiteralAccentColor

def stats_card(
    stat_name: str,
    value: int,
    prev_value: int,
    icon: str,
    icon_color: LiteralAccentColor,
    extra_char: str = "",
) -> rx.Component:
    percentage_change = (
        round(((value - prev_value) / prev_value) * 100, 2)
        if prev_value != 0
        else 0 if value == 0 else float("inf")
    )
    change = "increase" if value > prev_value else "decrease"
    arrow_icon = "trending-up" if value > prev_value else "trending-down"
    arrow_color = "grass" if value > prev_value else "tomato"
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    rx.icon(tag=icon, size=34),
                    color_scheme=icon_color,
                    radius="full",
                    padding="0.7rem",
                ),
                rx.vstack(
                    rx.heading(
                        f"{extra_char}{value:,}",
                        size="6",
                        weight="bold",
                    ),
                    rx.text(stat_name, size="4", weight="medium"),
                    spacing="1",
                    height="100%",
                    align_items="start",
                    width="100%",
                ),
                height="100%",
                spacing="4",
                align="center",
                width="100%",
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        tag=arrow_icon,
                        size=24,
                        color=rx.color(arrow_color, 9),
                    ),
                    rx.text(
                        f"{percentage_change}%",
                        size="3",
                        color=rx.color(arrow_color, 9),
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    f"{change} from last month",
                    size="2",
                    color=rx.color("gray", 10),
                ),
                align="center",
                width="100%",
            ),
            spacing="3",
        ),
        size="3",
        width="100%",
        box_shadow=styles.box_shadow_style,
    )

def stats_image_card(
    opcion_radio: str,
    image: str,
    #seleccionado: bool
) -> rx.Component:
    return rx.card(
      
        rx.inset(
            rx.image(
                src=image,
                width="195px",
                height="195px",
            ),
            side="top",
            pb="current",
        ),  
        rx.chakra.radio(opcion_radio 
                        #,default_checked=seleccionado
                        ), 
        
    )

def stats_cards(cards: list, name: str) -> rx.Component:
    return rx.grid(
        rx.chakra.radio_group(
            rx.chakra.hstack(
                # Usamos un for loop para generar dinámicamente las tarjetas
                *[stats_image_card(opcion_radio=card['opcion_radio'], image=card['image']
                                   #, seleccionado=card['cheked']
                                    ) for card in cards],
            ),
            default_value=cards[0]['opcion_radio'],
            default_checked=True,
            name=name,
            id="rg_"+name,
            on_change=ProfileState.radio_elige_tipo_tela
        ),
        width="100%",
    )
    
def titulo_con_icono(titulo: str, subtitulo: str) -> rx.Component:
    return rx.hstack(

            rx.icon_button(
                rx.icon("square-check-big"),
                #padding="0.5rem",
                radius="full",
                variant="soft",
                color_scheme="green",
                size="4",
            ),
            rx.vstack(
                rx.heading(titulo, size="3", padding_top="0.5rem"),
                rx.cond(subtitulo != "",
                        rx.blockquote(subtitulo, size="2")
                )
            )
            
        )

def check_image_card(
    opcion_checkbox: str,
    image: str
) -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src=image,
                width="195px",
                height="195px",
            ),
            side="top",
            pb="current",
        ),
        rx.checkbox(opcion_checkbox)
    )

def stats_cards2(cards: list, name: str) -> rx.Component:
    return rx.grid(
        rx.chakra.checkbox_group(
            rx.chakra.hstack(
                # Usamos un for loop para generar dinámicamente las tarjetas
                *[check_image_card(card["opcion_check"], card["image"]
                                   #, seleccionado=card['cheked']
                                    ) for card in cards],
            ),
            default_value=cards[0]['opcion_check'],
            name=name,
            id="rg_"+name
        ),
        width="100%",
    )
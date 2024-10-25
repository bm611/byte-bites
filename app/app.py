import reflex as rx
from .sections.hero import hero_section
from .sections.nav import nav_section
from .sections.input import input_section
from .sections.recipe import recipe_page


@rx.page(route="/", title="Byte Bites")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        nav_section(),
        hero_section(),
        input_section(),
        class_name="w-full flex items-center justify-center",
        size="4",
    )


@rx.page(route="/recipe", title="Recipe")
def recipe() -> rx.Component:
    return rx.container(
        recipe_page(),
        class_name="w-full flex items-center justify-center",
        size="4",
    )


style = {
    "font_family": "Lexend",
    "font_size": "16px",
    "background_color": "#FFDDE1",
    "color": "black",
}


app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css", "animate.css"],
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
)

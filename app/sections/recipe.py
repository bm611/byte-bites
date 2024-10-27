import reflex as rx
from typing import TypedDict
from .state import State
from .nav import nav_section


class Ingredient(TypedDict):
    item: str
    amount: int
    unit: str


def render_instructions(steps: str):
    return rx.list_item(
        steps,
        class_name="font-medium",
    )


def render_ingredients(items: Ingredient):
    return rx.hstack(
        rx.text(items["item"], class_name="font-bold"),
        rx.text(f"{items['amount']}{items['unit']}"),
        class_name="flex justify-between items-center border-b-2 border-black pb-2 w-full",
    )


def recipe_page() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.link(
                    rx.text(
                        "Byte-Bites",
                        class_name="text-3xl font-black text-center cursor-pointer text-black hover:text-gray-700",
                    ),
                    href="/",
                ),
                class_name="bg-orange-400 border-4 border-black p-4 transform rotate-1 mt-6",
            ),
            rx.box(
                rx.image(
                    src="https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&q=80",
                    class_name="w-full h-full object-cover opacity-80",
                ),
                rx.box(class_name="absolute inset-0 bg-black/20"),
                rx.heading(
                    State.recipe["title"],
                    class_name="absolute bottom-6 left-6 text-6xl font-black text-white tracking-tight drop-shadow-[2px_2px_0px_rgba(0,0,0,1)]",
                ),
                class_name="relative h-[40vh] bg-black mt-10",
            ),
            # Content
            rx.box(
                # Description Card
                rx.box(
                    rx.text(
                        State.recipe["description"],
                        class_name="text-xl",
                    ),
                    class_name="bg-white border-4 border-black p-6 mb-8 transform rotate-[-1deg]",
                ),
                # Meta Info
                rx.grid(
                    rx.box(
                        rx.icon("clock", size=24, class_name="mb-2"),
                        rx.text("Prep Time", class_name="font-bold"),
                        rx.text(State.recipe["prepTime"]),
                        class_name="bg-orange-400 border-4 border-black p-4 transform rotate-1",
                    ),
                    rx.box(
                        rx.icon("chef-hat", size=24, class_name="mb-2"),
                        rx.text("Cook Time", class_name="font-bold"),
                        rx.text(State.recipe["cookTime"]),
                        class_name="bg-green-400 border-4 border-black p-4 transform rotate-[-1deg]",
                    ),
                    rx.box(
                        rx.icon("users", size=24, class_name="mb-2"),
                        rx.text("Servings", class_name="font-bold"),
                        rx.text(f"{State.recipe['servings']} person"),
                        class_name="bg-blue-400 border-4 border-black p-4 transform rotate-1",
                    ),
                    rx.box(
                        rx.icon("flame", size=24, class_name="mb-2"),
                        rx.text("Calories", class_name="font-bold"),
                        rx.text(f"{State.recipe['calories']} kcal"),
                        class_name="bg-red-400 border-4 border-black p-4 transform rotate-[-1deg]",
                    ),
                    class_name="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12",
                ),
                # Two Column Layout
                rx.grid(
                    # Ingredients
                    rx.box(
                        rx.hstack(
                            rx.icon("utensils", size=24),
                            rx.heading("Ingredients", class_name="text-3xl font-black"),
                            class_name="text-3xl font-black mb-6 flex items-center gap-2",
                        ),
                        rx.vstack(
                            rx.foreach(State.ingredients, render_ingredients),
                            class_name="space-y-3",
                        ),
                        class_name="bg-purple-200 border-4 border-black p-6 transform rotate-1",
                    ),
                    # Instructions
                    rx.box(
                        rx.heading(
                            "Instructions", class_name="text-3xl font-black mb-6"
                        ),
                        rx.ordered_list(
                            rx.foreach(State.instructions, render_instructions),
                            class_name="list-decimal list-inside space-y-4",
                        ),
                        class_name="bg-cyan-200 border-4 border-black p-6 transform rotate-[-1deg]",
                    ),
                    class_name="grid md:grid-cols-2 gap-8",
                ),
                class_name="max-w-5xl mx-auto p-8",
            ),
            align="stretch",
            spacing="0",
            width="100%",
        ),
        class_name="min-h-screen bg-yellow-50",
        on_mount=State.handle_submit,
    )

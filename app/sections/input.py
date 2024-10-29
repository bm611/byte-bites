import reflex as rx
from reflex.components.core.colors import Color
from .state import State


def input_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "How would you like to cook?",
                class_name="text-2xl md:text-4xl font-semibold mt-2 md:mt-6 text-center animate-word text-black",
            ),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger(
                        "Search by Recipe",
                        value="tab1",
                        class_name="text-black text-sm md:text-lg",
                    ),
                    rx.tabs.trigger(
                        "Search by Ingredients",
                        value="tab2",
                        class_name="text-black text-sm md:text-lg",
                    ),
                    class_name="flex items-center justify-center",
                ),
                rx.tabs.content(
                    rx.input(
                        class_name="mt-2 md:mt-4 h-12 w-full px-2 md:w-[40rem] text-xl bg-transparent rounded-lg border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0)] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0)] hover:translate-x-1 hover:translate-y-1 transition-all focus:outline-none text-black",
                        on_change=State.set_query,
                    ),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.center(
                        rx.select(
                            [
                                "Japanese",
                                "Italian",
                                "Mexican",
                                "Chinese",
                                "Indian",
                                "Thai",
                                "French",
                                "Mediterranean",
                                "American",
                                "Korean",
                            ],
                            placeholder="Select Cuisine Type",
                            radius="full",
                            on_change=State.set_cuisine,
                        ),
                        class_name="mt-4",
                    ),
                    rx.input(
                        class_name="mt-2 md:mt-4 h-12 w-full px-2 md:w-[40rem] text-xl bg-transparent rounded-lg border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0)] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0)] hover:translate-x-1 hover:translate-y-1 transition-all focus:outline-none text-black",
                        on_change=State.set_query,
                    ),
                    value="tab2",
                ),
                default_value="tab1",
                class_name="w-full md:w-[40rem]",
                on_change=State.set_active_tab,
            ),
            rx.button(
                rx.hstack(
                    rx.icon("sparkles", class_name="text-2xl"),
                    "Generate Recipe",
                    rx.icon("sparkles", class_name="text-2xl"),
                    class_name="justify-center items-center",
                ),
                class_name="mb-4 w-full h-12 md:md:w-[40rem] px-8 py-4 text-xl font-bold bg-[#FF686B] text-black border-4 border-black rounded-lg shadow-[6px_6px_0px_0px_rgba(0,0,0)] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0)] hover:translate-x-1 hover:translate-y-1 transition-all",
                loading=State.is_generating,
                disabled=State.is_generating,
                on_click=[State.start_generation, State.handle_submit],
            ),
            class_name="flex justify-center items-center",
        ),
        class_name="w-full bg-[#E8E1FF] border-4 border-black rounded-xl mt-6 p-4 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)]",
    )

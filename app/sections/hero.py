import reflex as rx


def hero_section():
    return (
        rx.box(
            rx.vstack(
                rx.heading(
                    "Transform Your Kitchen Experience",
                    class_name="text-2xl md:text-4xl font-bold mt-2 md:mt-6 text-center animate-word text-black",
                ),
                rx.text(
                    "Harnessing the power of advanced language models to bring recipes to life",
                    class_name="text-sm md:text-xl max-w-lg mx-4 md:mx-0 mt-2 text-center animate-word text-black",
                ),
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("utensils", size=24),
                                rx.text(
                                    "Smart Recipe Search",
                                    class_name="text-lg",
                                ),
                                class_name="flex justify-center items-center",
                            ),
                            rx.text(
                                "Find the perfect recipe using advanced filters and AI-powered recommendations",
                                class_name="text-md text-black-600 mt-2 hidden md:block",
                            ),
                        ),
                        class_name="p-4 hover:shadow-lg transition-shadow cursor-pointer text-black border-2 border-black bg-[#FFE74C] shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("scale", size=24),
                                rx.text(
                                    "Ingredient Conversion",
                                    class_name="text-lg",
                                ),
                                class_name="flex justify-center items-center",
                            ),
                            rx.text(
                                "Easily convert measurements and scale recipes to your desired serving size",
                                class_name="text-md text-black-600 mt-2 hidden md:block",
                            ),
                        ),
                        class_name="p-4 hover:shadow-lg transition-shadow cursor-pointer text-black border-2 border-black bg-[#FF6E6C] shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("clock", size=24),
                                rx.text(
                                    "Meal Planning",
                                    class_name="text-lg",
                                ),
                                class_name="flex justify-center items-center",
                            ),
                            rx.text(
                                "Plan your weekly meals and automatically generate shopping lists",
                                class_name="text-md text-black-600 mt-2 hidden md:block",
                            ),
                        ),
                        class_name="p-4 hover:shadow-lg transition-shadow cursor-pointer text-black border-2 border-black bg-[#00E1D9] shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]",
                    ),
                    class_name="mt-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4",
                ),
                class_name="w-full flex items-center justify-center",
            ),
            class_name="px-8 py-4 mt-6 border-2 border-black relative rounded-xl w-full bg-[#E0FFE0] shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]",
        ),
    )

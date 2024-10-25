import reflex as rx


def recipe_page() -> rx.Component:
    return rx.box(
        # Hero Section
        rx.box(
            rx.image(
                src="https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&q=80",
                alt="Omelette",
                class_name="w-full h-full object-cover opacity-80",
            ),
            rx.box(class_name="absolute inset-0 bg-black/20"),
            rx.heading(
                "Healthy Breakfast Omelette",
                class_name="absolute bottom-6 left-6 text-6xl font-black text-white tracking-tight drop-shadow-[2px_2px_0px_rgba(0,0,0,1)]",
            ),
            class_name="relative h-[40vh] bg-black",
        ),
        # Content
        rx.box(
            # Description Card
            rx.box(
                rx.text(
                    "A light and nutritious omelette packed with vegetables.",
                    class_name="text-xl",
                ),
                class_name="bg-white border-4 border-black p-6 mb-8 transform rotate-[-1deg]",
            ),
            # Meta Info
            rx.grid(
                rx.box(
                    rx.icon("clock", size=24, class_name="mb-2"),
                    rx.text("Prep Time", class_name="font-bold"),
                    rx.text("5 minutes"),
                    class_name="bg-orange-400 border-4 border-black p-4 transform rotate-1",
                ),
                rx.box(
                    rx.icon("chef-hat", size=24, class_name="mb-2"),
                    rx.text("Cook Time", class_name="font-bold"),
                    rx.text("10 minutes"),
                    class_name="bg-green-400 border-4 border-black p-4 transform rotate-[-1deg]",
                ),
                rx.box(
                    rx.icon("users", size=24, class_name="mb-2"),
                    rx.text("Servings", class_name="font-bold"),
                    rx.text("1 person"),
                    class_name="bg-blue-400 border-4 border-black p-4 transform rotate-1",
                ),
                rx.box(
                    rx.icon("flame", size=24, class_name="mb-2"),
                    rx.text("Calories", class_name="font-bold"),
                    rx.text("250 kcal"),
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
                        rx.hstack(
                            rx.text("Eggs", class_name="font-bold"),
                            rx.text("2"),
                            class_name="flex justify-between items-center border-b-2 border-black pb-2 w-full",
                        ),
                        rx.hstack(
                            rx.text("Milk", class_name="font-bold"),
                            rx.text("20 ml"),
                            class_name="flex justify-between items-center border-b-2 border-black pb-2 w-full",
                        ),
                        rx.hstack(
                            rx.text("Bell Pepper", class_name="font-bold"),
                            rx.text("1/2"),
                            class_name="flex justify-between items-center border-b-2 border-black pb-2 w-full",
                        ),
                        rx.hstack(
                            rx.text("Mushrooms", class_name="font-bold"),
                            rx.text("50g"),
                            class_name="flex justify-between items-center border-b-2 border-black pb-2 w-full",
                        ),
                        rx.hstack(
                            rx.text("Baby Spinach", class_name="font-bold"),
                            rx.text("30g"),
                            class_name="flex justify-between items-center border-b-2 border-black pb-2 w-full",
                        ),
                        rx.hstack(
                            rx.text("Onion", class_name="font-bold"),
                            rx.text("1/4"),
                            class_name="flex justify-between items-center border-b-2 border-black pb-2 w-full",
                        ),
                        class_name="space-y-3",
                    ),
                    class_name="bg-purple-200 border-4 border-black p-6 transform rotate-1",
                ),
                # Instructions
                rx.box(
                    rx.heading("Instructions", class_name="text-3xl font-black mb-6"),
                    rx.ordered_list(
                        *[
                            rx.list_item(
                                step,
                                class_name="font-medium",
                            )
                            for step in [
                                "Whisk eggs and milk together in a bowl. Season with salt and pepper.",
                                "Heat olive oil in a non-stick pan over medium heat.",
                                "Add onion and cook until softened, about 2 minutes.",
                                "Add mushrooms and bell pepper, and cook for another 3-4 minutes until slightly tender.",
                                "Stir in spinach and cook until wilted, about 1 minute.",
                                "Pour egg mixture into the pan.",
                                "Cook until the edges are set, then gently lift the edges to allow uncooked egg to flow underneath.",
                                "Cook until the omelette is set but still slightly moist, about 3-4 minutes more.",
                                "Fold the omelette in half and serve immediately.",
                            ]
                        ],
                        class_name="list-decimal list-inside space-y-4",
                    ),
                    class_name="bg-cyan-200 border-4 border-black p-6 transform rotate-[-1deg]",
                ),
                class_name="grid md:grid-cols-2 gap-8",
            ),
            class_name="max-w-5xl mx-auto p-8",
        ),
        class_name="min-h-screen bg-yellow-50",
    )

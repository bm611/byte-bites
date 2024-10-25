import reflex as rx


def input_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "What do you want to cook?",
                class_name="text-xl md:text-4xl font-semibold mt-2 md:mt-6 text-center animate-word text-black",
            ),
            rx.input(
                class_name="mt-2 md:mt-4 h-12 w-full px-2 md:w-[40rem] text-xl bg-transparent rounded-lg border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0)] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0)] hover:translate-x-1 hover:translate-y-1 transition-all focus:outline-none text-black",
            ),
            rx.button(
                "Generate Recipe",
                class_name="mb-4 w-full h-12 md:md:w-[40rem] px-8 py-4 text-xl font-bold bg-[#FF90E8] text-black border-4 border-black rounded-lg shadow-[6px_6px_0px_0px_rgba(0,0,0)] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0)] hover:translate-x-1 hover:translate-y-1 transition-all",
            ),
            class_name="flex justify-center items-center",
        ),
        class_name="w-full bg-[#E8E1FF] border-4 border-black rounded-xl mt-6 p-4 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)]",
    )

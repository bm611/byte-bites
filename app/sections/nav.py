import reflex as rx


def nav_section() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.text(
                    "Byte-Bites",
                    class_name="text-3xl font-extrabold text-black cursor-pointer",
                ),
                on_click=rx.redirect("/"),
            ),
            rx.button(
                "Github",
                class_name="text-xl text-black bg-transparent hidden md:block underline cursor-pointer",
                on_click=rx.redirect(
                    "https://github.com/bm611/byte-bites/tree/main", external=True
                ),
            ),
            class_name="flex justify-center md:justify-between items-center h-full mx-6",
        ),
        class_name="w-full bg-[#FF90E8] border-4 border-black rounded-xl mt-3 md:mt-6 p-4 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)]",
    )

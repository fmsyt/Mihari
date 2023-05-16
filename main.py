import flet as ft
from page.index import Index
from page.settings import Settings

from config import Config
from flet.utils import is_windows

async def main(page: ft.Page):

    config = Config()

    page.title = "Mihari"

    page.theme_mode = config.application.theme_mode

    if is_windows():
        page.window_bgcolor = ft.colors.TRANSPARENT
        page.bgcolor = ft.colors.TRANSPARENT


    page.window_left = 400
    page.window_top = 200

    plot = Index()

    page.window_width = plot.width
    page.window_height = plot.height



    async def route_change(route):

        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[plot],
                bgcolor = ft.colors.TRANSPARENT,
            )
        )

        if page.route == "/":
            page.window_width = plot.width
            page.window_height = plot.height

            page.window_always_on_top = config.application.always_on_top
            page.window_maximizable = False

            page.window_title_bar_hidden = config.application.hide_toolbar
            page.window_frameless = config.application.hide_toolbar


        else:
            page.window_width = None
            page.window_height = None

            page.window_always_on_top = False
            page.window_maximizable = True

            page.window_title_bar_hidden = False
            page.window_frameless = False


        if page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        ft.AppBar(title=ft.Text("設定"), bgcolor=ft.colors.SURFACE_VARIANT),
                        Settings(),
                    ],
                )
            )


        await page.update_async()




    async def view_pop(view: ft.View):
        page.views.pop()
        top_view = page.views[-1]

        await page.go_async(top_view.route)

        page.window_width = 200
        page.window_height = 100

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    await page.go_async(page.route)



    # await page.add_async(plot)


if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)

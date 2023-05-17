import flet as ft
from page.index import Index
from page.settings import Settings

from config import Config
from flet.utils import is_windows

def page_initialize(page: ft.Page):
    config = Config()

    padding = config.plot.padding
    spacing = config.plot.spacing

    controls_count = 2

    windows_title_bar_height = 10

    page.padding = 0

    page.window_width=48 + 40 + 96 + padding * controls_count * 4 + spacing * controls_count
    page.window_height=(64 + padding + spacing) * controls_count

    page.window_title_bar_hidden = config.application.hide_toolbar
    page.window_frameless = config.application.frameless

    if is_windows() and config.application.hide_toolbar:
        page.window_height += windows_title_bar_height

async def main(page: ft.Page):

    config = Config()


    page.theme_mode = config.application.theme_mode

    if is_windows():
        page.window_bgcolor = ft.colors.TRANSPARENT
        page.bgcolor = ft.colors.TRANSPARENT


    page.window_left = 400
    page.window_top = 200

    page_initialize(page)

    async def route_change(route):

        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[Index()],
                    bgcolor = ft.colors.TRANSPARENT,
                )
            )


        if page.route == "/":
            page_initialize(page)

        else:
            page.window_width = 400
            page.window_height = 300

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


if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)

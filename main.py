import flet as ft

from page.plot import Plot, PlotCpu, PlotMemory

async def main(page: ft.Page):

    page.title = "Mihari"

    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT

    page.window_opacity = 1

    page.window_title_bar_hidden = True
    # page.window_frameless = True

    page.window_left = 400
    page.window_top = 200

    area = ft.WindowDragArea(
        ft.ListView(
            controls=[
                PlotCpu(),
                PlotMemory(),
            ],
            spacing=4,
        ),
        width=page.width,
        height=page.height,
    )

    await page.add_async(area)


if __name__ == "__main__":
    # ft.app(target=main, view=ft.FLET_APP_HIDDEN)
    ft.app(target=main, view=ft.FLET_APP)

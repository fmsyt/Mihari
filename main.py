import flet as ft
import asyncio

from page.plot import Plot, PlotCpu, PlotMemory

async def main(page: ft.Page):

    page.title = "Mihari"

    page.bgcolor = "#FFFFFFFF"
    page.window_bgcolor = "#FFFFFFFF"

    page.window_opacity = 1

    page.window_maximizable = False

    # page.window_title_bar_hidden = True
    # page.window_frameless = True

    page.window_left = 400
    page.window_top = 200

    await page.add_async(
        ft.WindowDragArea(
            ft.ResponsiveRow([
                PlotCpu(),
                # PlotMemory(),
            ])
        )
    )

    page.window_visible = True


if __name__ == "__main__":
    # ft.app(target=main, view=ft.FLET_APP_HIDDEN)
    ft.app(target=main, view=ft.FLET_APP)

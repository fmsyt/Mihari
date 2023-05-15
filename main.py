import flet as ft
from flet.utils import is_windows

from page.plot import PlotCpu, PlotMemory

async def main(page: ft.Page):

    page.title = "Mihari"

    page.window_title_bar_hidden = True
    page.window_frameless = True

    if is_windows():
        page.window_bgcolor = ft.colors.TRANSPARENT
        page.bgcolor = ft.colors.TRANSPARENT

    page.window_always_on_top = True

    page.window_left = 400
    page.window_top = 200

    controls = [
        PlotCpu(),
        PlotMemory(),
    ]

    controls_count = len(controls)

    padding = 8
    spacing = 4

    page.window_width = 48 + 40 + 96 + padding * controls_count * 4 + spacing * controls_count
    page.window_height = 64 * 2 + padding * controls_count * 2 + spacing * (controls_count - 1)

    page.window_visible = True


    area = ft.WindowDragArea(
        ft.ListView(
            controls,
            spacing=4,
        ),
        # width=page.width,
        # height=page.height,
        maximizable=False
    )

    await page.add_async(area)


if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)

import flet as ft

from config import Config
from flet.utils import is_windows

from component.plot import PlotCpu, PlotMemory

async def main(page: ft.Page):

    config = Config()

    page.title = "Mihari"

    page.theme_mode = config.application.theme_mode

    page.window_title_bar_hidden = config.application.hide_toolbar
    page.window_frameless = config.application.hide_toolbar

    if is_windows():
        page.window_bgcolor = ft.colors.TRANSPARENT
        page.bgcolor = ft.colors.TRANSPARENT

    page.window_always_on_top = config.application.always_on_top
    page.window_maximizable = False

    page.window_left = 400
    page.window_top = 200

    controls = [
        PlotCpu(),
        PlotMemory(),
    ]

    controls_count = len(controls)

    padding = config.plot.padding
    spacing = config.plot.spacing

    page.window_width = 48 + 40 + 96 + padding * controls_count * 4 + spacing * controls_count
    page.window_height = (64 + padding + spacing) * controls_count

    area = ft.WindowDragArea(
        ft.ListView(controls, spacing=spacing),
        maximizable=False
    )

    await page.add_async(area)


if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)

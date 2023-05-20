import flet as ft

from flet.utils import is_windows
from component.plot import PlotCpu, PlotMemory

from config import Config

class Monitor(ft.UserControl):

    component: ft.WindowDragArea = None

    def build(self):
        config = Config()

        controls = [
            PlotCpu(),
            PlotMemory(),
        ]

        self.settings_icon = ft.Icon(name="settings", color="#c1c1c1", visible=False)

        content = ft.ListView(controls, spacing=config.plot.spacing)

        self.component = ft.WindowDragArea(
            content=ft.Container(content),
            maximizable=False,
            height=self.height
        )

        return self.component


async def run(page: ft.Page):
    page.window_left = 400
    page.window_top = 200

    pageInitialize(page)

    await page.add_async(Monitor())
    await page.update_async()


def pageInitialize(page):
    config = Config()

    page.theme_mode = config.application.theme_mode

    padding = config.plot.padding
    spacing = config.plot.spacing

    controls_count = 2

    page.window_always_on_top = config.application.always_on_top

    page.window_maximizable = False
    page.window_resizable = False

    page.window_width=48 + 40 + 96 + padding * controls_count * 4 + spacing * controls_count
    page.window_height=(64 + padding + spacing) * controls_count

    page.window_title_bar_hidden = config.application.hide_toolbar
    page.window_frameless = config.application.frameless

    if is_windows():
        page.window_bgcolor = ft.colors.TRANSPARENT
        page.bgcolor = ft.colors.TRANSPARENT

    if is_windows() and config.application.hide_toolbar:
        windows_title_bar_height = 10
        page.window_height += windows_title_bar_height


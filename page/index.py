import flet as ft
from flet_core.control import OptionalNumber
from component.plot import PlotCpu, PlotMemory

from config import Config
from page.settings import Settings

class Index(ft.UserControl):

    component: ft.WindowDragArea = None

    def build(self):
        config = Config()

        controls = [
            PlotCpu(),
            PlotMemory(),
        ]

        self.settings_icon = ft.Icon(name="settings", color="#c1c1c1", visible=False)

        stack = ft.Stack(
            controls=[
                ft.ListView(controls, spacing=config.plot.spacing),
                ft.Container(content=self.settings_icon, right=0, padding=config.plot.padding, on_click=self.icon_click),
            ]
        )

        padding = config.plot.padding
        spacing = config.plot.spacing

        controls_count = 2

        self.component = ft.WindowDragArea(
            content=ft.Container(stack, on_hover=self.hover),
            maximizable=False,
            width=48 + 40 + 96 + padding * controls_count * 4 + spacing * controls_count,
            height=(64 + padding + spacing) * controls_count,
        )

        return self.component



    async def icon_click(self, e):
        await self.page.launch_url_async("/settings", web_window_name="settings")

    async def hover(self, e: ft.HoverEvent):
        self.settings_icon.visible = e.data == "true"
        await self.update_async()

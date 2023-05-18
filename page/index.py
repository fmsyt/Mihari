import flet as ft

from flet.utils import is_windows
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
            height=self.height
        )

        return self.component



    async def icon_click(self, e):
        await self.page.go_async("/settings")

    async def hover(self, e: ft.HoverEvent):
        self.settings_icon.visible = e.data == "true"
        await self.update_async()



async def run(page: ft.Page):

    config = Config()


    page.theme_mode = config.application.theme_mode

    if is_windows():
        page.window_bgcolor = ft.colors.TRANSPARENT
        page.bgcolor = ft.colors.TRANSPARENT


    page.window_left = 400
    page.window_top = 200

    pageInitialize(page)

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
            pageInitialize(page)

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




def pageInitialize(page):
    config = Config()

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

    if is_windows() and config.application.hide_toolbar:
        windows_title_bar_height = 10
        page.window_height += windows_title_bar_height


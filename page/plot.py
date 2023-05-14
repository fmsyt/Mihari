import asyncio
import flet as ft
import psutil as pu

class Plot(ft.UserControl):

    min: float = 0
    max: float = 100

    current: float = None

    _data_points: list[ft.LineChartDataPoint] = []
    _chart: ft.LineChart

    _view: ft.Row

    def __init__(self, label: str, initial: float = 0, min: float = 0, max: float = 100) -> None:

        super().__init__()

        self.label = label

        self.min = min
        self.max = max

        self.current = initial



    def build(self):

        self._data_points = list(map(lambda i: ft.LineChartDataPoint(x=i, y=0, show_tooltip=False), list(range(64))))

        d = ft.LineChartData(
            data_points=self._data_points,
            stroke_width=2,
            color=ft.colors.LIGHT_GREEN_800,
            below_line_bgcolor=ft.colors.LIGHT_GREEN,
            curved=False,
            stroke_cap_round=True,
            selected_point=False,
            selected_below_line=False,
        )

        self._chart = ft.LineChart(
            data_series=[d],
            border=ft.border.all(2, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
            horizontal_grid_lines=ft.ChartGridLines(
                interval=10, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
            ),
            vertical_grid_lines=ft.ChartGridLines(
                interval=8, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
            ),

            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
            min_y=min,
            max_y=max,
            min_x=0,
            max_x=63,
            # animate=5000,
            # expand=True,
            width=8 * 16,
            height=8 * 9,
            opacity=0.5,
        )

        self._view = ft.Row(
            controls=[
                ft.Text(self.label),
                self._chart,
                ft.Text(self.current)
            ],
            spacing=8,
        )

        return self._view


    def append_value(self, value: float) -> None:

        self.current = value

        l = len(self._data_points)

        for i in range(l):
            if i < l - 1:
                self._data_points[i].y = self._data_points[i + 1].y
            else:
                self._data_points[i].y = value


    async def did_mount_async(self):
        self.running = True
        asyncio.create_task(self.update_timer())

    async def will_unmount_async(self):
        self.running = False

    async def update_timer(self):
        while self.running:
            self.tick()

            self._chart.data_series[0].data_points = self._data_points
            await self._chart.update_async()

            await self.update_async()
            await asyncio.sleep(1)


    def tick(self) -> None:
        self.append_value(self.current - 1.0)



class PlotCpu(Plot):
    def __init__(self, label: str = "CPU") -> None:
        super().__init__(label)

    def tick(self) -> None:
        value = pu.cpu_percent()
        print(value)
        self.append_value(value)


class PlotMemory(Plot):
    def __init__(self, label: str = "Memory") -> None:
        super().__init__(label)

    def tick(self) -> None:
        value = pu.cpu_percent(pu.virtual_memory().percent)
        self.append_value(value)


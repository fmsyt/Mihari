import asyncio
import flet as ft
import psutil as pu

class Plot(ft.UserControl):

    min: float = 0
    max: float = 100

    prefix: str = ""
    postfix: str = "%"

    current: float = None

    _data_points: list[ft.LineChartDataPoint] = []
    _chart: ft.LineChart

    _monitor: ft.Text

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
            below_line_bgcolor="#808bc34a",
            curved=False,
            stroke_cap_round=True,
            selected_point=False,
            selected_below_line=False,
        )

        self._chart = ft.LineChart(
            data_series=[d],
            min_y=self.min,
            max_y=self.max,
            min_x=0,
            max_x=63,
            animate=1,
            # expand=True,
        )

        self._monitor = ft.Text(
            value = f"{self.prefix}{self.current}{self.postfix}",
            size=12,
        )

        self._view = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value = self.label,
                        size=12,
                    ),
                    bgcolor="#AA000000",
                    padding=8,
                    width=48,
                    height=64,
                    alignment=ft.alignment.top_left,
                    col=3
                ),
                ft.Container(
                    content=self._monitor,
                    bgcolor="#AA000000",
                    padding=8,
                    width=40,
                    height=64,
                    alignment=ft.alignment.top_left,
                    col=3
                ),
                ft.Container(
                    content=self._chart,
                    bgcolor="#AA000000",
                    padding=8,
                    width=96,
                    height=64,
                    alignment=ft.alignment.top_left,
                    col=6
                ),

            ],
            spacing=4,
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
            self._monitor.value = f"{self.prefix}{self.current}{self.postfix}"

            tasks = [
                self._chart.update_async(),
                self._monitor.update_async(),
                self.update_async(),
                asyncio.sleep(1),
            ]

            await asyncio.gather(*tasks)


    def tick(self) -> None:
        self.append_value(self.current - 1.0)



class PlotCpu(Plot):
    def __init__(self, label: str = "CPU") -> None:
        super().__init__(label, min=0, max=100)

    def tick(self) -> None:
        value = pu.cpu_percent()
        self.append_value(round(value))


class PlotMemory(Plot):
    def __init__(self, label: str = "Mem") -> None:
        super().__init__(label, min=0, max=100)

    def tick(self) -> None:
        value = pu.virtual_memory().percent
        self.append_value(round(value))


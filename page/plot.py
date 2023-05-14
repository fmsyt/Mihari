import flet as ft
import psutil as pu

class Plot():

    min: float = 0
    max: float = 100

    point_list: list[ft.LineChartDataPoint] = []

    view: ft.View

    _chart: ft.LineChart

    def __init__(self, label: str, initial: float = 0, min: float = 0, max: float = 100) -> None:

        self.min = min or initial
        self.max = max or initial

        self.point_list = list(map(lambda i: ft.LineChartDataPoint(x=i, y=0, show_tooltip=False), list(range(64))))

        d = ft.LineChartData(
            data_points=self.point_list,
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

        self.view = ft.Row(
            controls=[
                ft.Text(label),
                self._chart
            ],
            spacing=8,
        )

    def append_value(self, value: float):
        self.point_list.pop()
        self.point_list.append(ft.LineChartDataPoint(y=value, show_tooltip=False))

        for (i, point) in enumerate(self.point_list):
            point.x = i


    def update(self) -> None:
        self._chart.data_series[0].data_points = self.point_list
        self._chart.update()




class PlotCpu(Plot):
    def __init__(self, label: str = "CPU") -> None:
        super().__init__(label)

    def update(self) -> None:
        value = pu.cpu_percent()
        print(value)
        self.append_value(value)

        super().update()


class PlotMemory(Plot):
    def __init__(self, label: str = "Memory") -> None:
        super().__init__(label)

    def update(self) -> None:
        value = pu.cpu_percent(pu.virtual_memory().percent)
        self.append_value(value)

        super().update()


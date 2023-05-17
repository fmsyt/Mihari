import json
import flet as ft

from flet.utils import is_windows


class ConfigApplication:
    transparent = False
    always_on_top = True
    hide_toolbar = True
    frameless = False
    theme_mode = ft.ThemeMode.DARK

    def __init__(self) -> None:
        self.transparent = is_windows()

class ConfigPlot:
    padding = 8
    spacing = 4

    def __init__(self) -> None:
        pass

class Config:
    _instance = None

    application: ConfigApplication
    plot: ConfigPlot

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.initialize()

    def initialize(self):
        self.application = ConfigApplication()
        self.plot = ConfigPlot()

    def save(self):
        pass


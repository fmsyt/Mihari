import json

from flet.utils import is_windows

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.initialize()

    def initialize(self):
        defaults = self.get_defaults()

        self.application = defaults.application
        self.plot = defaults.plot

    def get_defaults(self):
        return {
            "application": {
                "transparent": is_windows(),
                "always_on_top": True,
            },
            "plot": {
                "spacing": 4,
            }
        }

    @NotImplemented
    def save(self):
        pass

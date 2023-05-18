import flet as ft
import threading

from pystray import Icon, MenuItem, Menu
from page.index import run
from PIL import Image

class TaskTray:

    plotAppStarted = False

    def __init__(self, image: str):
        self.plotAppStarted = False

        icon = Image.open(image)

        menu = Menu(
            MenuItem('Open', self.runPlotApp),
            MenuItem('Exit', self.stopProgram),
        )

        self.icon = Icon(
            name='Mihari',
            title='Mihari',
            icon=icon,
            menu=menu,
        )

    def stopProgram(self, icon):
        self.plotAppStarted = False

        ## 停止
        self.icon.stop()


    def run(self):
        self.runPlotApp()
        self.icon.run()

    def runPlotApp(self):
        ft.app(target=run, view=ft.FLET_APP)




if __name__ == "__main__":
    # system_tray = TaskTray("icon_x128.png")
    # system_tray.run()

    ft.app(target=run, view=ft.FLET_APP)
    print("exit.")


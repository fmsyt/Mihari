from pystray import Icon, MenuItem, Menu

import flet as ft
from page.index import run

from PIL import Image

class TaskTray:
    def __init__(self, image: str):
        self.status = False

        icon = Image.open(image)

        menu = Menu(
            MenuItem('Exit', self.stopProgram),
        )

        self.icon = Icon(name='Mihari', title='Mihari', icon=icon, menu=menu)

    def stopProgram(self, icon):
        self.status = False

        ## 停止
        self.icon.stop()


    def run(self):
        self.status = True

        ft.app(target=run, view=ft.FLET_APP)

        ## 実行
        self.icon.run()



if __name__ == "__main__":
    system_tray = TaskTray("icon_x128.png")
    system_tray.run()


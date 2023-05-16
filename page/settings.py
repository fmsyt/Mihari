import flet as ft
class Settings(ft.UserControl):
    def build(self):
        return ft.Container(ft.ElevatedButton(text="戻る", on_click=self.back))

    async def back(self, e):
        await self.page.go_async("/")

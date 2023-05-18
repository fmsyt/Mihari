import pystray
from PIL import Image

def on_quit():
    print("Quitting...")
    pystray.stop()

def on_click():
    print("Clicked!")

def main():
    image_path = "icon_x128.png"
    image = Image.open(image_path)

    menu = (
        pystray.MenuItem('Click Me', on_click),
        pystray.MenuItem('Quit', on_quit)
    )

    tray = pystray.Icon("name", image, "Title", menu)
    tray.run()

if __name__ == '__main__':
    main()

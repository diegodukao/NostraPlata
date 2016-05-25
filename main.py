import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '700')

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

from kivy.app import App
from kivy.uix.listview import ListItemButton


class CustomListItemButton(ListItemButton):
    pass


class NostraPlata(App):
    pass


if __name__ == "__main__":
    NostraPlata().run()

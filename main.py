import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '700')

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

from kivy.app import App


class NostraPlataApp(App):
    pass


if __name__ == "__main__":
    NostraPlataApp().run()

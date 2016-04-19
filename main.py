import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'width', '394')
Config.set('graphics', 'height', '700')


class NostraPlataApp(App):
    pass


if __name__ == "__main__":
    NostraPlataApp().run()

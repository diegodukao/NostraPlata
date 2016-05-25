import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '700')

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

from kivy.app import App
from kivy.garden.androidtabs import AndroidTabsBase, AndroidTabs
from kivy.uix.boxlayout import BoxLayout


class MainTab(BoxLayout, AndroidTabsBase):
    pass


class NostraPlata(App):

    def build(self):
        tabs = AndroidTabs()
        main_tab = MainTab(text="Main")

        tabs.add_widget(main_tab)

        return tabs


if __name__ == "__main__":
    NostraPlata().run()

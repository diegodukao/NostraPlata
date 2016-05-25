import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '700')

# from kivy.core.window import Window
# Window.clearcolor = (1, 1, 1, 1)

from kivy.app import App
from kivy.garden.androidtabs import AndroidTabsBase, AndroidTabs
from kivy.uix.actionbar import ActionBar
from kivy.uix.boxlayout import BoxLayout


class Bar(ActionBar):
    pass


class MainTab(BoxLayout, AndroidTabsBase):
    pass


class HistoryTab(BoxLayout, AndroidTabsBase):
    pass


class NostraPlata(App):

    def build(self):
        bar = Bar()

        tabs = AndroidTabs()
        tab1 = MainTab(text="Status")
        tab2 = HistoryTab(text="History")

        tabs.add_widget(tab1)
        tabs.add_widget(tab2)

        main_screen = BoxLayout(orientation="vertical")
        main_screen.add_widget(bar)
        main_screen.add_widget(tabs)

        return main_screen

if __name__ == "__main__":
    NostraPlata().run()

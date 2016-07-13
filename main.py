import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '700')

# from kivy.core.window import Window
# Window.clearcolor = (1, 1, 1, 1)

from kivy.app import App
from kivy.garden.androidtabs import AndroidTabsBase, AndroidTabs
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionBar
from kivy.uix.boxlayout import BoxLayout


class NostraRoot(BoxLayout):
    main_screen = ObjectProperty()
    add_transaction_screen = ObjectProperty()

    def show_main_screen(self):
        self.remove_widget(self.add_transaction_screen)
        self.add_widget(self.main_screen)

    def show_add_transaction_screen(self):
        self.remove_widget(self.main_screen)

        if not self.add_transaction_screen:
            self.add_transaction_screen = AddTransactionScreen()
        self.add_widget(self.add_transaction_screen)


class MainScreen(AndroidTabs):
    pass


class AddTransactionScreen(BoxLayout):
    pass


class Bar(ActionBar):
    pass


class DashboardTab(BoxLayout, AndroidTabsBase):

    def populate_listview(self):
        items = ["History number %i" % index for index in range(30)]
        self.listview.adapter.data = items


class HistoryTab(BoxLayout, AndroidTabsBase):
    pass


class NostraPlata(App):

    def on_start(self):
        self.root.main.dashboard.populate_listview()
        self.root.main_screen = self.root.main

if __name__ == "__main__":
    NostraPlata().run()

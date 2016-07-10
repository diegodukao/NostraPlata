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


class NostraRoot(BoxLayout):

    def show_main_screen(self):
        self.clear_widgets()
        self.add_widget(MainScreen())

    def show_add_transaction_screen(self):
        self.clear_widgets()
        self.add_widget(AddTransactionScreen())


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

if __name__ == "__main__":
    NostraPlata().run()

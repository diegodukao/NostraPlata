import kivy
kivy.require('1.9.1')

from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '700')

# from kivy.core.window import Window
# Window.clearcolor = (1, 1, 1, 1)

from kivy.app import App
from kivy.garden.androidtabs import AndroidTabsBase, AndroidTabs
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionBar
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton

Builder.load_file('main_screen.kv')
Builder.load_file('new_loan_screen.kv')


class NostraRoot(BoxLayout):
    main_screen_widget = ObjectProperty()
    members_screen_widget = ObjectProperty()
    new_loan_screen_widget = ObjectProperty()
    current_screen = ObjectProperty()

    def show_main_screen(self):
        self.remove_widget(self.current_screen)
        self.add_widget(self.main_screen_widget)
        self.current_screen = self.main_screen_widget

    def show_members_screen(self):
        self.remove_widget(self.current_screen)

        if not self.members_screen_widget:
            self.members_screen_widget = MembersScreen()
        self.add_widget(self.members_screen_widget)
        self.current_screen = self.members_screen_widget

    def show_new_loan_screen(self):
        self.remove_widget(self.current_screen)

        if not self.new_loan_screen_widget:
            self.new_loan_screen_widget = NewLoanScreen()
        self.add_widget(self.new_loan_screen_widget)
        self.current_screen = self.new_loan_screen_widget


class MainScreen(AndroidTabs):
    pass


class MembersScreen(BoxLayout):
    pass


class MemberButton(ListItemButton):
    pass


class NewLoanScreen(BoxLayout):
    amount_input = ObjectProperty()

    def save_loan(self):
        loan_type_btns = ToggleButtonBehavior.get_widgets("loan_type")
        pressed_btns = [btn.text for btn in loan_type_btns if btn.state == "down"]
        if len(pressed_btns) == 1:
            loan_type = pressed_btns[0]
            print(self.amount_input.text)
            print(loan_type)


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
        self.root.main_screen_widget = self.root.main
        self.root.current_screen = self.root.main

if __name__ == "__main__":
    NostraPlata().run()

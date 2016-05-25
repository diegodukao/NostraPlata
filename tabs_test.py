from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
from kivy.garden.androidtabs import AndroidTabsBase, AndroidTabs


Builder.load_string('''
<Tab1>:
    canvas:
        Color:
            rgba: .5, 0, .5, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "rollan!"

<Tab2>:
    canvas:
        Color:
            rgba: 0, .5, .5, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "reagan!"
''')


class Tab1(BoxLayout, AndroidTabsBase):
    pass


class Tab2(BoxLayout, AndroidTabsBase):
    pass


class Example(App):

    def build(self):

        android_tabs = AndroidTabs()
        tab1 = Tab1(text="Status")
        tab2 = Tab2(text="History")

        android_tabs.add_widget(tab1)
        android_tabs.add_widget(tab2)

        return android_tabs

app = Example()
app.run()

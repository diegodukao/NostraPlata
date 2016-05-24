from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
from kivy.garden.androidtabs import AndroidTabsBase, AndroidTabs


Builder.load_string('''
<MyTab>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

<AndroidTabsBar>:
    canvas:
        Color:
            rgba: 0,0,0,.3
        Rectangle:
            pos: self.pos[0], self.pos[1] - 1
            size: self.size[0], 1
        Color:
            rgba: 0,0,0,.2
        Rectangle:
            pos: self.pos[0], self.pos[1] - 2
            size: self.size[0], 1
        Color:
            rgba: 0,0,0,.05
        Rectangle:
            pos: self.pos[0], self.pos[1] - 3
            size: self.size[0], 1
''')


class MyTab(BoxLayout, AndroidTabsBase):
    pass


class Example(App):

    def build(self):

        android_tabs = AndroidTabs()

        for n in range(1, 3):
            tab = MyTab(text='TAB %s' % n)
            android_tabs.add_widget(tab)

        return android_tabs

app = Example()
app.run()

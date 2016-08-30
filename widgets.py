from kivy.properties import StringProperty, NumericProperty
from kivy.uix.listview import ListItemButton


class FriendButton(ListItemButton):
    name = StringProperty()
    balance = NumericProperty()



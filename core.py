from kivy.event import EventDispatcher
from kivy.properties import StringProperty, BooleanProperty

class Kontrol(EventDispatcher):
    button_state    = StringProperty('OFF')
    busy            = BooleanProperty(False)

    def toggle_button(self):
        self.button_state = 'ON' if self.button_state == 'OFF' else 'OFF'
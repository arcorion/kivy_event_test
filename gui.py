from kivy.app import App
from kivy.lang import Builder
from core import Kontrol
from kivy.clock import Clock

KV = "gui.kv"

class KontrolApp(App):
    def build(self):
        self.kontrol = Kontrol()
        Clock.schedule_interval(lambda dt: setattr(self.kontrol, 'busy',
                                not self.kontrol.busy), 1)
        return Builder.load_file(KV)
    
def run():
    KontrolApp().run()
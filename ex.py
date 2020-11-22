from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen, ScreenManager

kv = """

BoxLayout: 
    orientation: 'vertical'
    MDToolbar:
        title: 'test'

    MDTabs:
        id: tabs

<Tab>:
    MDLabel:
        id: label
        text: 'Hello World'
        halign: 'center'


"""

class Hello(Screen):
    pass

class Tab(FloatLayout, MDTabsBase):
    pass

class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)

    # def on_start(self):
        # self.root.ids.tabs.add_widget(Tab(text='Mine'))

if __name__ == "__main__":
    Main().run()
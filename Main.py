# This is Class 7 MAIN Python file of Project SMS - Mudasir Ali

# Importing
from kivymd.app import MDApp
from kivymd.utils import asynckivy
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Importing Layouts
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.gridlayout import GridLayout

# Importing KivyMD Components
from kivymd.uix.button import (
MDFillRoundFlatButton, MDRaisedButton,
)
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from  kivy.metrics import dp

# Setting Window Maxamize - Mudasir Ali
Window.maximize()

# Chapter 1 Variables - Mudasir Ali
Chapter_1_name = 'Computer System'
Chapter_1_qn = '2'
Chapter_1_fb = '4'
Chapter_1_tf = '4'



class Class_7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Chapter_1_table = MDDataTable(
            size_hint=(.5, .3),
            pos_hint={'center_x': .5, 'center_y': .5},
            column_data=[
                ('Questions/Answers', dp(50)),
                ('True/False', dp(50)),
                ('Fill in the Blanks', dp(50)),
            ],
            row_data=[
                (Chapter_1_qn,Chapter_1_tf,Chapter_1_fb ),
                ('', '',  '')
                
            ]
        )
        self.Chapter_1_button = MDRaisedButton(text='Show More', pos_hint={'center_x': .5, 'center_y': .2})

        self.Chapter_2_table = MDDataTable(
            size_hint=(.5, .3),
            pos_hint={'center_x': .5, 'center_y': .5},
            column_data=[
                ('Questions/Answers', dp(50)),
                ('True/False', dp(50)),
                ('Fill in the Blanks', dp(50)),
            ],
            row_data=[
                (Chapter_1_qn,Chapter_1_tf,Chapter_1_fb ),
                ('', '',  '')
                
            ]
        )
        self.Chapter_2_button = MDRaisedButton(text='Show More', pos_hint={'center_x': .5, 'center_y': .2})

        self.Chapter_3_table = MDDataTable(
            size_hint=(.5, .3),
            pos_hint={'center_x': .5, 'center_y': .5},
            column_data=[
                ('Questions/Answers', dp(50)),
                ('True/False', dp(50)),
                ('Fill in the Blanks', dp(50)),
            ],
            row_data=[
                (Chapter_1_qn,Chapter_1_tf,Chapter_1_fb ),
                ('', '',  '')
                
            ]
        )
        self.Chapter_3_button = MDRaisedButton(text='Show More', pos_hint={'center_x': .5, 'center_y': .2})

        self.Chapter_4_table = MDDataTable(
            size_hint=(.5, .3),
            pos_hint={'center_x': .5, 'center_y': .5},
            column_data=[
                ('Questions/Answers', dp(50)),
                ('True/False', dp(50)),
                ('Fill in the Blanks', dp(50)),
            ],
            row_data=[
                (Chapter_1_qn,Chapter_1_tf,Chapter_1_fb ),
                ('', '',  '')
                
            ]
        )
        self.Chapter_4_button = MDRaisedButton(text='Show More', pos_hint={'center_x': .5, 'center_y': .2})

        self.Chapter_5_table = MDDataTable(
            size_hint=(.5, .3),
            pos_hint={'center_x': .5, 'center_y': .5},
            column_data=[
                ('Questions/Answers', dp(50)),
                ('True/False', dp(50)),
                ('Fill in the Blanks', dp(50)),
            ],
            row_data=[
                (Chapter_1_qn,Chapter_1_tf,Chapter_1_fb ),
                ('', '',  '')
                
            ]
        )
        self.Chapter_5_button = MDRaisedButton(text='Show More', pos_hint={'center_x': .5, 'center_y': .2})

        self.label = MDLabel(size_hint_y=None, height=dp(10))

        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)
            
            # Adding Widgets to the Cards - Mudasir Ali
            self.ids.chapter_1_heading.text = f'Ch:1, {Chapter_1_name}'
            self.ids.card_1.add_widget(self.Chapter_1_table)
            self.ids.card_1.add_widget(self.Chapter_1_button)
            self.ids.card_1.add_widget(self.label)

            self.ids.chapter_2_heading.text = f'Ch:2, {Chapter_1_name}'
            self.ids.card_2.add_widget(self.Chapter_2_table)
            self.ids.card_2.add_widget(self.Chapter_2_button)
            

            self.ids.chapter_3_heading.text = f'Ch:3, {Chapter_1_name}'
            self.ids.card_3.add_widget(self.Chapter_3_table)
            self.ids.card_3.add_widget(self.Chapter_3_button)

            self.ids.chapter_4_heading.text = f'Ch:4, {Chapter_1_name}'
            self.ids.card_4.add_widget(self.Chapter_4_table)
            self.ids.card_4.add_widget(self.Chapter_4_button)

            self.ids.chapter_5_heading.text = f'Ch:5, {Chapter_1_name}'
            self.ids.card_5.add_widget(self.Chapter_5_table)
            self.ids.card_5.add_widget(self.Chapter_5_button)
    


        asynckivy.start(show())

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.title = 'SMS - Class 7 - Created by MUDASIR ALI'
        Style = Builder.load_file('Main.kv')
        return Style

if __name__ == '__main__':
    MainApp().run()

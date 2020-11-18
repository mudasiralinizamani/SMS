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
MDFillRoundFlatButton,
MDRaisedButton,
MDRectangleFlatButton,
)
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from  kivy.metrics import dp

# Setting Window Maxamize - Mudasir Ali
Window.maximize()

# Variables for Users - Mudasir Ali
Usernames = ['mudasir', 'nida']
Passwords = {Usernames[0]: '12345', Usernames[1]: '12345'}

# Chapter 1 Variables - Mudasir Ali
Chapter_1_name = 'Computer System'
Chapter_1_qn = '8'
Chapter_1_fb = '10'
Chapter_1_tf = '10'
# Variables for True False - Mudasir Ali
Chapter_1_truefalse = ['A joystick if used for playing games.',
                                                'A scanner is an output device.',
                                                'MICR characters use the normal black int.',
                                                'An OMR can read any type of marks on answer.',
                                                'Touch screens are very easy to use.',
                                                'A microphone is an output device.',
                                                'A printed copy is  know as hard copy.',
                                                'A speaker is an output device',
                                                'CD stands for computer disc',
                                                'A DVD has more storage capacity than a CD']

Chapter_1_trues_false = {Chapter_1_truefalse[0]: 'True', Chapter_1_truefalse[1]: 'False', 
                                                    Chapter_1_truefalse[2]: 'True', Chapter_1_truefalse[3]: 'True', 
                                                    Chapter_1_truefalse[4]: 'True', Chapter_1_truefalse[5]: 'True', 
                                                    Chapter_1_truefalse[6]: 'True', Chapter_1_truefalse[7]: 'True', 
                                                    Chapter_1_truefalse[8]: 'True', Chapter_1_truefalse[9]: 'True'}

# Variables for Fill in the Blanks - Mudasir Ali
Chapter_1_fill_in_blanks = ['The evolution of computers started way back in the late ____.',
                                                            'First generation computers were based on ____.',
                                                            'The devices attached to a computer are called ____.',
                                                            '____ software controls the internal computer operations.',
                                                            '____ are those simple programs that assist the computer by performing functions.',
                                                            'Bluetooth technology is a form of ____ communication.',
                                                            'The types of transmission channels are ____ and ____.',
                                                            'In ____ topology, all the workstations are connected to the central hub.',
                                                            '____ is a computer that manages the storage and retrieval of files.',
                                                            'In ____ the computer are interconnected within a limited geographical area.']

Chapter_1_blanks = {Chapter_1_fill_in_blanks[0]: '1930',
                                            Chapter_1_fill_in_blanks[1]: 'Vaccum tube',
                                            Chapter_1_fill_in_blanks[2]: 'Peripheral',
                                            Chapter_1_fill_in_blanks[3]: 'System',
                                            Chapter_1_fill_in_blanks[4]: 'Communicate',
                                            Chapter_1_fill_in_blanks[5]: 'Wireless',
                                            Chapter_1_fill_in_blanks[6]: ['Wired', 'Wireless'],
                                            Chapter_1_fill_in_blanks[7]: 'Start',
                                            Chapter_1_fill_in_blanks[8]: 'A server',
                                            Chapter_1_fill_in_blanks[9]: 'LAN'}

Chapter_1_questions = ['What is a peripheral device? Give examples of some peripheral devices.',
                                                'Where is a touch screen used?',
                                                'Why are secondary storage devices needed?',
                                                'Where is MICR normally used and why?',
                                                'Name the computers used in different generations?',
                                                'What is networking? Give its two advantages?',
                                                'What are the different components of a computer network? Explain them briefly.',
                                                'What s topology? Give examples.']

Chapter_1_answers = {Chapter_1_questions[0]: ['The word peripheral comes form preipheral which at the edge or border in computer terminology peripheral', '1: Input Devices, 2: Output Devices, 3: Storage Devices'],
                                            Chapter_1_questions[1]: '',
                                            Chapter_1_questions[2]: '',
                                            Chapter_1_questions[3]: '',
                                            Chapter_1_questions[4]: '',
                                            Chapter_1_questions[5]: '',
                                            Chapter_1_questions[6]: '',
                                            Chapter_1_questions[7]: ''}

# Chapter 2 Variables - Mudasir Ali
Chapter_2_name = 'Feature of Windows'
Chapter_2_qn = '4'
Chapter_2_fb = '4'
Chapter_2_tf = '10'

# Chapter 3 Variables - Mudasir Ali
Chapter_3_name = 'MD Word-Advance Features'
Chapter_3_qn = '5'
Chapter_3_fb = '8'
Chapter_3_tf = '6'

# Chapter 4 Variables - Mudasir Ali
Chapter_4_name = 'PowerPoint-Advance Features'
Chapter_4_qn = '6'
Chapter_4_fb = '6'
Chapter_4_tf = '4'

# Chapter 5 Variables - Mudasir Ali
Chapter_5_name = 'MS Excel-Advance Features'
Chapter_5_qn = '5'
Chapter_5_fb = '5'
Chapter_5_tf = '5'



class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Dialog_box = MDDialog(title='None', size_hint=(.8, 1))
        self.Close_button = MDRaisedButton(text='Close', on_release=self.Close_dialog)
        self.Continue_button = MDRaisedButton(text='Continue', on_release=self.Continue)

    def User_login(self):
        username = str(self.ids.username_field.text)
        password = str(self.ids.password_field.text)

        if username in Usernames and password == Passwords.get(username):
            self.Dialog_box = MDDialog(title=f'Hi {username}, Welcome to the SMS', size_hint=(.8, 1), buttons=[self.Continue_button])
        elif username in Usernames and password != Passwords.get(username):
            self.Dialog_box = MDDialog(title=f'{username}, Your password is incorrect.', buttons=[self.Close_button], size_hint=(.8, 1))
        else:
            self.Dialog_box = MDDialog(title=f'Username and Password are incorrect.', buttons=[self.Close_button], size_hint=(.8, 1))

        self.Dialog_box.open()

    def Close_dialog(self, obg):
        self.Dialog_box.dismiss()
    
    def Continue(self, obg):
        self.manager.current = 'class_7'
        self.Dialog_box.dismiss()

# Main Screen - Mudasir Ali
class Class_7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creating Tables and buttons for show data of Chapters - mudasir Ali
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
        self.Chapter_1_button = Builder.load_file('Styles/Main/showmore_1.kv')

        self.Chapter_2_table = MDDataTable(
            size_hint=(.5, .3),
            pos_hint={'center_x': .5, 'center_y': .5},
            column_data=[
                ('Questions/Answers', dp(50)),
                ('True/False', dp(50)),
                ('Fill in the Blanks', dp(50)),
            ],
            row_data=[
                (Chapter_2_qn,Chapter_2_tf,Chapter_2_fb ),
                ('', '',  '')
                
            ]
        )
        self.Chapter_2_button = MDRectangleFlatButton(text='Show More', pos_hint={'center_x': .5, 'center_y': .2})

        self.Chapter_3_table = MDDataTable(
            size_hint=(.5, .3),
            pos_hint={'center_x': .5, 'center_y': .5},
            column_data=[
                ('Questions/Answers', dp(50)),
                ('True/False', dp(50)),
                ('Fill in the Blanks', dp(50)),
            ],
            row_data=[
                (Chapter_3_qn,Chapter_3_tf,Chapter_3_fb ),
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
                (Chapter_4_qn,Chapter_4_tf,Chapter_4_fb ),
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
                (Chapter_5_qn,Chapter_5_tf,Chapter_5_fb ),
                ('', '',  '')
                
            ]
        )
        self.Chapter_5_button = MDRaisedButton(text='Show More', pos_hint={'center_x': .5, 'center_y': .2})

        # These labels are just for Spacing - Mudasir Ali, I will fix this later
        self.label = MDLabel(size_hint_y=None, height=dp(10))
        self.label_2 = MDLabel(size_hint_y=None, height=dp(10))
        self.label_3 = MDLabel(size_hint_y=None, height=dp(10))
        self.label_4 = MDLabel(size_hint_y=None, height=dp(10))
        self.label_5 = MDLabel(size_hint_y=None, height=dp(10))

        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)
            
            # Adding Widgets to the Cards - Mudasir Ali
            self.ids.chapter_1_heading.text = f'Ch:1, {Chapter_1_name}'
            self.ids.card_1.add_widget(self.Chapter_1_table)
            self.ids.card_1.add_widget(self.Chapter_1_button)
            self.ids.card_1.add_widget(self.label)

            self.ids.chapter_2_heading.text = f'Ch:2, {Chapter_2_name}'
            self.ids.card_2.add_widget(self.Chapter_2_table)
            self.ids.card_2.add_widget(self.Chapter_2_button)
            # self.ids.card_2.add_widget(self.label_2)
            

            self.ids.chapter_3_heading.text = f'Ch:3, {Chapter_3_name}'
            self.ids.card_3.add_widget(self.Chapter_3_table)
            self.ids.card_3.add_widget(self.Chapter_3_button)
            self.ids.card_3.add_widget(self.label_3)

            self.ids.chapter_4_heading.text = f'Ch:4, {Chapter_4_name}'
            self.ids.card_4.add_widget(self.Chapter_4_table)
            self.ids.card_4.add_widget(self.Chapter_4_button)
            self.ids.card_4.add_widget(self.label_4)

            self.ids.chapter_5_heading.text = f'Ch:5, {Chapter_5_name}'
            self.ids.card_5.add_widget(self.Chapter_5_table)
            self.ids.card_5.add_widget(self.Chapter_5_button)
            self.ids.card_5.add_widget(self.label_5)
    
        asynckivy.start(show())


# Screen Classes for chapters - Mudasir Ali
class Chapter_1_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creating table for Chapter True False - Mudasir Ali

        self.true_false_table = MDDataTable(
            size_hint=(.8, .8),
            pos_hint={'center_x': .5, 'center_y': .5},
            use_pagination=True,
            rows_num=5,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(165)),
                ('True/False', dp(30))],
            row_data=[
                ('1', Chapter_1_truefalse[0], Chapter_1_trues_false.get(Chapter_1_truefalse[0])),
                ('2', Chapter_1_truefalse[1], Chapter_1_trues_false.get(Chapter_1_truefalse[1])),
                ('3', Chapter_1_truefalse[2], Chapter_1_trues_false.get(Chapter_1_truefalse[2])),
                ('4', Chapter_1_truefalse[3], Chapter_1_trues_false.get(Chapter_1_truefalse[3])),
                ('5', Chapter_1_truefalse[4], Chapter_1_trues_false.get(Chapter_1_truefalse[4])),
                ('6', Chapter_1_truefalse[5], Chapter_1_trues_false.get(Chapter_1_truefalse[5])),
                ('7', Chapter_1_truefalse[6], Chapter_1_trues_false.get(Chapter_1_truefalse[6])),
                ('8', Chapter_1_truefalse[7], Chapter_1_trues_false.get(Chapter_1_truefalse[7])),
                ('9', Chapter_1_truefalse[8], Chapter_1_trues_false.get(Chapter_1_truefalse[8])),
                ('10', Chapter_1_truefalse[9], Chapter_1_trues_false.get(Chapter_1_truefalse[9])),
            ]
        )

        self.fill_in_blanks_table = MDDataTable(
            size_hint=(.8, .8),
            pos_hint={'center_x': .5, 'center_y': .5},
            use_pagination=True,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(155)),
                ('Blanks', dp(40))],
            row_data=[
                ('1', Chapter_1_fill_in_blanks[0], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[0])),
                ('2', Chapter_1_fill_in_blanks[1], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[1])),
                ('3', Chapter_1_fill_in_blanks[2], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[2])),
                ('4', Chapter_1_fill_in_blanks[3], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[3])),
                ('5', Chapter_1_fill_in_blanks[4], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[4])),
                ('6', Chapter_1_fill_in_blanks[5], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[5])),
                ('7', Chapter_1_fill_in_blanks[6], f'{Chapter_1_blanks.get(Chapter_1_fill_in_blanks[6])[0]} {Chapter_1_blanks.get(Chapter_1_fill_in_blanks[6])[1]}'),
                ('8', Chapter_1_fill_in_blanks[7], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[7])),
                ('9', Chapter_1_fill_in_blanks[8], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[8])),
                ('10', Chapter_1_fill_in_blanks[9], Chapter_1_blanks.get(Chapter_1_fill_in_blanks[9])),
                
            ]
        )
         # Labels for questions and answers - Mudasir Ali
        self.question_1 = MDLabel(text=f'Q 1: {Chapter_1_questions[0]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_1 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[0])[0]}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_1_2 = MDLabel(text=f'Eg {Chapter_1_answers.get(Chapter_1_questions[0])[1]}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))

        self.question_2 = MDLabel(text=f'Q 2: {Chapter_1_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_2 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))

        self.question_3 = MDLabel(text=f'Q 3: {Chapter_1_questions[2]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_3 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[2])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))

        self.question_4 = MDLabel(text=f'Q 4: {Chapter_1_questions[3]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_4 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[3])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))

        self.question_5 = MDLabel(text=f'Q 5: {Chapter_1_questions[4]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_5 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[4])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))

        self.question_6 = MDLabel(text=f'Q 6: {Chapter_1_questions[5]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_6 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[5])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))

        self.question_7 = MDLabel(text=f'Q 7: {Chapter_1_questions[6]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_7 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[6])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))

        self.question_8 = MDLabel(text=f'Q 8: {Chapter_1_questions[7]}', italic=True, theme_text_color='Primary', font_style='H6', size_hint_y=None, height=dp(30))
        self.answer_8 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[7])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(30))


        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)

            # Adding Widgets to the Cards - Mudasir Ali
            self.ids.true_false_card.add_widget(self.true_false_table)
            self.ids.fill_in_blanks_card.add_widget(self.fill_in_blanks_table)

            # Adding questions/answers to the Cards - Mudasir Ali
            self.ids.question_answer_card.add_widget(self.question_1)
            self.ids.question_answer_card.add_widget(self.answer_1)
            self.ids.question_answer_card.add_widget(self.answer_1_2)

            self.ids.question_answer_card.add_widget(self.question_2)
            self.ids.question_answer_card.add_widget(self.answer_2)

            self.ids.question_answer_card.add_widget(self.question_3)
            self.ids.question_answer_card.add_widget(self.answer_3)

            self.ids.question_answer_card.add_widget(self.question_4)
            self.ids.question_answer_card.add_widget(self.answer_4)

            self.ids.question_answer_card.add_widget(self.question_5)
            self.ids.question_answer_card.add_widget(self.answer_5)

            self.ids.question_answer_card.add_widget(self.question_6)
            self.ids.question_answer_card.add_widget(self.answer_6)

            self.ids.question_answer_card.add_widget(self.question_7)
            self.ids.question_answer_card.add_widget(self.answer_7)

            self.ids.question_answer_card.add_widget(self.question_8)
            self.ids.question_answer_card.add_widget(self.answer_8)


        asynckivy.start(show())
class Chapter_2_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Chapter_3_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Chapter_4_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Chapter_5_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



# ScreenManager Class - Mudasir Ali
class WindowManager(ScreenManager):
    pass

# MainApp for Class_7 - Mudasir Ali
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.title = 'SMS - Class 7 - Created by MUDASIR ALI'
        Style = Builder.load_file('Main.kv')
        return Style

# Running the Class_7 Main App - Mudasir Ali
if __name__ == '__main__':
    MainApp().run()

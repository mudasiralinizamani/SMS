# This is Class 7 MAIN Python file of Project SMS - Mudasir Ali

# Importing
from kivymd.app import MDApp
from kivymd.utils import asynckivy
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Importing Layouts
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

# Importing from  KivyMD - Mudasir Ali
from kivymd.uix.button import (
MDFillRoundFlatButton,
MDRaisedButton,
MDRectangleFlatButton,
)
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.tab import MDTabsBase

# Importing from kivy - Mudasir Ali
from  kivy.metrics import dp
from kivy.core.text import LabelBase

# Importing data from Chapters - Mudasir Ali
from Chapter_data.chapter_1 import * 
from Chapter_data.chapter_2 import * 
from Chapter_data.chapter_3 import * 
from Chapter_data.chapter_4 import * 
from Chapter_data.chapter_5 import * 


# Registring Fonts - Mudasir Ali
LabelBase.register('NotoSansJP-Regular', 'Fonts/Nerko_One/NerkoOne-Regular.ttf')


# Setting Window Maxamize - Mudasir Ali
Window.maximize()

# Variables for Users - Mudasir Ali
Usernames = ['mudasir', 'nida']
Passwords = {Usernames[0]: '12345', Usernames[1]: '12345'}




# Login Classs - Mudasir Ali
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


class Courses(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    

class Ms_Word_Courses(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MS_Excel_Course(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Main Screen for class 7 - Mudasir Ali
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
        self.Chapter_2_button = Builder.load_file('Styles/Main/showmore_2.kv')

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
        self.Chapter_3_button = Builder.load_file('Styles/Main/showmore_3.kv')

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
        self.Chapter_4_button = Builder.load_file('Styles/Main/showmore_4.kv')


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
        self.Chapter_5_button = Builder.load_file('Styles/Main/showmore_4.kv')

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

# Class for Chapter 1 - Mudasir Ali
class Chapter_1_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)
            
            # Adding Tabs to the Screen - Mudasir Ali
            self.ids.tabs.add_widget(self.Chapter_1_Question_Answers(text='Question Answers'))
            self.ids.tabs.add_widget(self.Chapter_1_Fill_in_blanks(text='Fill in the Blanks'))
            self.ids.tabs.add_widget(self.Chapter_1_True_False(text='True False'))

        asynckivy.start(show())

    # Class for Chapter 1, Question_Answers - Mudasir Ali
    class Chapter_1_Question_Answers(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            # Labels for questions and answers - Mudasir Ali
            self.question_1 = MDLabel(text=f'Q 1: {Chapter_1_questions[0]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_1 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[0])[0]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_1_2 = MDLabel(text=f'Eg {Chapter_1_answers.get(Chapter_1_questions[0])[1]}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_1 = MDLabel()

            self.question_2 = MDLabel(text=f'Q 2: {Chapter_1_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_2 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_2 = MDLabel()

            self.question_3 = MDLabel(text=f'Q 3: {Chapter_1_questions[2]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_3 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[2])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_3 = MDLabel()

            self.question_4 = MDLabel(text=f'Q 4: {Chapter_1_questions[3]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_4 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[3])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_4 = MDLabel()

            self.question_5 = MDLabel(text=f'Q 5: {Chapter_1_questions[4]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_5_1 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[4])[0]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_2 = MDLabel(text=f'2: {Chapter_1_answers.get(Chapter_1_questions[4])[1]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_3 = MDLabel(text=f'3: {Chapter_1_answers.get(Chapter_1_questions[4])[2]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_4 = MDLabel(text=f'4: {Chapter_1_answers.get(Chapter_1_questions[4])[3]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_5 = MDLabel(text=f'5: {Chapter_1_answers.get(Chapter_1_questions[4])[4]}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_5 = MDLabel()

            self.question_6 = MDLabel(text=f'Q 6: {Chapter_1_questions[5]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_6_1 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[5])[0]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_6_2 = MDLabel(text=f'1: {Chapter_1_answers.get(Chapter_1_questions[5])[1]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_6_3 = MDLabel(text=f'2: {Chapter_1_answers.get(Chapter_1_questions[5])[2]}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_6 = MDLabel()

            self.question_7 = MDLabel(text=f'Q 7: {Chapter_1_questions[6]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_7 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[6])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(100))

            self.spacing_7 = MDLabel()

            self.question_8 = MDLabel(text=f'Q 8: {Chapter_1_questions[7]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_8 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[7])}', italic=True, theme_text_color='Secondary', font_style='H6', size_hint_y=None, height=dp(50))

            self.Show()

        def Show(self):
            async def show():

                # Adding questions/answers to the Cards - Mudasir Ali
                self.ids.question_answer_card.add_widget(self.question_1)
                self.ids.question_answer_card.add_widget(self.answer_1)
                self.ids.question_answer_card.add_widget(self.answer_1_2)

                self.ids.question_answer_card.add_widget(self.spacing_1)
                
                self.ids.question_answer_card.add_widget(self.question_2)
                self.ids.question_answer_card.add_widget(self.answer_2)

                self.ids.question_answer_card.add_widget(self.spacing_2)

                self.ids.question_answer_card.add_widget(self.question_3)
                self.ids.question_answer_card.add_widget(self.answer_3)

                self.ids.question_answer_card.add_widget(self.spacing_3)

                self.ids.question_answer_card.add_widget(self.question_4)
                self.ids.question_answer_card.add_widget(self.answer_4)

                self.ids.question_answer_card.add_widget(self.spacing_4)

                self.ids.question_answer_card.add_widget(self.question_5)
                self.ids.question_answer_card.add_widget(self.answer_5_1)
                self.ids.question_answer_card.add_widget(self.answer_5_2)
                self.ids.question_answer_card.add_widget(self.answer_5_3)
                self.ids.question_answer_card.add_widget(self.answer_5_4)
                self.ids.question_answer_card.add_widget(self.answer_5_5)

                self.ids.question_answer_card.add_widget(self.spacing_5)

                self.ids.question_answer_card.add_widget(self.question_6)
                self.ids.question_answer_card.add_widget(self.answer_6_1)
                self.ids.question_answer_card.add_widget(self.answer_6_2)
                self.ids.question_answer_card.add_widget(self.answer_6_3)

                self.ids.question_answer_card.add_widget(self.spacing_6)

                # self.ids.question_answer_card.add_widget(self.question_7)
                # self.ids.question_answer_card.add_widget(self.answer_7)

                # self.ids.question_answer_card.add_widget(self.spacing_7)

                # self.ids.question_answer_card.add_widget(self.question_8)
                # self.ids.question_answer_card.add_widget(self.answer_8)
            
            asynckivy.start(show())

    # Class for Chapter 1, Fill in the Blanks - Mudasir Ali
    class Chapter_1_Fill_in_blanks(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.fill_in_blanks_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            rows_num=7,
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

            self.Show()
        
        def Show(self):
            async def show():

                self.ids.fill_in_blanks_box.add_widget(self.fill_in_blanks_table)
            
            asynckivy.start(show())

    # Class for Chapter 1, True False - Mudasir Ali
    class Chapter_1_True_False(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.true_false_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            use_pagination=True,
            rows_num=7,
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
                ('10', Chapter_1_truefalse[9], Chapter_1_trues_false.get(Chapter_1_truefalse[9]))])

            self.Show()
        
        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.true_false_box.add_widget(self.true_false_table)
            
            asynckivy.start(show())

# Screen Class for Chapter 2 - Mudasir Ali
class Chapter_2_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)
            
            # Adding tabs to the SCreen
            self.ids.tabs.add_widget(self.Chapter_2_Question_Answers(text='Question Answers'))
            self.ids.tabs.add_widget(self.Chapter_2_Fill_in_blanks(text='Fill in the Blanks'))
            self.ids.tabs.add_widget(self.Chapter_2_True_False(text='True False'))
            
        asynckivy.start(show())

    # Class for Chapter 2, Question_Answers - Mudasir Ali
    class Chapter_2_Question_Answers(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            # Labels for Questions Answers - Mudasir Ali
            self.question_1 = MDLabel(text=f'Q 1: {Chapter_2_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_1 = MDLabel(text=f'Ans: {Chapter_2_answers.get(Chapter_2_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_1 = MDLabel()

            self.question_2 = MDLabel(text=f'Q 2: {Chapter_2_questions[2]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_2 = MDLabel(text=f'Ans: {Chapter_2_answers.get(Chapter_2_questions[2])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.spacing_2 = MDLabel()

            self.question_3 = MDLabel(text=f'Q 3: {Chapter_2_questions[3]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_3_1 = MDLabel(text=f'Ans: {Chapter_2_answers.get(Chapter_2_questions[3])[1]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_3_2 = MDLabel(text=f'Screen Saver: {Chapter_2_answers.get(Chapter_2_questions[3])[2]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_3_3 = MDLabel(text=f'Appearance: {Chapter_2_answers.get(Chapter_2_questions[3])[3]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_3_4 = MDLabel(text=f'Settings: {Chapter_2_answers.get(Chapter_2_questions[3])[4]}', italic=True, theme_text_color='Secondary', font_style='H6')
        
            self.spacing_4 = MDLabel()

            self.question_4 = MDLabel(text=f'Q 4: {Chapter_2_questions[4]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_4 = MDLabel(text=f'Ans: {Chapter_2_answers.get(Chapter_2_questions[4])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.question_answer_card.add_widget(self.question_1)
                self.ids.question_answer_card.add_widget(self.answer_1)

                self.ids.question_answer_card.add_widget(self.spacing_1)

                self.ids.question_answer_card.add_widget(self.question_2)
                self.ids.question_answer_card.add_widget(self.answer_2)

                self.ids.question_answer_card.add_widget(self.spacing_2)

                self.ids.question_answer_card.add_widget(self.question_3)
                self.ids.question_answer_card.add_widget(self.answer_3_1)
                self.ids.question_answer_card.add_widget(self.answer_3_2)
                self.ids.question_answer_card.add_widget(self.answer_3_3)
                self.ids.question_answer_card.add_widget(self.answer_3_4)

                self.ids.question_answer_card.add_widget(self.spacing_4)

                self.ids.question_answer_card.add_widget(self.question_4)
                self.ids.question_answer_card.add_widget(self.answer_4)

            asynckivy.start(show())

    # Class for Chapter 2, Fill in the blanks - Mudasir Ali
    class Chapter_2_Fill_in_blanks(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.fill_in_blanks_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            rows_num=7,
            use_pagination=True,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(155)),
                ('Blanks', dp(40))],
            row_data=[
                ('1', Chapter_2_fill_in_blanks[1], Chapter_2_blanks.get(Chapter_2_fill_in_blanks[1])),
                ('2', Chapter_2_fill_in_blanks[2], Chapter_2_blanks.get(Chapter_2_fill_in_blanks[2])),
                ('3', Chapter_2_fill_in_blanks[3], Chapter_2_blanks.get(Chapter_2_fill_in_blanks[3])),
                ('4', Chapter_2_fill_in_blanks[4], Chapter_2_blanks.get(Chapter_2_fill_in_blanks[4]))])

            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.fill_in_blanks_box.add_widget(self.fill_in_blanks_table)

            asynckivy.start(show())

    # Class for Chapter 2, True False - Mudasir Ali
    class Chapter_2_True_False(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.true_false_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            use_pagination=True,
            rows_num=7,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(165)),
                ('True/False', dp(30))],
            row_data=[
                ('1', Chapter_2_truefalse[1], Chapter_2_trues_false.get(Chapter_2_truefalse[1])),
                ('2', Chapter_2_truefalse[2], Chapter_2_trues_false.get(Chapter_2_truefalse[2])),
                ('3', Chapter_2_truefalse[3], Chapter_2_trues_false.get(Chapter_2_truefalse[3])),
                ('4', Chapter_2_truefalse[4], Chapter_2_trues_false.get(Chapter_2_truefalse[4])),
                ('5', Chapter_2_truefalse[5], Chapter_2_trues_false.get(Chapter_2_truefalse[5])),
                ('6', Chapter_2_truefalse[6], Chapter_2_trues_false.get(Chapter_2_truefalse[6])),
                ('7', Chapter_2_truefalse[7], Chapter_2_trues_false.get(Chapter_2_truefalse[7])),
                ('8', Chapter_2_truefalse[8], Chapter_2_trues_false.get(Chapter_2_truefalse[8])),
                ('9', Chapter_2_truefalse[9], Chapter_2_trues_false.get(Chapter_2_truefalse[9])),
                ('10', Chapter_2_truefalse[10], Chapter_2_trues_false.get(Chapter_2_truefalse[10]))])
        
            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.true_false_box.add_widget(self.true_false_table)

            asynckivy.start(show())

# Screen Class for chapter 3 - Mudasir Ali
class Chapter_3_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)
            
            # Adding tabs to the SCreen
            self.ids.tabs.add_widget(self.Chapter_3_Question_Answers(text='Question Answers'))
            self.ids.tabs.add_widget(self.Chapter_3_Fill_in_blanks(text='Fill in the Blanks'))
            self.ids.tabs.add_widget(self.Chapter_3_True_False(text='True False'))
            
        asynckivy.start(show())
    
    # Class for Chapter 3, Question Answers - Mudasir Ali
    class Chapter_3_Question_Answers(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            # Labels for Questions Answers - Mudasir Ali
            self.spacing_1 = MDLabel()

            self.question_1 = MDLabel(text=f'Q 1: {Chapter_3_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_1 = MDLabel(text=f'Ans: {Chapter_3_answers.get(Chapter_3_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6')


            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.question_answer_card.add_widget(self.spacing_1)

                self.ids.question_answer_card.add_widget(self.question_1)
                self.ids.question_answer_card.add_widget(self.answer_1)


            asynckivy.start(show())

    # Class for Chapter 3, Fill in the blanks - Mudasir Ali
    class Chapter_3_Fill_in_blanks(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.fill_in_blanks_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            rows_num=7,
            use_pagination=True,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(155)),
                ('Blanks', dp(40))],
            row_data=[
                ('1', Chapter_3_fill_in_blanks[1], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[1])),
                ('2', Chapter_3_fill_in_blanks[2], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[2])),
                ('3', Chapter_3_fill_in_blanks[3], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[3])),
                ('4', Chapter_3_fill_in_blanks[4], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[4])),
                ('5', Chapter_3_fill_in_blanks[5], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[5])),
                ('6', Chapter_3_fill_in_blanks[6], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[6])),
                ('7', Chapter_3_fill_in_blanks[7], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[7])),
                ('8', Chapter_3_fill_in_blanks[8], Chapter_3_blanks.get(Chapter_3_fill_in_blanks[8]))])

            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.fill_in_blanks_box.add_widget(self.fill_in_blanks_table)

            asynckivy.start(show())

    # Class for Chapter 3, True False - Mudasir Ali
    class Chapter_3_True_False(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.true_false_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            use_pagination=True,
            rows_num=7,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(165)),
                ('True/False', dp(30))],
            row_data=[
                ('1', Chapter_3_truefalse[1], Chapter_3_trues_false.get(Chapter_3_truefalse[1])),
                ('2', Chapter_3_truefalse[2], Chapter_3_trues_false.get(Chapter_3_truefalse[2])),
                ('3', Chapter_3_truefalse[3], Chapter_3_trues_false.get(Chapter_3_truefalse[3])),
                ('4', Chapter_3_truefalse[4], Chapter_3_trues_false.get(Chapter_3_truefalse[4])),
                ('5', Chapter_3_truefalse[5], Chapter_3_trues_false.get(Chapter_3_truefalse[5])),
                ('6', Chapter_3_truefalse[6], Chapter_3_trues_false.get(Chapter_3_truefalse[6]))])
        
            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.true_false_box.add_widget(self.true_false_table)

            asynckivy.start(show())

# Screen Class for chapter 4- Mudasir Ali
class Chapter_4_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)
            
            # Adding tabs to the SCreen
            self.ids.tabs.add_widget(self.Chapter_4_Question_Answers(text='Question Answers'))
            self.ids.tabs.add_widget(self.Chapter_4_Fill_in_blanks(text='Fill in the Blanks'))
            self.ids.tabs.add_widget(self.Chapter_4_True_False(text='True False'))
            
        asynckivy.start(show())
    
    # Class for Chapter 4, Question Answers - Mudasir Ali
    class Chapter_4_Question_Answers(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            # Labels for Questions Answers - Mudasir Ali
            self.spacing_1 = MDLabel()

            self.question_1 = MDLabel(text=f'Q 1: {Chapter_4_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_1 = MDLabel(text=f'Ans: {Chapter_4_answers.get(Chapter_4_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6')


            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.question_answer_card.add_widget(self.spacing_1)

                self.ids.question_answer_card.add_widget(self.question_1)
                self.ids.question_answer_card.add_widget(self.answer_1)


            asynckivy.start(show())

    # Class for Chapter 4, Fill in the blanks - Mudasir Ali
    class Chapter_4_Fill_in_blanks(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.fill_in_blanks_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            rows_num=7,
            use_pagination=True,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(155)),
                ('Blanks', dp(40))],
            row_data=[
                ('1', Chapter_4_fill_in_blanks[1], Chapter_4_blanks.get(Chapter_4_fill_in_blanks[1])),
                ('2', Chapter_4_fill_in_blanks[2], Chapter_4_blanks.get(Chapter_4_fill_in_blanks[2])),
                ('3', Chapter_4_fill_in_blanks[3], Chapter_4_blanks.get(Chapter_4_fill_in_blanks[3])),
                ('4', Chapter_4_fill_in_blanks[4], Chapter_4_blanks.get(Chapter_4_fill_in_blanks[4])),
                ('5', Chapter_4_fill_in_blanks[5], Chapter_4_blanks.get(Chapter_4_fill_in_blanks[5])),
                ('6', Chapter_4_fill_in_blanks[6], Chapter_4_blanks.get(Chapter_4_fill_in_blanks[6])),])

            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.fill_in_blanks_box.add_widget(self.fill_in_blanks_table)

            asynckivy.start(show())

    # Class for Chapter 4, True False - Mudasir Ali
    class Chapter_4_True_False(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.true_false_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            use_pagination=True,
            rows_num=7,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(165)),
                ('True/False', dp(30))],
            row_data=[
                ('1', Chapter_4_truefalse[1], Chapter_4_trues_false.get(Chapter_4_truefalse[1])),
                ('2', Chapter_4_truefalse[2], Chapter_4_trues_false.get(Chapter_4_truefalse[2])),
                ('3', Chapter_4_truefalse[3], Chapter_4_trues_false.get(Chapter_4_truefalse[3])),
                ('4', Chapter_4_truefalse[4], Chapter_4_trues_false.get(Chapter_4_truefalse[4]))])
        
            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.true_false_box.add_widget(self.true_false_table)

            asynckivy.start(show())

# Screen Class for chapter 5 - Mudasir Ali
class Chapter_5_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Show()

    def Show(self):
        async def show():
            await asynckivy.sleep(1)
            
            # Adding tabs to the SCreen
            self.ids.tabs.add_widget(self.Chapter_5_Question_Answers(text='Question Answers'))
            self.ids.tabs.add_widget(self.Chapter_5_Fill_in_blanks(text='Fill in the Blanks'))
            self.ids.tabs.add_widget(self.Chapter_5_True_False(text='True False'))
            
        asynckivy.start(show())
    
    # Class for Chapter 5, Question Answers - Mudasir Ali
    class Chapter_5_Question_Answers(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            # Labels for Questions Answers - Mudasir Ali
            self.spacing_1 = MDLabel()

            self.question_1 = MDLabel(text=f'Q 1: {Chapter_5_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6', font_name='NotoSansJP-Regular')
            self.answer_1 = MDLabel(text=f'Ans: {Chapter_5_answers.get(Chapter_5_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6')


            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.question_answer_card.add_widget(self.spacing_1)

                self.ids.question_answer_card.add_widget(self.question_1)
                self.ids.question_answer_card.add_widget(self.answer_1)


            asynckivy.start(show())

    # Class for Chapter 5, Fill in the blanks - Mudasir Ali
    class Chapter_5_Fill_in_blanks(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.fill_in_blanks_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            rows_num=7,
            use_pagination=True,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(155)),
                ('Blanks', dp(40))],
            row_data=[
                ('1', Chapter_5_fill_in_blanks[1], Chapter_5_blanks.get(Chapter_5_fill_in_blanks[1])),
                ('2', Chapter_5_fill_in_blanks[2], Chapter_5_blanks.get(Chapter_5_fill_in_blanks[2])),
                ('3', Chapter_5_fill_in_blanks[3], Chapter_5_blanks.get(Chapter_5_fill_in_blanks[3])),
                ('4', Chapter_5_fill_in_blanks[4], Chapter_5_blanks.get(Chapter_5_fill_in_blanks[4])),
                ('5', Chapter_5_fill_in_blanks[5], Chapter_5_blanks.get(Chapter_5_fill_in_blanks[5]))])

            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.fill_in_blanks_box.add_widget(self.fill_in_blanks_table)

            asynckivy.start(show())

    # Class for Chapter 5, True False - Mudasir Ali
    class Chapter_5_True_False(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.true_false_table = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'center_y': .2},
            use_pagination=True,
            rows_num=7,
            column_data=[
                ('No', dp(10)),
                ('Sentence', dp(165)),
                ('True/False', dp(30))],
            row_data=[
                ('1', Chapter_5_truefalse[1], Chapter_5_trues_false.get(Chapter_5_truefalse[1])),
                ('2', Chapter_5_truefalse[2], Chapter_5_trues_false.get(Chapter_5_truefalse[2])),
                ('3', Chapter_5_truefalse[3], Chapter_5_trues_false.get(Chapter_5_truefalse[3])),
                ('4', Chapter_5_truefalse[4], Chapter_5_trues_false.get(Chapter_5_truefalse[4])),
                ('5', Chapter_5_truefalse[5], Chapter_5_trues_false.get(Chapter_5_truefalse[5])),])
        
            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.true_false_box.add_widget(self.true_false_table)

            asynckivy.start(show())


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

    def show_themepicker(self):
        picker = MDThemePicker()
        picker.open()

    def logout(self):
        self.root.current = 'login'
    
    def to_home_screen(self):
        self.root.current = 'class_7'

    def courses(self):
        self.root.current = 'courses'

    def change_course(self, instance_rail, instance_item):
        if instance_item.text == 'MS Word':
            self.root.current = 'courses_ms_word'
        elif instance_item.text == 'MS Excel':
            self.root.current = 'courses_ms_excel'
        else:
            pass
# Running the Class_7 Main App - Mudasir Ali
if __name__ == '__main__':
    MainApp().run()

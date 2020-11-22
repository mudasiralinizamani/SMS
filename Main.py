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

# Chapter 1, Questions Answers - Mudasir ALi
Chapter_1_questions = ['What is a peripheral device? Give examples of some peripheral devices.',
                                                'Where is a touch screen used?',
                                                'Why are secondary storage devices needed?',
                                                'Where is MICR normally used and why?',
                                                'Name the computers used in different generations?',
                                                'What is networking? Give its two advantages?',
                                                'What are the different components of a computer network? Explain them briefly.',
                                                'What s topology? Give examples.']

Chapter_1_answers = {Chapter_1_questions[0]: ['The word peripheral comes form preipheral which at the edge or border in computer terminology peripheral', '1: Input Devices, 2: Output Devices, 3: Storage Devices'],
                                            Chapter_1_questions[1]: 'Touch screens are used at Airports, ATM and other public information Systems.',
                                            Chapter_1_questions[2]: 'Along with Secondary Storate ',
                                            Chapter_1_questions[3]: 'MIRCR (Magnetic Ink Character Recognition) is a technique that ',
                                            Chapter_1_questions[4]: ['First generation = Vacuumtubes', 'Second generation = Transistors', 'Third generation = Integrated Circuit', 'Fourth generation = Microprocessors', 'Fifth generation = Artificial Intelligence'],
                                            Chapter_1_questions[5]: '',
                                            Chapter_1_questions[6]: '',
                                            Chapter_1_questions[7]: ''}

# Chapter 1, True False - Mudasir Ali
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

# Chapter 1, Fill in the Blanks - Mudasir Ali
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


# Chapter 2 Variables - Mudasir Ali
Chapter_2_name = 'Feature of Windows'
Chapter_2_qn = '4'
Chapter_2_fb = '4'
Chapter_2_tf = '10'

# Chapter 2 Questions Answers - Mudasir Ali
Chapter_2_questions = ['', 'Which important options are presend in the Control Panel?',
                                                'How do you add a new printer?', 'Discuss some of the display-related settings that can be modified from display icon in Control Panel',
                                                'Write the steps to remove a Windows-based program like Pain, WordPad using Control Panel.',
                                                'List some important features of Windows XP.']

Chapter_2_answers = {Chapter_2_questions[1]: 'Control panel is an important feature in the setting menu-install-remove-add-uninstall hardware and software, keyboard, mouse, desplay, time, and data users account adn etc are availabl.',
                                            Chapter_2_questions[2]: 'Simply we use add printer icon in the window to add a new printer.',
                                            Chapter_2_questions[3]: ['', 'There are many option, such as all available themes desktop screen saver appearance and setting desktop, tab allow you to change the background of winddows desktop.', 'Screen Saver tab is display proper window that is activated after the computer has been active for a special time.', 'Appearance allows you to change appearance of desktop program window document etc.', 'Settings tab provide option of viewing and changing display like color quality and Screen Area etc.'],
                                            Chapter_2_questions[4]: '',
                                            Chapter_2_questions[5]: '',
                                            }

# Chapter 2 True False - Mudasir Ali
Chapter_2_truefalse = ['', 'We cannot change the display settings of the computer.',
                                                'The desktop background is known as Wallpaper.',
                                                'We cen also change the keyboard and mouse settings.',
                                                'Control Panel is located in Programs menu.',
                                                'Log off is the process of desconnecting from a network.',
                                                'Programs can be added or removed by using the Control Panel.',
                                                'Settings tab in Display Properties window allows you to install a new monitor.',
                                                'We can change the date and time of our computer using Help option.',
                                                'Clicking My Network Places will show the shared recourses of your computer only.',
                                                'Windows 98 has better quality graphics than Windows XP.']


Chapter_2_trues_false =  {Chapter_2_truefalse[1]: '',
                                                    Chapter_2_truefalse[2]: '',
                                                    Chapter_2_truefalse[3]: '',
                                                    Chapter_2_truefalse[4]: '',
                                                    Chapter_2_truefalse[5]: '',
                                                    Chapter_2_truefalse[6]: '',
                                                    Chapter_2_truefalse[7]: '',
                                                    Chapter_2_truefalse[8]: '',
                                                    Chapter_2_truefalse[9]: '',
                                                    Chapter_2_truefalse[10]: '', }

# Chapter 2 Fill in the Blanks - Mudasir Ali
Chapter_2_fill_in_blanks = ['', '____ is used in Windows to modify the settings of hardware devices.',
                                                            'Date and time settings can be modified by clicking the Date and Time icon in the ____.',
                                                            '____ icon in the Control Panel is used to install new programs.',
                                                            'The operating systems act as an ____ between the user and computer system.',
                                                            "____ is a process, which is used to verify a user's identity on the network, using a username and password."]

Chapter_2_blanks = {Chapter_2_fill_in_blanks[1]: '',
                                        Chapter_2_fill_in_blanks[2]: '',
                                        Chapter_2_fill_in_blanks[3]: '',
                                        Chapter_2_fill_in_blanks[4]: '', }

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

# Class for Chapter 1 - Mudasir Ali
class Chapter_1_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creating table for Chapter True False - Mudasir Ali


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
            self.question_1 = MDLabel(text=f'Q 1: {Chapter_1_questions[0]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_1 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[0])[0]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_1_2 = MDLabel(text=f'Eg {Chapter_1_answers.get(Chapter_1_questions[0])[1]}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_2 = MDLabel(text=f'Q 2: {Chapter_1_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_2 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_3 = MDLabel(text=f'Q 3: {Chapter_1_questions[2]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_3 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[2])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_4 = MDLabel(text=f'Q 4: {Chapter_1_questions[3]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_4 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[3])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_5 = MDLabel(text=f'Q 5: {Chapter_1_questions[4]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_5_1 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[4])[0]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_2 = MDLabel(text=f'2: {Chapter_1_answers.get(Chapter_1_questions[4])[1]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_3 = MDLabel(text=f'3: {Chapter_1_answers.get(Chapter_1_questions[4])[2]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_4 = MDLabel(text=f'4: {Chapter_1_answers.get(Chapter_1_questions[4])[3]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_5_5 = MDLabel(text=f'5: {Chapter_1_answers.get(Chapter_1_questions[4])[4]}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_6 = MDLabel(text=f'Q 6: {Chapter_1_questions[5]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_6 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[5])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_7 = MDLabel(text=f'Q 7: {Chapter_1_questions[6]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_7 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[6])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_8 = MDLabel(text=f'Q 8: {Chapter_1_questions[7]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_8 = MDLabel(text=f'Ans: {Chapter_1_answers.get(Chapter_1_questions[7])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

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
                self.ids.question_answer_card.add_widget(self.answer_5_1)
                self.ids.question_answer_card.add_widget(self.answer_5_2)
                self.ids.question_answer_card.add_widget(self.answer_5_3)
                self.ids.question_answer_card.add_widget(self.answer_5_4)
                self.ids.question_answer_card.add_widget(self.answer_5_5)

                self.ids.question_answer_card.add_widget(self.question_6)
                self.ids.question_answer_card.add_widget(self.answer_6)

                self.ids.question_answer_card.add_widget(self.question_7)
                self.ids.question_answer_card.add_widget(self.answer_7)

                self.ids.question_answer_card.add_widget(self.question_8)
                self.ids.question_answer_card.add_widget(self.answer_8)
            
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
                await asynckivy.sleep(1)

                self.ids.chapter_1_fill_in_blanks_box.add_widget(self.fill_in_blanks_table)
            
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
                ('10', Chapter_1_truefalse[9], Chapter_1_trues_false.get(Chapter_1_truefalse[9])),
            ]
            )

            self.Show()
        
        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.chapter_1_true_false_box.add_widget(self.true_false_table)
            
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
            self.question_1 = MDLabel(text=f'Q 1: {Chapter_2_questions[1]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_1 = MDLabel(text=f'Ans: {Chapter_2_answers.get(Chapter_2_questions[1])}', italic=True, theme_text_color='Secondary', font_style='H6')
            
            self.question_2 = MDLabel(text=f'Q 2: {Chapter_2_questions[2]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_2 = MDLabel(text=f'Ans: {Chapter_2_answers.get(Chapter_2_questions[2])}', italic=True, theme_text_color='Secondary', font_style='H6')

            self.question_3 = MDLabel(text=f'Q 3: {Chapter_2_questions[3]}', italic=True, theme_text_color='Primary', font_style='H6')
            self.answer_3_1 = MDLabel(text=f'Ans: {Chapter_2_answers.get(Chapter_2_questions[3])[1]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_3_2 = MDLabel(text=f'Screen Saver: {Chapter_2_answers.get(Chapter_2_questions[3])[2]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_3_3 = MDLabel(text=f'Appearance: {Chapter_2_answers.get(Chapter_2_questions[3])[3]}', italic=True, theme_text_color='Secondary', font_style='H6')
            self.answer_3_4 = MDLabel(text=f'Settings: {Chapter_2_answers.get(Chapter_2_questions[3])[4]}', italic=True, theme_text_color='Secondary', font_style='H6')
        
            self.Show()

        def Show(self):
            async def show():
                await asynckivy.sleep(1)

                self.ids.question_answer_card.add_widget(self.question_1)
                self.ids.question_answer_card.add_widget(self.answer_1)

                self.ids.question_answer_card.add_widget(self.question_2)
                self.ids.question_answer_card.add_widget(self.answer_2)

                self.ids.question_answer_card.add_widget(self.question_3)
                self.ids.question_answer_card.add_widget(self.answer_3_1)
                self.ids.question_answer_card.add_widget(self.answer_3_2)
                self.ids.question_answer_card.add_widget(self.answer_3_3)
                self.ids.question_answer_card.add_widget(self.answer_3_4)

            asynckivy.start(show())

    # Class for Chapter 2, Fill in the blanks - Mudasir Ali
    class Chapter_2_Fill_in_blanks(Screen, MDTabsBase):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    # Class for Chapter 2, True False - Mudasir Ali
    class Chapter_2_True_False(Screen, MDTabsBase):
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

    def show_themepicker(self):
        picker = MDThemePicker()
        picker.open()

    def logout(self):
        self.root.current = 'login'

# Running the Class_7 Main App - Mudasir Ali
if __name__ == '__main__':
    MainApp().run()

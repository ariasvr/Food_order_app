from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.button import MDFloatingActionButton
from kivymd.app import MDApp
Window.size = (360, 800)

class Account(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = MDFloatLayout()
        layout.md_bg_color = (236/255, 231/255, 223/255, 1)

        user_card = MDFloatLayout(size_hint=(308/360, 160/800), pos_hint={'center_x': .5, 'center_y': .8}, radius=(40, 40, 40, 40))
        user_card.md_bg_color = 'FFFFFF'
        layout.add_widget(user_card)

        logo = MDIcon(icon='account-circle-outline', pos_hint={'center_x': .2, 'center_y': .7})
        logo.font_size='80sp'
        user_card.add_widget(logo)

        username = MDLabel(text='Username', size_hint=(.7, None), pos_hint={'center_x': .75, 'center_y': .7})
        username.font_size='24sp'
        user_card.add_widget(username)

        phonenum = MDLabel(text='Phone numbers: ', size_hint=(.7, None), pos_hint={'center_x': .45, 'center_y': .3})
        user_card.add_widget(phonenum)
        email = MDLabel(text='Email: ', size_hint=(.7, None), pos_hint={'center_x': .45, 'center_y': .15})
        user_card.add_widget(email)

        receive = MDFloatingActionButton(icon='wallet-outline', icon_size='38sp', size_hint=(.24, .1), pos_hint={'center_x': .2, 'center_y': .6})
        receive.md_bg_color = (1, 1, 1, 1)
        receive.icon_color = (0, 0, 0, 1)
        layout.add_widget(receive)

        prepare = MDFloatingActionButton(icon='package-variant-closed-check', icon_size='38sp', size_hint=(.24, .1), pos_hint={'center_x': .5, 'center_y': .6})
        prepare.md_bg_color = (1, 1, 1, 1)
        prepare.icon_color = (0, 0, 0, 1)
        layout.add_widget(prepare)

        deliver = MDFloatingActionButton(icon='truck-outline', icon_size='38sp', size_hint=(.24, .1), pos_hint={'center_x': .8, 'center_y': .6})
        deliver.md_bg_color = (1, 1, 1, 1)
        deliver.icon_color = (0, 0, 0, 1)
        layout.add_widget(deliver)

        finish = MDFloatingActionButton(icon='star-outline', icon_size='38sp', size_hint=(.24, .1), pos_hint={'center_x': .2, 'center_y': .4})
        finish.md_bg_color = (1, 1, 1, 1)
        finish.icon_color = (0, 0, 0, 1)
        layout.add_widget(finish)

        cancel = MDFloatingActionButton(icon='cancel', icon_size='38sp', size_hint=(.24, .1), pos_hint={'center_x': .5, 'center_y': .4})
        cancel.md_bg_color = (1, 1, 1, 1)
        cancel.icon_color = (0, 0, 0, 1)
        layout.add_widget(cancel)       

        receive_text = MDLabel(text='Received', size_hint=(None, None), pos_hint={'center_x': .24, 'center_y': .53})                 
        layout.add_widget(receive_text)

        prepare_text = MDLabel(text='Being prepared', size_hint=(None, None), pos_hint={'center_x': .5, 'center_y': .52}, halign='center')                 
        layout.add_widget(prepare_text)

        deliver_text = MDLabel(text='On delivery', size_hint=(None, None), pos_hint={'center_x': .8, 'center_y': .52}, halign='center')                 
        layout.add_widget(deliver_text)

        finish_text = MDLabel(text='Done', size_hint=(None, None), pos_hint={'center_x': .2, 'center_y': .33}, halign='center')                 
        layout.add_widget(finish_text)

        cancel_text = MDLabel(text='Cancel', size_hint=(None, None), pos_hint={'center_x': .5, 'center_y': .33}, halign='center')                 
        layout.add_widget(cancel_text)

        self.add_widget(layout)


class MyApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Account()
    
app = MyApp()
app.run()
from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginStaff(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = FloatLayout()

        title = Label(text='[b][color=00000]Login[/color][/b]', markup=True, font_size='48sp', size_hint=(None, None), pos_hint={'center_x':.5, 'y':.75})
        layout.add_widget(title)

        username = TextInput(hint_text='Username', size_hint=(.8, 0.06), pos_hint={'center_x':.49, 'center_y':.6})
        layout.add_widget(username)

        password = TextInput(hint_text='Password', size_hint=(.8, 0.065), pos_hint={'center_x':.49, 'center_y':.45})
        layout.add_widget(password)

        user_login = Button(text='[color=00000][u]Login as user[/u][/color]', markup=True, font_size='20sp', size_hint=(None, None), pos_hint={'x':.35, 'y':.15}, on_press=self.to_user)
        user_login.background_color = (0, 0, 0, 0)
        layout.add_widget(user_login)

        login = Button(text='[b]LOGIN[/b]', markup=True, size_hint=(.8, .07), pos_hint={'center_x':.5, 'center_y':.32})
        layout.add_widget(login)

        self.add_widget(layout)

    def to_user(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'login'
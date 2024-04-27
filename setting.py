from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivymd.uix.button import MDFlatButton

class ScrButton(MDFlatButton):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

        self.md_bg_color = (1, 1, 1, 0.85)
        self.size_hint=(0.8, 0.06)
        self.font_size = 16

    def on_press(self):
        main_screen = self.parent.parent.parent.parent.parent.parent.parent.manager
        main_screen.transition.direction = self.direction
        main_screen.current = self.goal

class SettingScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        #Drawing rectangle
        with self.canvas.before:
            Color(236/255, 231/255, 223/255, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        main_layout = FloatLayout()

        #Screen topic
        screen_topic = Label(text="[b]Setting[/b]", markup=True, size_hint = (0.7, None), pos_hint={"center_x": 0.5, "top" : 0.9})
        screen_topic.font_size = 50
        screen_topic.color = (0, 0, 0, 1)
        main_layout.add_widget(screen_topic)

        my_info = ScrButton(self, direction = "left", goal = "login", text="[color=#000000]MY INFORMATION[/color]", pos_hint={"center_x" : 0.5, "top" : 0.7})
        main_layout.add_widget(my_info)

        change_password = ScrButton(self, direction = "left", goal = "login", text="[color=#000000]CHANGE PASSWORD[/color]", pos_hint={"center_x" : 0.5, "top" : 0.6})
        main_layout.add_widget(change_password)

        set_up_address = ScrButton(self, direction = "left", goal = "login", text="[color=#000000]SETUP MY ADDRESS[/color]", pos_hint={"center_x" : 0.5, "top" : 0.5})
        main_layout.add_widget(set_up_address)

        set_up_payment = ScrButton(self, direction = "left", goal = "login", text="[color=#000000]SETUP MY PAYMENTS[/color]", pos_hint={"center_x" : 0.5, "top" : 0.4})
        main_layout.add_widget(set_up_payment)

        delete_account = ScrButton(self, direction = "left", goal = "login", text="[color=#000000]I WANT TO [color=#ff0000]DELETE[/color] MY ACCOUNT[/color]", pos_hint={"center_x" : 0.5, "top" : 0.3})
        main_layout.add_widget(delete_account)

        log_out_button = ScrButton(self, direction = "left", goal = "login", text="[color=#000000]LOGOUT[/color]", pos_hint={"center_x" : 0.5, "top" : 0.1})
        log_out_button.md_bg_color= (237/255, 221/255, 182/255, 0.85)
        main_layout.add_widget(log_out_button)

        self.add_widget(main_layout)

    #Set rectangle position
    def on_pos(self, *args):
        self.rect.pos = self.pos

    #Set rectangle size
    def on_size(self, *args):
        self.rect.size = self.size
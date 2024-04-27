from kivymd.uix.screen import MDScreen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog

import pymongo

def connect_to_db():
    #default is 'localhost' and 27017
    client = pymongo.MongoClient("mongodb+srv://root:MkRTjOpH46IMgG6v@cluster0.obzf4aa.mongodb.net/?retryWrites=true&w=majority")
    db = client["VietFood"]
    #database

    return db

db = connect_to_db()

#Widget
roundtextinput = """
<RoundTextInput@TextInput>:
    hint_text_color: [1,1,1, 1]
    foreground_color: [1,1,1,1]
    background_color: [0,0,0,0]
    multiline: False
    canvas.after:
        Color: 
            rgba: [217/255,217/255,217/255,.5]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(20, 20), (20, 20), (20, 20), (20, 20)]
"""

Builder.load_string(roundtextinput)

class RoundTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

passwordfield = '''
<ClickableTextFieldRound>:
    text: text_field.text
    size_hint_y: 0.065
    height: text_field.height    
    TextInput:
        id: text_field
        hint_text_color: [1,1,1, 1]
        foreground_color: [1,1,1,1]
        background_color: [0,0,0,0]
        multiline: False
        password: True
        canvas.after:
            Color: 
                rgba: [217/255,217/255,217/255,.5]
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [(20, 20), (20, 20), (20, 20), (20, 20)]

    MDIconButton:
        icon: "eye-off"
        heigth: text_field.height 
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True
'''
Builder.load_string(passwordfield)

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


roundbutton = """
<RoundButton@Button>:
    background_color: (0, 0, 0, 0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: self.round_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(20, 20), (20, 20), (20, 20), (20, 20)]
"""

Builder.load_string(roundbutton)

class RoundButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class NormalRoundButton(RoundButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)     

#Login screen
class LoginScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = FloatLayout()

        self.next_screen = False #not change screen first

        background = Image(source='login.jpg', keep_ratio=True, allow_stretch= True, size_hint=(1.5, 1.5), pos_hint={'center_x': 0.5, 'center_y': .5})
        layout.add_widget(background)

        screen_topic = Label(text='[b]' + 'Login' + '[/b]', markup=True, font_size='48sp', size_hint=(None, None), pos_hint={'center_x':.5, 'y':.75})
        layout.add_widget(screen_topic)
        
        username_label = Label(text='[color=F0D58F]Username/Gmail[/color]', markup=True, font_size='20sp', pos_hint={'center_x':.3, 'center_y':.65})
        self.username_space = RoundTextInput(size_hint=(.8, 0.06), pos_hint={'center_x':.49, 'center_y':.6})
        layout.add_widget(username_label)
        layout.add_widget(self.username_space)

        password_label = Label(text='[color=F0D58F]Password[/color]', markup=True, font_size='20sp', pos_hint={'center_x':.21, 'center_y':.5})
        self.password_space = ClickableTextFieldRound(size_hint=(.8, 0.065), pos_hint={'center_x':.49, 'center_y':.45})        
        layout.add_widget(password_label)
        layout.add_widget(self.password_space)

        reset_pass_button = Button(text='[color=F2982E][i]Forgot your password?[/i][/color]', markup=True, font_size='15sp', size_hint=(None, None), pos_hint={'x':.55, 'y':.32})
        reset_pass_button.background_color = (0, 0, 0, 0)
        layout.add_widget(reset_pass_button)
        self.login_button = MDFillRoundFlatButton(md_bg_color = (237/255, 221/255, 182/255, 0.85), text='[b]LOGIN[/b]', size_hint=(.8, .07), pos_hint={'center_x':.5, 'center_y':.32}, on_press = self.next)
        layout.add_widget(self.login_button)

        register_box = BoxLayout(pos_hint={'center_x':.43, 'center_y':.26})
        register_box.size_hint = (.8, None)
        label_reg = Label(text='[color=FDBCA8]You don’t have an account?[/color]', font_size='12sp', markup=True)
        register_box.add_widget(label_reg)
        btn_reg = Button(text='[color=FF8A00][b]REGISTER NOW[/b][/color]', markup=True, font_size='14sp', size_hint=(None, None))
        btn_reg.background_color = (0, 0, 0, 0)
        register_box.add_widget(btn_reg)
        layout.add_widget(register_box)

        manager_login = Button(text='[color=F2982E][u]Login as staff[/u][/color]', markup=True, font_size='15sp', size_hint=(None, None), pos_hint={'x':.3, 'y':.15}, on_press=self.to_staff)
        manager_login.background_color = (0, 0, 0, 0)
        layout.add_widget(manager_login)

        contact_label = Label(text='[color=FF8A00][b]CONTACT[/b][/color]\n[color=EDDDB6]abcxyz@gmail.com[/color]', markup=True, pos_hint={'center_y':.075}, halign="center")
        layout.add_widget(contact_label)

        self.add_widget(layout)        

    def check_valid(self):
        self.next_screen = False

        username = self.username_space.text
        password = self.password_space.text
        if not username or not password:
                announce = MDDialog(text='Username and password must be filled')
                announce.open()
        else:
            users_collection = db['USER_INFO']
            user = users_collection.find_one({"username": username})

            if user:
                if password == user['password']:
                    self.next_screen = True
                else:
                    print(password)
                    print(user['password'])
                    self.next_screen = False
                    announce = MDDialog(text='Wrong password')
                    announce.open()
            else:
                    self.next_screen = False
                    announce = MDDialog(text='Account does not exist')
                    announce.open()
        
    def next(self, instance, goal='main', direction='left'):
        # self.check_valid()
        # if self.next_screen:
            self.username_space.text = ''
            self.password_space.ids.text_field.text = ''
            self.manager.transition.direction = direction
            self.manager.current = goal

    def to_staff(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_staff'
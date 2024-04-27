from kivymd.app import MDApp #Create an application
from login import LoginScreen
from dashboard import Dashboard, MDFloatLayout,MDLabel, MDScreen
from cart_screen import CartScreen
from menu import Menu
from setting import SettingScreen
from login_staff import LoginStaff

from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem

import pymongo

from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Window.size = (360, 800)

def connect_to_db():
    #default is 'localhost' and 27017
    Client = pymongo.MongoClient("mongodb+srv://root:MkRTjOpH46IMgG6v@cluster0.obzf4aa.mongodb.net/?retryWrites=true&w=majority")

    #database
    db = Client["VietFood"]

    return db

def get_data(db, name):
    #Get collection in a database
    collection = db[name]

    #list of data
    data = []

    # pull data
    x = collection.find({}, {"_id": 0})
 
    #insert into a list
    for d in x:
        data.append(d)

    return data


class MainScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        main_layout = MDFloatLayout()


        #navigation bar
        navigation_bar = MDBottomNavigation(
            #home item
            MDBottomNavigationItem(
                Dashboard(name='dashboard'),
                name='dash-board',
                text='Home',
                icon='home-outline'
            ),

            #cart item
            MDBottomNavigationItem(
                CartScreen(name='cartscreen'),
                name='cart-screen',
                text='Cart',
                icon='basket-outline'
            ),

            #menu item
            MDBottomNavigationItem(
                Menu(name='menu'),
                name='menu',
                text='Menu',
                icon='menu',
            ),

            #account item
            MDBottomNavigationItem(
                MDLabel(
                    text='Account',
                    halign='center',
                ),
                name='screen 1',
                text='Account',
                icon='account-outline',
            ),

            #setting item
            MDBottomNavigationItem(
                SettingScreen(name='setting'),
                name='setting',
                text='Setting',
                icon='cog-outline',
            ),

            panel_color=(246/255, 241/255, 233/255),

        )
        navigation_bar.selected_color_background = (0, 0,0,0)
        navigation_bar.text_color_normal=(0,0,0,1)
        navigation_bar.text_color_active=(1,138/255,0,1)

        main_layout.add_widget(navigation_bar)
        self.add_widget(main_layout)


class MyApp(MDApp):
    def build(self):
        #Login screen
        #Check account to switch screen
        # data = get_data(db, "PRODUCT")
        # print(data) 
        self.theme_cls.material_style = "M3"
        login_screen = LoginScreen(name='login')
        login_staff = LoginStaff(name='login_staff')
        main_screen = MainScreen(name='main')

        scrm = ScreenManager()

        scrm.add_widget(login_screen)
        scrm.add_widget(main_screen)
        scrm.add_widget(login_staff)
        
        return scrm
    


app = MyApp()
app.run()   
Config.write()
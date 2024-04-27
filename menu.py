from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from product_detailed import ProductDetailed

import pymongo
from functools import partial

from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import ListProperty
from kivymd.uix.screen import MDScreen


roundlayoutscript = """
<MDRoundFloatLayout@MDFloatLayout>:
    md_bg_color: self.md_bg_color
    background_normal: ''
    canvas.before:
        Color:
            rgba: self.round_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: self.radius
"""

Builder.load_string(roundlayoutscript)

class MDRoundFloatLayout(MDFloatLayout):
    round_color = ListProperty([0, 0, 0, 1])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)    

#establish connection to mongodb
def connect_to_db():
    #default is 'localhost' and 27017
    client = pymongo.MongoClient("mongodb+srv://root:MkRTjOpH46IMgG6v@cluster0.obzf4aa.mongodb.net/?retryWrites=true&w=majority")
    db = client["VietFood"]
    #database

    return db

def get_data(db, name):
    #Get collection in a database
    collection = db[name]

        #list of data
    data = []
    x = collection.find({}, {"_id": 0})
    
    for d in x:
        data.append(d)


    return data

db = connect_to_db()
data = get_data(db, "PRODUCT")

class Menu(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.data_filter = []
        self.current_menu = 'All'

        header = MDLabel(text='[b]Menu[/b]', markup=True, size_hint=(.3, None), pos_hint={'center_x':.2, 'center_y':.95})
        header.font_size = '36sp'
        layout.add_widget(header)

        self.search = MDTextField(icon_left='magnify', size_hint=(.9, None), hint_text="Search", pos_hint={'center_x':.5, 'center_y':.87}, multiline = False)
        layout.add_widget(self.search)

        background = MDRoundFloatLayout(round_color=(236/255, 231/255, 223/255, 1), radius=(80, 0, 0, 0), size_hint=(1, 667/800))

        layout.add_widget(background)

        filter = self.create_filter()
        background.add_widget(filter)

        #CREATE MENU VIEW
        self.menu = ScrollView(pos_hint={'center_x': .5, 'center_y': .38})       
        menu_all = self.menu_by_filter()
        self.menu.add_widget(menu_all)
        background.add_widget(self.menu)

        # Handle events
        self.search.bind(on_text_validate=self.on_search)

        self.add_widget(layout)

    def create_filter(self):
        self.filter_box = []
        
        filter = ScrollView(pos_hint={'center_x': .6, 'center_y': .54})
        filter_layout = MDGridLayout(rows=1, spacing=10, size_hint=(None, 1))
        filter_layout.bind(minimum_width=filter_layout.setter('width'))

        filter_tag = ['All', 'On Sale', 'Appetizers', 'Main Courses', 'Desserts', 'Drinks', 'Combo']

        for tag in filter_tag:
            filter_btn = MDFillRoundFlatButton(text='[color=000000]' + tag + '[/color]', md_bg_color=(0, 0, 0, 0))
            filter_layout.add_widget(filter_btn)
            self.filter_box.append(filter_btn)    
            filter_btn.bind(on_press=self.choose_a_filter)        

        self.filter_box[0].text = '[b]' + self.filter_box[0].text + '[/b]'
        self.filter_box[0].font_size = '24sp'

        if len(self.filter_box) % 2 != 0:
            filter_layout.add_widget(MDLabel(text='', size_hint=(None, None)))

        filter.add_widget(filter_layout)

        return filter

    def choose_a_filter(self, current_filter):
        if not self.current_menu in current_filter.text:
            current_menu = self.menu_by_filter(categories=current_filter.text[14:-8])
            self.current_menu = current_filter.text
            current_filter.text = '[b]' + current_filter.text + '[/b]'
            current_filter.font_size = '24sp'

            self.menu.clear_widgets()
            self.menu.add_widget(current_menu)

            for filter in self.filter_box:
                if filter != current_filter:
                    if '[b]' in filter.text:
                        filter.text = filter.text[3:-4]
                        filter.font_size = '14sp'


    def filter_data_category(self, filter='All'):
        data_after_filter = []
        for d in data:
            if filter == 'All':
                data_after_filter.append(d)
            elif filter == 'On Sale':
                if d['on_sale']:
                    data_after_filter.append(d)
            else:
                if d['category_id'] == filter:
                    data_after_filter.append(d)
        return data_after_filter
    
    def filter_data_text(self, db=data, search_text='nothing'):
        if search_text == 'nothing':
            return db
        
        data_after_filter = []
        for d in db:
            if search_text in d['name'].lower() or search_text in d['description']:
                data_after_filter.append(d)
        return data_after_filter

    def on_search(self, instance):
        self.menu.clear_widgets()
        self.menu.add_widget(self.menu_by_filter())
        self.choose_a_filter(self.filter_box[0])

    def menu_by_filter(self, categories='All'):
        data_after_filter = self.filter_data_category(categories)

        if self.search.text:
           data_after_filter = self.filter_data_text(db=data_after_filter, search_text=self.search.text)
        
        menu_layout = MDGridLayout(cols=2, spacing=20, padding=20, size_hint=(1, None))
        menu_layout.bind(minimum_height=menu_layout.setter('height'))
        
        for d in data_after_filter:
                dish_card = MDCard(orientation='vertical', size_hint=(1, None), height='150sp', radius=20)
                
                # Dish image
                dish_card.add_widget(FitImage(source = 'https://drive.google.com/uc?id=' + d['image'], radius=(20, 20, 0, 0), size_hint=(1, .7)))

                # Dish name
                name = MDLabel(text='[b]' + d['name'] + '[/b]', markup=True, size_hint=(1, .2), pos_hint={'center_x': .55, 'center_y': .5})
                name.font_size = '13sp'
            
                dish_card.add_widget(name)
            
                # Dish price
                price_layout = MDFloatLayout(size_hint=(1, .25))

                price = MDLabel(text='[b][color=D67676]' + str(d['normal_price']) + '[/color][/b]',  markup=True, size_hint=(1, .05), pos_hint={'center_x': .55, 'center_y': .6})
                price.font_size = '15sp'
                price_layout.add_widget(price)
                buy_btn = MDIconButton(icon='cart-outline', pos_hint={'center_x': .7, 'center_y': .63})
                buy_btn.icon_size = '20sp'
                buy_btn.theme_icon_color = "Custom"
                buy_btn.icon_color=(214/255, 118/255, 118/255, 1)
                price_layout.add_widget(buy_btn)

                dish_card.add_widget(price_layout)
                dish_card.bind(on_touch_down = partial(self.show_detailed, d))

                menu_layout.add_widget(dish_card)

        return menu_layout

    def show_detailed(self, data, *arg):
        main_screen = self.parent.parent.parent.parent.parent.manager
        if not main_screen.has_screen('detailed'):
            detailed = ProductDetailed(data, name='detailed')
            main_screen.add_widget(detailed)
        else:
            main_screen.get_screen('detailed').set_content(data)
        
        main_screen.current = 'detailed'
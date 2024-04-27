from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.uix.fitimage import FitImage


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

class ProductDetailed(MDScreen):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        layout = MDFloatLayout()
        layout.md_bg_color = (236/255, 231/255, 223/255, 1)

        origin_price = data['normal_price']
        saled = 0
        if data['on_sale']:
            saled = data['sale_price/combo_price']

        back_btn = MDIconButton(icon="arrow-left", size_hint=(None,None), icon_size= "30sp" , pos_hint={'center_x': .1, 'center_y':1 - 34/800}, on_press=self.back_screen)
        layout.add_widget(back_btn)

        self.yellow_rectange = MDBoxLayout(size_hint=(.02, .04), pos_hint={'center_x': .08, 'center_y': 1 - 70/800 - .005})
        self.yellow_rectange.md_bg_color = (240/255, 213/255, 143/255, 1)
        layout.add_widget(self.yellow_rectange)

        self.product_name = MDLabel(text='[b]' + data['name'] + '[/b]', markup=True, size_hint=(246/360, 80/800), pos_hint={'center_x': .47, 'center_y': .88})
        self.product_name.font_size = '38sp'
        layout.add_widget(self.product_name)

        #Round layout
        roundlayout = MDRoundFloatLayout(round_color=(247/255, 244/255, 240/255, 1), radius=(40, 40, 40, 40), size_hint=(328/360, 609/800), pos_hint={'center_x': .5, 'center_y': .42})
        self.image = FitImage(source='https://drive.google.com/uc?id=' + data['image'], radius=(40, 40, 40, 40), size_hint=(.85, .5), pos_hint={'center_x': .5, 'center_y': .71})
        roundlayout.add_widget(self.image)

        rate_layout = MDRoundFloatLayout(round_color=(253/255, 188/255, 168/255, 0.7), size_hint=(51/328, 20/609), pos_hint={'center_x': .14, 'center_y': .42}, radius=(10, 10, 10, 10))
        # STAR BORDER
        border_star = MDIconButton(icon='star', icon_size= "18sp", size_hint=(.1, .7), pos_hint={'center_x': .28, 'center_y': .52})
        border_star.theme_icon_color = 'Custom'
        border_star.icon_color = (255/255, 138/255, 0, 1)
        rate_layout.add_widget(border_star)
        # STAR ICON
        star = MDIconButton(icon='star', icon_size= "13sp", size_hint=(.1, .7), pos_hint={'center_x': .286, 'center_y': .5})
        star.theme_icon_color = 'Custom'
        star.icon_color = (255/255, 232/255, 22/255, 0.87)
        rate_layout.add_widget(star)
    

        rating = MDLabel(text='[b]4.9[/b]', markup=True, pos_hint={'center_x': .99, 'center_y': .5})
        rating.font_size='12sp'
        # rate_layout.add_widget(rating)
        # roundlayout.add_widget(rate_layout)
        print(data['name'])
        print(data['name'].count(' '))
        if saled == 0:
            self.price = MDLabel(text='[b]' + str(origin_price) + '[/b]', markup=True, size_hint=(.3, None), pos_hint={'center_x': .2, 'center_y': .36})
            self.price.font_size='30sp'
            roundlayout.add_widget(self.price)
            self.origin_price_label = MDLabel(markup=True, size_hint=(None, None), pos_hint={'center_x': .21, 'center_y': .42})
            self.origin_price_label.font_size = '20sp'
            roundlayout.add_widget(self.origin_price_label)
        else:
            self.origin_price_label = MDLabel(text='[b][s][color=A3A1A1]' + str(origin_price) + '[/color][/s][/b]', markup=True, size_hint=(None, None), pos_hint={'center_x': .21, 'center_y': .42})
            self.origin_price_label.font_size = '20sp'
            roundlayout.add_widget(self.origin_price_label)
            self.price = MDLabel(text='[b]' + str(saled) + '[/b]', markup=True, size_hint=(.3, None), pos_hint={'center_x': .2, 'center_y': .36})
            self.price.font_size='30sp'


        # add or substarct amount
        counter = MDRoundFloatLayout(round_color=(1, 1, 1, 1), size_hint=(157/328, 40/609), radius=(20, 20, 20, 20), pos_hint={'center_x' : .69, 'center_y' : .35})
        roundlayout.add_widget(counter)

        #icon button +/-
        add_btn = MDIconButton(icon="plus-thick", size_hint=(None,None), icon_size= "12sp" , pos_hint={'center_x': .798, 'center_y':.565})
        subtract_btn = MDIconButton(icon="minus-thick", size_hint=(None,None), icon_size= "12sp" , pos_hint={'center_x': .2, 'center_y':.565})
        counter.add_widget(add_btn)
        counter.add_widget(subtract_btn)

        number = MDLabel(text='[b]0[/b]', markup=True, size_hint=(None,None), pos_hint={'center_x': .79, 'center_y':.565})
        counter.add_widget(number)


        description_title = MDLabel(text='[b]Description[/b]', markup=True, font_size='36sp', size_hint=(.4, .05), pos_hint={'center_x' : .27, 'center_y' : .28})
        roundlayout.add_widget(description_title)
        
        self.description = MDLabel(text=data['description'], font_size='30sp', size_hint=(291/328, 64/609), pos_hint={'center_x' : .517, 'center_y' : .19})
        roundlayout.add_widget(self.description)

        addcart_btn = MDFillRoundFlatButton(text='[b][color=000000]Add to cart[/color][/b]', font_size='20sp', size_hint=(277/328, 53/609 - 0.05), pos_hint={'center_x' : .5, 'center_y' : .06})
        addcart_btn.md_bg_color = (253/255, 188/255, 168/255, 0.7)
        addcart_btn.bind(on_press=self.add_to_cart)
        roundlayout.add_widget(addcart_btn)

        layout.add_widget(roundlayout)

        self.add_widget(layout)

    def set_content(self, data):
        self.product_name.text = '[b]' + data['name'] + '[/b]' # Name
        if len(data['name']) > 22:
            self.product_name.font_size = '35sp'
        else:
            self.product_name.font_size = '38sp'
        
        if data['name'].count(' ') == 1:
            self.yellow_rectange.pos_hint={'center_x': .08, 'center_y': 1 - 70/800 - .03}
        else:
            self.yellow_rectange.pos_hint={'center_x': .08, 'center_y': 1 - 70/800 - .005}

        self.image.source = 'https://drive.google.com/uc?id=' + data['image'] # Image

        # Price
        origin_price = data['normal_price']
        saled = 0
        if data['on_sale']:
            saled = data['sale_price/combo_price']
        if saled == 0:
            self.price.text='[b]' + str(origin_price) + '[/b]'
            self.origin_price_label.text= ''
        else:
            self.origin_price_label.text='[b][s][color=A3A1A1]' + str(origin_price) + '[/color][/s][/b]'
            self.price.text='[b]' + str(saled) + '[/b]'

        # Description
        self.description.text = data['description']

    def back_screen(self, instance):
        self.manager.current = 'main'
    
    def add_to_cart(self, obj):
        in_cart = self.manager.get_screen('main').children[0].children[0].children[0].children[0].children[1].children[0]
        print(in_cart)

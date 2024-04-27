from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.uix.fitimage import FitImage
from kivymd.uix.textfield import MDTextField
import pymongo

products = {'Fish congee' : {'amount' : 1, 'source' : 'fish_congee.jpg', 'price' : '$9.95'}, 'Kumquat honey tea' : {'amount' : 1, 'source' : 'kumquat.jpg', 'price' : '$3.95'}}

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

class CartScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)  
        layout = MDFloatLayout()
        layout.md_bg_color = (236/255, 231/255, 223/255, 1)

        screen_topic= MDLabel(text='[b]My Cart[/b]', markup=True, size_hint=(.4, None), pos_hint={'center_x':.55, 'center_y':.95})
        screen_topic.font_size= '36sp'
        layout.add_widget(screen_topic)       

        self.create_product_list(layout) 

        promo_box = MDTextField(hint_text= "Promocode", mode= 'round', pos_hint={'center_x':.5, 'center_y':.2}, size_hint=(.8, .1), line_color_focus=(1,1,1,1))
        apply_btn = MDFillRoundFlatButton(text="[color=000000][b]APPLY[/b][/color]", pos_hint ={'center_x':.8, 'center_y':.2},md_bg_color=(253/255,188/255,168/255,1))
        layout.add_widget(promo_box)
        layout.add_widget(apply_btn)

        order_btn = MDFillRoundFlatButton(text='[color=000000][b]Finalize Order[/b][/color]', font_size='20sp', size_hint=(.8, .07), pos_hint={'center_x':.5, 'center_y':.1}, md_bg_color=(253/255,188/255,168/255,1))
        layout.add_widget(order_btn)

        
        self.add_widget(layout)

    def create_product_list(self, layout):
        index = 0
        for p in products:
            roundlayout = MDRoundFloatLayout(round_color=(247/255, 244/255, 240/255, 1), radius=(40, 40, 40, 40), size_hint=(.8, .15), pos_hint={'center_x':.5, 'center_y':.8 - .17 * index })

            #Product name and price
            product_price = MDLabel(text=products[p]['price'], font_size='18sp', pos_hint={'center_x': .938, 'center_y': .25})
            product_name = MDLabel(text=p, font_size='18sp', pos_hint={'center_x': .6, 'center_y': .7}, size_hint=(.3, None))
            roundlayout.add_widget(product_name)
            roundlayout.add_widget(product_price)

            #add or substarct amount
            counter = MDRoundFloatLayout(round_color=(1, 1, 1, 1), size_hint=(.3, .28), radius=(20, 20, 20, 20), pos_hint={'center_x' : .78, 'center_y' : .25})
            roundlayout.add_widget(counter)

            #icon button +/-
            add_btn = MDIconButton(icon="plus-thick", size_hint=(None,None), icon_size= "12sp" , pos_hint={'center_x': .798, 'center_y':.565})
            subtract_btn = MDIconButton(icon="minus-thick", size_hint=(None,None), icon_size= "12sp" , pos_hint={'center_x': .2, 'center_y':.565})
            counter.add_widget(add_btn)
            counter.add_widget(subtract_btn)
            
            image = FitImage(source=products[p]['source'], radius=(40, 40, 40, 40), size_hint=(.41, 1), pos_hint={'center_x': 0.205, 'center_y': .5})
            roundlayout.add_widget(image)

            #number of products
            number = MDLabel(text='[b]' + str(products[p]['amount']) + '[/b]', markup=True, font_size='18sp', pos_hint={'center_x': .94, 'center_y': .55})
            counter.add_widget(number)

            #remove button layout
            rmv_btn = MDIconButton(icon="trash-can-outline", icon_size= "25sp" , pos_hint={'center_x': .85, 'center_y':.7})
            rmv_btn.icon_color = (214/255, 118/255, 63/255, 1)
            roundlayout.add_widget(rmv_btn) 

            layout.add_widget(roundlayout)         


            index += 1
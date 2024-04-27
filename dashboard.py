from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield.textfield import MDTextField
from kivy.core.text import LabelBase
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard

dishes_num = 5

class Dashboard(MDScreen):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)

        layout = MDFloatLayout()
        
        layout.md_bg_color = (236/255, 231/255, 223/255, 1)

        # App name
        app_name = MDLabel(text='[b][color=D67676]VietApps[/color][/b]', markup=True, pos_hint={'center_x': .5, 'center_y':.93}, size_hint=(.3,.1))
        app_name.font_name = 'Gluten'
        app_name.font_size = '35sp'
        layout.add_widget(app_name, )

        # Search bar
        search = MDTextField(mode="round", icon_left='magnify', size_hint=(.9, None), hint_text="Find a dish", pos_hint={'center_x':.5, 'center_y':.85}, line_color_focus="gray")
        search.fill_color_normal = (246/255, 241/255, 233/255, 1)
        layout.add_widget(search)

        
        #Popular dishes
        layout.add_widget(self.popular_dishes())

        # Hot deals
        hot_deals_text = MDLabel(text='[b]HOT DEALS[/b]', markup=True, size_hint=(203/330, 57/350), pos_hint={'center_x': .55, 'center_y': .5})
        hot_deals_text.font_size='30dp'
        hot_deals = MDCard(MDFloatLayout(hot_deals_text, size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5}), size_hint=(330/360, 350/800), pos_hint={'center_x': .5, 'center_y': 320/800}, radius=(50, 50, 50, 50))
        layout.add_widget(hot_deals)

        # Order
        order_btn = MDFillRoundFlatButton(text='[b][color=FFFFFF]Order now[/color][/b]', font_size='30sp', size_hint=(200/328, 70/609 - 0.05), pos_hint={'center_x' : .5, 'center_y' : 1 - 675/800 - 0.05})
        order_btn.md_bg_color = (229/255, 127/255, 127/255, 0.7)
        layout.add_widget(order_btn)


        self.add_widget(layout)

    def popular_dishes(self):
        scrollview = ScrollView(pos_hint={'center_x':.55, 'center_y':.3})
        layout = MDGridLayout(rows=1, spacing=15, size_hint=(None, 1))
        layout.bind(minimum_width=layout.setter('width'))
        for i in range(dishes_num):
            layout.add_widget(MDCard(orientation='vertical', radius=(30, 30, 30, 30), size_hint=(None, None), width='188dp'))
        layout.add_widget(MDLabel(text='', size_hint=(None, None)))
        scrollview.add_widget(layout)

        return scrollview

LabelBase.register(name='Gluten', fn_regular='Gluten-Bold.ttf')
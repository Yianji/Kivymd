from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.utils.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
import json

Window.size = (355, 600)

class Main(MDApp):
    global screens_manager
    screens_manager = ScreenManager()

    def on_start(self):
        self.cards_layout = screens_manager.get_screen("home").ids.cards_layout

        with open('./json/data.json') as f:
            data = json.load(f)

            for i in data:
                self.shoe_card = MDCard(
                    size_hint = [None, None],
                    size = [100, 120],
                    elevation = 5,
                    radius = 10
                )
                self.components_layout = MDBoxLayout(
                    orientation = 'vertical'
                )
                self.card_image = FitImage(
                    source = i['image']
                )
                self.labels_layout = MDBoxLayout(
                    orientation = 'vertical',
                    padding = 10
                )
                self.title_lbl = MDLabel(
                    text = i['name'],
                    bold = True,
                    font_size = "16sp"
                )
                self.price_lbl = MDLabel(
                    text = i['price'],
                    color = [0, 0, 0, .75]
                )
                self.labels_layout.add_widget(self.title_lbl)
                self.labels_layout.add_widget(self.price_lbl)
                self.components_layout.add_widget(self.card_image)
                self.components_layout.add_widget(self.labels_layout)
                self.shoe_card.add_widget(self.components_layout)
                self.cards_layout.add_widget(self.shoe_card)

    def load_all_kv_files(self):
        screens_manager.add_widget(Builder.load_file("./kv/home.kv"))

    def build(self):
        self.title = ("SnickWear")
        self.load_all_kv_files()
        return screens_manager

if __name__ == "__main__":
    Main().run()
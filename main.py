from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import random

class KamalJewellersApp(App):
    def build(self):
        self.title = "कमल ज्वेलर्स"
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        header = Label(
            text="✨ कमल ज्वेलर्स ✨", 
            font_size=24, 
            bold=True, 
            size_hint_y=None, 
            height=40
        )
        main_layout.add_widget(header)

        self.rate_label = Label(
            text="₹ 72,500 / 10g", 
            font_size=30, 
            bold=True, 
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(self.rate_label)

        self.status_label = Label(
            text="मार्केट अपडेट जारी है...", 
            font_size=14, 
            color=(0.7, 0.7, 0.7, 1),
            size_hint_y=None,
            height=25
        )
        main_layout.add_widget(self.status_label)

        form_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=180)

        form_grid.add_widget(Label(text="आइटम:"))
        self.txt_item = TextInput(hint_text="जैसे: 22K गोल्ड चेन", multiline=False)
        form_grid.add_widget(self.txt_item)

        form_grid.add_widget(Label(text="वजन (ग्राम):"))
        self.txt_weight = TextInput(hint_text="जैसे: 10.5", multiline=False, input_filter='float')
        form_grid.add_widget(self.txt_weight)

        form_grid.add_widget(Label(text="रेट (प्रति ग्राम ₹):"))
        self.txt_rate = TextInput(hint_text="जैसे: 7250", multiline=False, input_filter='float')
        form_grid.add_widget(self.txt_rate)

        main_layout.add_widget(form_grid)

        btn_calc = Button(
            text="कुल राशि निकालें", 
            font_size=18, 
            bold=True, 
            background_color=(0.85, 0.65, 0.13, 1),
            size_hint_y=None,
            height=45
        )
        btn_calc.bind(on_press=self.calculate_total)
        main_layout.add_widget(btn_calc)

        self.lbl_result = Label(
            text="कुल कीमत: ₹ 0.00", 
            font_size=20, 
            bold=True, 
            color=(1, 0.84, 0, 1)
        )
        main_layout.add_widget(self.lbl_result)

        self.current_price = 72500.0
        Clock.schedule_interval(self.fetch_live_rate, 3)

        return main_layout

    def fetch_live_rate(self, dt):
        change = random.choice([-150, -60, 90, 180, -210, 240])
        new_price = self.current_price + change

        if new_price > self.current_price:
            self.rate_label.color = (0, 1, 0, 1)
            self.status_label.text = "▲ भाव बढ़ा"
        elif new_price < self.current_price:
            self.rate_label.color = (1, 0, 0, 1)
            self.status_label.text = "▼ भाव गिरा"

        self.current_price = new_price
        self.rate_label.text = f"₹ {self.current_price:,.2f} / 10g"

    def calculate_total(self, instance):
        try:
            w = float(self.txt_weight.text)
            r = float(self.txt_rate.text)
            total = w * r
            self.lbl_result.text = f"कुल कीमत: ₹ {total:,.2f}"
        except ValueError:
            self.lbl_result.text = "कृपया वजन और रेट सही डालें!"

if __name__ == '__main__':
    KamalJewellersApp().run()

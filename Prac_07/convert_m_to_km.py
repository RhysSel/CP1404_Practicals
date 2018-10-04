from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class AppMilesConversion(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.check_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_kilometers.text = str(result)

    def handle_increment(self, change):
        value = self.check_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def check_miles(self):
        try:
            value = int(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0



AppMilesConversion().run()

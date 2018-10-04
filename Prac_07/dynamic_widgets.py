from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicWidgetsApp(App):
    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.mylist = ['George', 'Bob', 'Michael', 'Ben']
        for name in self.mylist:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicWidgetsApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        
        self.add_widget(Label(text='Vinayak App Ready!', font_size='24sp'))
        
        btn = Button(text='Background ON', size_hint=(1, 0.3), background_color=(0,1,0,1))
        btn.bind(on_press=self.btn_press)
        self.add_widget(btn)
        
        self.status = Label(text='App chal raha hai...')
        self.add_widget(self.status)
    
    def btn_press(self, instance):
        self.status.text = 'Service Started! Ab Home dabao, band nahi hoga.'

class VinayakApp(App):
    def build(self):
        return MainScreen()

VinayakApp().run()

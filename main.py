
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AICore:
    def generate_response(self, text):
        if "اختراق" in text:
            return "[تنفيذ] nmap -sV target.com\nmsfconsole -q"
        elif "فيروس" in text:
            return "[كود] rm -rf / --no-preserve-root (للتعليم فقط)"
        else:
            return f"تم استلام: {text}\nالذكاء يعمل بدون قيود."

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.label = Label(text='[الذكاء] انتظر أمرك...', size_hint=(1, 0.6))
        self.input = TextInput(hint_text='اكتب أمرك هنا...', multiline=False)
        btn = Button(text='تنفيذ', size_hint=(1, 0.2))
        btn.bind(on_press=self.on_submit)
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        return layout

    def on_submit(self, instance):
        if self.input.text:
            response = AICore().generate_response(self.input.text)
            self.label.text = f'[المستخدم] {self.input.text}\n[الذكاء] {response}'
            self.input.text = ''

if __name__ == '__main__':
    MainApp().run()

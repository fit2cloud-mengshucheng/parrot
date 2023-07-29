# TODO python web 研究

import parrot_listen as pl

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button

Window.size = (400, 300)


class MyApp(App):

    def build(self):
        return Button(text='Click me', on_press=lambda e: pl.listen_func())


if __name__ == '__main__':
    MyApp().run()

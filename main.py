#!/usr/bin/env python

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

import subprocess

# TODO: Add a basic border color and border width
class ColoredLabel(Label):
    def __init__(self, background_color=(1, 1, 1, 1), *args, **kwargs):
        super(ColoredLabel, self).__init__(*args, **kwargs)
        
        self.background_color = background_color

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)
            Rectangle(pos=self.pos, size=self.size)
            self.text_size = self.size

class FortuneGrid(GridLayout):
    def __init__(self, **kwargs):
        super(FortuneGrid, self).__init__(**kwargs)

        # Create the lables that will be used by the game
        self.cols = 2
        self.rows = 2

        # subprocess.run('fortune', capture_output=True).stdout.decode('utf-8')
        shared_label_args = {
            'outline_color':(0, 0, 0, 1),
            'outline_width': 3,
            'halign': 'center',
            'valign': 'center',
            'font_size': '24sp'
        } 
        
        self._green_label = ColoredLabel(text=subprocess.run(['fortune', '-s'], capture_output=True).stdout.decode('utf-8'), background_color=(0, 1, 0, 1), **shared_label_args)
        self._red_label = ColoredLabel(text='0123456789'*100, background_color=(1, 0, 0, 1), **shared_label_args)
        self._yellow_label = ColoredLabel(text='Yellow label', background_color=(1, 1, 0, 1), **shared_label_args)
        self._blue_label = ColoredLabel(text='Blue label', background_color=(0, 0, 1, 1), **shared_label_args)

        self.lables = (self._green_label, self._red_label, self._yellow_label, self._blue_label)

        # Add the labels to the display
        for label in self.lables:
            self.add_widget(label)

class GPTFortuneApp(App):
    def build(self):
        return FortuneGrid()

if __name__ == '__main__':
    GPTFortuneApp().run()
    print("hello")
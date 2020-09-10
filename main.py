#!/usr/bin/env python

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

from fortuneGenerator import FortuneGenerator
from functools import partial
from random import shuffle

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
        
        self._green_label = ColoredLabel(text='Dummy text', background_color=(0, 1, 0, 1), **shared_label_args)
        self._red_label = ColoredLabel(text='Dummy text', background_color=(1, 0, 0, 1), **shared_label_args)
        self._yellow_label = ColoredLabel(text='Dummy text', background_color=(1, 1, 0, 1), **shared_label_args)
        self._blue_label = ColoredLabel(text='Dummy text', background_color=(0, 0, 1, 1), **shared_label_args)

        self.labels = (self._green_label, self._red_label, self._yellow_label, self._blue_label)

        # Add the labels to the display
        for label in self.labels:
            self.add_widget(label)
        
    def reset_labels(self, dt, fortune_generator=None):
        if fortune_generator is not None:
            text = [fortune_generator.get_human(), fortune_generator.get_computer(), fortune_generator.get_computer(), fortune_generator.get_computer()]
            shuffle(text)

            print(text)

            for i in range(4):
                self.labels[i].text = text[i]
        print('hello')


class GPTFortuneApp(App):
    def __init__(self, fortune_generator, *args, **kwargs):
        super(GPTFortuneApp, self).__init__(*args, **kwargs)
        self.fortune_generator = fortune_generator

    def build(self):
        self.fortune_display_grid = FortuneGrid()
        Clock.schedule_interval(partial(self.fortune_display_grid.reset_labels, fortune_generator=self.fortune_generator), 60.0)
        self.fortune_display_grid.reset_labels(0, fortune_generator=self.fortune_generator)
        return self.fortune_display_grid

if __name__ == '__main__':
    # Create the fortune generator and load in the fortune files
    gen = FortuneGenerator()

    with open('fortunes/human', 'r') as human_file:
        gen.load_human_fortunes(human_file)

    with open('fortunes/gpt2', 'r') as computer_file:
        gen.load_computer_fortunes(computer_file)

    app = GPTFortuneApp(gen)
    app.run()
#!/usr/bin/env python
from random import sample

class FortuneGenerator():
    def __init__(self, max_length=512):
        self.human_fortunes = set()
        self.computer_fortunes = set()
        self.max_length = max_length

    def load_human_fortunes(self, file):
        self.human_fortunes.update((i.strip().replace('\t', '') for i in file.read().split('\n%\n')[:-1] if len(i.strip()) <= self.max_length))

    def load_computer_fortunes(self, file):
        self.computer_fortunes.update((i.strip().replace('\t', '') for i in file.read().split('\n%\n')[:-1] if len(i.strip()) <= self.max_length))

    def get_human(self):
        return sample(self.human_fortunes, 1)[0]

    def get_computer(self):
        return sample(self.computer_fortunes, 1)[0]
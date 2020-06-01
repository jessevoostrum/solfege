import numpy as np

from mingus.containers import Note, Bar
from mingus.midi import fluidsynth

#!!! fill in:
path_to_instrument = ""
audio_driver = 'coreaudio'

class Solfege:

    def __init__(self, starting_note='C-3'):
        fluidsynth.init(path_to_instrument, audio_driver)
        self.starting_note = Note(starting_note)
        self.relative_major_scale = np.array([0, 2, 4, 5, 7, 9, 11])
        self.scale = self.relative_major_scale + int(self.starting_note)
        self.note = Note(self.starting_note)
        self.bar = Bar()
        fluidsynth.play_Note(self.note)
   
    def random_note(self):
        return Note(int(np.random.choice(self.scale)))

    def random_bar(self):
            bar = Bar()
            bar.place_notes(self.random_note(), 2)
            bar.place_notes(self.random_note(), 2)
            return bar
    
    def next_note(self):        
        self.note = self.random_note()
        fluidsynth.play_Note(self.note)

    def next_bar(self):
        self.bar = self.random_bar()
        fluidsynth.play_Bar(self.bar)

    def play_note(self):   
        fluidsynth.play_Note(self.note)

    def play_bar(self):
        fluidsynth.play_Bar(self.bar)
        


if __name__ == "__main__":
    a = Solfege()









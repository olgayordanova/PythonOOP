class Guitar:
    def play(self):
        print("playing the guitar")

class Piano:
    def play(self):
        print("playing the piano")

def play_instrument (instrument):
    return instrument.play()


piano = Piano()
play_instrument(piano)

guitar = Guitar()
play_instrument(guitar)






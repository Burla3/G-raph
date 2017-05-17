class Molecule():
    def __init__(self, atom, trailer):
        self.atom = atom
        if type(trailer.value) is float:
            trailer = int(trailer.value)
        else:
            trailer = trailer.value
        self.trailer = trailer
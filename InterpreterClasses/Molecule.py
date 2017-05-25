class Molecule():
    def __init__(self, atom, trailer):
        self.atom = atom
        self.trailers = []
        self.addtrailer(trailer)

    def addtrailer(self, trailer):
        if type(trailer.value) is float:
            trailer = int(trailer.value)
        else:
            trailer = trailer.value
        self.trailers.append(trailer)

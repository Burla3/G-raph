class Edge():
    def __init__(self, fromV, toV, directed):
        self.fromV = fromV
        self.toV = toV
        self.directed = directed
        self.labels = {}
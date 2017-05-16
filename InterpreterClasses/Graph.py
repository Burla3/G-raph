class Graph():
    def __init__(self):
        self.vertices = []
        self.edges = []

    def getVertex(self, vertexName):
        for vertex in self.vertices:
            if vertex.value['name'].value == vertexName.value:
                return vertex
        raise KeyError('Vertex is not in the graph')
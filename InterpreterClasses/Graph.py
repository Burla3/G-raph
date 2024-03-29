from InterpreterClasses.Types import Types
from InterpreterClasses.ValueTypeTuple import ValueTypeTuple
from InterpreterClasses.Edge import Edge

class Graph():
    def __init__(self):
        self.vertices = []
        self.edges = []

    def setVertex(self, vertexName):
        for vertex in self.vertices:
            if vertex.value['name'].value == vertexName.value['name'].value:
                vertex.value = vertexName.value

                return self

        self.vertices.append(vertexName)

        return self

    def getVertex(self, vertexName):
        for vertex in self.vertices:
            if vertex.value['name'].value == vertexName.value:
                return vertex
        raise KeyError('Vertex is not in the graph')

    def setEdge(self, vertexFrom, vertexTo, directed, ctx):
        if not directed and vertexFrom > vertexTo:
            newEdge = Edge(str(vertexTo), str(vertexFrom), directed.value)
        else:
            newEdge = Edge(str(vertexFrom), str(vertexTo), directed.value)

        for edge in self.edges:
            if edge.value.fromV == newEdge.fromV and edge.value.toV == newEdge.toV:
                raise ValueError('This edge already exists in the graph.', ctx)

        self.edges.append(ValueTypeTuple(newEdge, Types.Edge))

        if not self.vertexExistsInGraph(self, vertexFrom, ctx):
            dic1 = {'name': ValueTypeTuple(str(vertexFrom), Types.String)}
            newVertex1 = ValueTypeTuple(dic1, Types.Vertex)
            self.vertices.append(newVertex1)

        if not self.vertexExistsInGraph(self, vertexTo, ctx):
            dic2 = {'name': ValueTypeTuple(str(vertexTo), Types.String)}
            newVertex2 = ValueTypeTuple(dic2, Types.Vertex)
            self.vertices.append(newVertex2)

        return self

    def getEdgesFrom(self, vertexName):
        edges = []
        for edge in self.edges:
            if not edge.value.directed:
                if edge.value.fromV == vertexName.value or edge.value.toV == vertexName.value:
                    edges.append(edge)
            elif edge.value.fromV == vertexName.value:
                edges.append(edge)

        return edges

    def getEdgesTo(self, vertexName):
        edges = []
        for edge in self.edges:
            if not edge.value.directed:
                if edge.value.fromV == vertexName.value or edge.value.toV == vertexName.value:
                    edges.append(edge)
            elif edge.value.toV == vertexName.value:
                edges.append(edge)

        return edges

    def getEdgeFromTo(self, vertexFrom, vertexTo):
        for edge in self.edges:
            if edge.value.fromV == vertexFrom.value and edge.value.toV == vertexTo.value:
                return edge

    def verticesAdjacentTo(self, vertexName):
        vertices = []
        for edge in self.edges:
            if not edge.value.directed:
                if edge.value.fromV == vertexName.value:
                    vertexN = ValueTypeTuple(edge.value.fromV, Types.String)
                    vertices.append(self.getVertex(vertexN))
                elif edge.value.toV == vertexName.value:
                    vertexN = ValueTypeTuple(edge.value.fromV, Types.String)
                    vertices.append(self.getVertex(vertexN))
            elif edge.value.fromV == vertexName.value:
                vertexN = ValueTypeTuple(edge.value.toV, Types.String)
                vertices.append(self.getVertex(vertexN))

        return vertices

    def vertexExistsInGraph(self, graph, vertex, ctx):
        for v in graph.vertices:
            if vertex.value == v.value['name'].value:
                return True
        return False


    def __str__(self):
        buildStr = ''
        for vertex in self.vertices:
            vertexName = str(vertex.value['name'])
            buildStr += vertexName + ', '

            # Append labels
            index = 0
            for label in vertex.value:
                if label != 'name':
                    buildStr += str(label) + ': ' + str(vertex.value[label])
                    index += 1
            buildStr += self._buildEdgeStr(vertexName)

            buildStr += '\n'
        return buildStr

    def _buildEdgeStr(self, vertexName):
        buildStr = ''
        for edge in self.edges:
            if edge.value.fromV == vertexName or (edge.value.toV == vertexName and not edge.value.directed):
                buildStr += '\n'

                # Append direction
                if edge.value.directed:
                    buildStr += '  ->'
                else:
                    buildStr += '    '

                # Append edge name
                if edge.value.fromV == vertexName:
                    buildStr += edge.value.toV
                else:
                    buildStr += edge.value.fromV
                buildStr += ', '

                # Append labels
                index = 0
                for label in edge.value.labels:
                    buildStr += str(label) + ': ' + str(edge.value.labels[label])
                    index += 1
                    if index < len(edge.value.labels):
                        buildStr += ', '
        return buildStr

    def __eq__(self, other):
        if not isinstance(other, Graph):
            return False

        if len(self.vertices) != len(other.vertices):
            return False

        if len(self.edges) != len(other.edges):
            return False

        sortedSelfVertices = sorted(self.vertices, key=lambda x: x.value['name'].value)
        sortedOtherVertices = sorted(other.vertices, key=lambda x: x.value['name'].value)

        if sortedSelfVertices != sortedOtherVertices:
            return False

        sortedSelfEdges = sorted(self.edges, key=lambda x: (x.value.fromV, x.value.directed, x.value.toV))
        sortedOtherEdges = sorted(other.edges, key=lambda x: (x.value.fromV, x.value.directed, x.value.toV))

        if sortedSelfEdges != sortedOtherEdges:
            return False

        return True

    def __ne__(self, other):
        return not self == other

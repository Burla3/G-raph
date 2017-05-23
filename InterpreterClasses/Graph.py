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

    def getEdgesFrom(self, vertexName):
        edges = []
        for edge in self.edges:
            if not edge.value.directed:
                if edge.value.fromV == vertexName.value or edge.value.toV == vertexName.value:
                    edges.append(edge)
            elif edge.value.fromV == vertexName:
                edges.append(edge)

        return edges

    def getEdgesTo(self, vertexName):
        edges = []
        for edge in self.edges:
            if not edge.value.directed:
                if edge.value.fromV == vertexName.value or edge.value.toV == vertexName.value:
                    edges.append(edge)
            elif edge.value.toV == vertexName:
                edges.append(edge)

        return edges

    def getEdgesFromTo(self, vertexFrom, vertexTo):
        edges = []
        for edge in self.edges:
            if not edge.value.directed:
                if edge.value.fromV == vertexFrom.value or edge.value.toV == vertexFrom.value:
                    if edge.value.fromV == vertexTo.value or edge.value.toV == vertexTo.value:
                        edges.append(edge)
            elif edge.value.fromV == vertexFrom.value and edge.value.toV == vertexTo.value:
                edges.append(edge)

        return edges


    def verticesAdjacentTo(self, vertexName):
        vertices = []
        for edge in self.edges:
            if not edge.value.directed:
                if edge.value.fromV == vertexName.value:
                    vertices.append(edge.value.toV)
                elif edge.value.toV == vertexName.value:
                    vertices.append(edge.value.fromV)
            elif edge.value.fromV == vertexName.value:
                vertices.append(edge.value.toV)

        return vertices


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

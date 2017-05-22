class Edge():
    def __init__(self, fromV, toV, directed):
        self.fromV = fromV
        self.toV = toV
        self.directed = directed
        self.labels = {}

    def __eq__(self, other):
        if self.directed != other.directed:
            return False

        if self.fromV != other.fromV:
            return False

        if self.toV != other.toV:
            return False

        if len(self.labels) != len(other.labels):
            return False

        for key in self.labels:
            if key not in other.labels:
                return False

            if self.labels[key] != other.labels[key]:
                return False

        return True

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        buildStr = ''

        buildStr += self.fromV
        if self.directed:
            buildStr += '->'
        else:
            buildStr += '-'
        buildStr += self.toV
        buildStr += ' { '
        first = True
        for key in self.labels:
            if first:
                first = False
            else:
                buildStr += ', '
            buildStr += key
            buildStr += ': '
            buildStr += str(self.labels[key].value)
        buildStr += '}'

        return buildStr

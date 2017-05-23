from InterpreterClasses.Types import Types


class ValueTypeTuple():
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        if self.type == Types.List:
            buildStr = '['

            first = True
            for ele in self.value:
                if first:
                    first = False
                else:
                    buildStr += ', '
                buildStr += str(ele)

            buildStr += ']'

            return buildStr

        if self.type == Types.Vertex:
            vertexName = str(self.value['name'])
            buildStr = vertexName + ' { '

            # Append labels
            index = 0
            for label in self.value:
                if label != 'name':
                    buildStr += str(label) + ': ' + str(self.value[label])
                    index += 1
                    if index < len(self.value) - 1:
                        buildStr += ', '
            buildStr += ' }'
            return buildStr

        return str(self.value)

    def __eq__(self, other):
        if not isinstance(other, ValueTypeTuple):
            return False

        if self.type != other.type:
            return False

        if self.value != other.value:
            return False

        return True

    def __ne__(self, other):
        return not self == other

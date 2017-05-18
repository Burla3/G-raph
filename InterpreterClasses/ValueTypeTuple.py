from InterpreterClasses.Types import Types


class ValueTypeTuple():
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        if self.type == Types.List:
            buildStr = '['
            index = 0

            while index < len(self.value) - 1:
                buildStr += str(self.value[index]) + ', '
                index += 1

            buildStr += str(self.value[index]) + ']'
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

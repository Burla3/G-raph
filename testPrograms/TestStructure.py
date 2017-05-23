from InterpreterClasses.Graph import Graph
from InterpreterClasses.ValueTypeTuple import ValueTypeTuple
from InterpreterClasses.Types import Types
from InterpreterClasses.Edge import Edge

def listcomp(vale, valf):
    if len(vale) != len(valf):
        return False
    count = 0
    for ve in vale:
        if ve != valf[count].value:
            return False
        count += 1
    return True

def vertexComp(valExpected, valFound):
    verticesFound = valFound.vertices
    if len(valExpected) != len(verticesFound):
        return False
    count = 0
    for veLabels in valExpected:
        for veLabel in veLabels:
            # Contains key?
            if veLabel not in verticesFound[count].value:
                return False
            # Is the value the same?
            if veLabels.get(veLabel) != verticesFound[count].value.get(veLabel).value:
                return False
        count += 1

    return True

def edgeComp(valExpected, valFound):
    edgesFound = valFound.edges
    if len(valExpected) != len(edgesFound):
        return False
    count = 0
    for veEdge in valExpected:
        edgeFound = edgesFound[count].value
        if veEdge[0] != edgeFound.fromV:
            return False
        if veEdge[1] != edgeFound.toV:
            return False
        if veEdge[2] != edgeFound.directed:
            return False
        if len(veEdge[3]) != len(edgeFound.labels):
            return False

        for veLabel in veEdge[3]:
            # Contains key?
            if veLabel not in edgeFound.labels:
                return False
            # Is the value the same?
            if veEdge[3].get(veLabel) != edgeFound.labels.get(veLabel).value:
                return False
        count += 1

    return True

tests = [
    {
        'file': 'arith_op.graph',
        'state': [
            ('plus', 6),
            ('minus', 0),
            ('mul', 9),
            ('div', 1),
            ('mod', 0),
            ('power', 9),
            ('unaryMinus', -3),
        ],
        'output': [

        ]
    },
    {
        'file': 'comp_op.graph',
        'state': [
            ('less', False),
            ('greater', True),
            ('leEq', True),
            ('grEq', False),
            ('equal', True),
            ('notEq', False),
            ('andComb', False),
            ('orComb', True),
            ('neg', False),
        ],
        'output': [

        ]
    },
    {
        'file': 'range_ex.graph',
        'state': [
            ('listVar', [1], listcomp),
            ('listVar2', [1, 5, 8], listcomp),
            ('ascendingOrderRange', [3, 4, 5, 6, 7, 8, 9], listcomp),
            ('descendingOrderRange', [9, 8, 7, 6, 5, 4, 3], listcomp),
        ],
        'output': [

        ]
    },
    {
        'file': 'set_op.graph',
        'state': [
            ('rangeOne', [1, 2, 3], listcomp),
            ('rangeTwo', [3, 4, 5], listcomp),
            ('rangeConcat', [1, 2, 3, 3, 4, 5], listcomp),
            ('firstG', [{'name': 'a'}, {'name': 'b'}], vertexComp),
            ('firstG', [['a', 'b', False, {}]], edgeComp),
            ('secondG', [{'name': 'b'}, {'name': 'c'}], vertexComp),
            ('secondG', [['b', 'c', False, {}]], edgeComp),
            ('unionedG', [{'name': 'a'}, {'name': 'b'}, {'name': 'c'}], vertexComp),
            ('unionedG', [['a', 'b', False, {}], ['b', 'c', False, {}]], edgeComp),
            ('intersectedG', [{'name': 'b'}], vertexComp),
            ('diffedG', [{'name': 'a'}], vertexComp),
        ],
        'output': [

        ]
    },
    {
        'file': 'string_manip.graph',
        'state': [
        ],
        'output': [
            'The 3 elephants?',
            'The 25 elephants?',
            'The amount monkeys?',
            'The 25 monkeys?',
        ]
    },
    {
        'file': 'ctrl_strc.graph',
        'state': [
        ],
        'output': [
            'Passed: Excellent',
            'I am hungry',
            'Countdown',
            '3',
            '2',
            '1',
            'GO!',
        ]
    },
    {
        'file': 'func_ex.graph',
        'state': [
        ],
        'output': [
            'Hello, Peter!',
            'My name is Peter',
        ]
    },
]

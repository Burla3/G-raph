from InterpreterClasses.Graph import Graph
from InterpreterClasses.ValueTypeTuple import ValueTypeTuple
from InterpreterClasses.Types import Types
from InterpreterClasses.Edge import Edge

def listcomp(vale, valf):
    if len(vale) != len(valf):
        return False
    count = 0
    for ve in vale:
        if valf[count].type in [Types.Vertex, Types.Edge]:
            var = str(valf[count])
            if str(ve) != str(valf[count]):
                return False
        elif ve != valf[count].value:
            return False
        count += 1
    return True

def vertexComp(valExpected, valFound):
    if hasattr(valFound, 'vertices'):
        verticesFound = valFound.vertices
    else:
        verticesFound = [ValueTypeTuple(valFound, Types.Vertex)]

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
        'file': 'graphs_ex.graph',
        'state': [
            ('vertices', ['a {  }', 'b {  }', 'c {  }', 'd {  }', 'e {  }', 'f {  }', 'g {  }'], listcomp),
            ('edges', ['b-c { w: 2.0}', 'c-d { label: 5.0}', 'd->e { }', 'e->f { label: 7.0}', 'e->g { label: 3.0}'], listcomp),
            ('edgesFromE', ['e->f { label: 7.0}', 'e->g { label: 3.0}'], listcomp),
            ('edgesToE', ['d->e { }'], listcomp),
            ('vertex', [{'name': 'a', 'd': 3.0}], vertexComp),
            ('graphVar', [{'name': 'a', 'd': 3.0}, {'name': 'b'}, {'name': 'c'}, {'name': 'd'}, {'name': 'e'}, {'name': 'f'}, {'name': 'g'}], vertexComp),
            ('graphVar', [['b', 'c', False, {'w': 2.0}], ['c', 'd', False, {}], ['d', 'e', True, {}], ['e', 'f', True, {}], ['e', 'g', True, {}]], edgeComp),
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
            'The 25.0 elephants?',
            'The amount monkeys?',
            'The 25.0 monkeys?',
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
            '3.0',
            '2.0',
            '1.0',
            'GO!',
        ]
    },
    {
        'file': 'func_ex.graph',
        'state': [
        ],
        'output': [
            'Hello, Peter!',
            'My name is Peter.',
        ]
    },
    {
        'file': 'parameter_passing.graph',
        'state': [
            ('number', 64),
        ],
        'output': [
            'result = 64.0',
            '8.0',
            'result = 64.0',
            '64.0',
        ]
    },
    {
        'file': 'scope_access.graph',
        'state': [
            ('number', 3),
        ],
        'output': [
            '3',
            '3',
            'error',
        ]
    },
]

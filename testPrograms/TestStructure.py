def listcomp(vale, valf):
    if len(vale) != len(valf):
        return False
    count = 0
    for ve in vale:
        if ve != valf[count].value:
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




tests = [
    {
        'file': 'arith_op.graph',
        'output': [
            ('plus', 6),
            ('minus', 0),
            ('mul', 9),
            ('div', 1),
            ('mod', 0),
            ('power', 9),
            ('unaryMinus', -3),
        ]
    },
    {
        'file': 'comp_op.graph',
        'output': [
            ('less', False),
            ('greater', True),
            ('leEq', True),
            ('grEq', False),
            ('equal', True),
            ('notEq', False),
            ('andComb', False),
            ('orComb', True),
            ('neg', False),
        ]
    },
    {
        'file': 'comp_op.graph',
        'output': [
            ('listVar', [1]),
            ('listVar2', [1, 5, 8]),
            ('ascendingOrderRange', [3, 4, 5, 6, 7, 8, 9]),
            ('descendingOrderRange', [9, 8, 7, 6, 5, 4, 3]),
        ]
    },
]
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
            ('listVar', [1]),
            ('listVar2', [1, 5, 8]),
            ('ascendingOrderRange', [3, 4, 5, 6, 7, 8, 9]),
            ('descendingOrderRange', [9, 8, 7, 6, 5, 4, 3]),
        ],
        'output': [

        ]
    },
    {
        'file': 'range_ex.graph',
        'state': [
            ('listVar', [1]),
            ('listVar2', [1, 5, 8]),
            ('ascendingOrderRange', [3, 4, 5, 6, 7, 8, 9]),
            ('descendingOrderRange', [9, 8, 7, 6, 5, 4, 3]),
        ],
        'output': [

        ]
    },
]
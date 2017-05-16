from antlr4 import *

from ASTBuilder import ASTBuilder
from Antlr.GraphLexer import GraphLexer
from Antlr.GraphParser import GraphParser
from InterpreterMain import GraphVisitor

from contextlib import redirect_stdout
from io import StringIO

from testPrograms.TestStructure import tests



def testrunner(filepath):
    input_stream = FileStream(filepath)
    lexer = GraphLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = GraphParser(stream)
    try:
        tree = parser.program()
    except Exception as e:
        print(e.args)
        return

    visitor = ASTBuilder()
    visitor.visitProgram(tree)

    visitor = GraphVisitor()
    f = StringIO()
    with redirect_stdout(f):
        visitorResult = visitor.visitProgram(tree)

    return f.getvalue().split('\n')

def main():
    globaltestcount = 0
    globaltesterrors = 0
    toofew = False
    for test in tests:
        progoutput = testrunner('testPrograms/' + test['file'])
        tcount = 0
        print('Testing {0}:'.format(test['file']))
        localtestcount = 0
        localtesterrors = 0
        if len(test['output']) < len(progoutput):
            toofew = True
            print('\x1b[0;31;40m Too few tests \x1b[0m')
        for testline in test['output']:
            try:
                progoutput[tcount]
            except:
                KeyError('Not enough program output')

            if progoutput[tcount] == testline:
                color = '0;32;40'
                state = '[PASSED]'
            else:
                color = '0;31;40'
                state = '[FAILED]'
                localtesterrors += 1


            print('\x1b[{color}m {state} \x1b[0m T#{tnumber:03d}. Want: {lookfor}({ltype}) Found: {got}({gtype})'.format(
                tnumber=tcount,
                lookfor=testline,
                ltype=type(testline).__name__,
                got=progoutput[tcount],
                gtype=type(progoutput[tcount]).__name__,
                color=color,
                state=state))
            localtestcount += 1
            tcount += 1

        print('------------------------------')
        if localtesterrors == 0:
            color = '0;32;40'
        else:
            color = '0;31;40'

        print('\x1b[{color}m {fail} of {total} tests passed \x1b[0m'.format(color=color, fail=localtestcount-localtesterrors, total=localtestcount))
        print('------------------------------')

        globaltestcount += localtestcount
        globaltesterrors += localtesterrors

    print('============Totals============')
    if globaltesterrors == 0:
        color = '0;32;40'
    else:
        color = '0;31;40'

    print('\x1b[{color}m {fail} of {total} tests passed \x1b[0m'.format(color=color, fail=globaltestcount-globaltesterrors,
                                                                        total=globaltestcount))
    if toofew:
        print('\x1b[0;31;40m At least one file had too few tests \x1b[0m')
    print('==============================')




if __name__ == '__main__':
    main()
import traceback
from antlr4 import *

from ASTBuilder import ASTBuilder
from Antlr.GraphLexer import GraphLexer
from Antlr.GraphParser import GraphParser
from InterpreterMain import GraphVisitor

from contextlib import redirect_stdout
from io import StringIO

from testPrograms.TestStructure import tests


class TestVisitor(GraphVisitor):
    closedscopes = []
    outputlines = []

    def closeScope(self):
        self.closedscopes.append(self.getCurrentScope())
        self.symbolTableStack.pop()


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

    ASTvisitor = ASTBuilder()
    ASTvisitor.visitProgram(tree)

    visitor = TestVisitor()
    f = StringIO()
    with redirect_stdout(f):
        visitorResult = visitor.visitProgram(tree)

    while visitor.symbolTableStack.size() > 0:
        visitor.closeScope()
    while lexer.tokens.poll():
        pass
    visitor.outputlines = f.getvalue().split('\n')
    return visitor

def getFromSymtable(tables, key):
    if not tables:
        tables = []
    for symtab in tables:
        try:
            return symtab.get(key)
        except KeyError:
            continue
    raise KeyError('Key not in any table')

def testexec(testtup, value, localtestcount):
    localtesterrors = 0
    if len(testtup) is 3:
        comp = testtup[2](testtup[1], value)
    else:
        comp = value == testtup[1]

    if comp:
        color = '0;32;40'
        state = '[PASSED]'
    else:
        color = '0;31;40'
        state = '[FAILED]'
        localtesterrors += 1

    print('\x1b[{color}m {state} \x1b[0m T#{tnumber:03d}. Expected: {lookfor}({ltype}) Found: {got}({gtype})'.format(
        tnumber=localtestcount + 1,
        lookfor=testtup[1],
        ltype=type(testtup[1]).__name__,
        got=value,
        gtype=type(value).__name__,
        color=color,
        state=state))
    return localtesterrors

def main():
    globaltestcount = 0
    globaltesterrors = 0
    for test in tests:
        print('Testing {0}:'.format(test['file']))
        try:
            progoutput = testrunner('testPrograms/' + test['file'])
        except Exception as e:
            globaltestcount += 1
            globaltesterrors += 1
            print(traceback.format_exc())
            # print('Error interpreting G-raph code: ' + str(e))
            print('------------------------------')
            continue

        localtestcount = 0
        localtesterrors = 0
        for testtup in test['state']:
            try:
                value = getFromSymtable(progoutput.closedscopes, testtup[0])['value']
            except KeyError as e:
                localtestcount += 1
                localtesterrors += 1
                print('\x1b[0;31;40m [FAILED] \x1b[0m' + str(e))
                continue

            localtesterrors += testexec(testtup, value, localtestcount)
            localtestcount += 1

        outcount = 0
        for testval in test['output']:
            testtup = (testval, testval)
            localtesterrors += testexec(testtup, progoutput.outputlines[outcount], localtestcount)
            localtestcount += 1
            outcount += 1

        print('------------------------------')
        if localtesterrors == 0:
            color = '0;32;40'
        else:
            color = '0;31;40'

        print('\x1b[{color}m {fail} of {total} tests passed \x1b[0m'.format(color=color, fail=localtestcount-localtesterrors, total=localtestcount))
        print('------------------------------')

        globaltestcount += localtestcount
        globaltesterrors += localtesterrors

    print('\n\n============Totals============')
    if globaltesterrors == 0:
        color = '0;32;40'
    else:
        color = '0;31;40'

    print('\x1b[{color}m {fail} of {total} tests passed \x1b[0m'.format(color=color, fail=globaltestcount-globaltesterrors,
                                                                        total=globaltestcount))





if __name__ == '__main__':
    main()
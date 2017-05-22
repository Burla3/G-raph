from antlr4 import *

from ASTBuilder import ASTBuilder
from Antlr.GraphLexer import GraphLexer
from Antlr.GraphParser import GraphParser
from InterpreterMain import GraphVisitor
from JSONBuilder import JSONBuilder

from contextlib import redirect_stdout
from io import StringIO

def errorPrinter(e, filename):
    '\x1b[0;31;40m {state} \x1b[0m'
    start = e.args[1].start
    stop = e.args[1].stop

    with open(filename) as f:
        content = f.read().splitlines()

    line = content[start.line-1]
    output = ['', '', '']

    if (start.line-2) >= 0:
        output[0] = '{linenumber}:{line}'.format(linenumber=start.line-1, line=content[start.line-2])


    output[1] = '{linenumber}:{begin}\x1b[0;31;40m{error}\x1b[0m{end}'.format(
        linenumber=start.line,
        begin=line[:start.column],
        error=line[start.column:stop.column],
        end=line[stop.column:]
    )

    if (start.line) <= len(content):
        output[2] = '{linenumber}:{line}'.format(linenumber=start.line+1, line=content[start.line])


    print(e.args[0])
    print('\n'.join(output))


def main():
    filename = 'testPrograms/test.graph'
    input = FileStream(filename)
    #input = FileStream('testPrograms/assosiativityTest.graph')
    lexer = GraphLexer(input)
    stream = CommonTokenStream(lexer)


    #stream.fill()

    #for token in stream.tokens:
    #    if '\r\n' in token.text:
    #        print('newline', ' ', token.type)
    #    elif token.text is not ' ':
    #        print(token.text, ' ', token.type)

    f = StringIO()

    parser = GraphParser(stream)
    try:
        with redirect_stdout(f):
            tree = parser.program()
    except Exception as e:
        print(e.args)
        # return True

    fl = f.getvalue()
    if len(fl) > 0:
        for line in fl.split('\n'):
            print(line + '\n')
        # return True

    astb = JSONBuilder(tree)

    file = open('treeInJSON.json', 'w')
    json = astb.ConvertToJSON()
    file.write(json)
    file.close()

    #visitor = GraphVisitor()
    #try:
    #    visitorResult = visitor.visitProgram(tree)
    #except Exception as e:
    #    print(e.args)
    #    return

    visitor = ASTBuilder()
    visitor.visitProgram(tree)

    visitor = GraphVisitor()
    try:
        visitorResult = visitor.visitProgram(tree)
    except BaseException as e:
        errorPrinter(e, filename)



if __name__ == '__main__':
    main()
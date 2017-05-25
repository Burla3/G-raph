#!/usr/bin/python3
import sys, os
from antlr4 import *

from ASTBuilder import ASTBuilder
from Antlr.GraphLexer import GraphLexer
from Antlr.GraphParser import GraphParser
from InterpreterMain import GraphVisitor
from JSONBuilder import JSONBuilder

from contextlib import redirect_stderr
from io import StringIO


def errorprinter(e, filename):
    if len(e.args) < 2:
        print(e.args[0])
        return True
    start = e.args[1].start
    stop = e.args[1].stop


    with open(filename) as f:
        content = f.read().splitlines()

    line = content[start.line-1]
    output = ['', '', '']

    if start.column == stop.column:
        errorval = ' '
    else:
        errorval = line[start.column:stop.column]

    if (start.line-2) >= 0:
        output[0] = '{linenumber}:{line}'.format(linenumber=start.line-1, line=content[start.line-2])

    output[1] = '{linenumber}:{begin}\x1b[0;31;40m{error}\x1b[0m{end}'.format(
        linenumber=start.line,
        begin=line[:start.column],
        error=errorval,
        end=line[stop.column:]
    )

    if (start.line) < len(content):
        output[2] = '{linenumber}:{line}'.format(linenumber=start.line+1, line=content[start.line])

    print('Error encountered while running {filename}'.format(filename=filename))
    print(e.args[0])
    print('\n'.join(output))


def main():
    if not len(sys.argv) > 1:
        print('G-raph takes a single argument that must the path to a .graph file')
        return True
    else:
        filename = sys.argv[1]

    if not filename[0] == '/':
        filename = os.path.join(os.getcwd(), filename)

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
        with redirect_stderr(f):
            tree = parser.program()
    except Exception as e:
        print(e.args)
        return True

    fl = f.getvalue()

    if len(fl) > 0:
        print(fl)
        return True

    astb = JSONBuilder(tree)

    #astb.BuildAST()

    file = open('treeInJSON.json', 'w')
    json = astb.ConvertToJSON()
    file.write(json)
    file.close()

    visitor = ASTBuilder()
    visitor.visitProgram(tree)



    file = open('treeInJSONAfter.json', 'w')
    json = astb.ConvertToJSON()
    file.write(json)
    file.close()

    visitor = GraphVisitor()
    try:
        visitorResult = visitor.visitProgram(tree)
    except BaseException as e:
        errorprinter(e, filename)



if __name__ == '__main__':
    main()
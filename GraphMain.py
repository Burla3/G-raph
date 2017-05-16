from antlr4 import *

from ASTBuilder import ASTBuilder
from Antlr.GraphLexer import GraphLexer
from Antlr.GraphParser import GraphParser
from InterpreterMain import GraphVisitor
from JSONBuilder import JSONBuilder


def main():
    input = FileStream('testPrograms/test.graph')
    #input = FileStream('testPrograms/assosiativityTest.graph')
    lexer = GraphLexer(input)
    stream = CommonTokenStream(lexer)


    #stream.fill()

    #for token in stream.tokens:
    #    if '\r\n' in token.text:
    #        print('newline', ' ', token.type)
    #    elif token.text is not ' ':
    #        print(token.text, ' ', token.type)

    parser = GraphParser(stream)
    try:
        tree = parser.program()
    except Exception as e:
        print(e.args)
        return

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
    visitorResult = visitor.visitProgram(tree)



if __name__ == '__main__':
    main()
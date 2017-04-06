from antlr4 import *
from GraphLexer import GraphLexer
from GraphParser import GraphParser
from ASTBuilder import ASTBuilder
import copy


def main():
    input = FileStream('test.graph')
    lexer = GraphLexer(input)
    stream = CommonTokenStream(lexer)


    stream.fill()

    for token in stream.tokens:
        if '\r\n' in token.text:
            print('newline', ' ', token.type)
        elif token.text is not ' ':
            print(token.text, ' ', token.type)

    parser = GraphParser(stream)
    try:
        tree = parser.program()
    except Exception as e:
        print(e.args)
        return

    astb = ASTBuilder(tree)
    #astb.BuildAST()

    file = open('treeInJSON.json', 'w')
    json = astb.ConvertToJSON()
    file.write(json)
    file.close()


if __name__ == '__main__':
    main()
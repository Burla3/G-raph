# Generated from Graph.g4 by ANTLR 4.7
import re

#from InterpreterClasses import *
from InterpreterClasses.EdgeDecleration import EdgeDecleration
from InterpreterClasses.FormalActualTuple import FormalActualTuple
from InterpreterClasses.Graph import Graph
from InterpreterClasses.Stack import Stack
from InterpreterClasses.ValueTypeTuple import ValueTypeTuple
from InterpreterClasses.VertexDecleration import VertexDecleration
from antlr4 import *

from InterpreterClasses.Edge import Edge
from SymTab.SymbolTable import SymbolTable

if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete generic visitor for a parse tree produced by GraphParser.

class GraphVisitor(ParseTreeVisitor):

    symbolTableStack = Stack()
    envF = {}

    def newScope(self):
        self.symbolTableStack.push(SymbolTable())

    def closeScope(self):
        self.symbolTableStack.pop()

    def getCurrentScope(self):
        return self.symbolTableStack.peek()



    # Visit a parse tree produced by GraphParser#program.
    def visitProgram(self, ctx:GraphParser.ProgramContext):
        self.symbolTableStack.push(SymbolTable())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#funcDef.
    def visitFuncDef(self, ctx:GraphParser.FuncDefContext):
        name = ctx.children[0].symbol.text
        self.envF[name] = ctx


    # Visit a parse tree produced by GraphParser#formalParams.
    def visitFormalParams(self, ctx:GraphParser.FormalParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#block.
    def visitBlock(self, ctx:GraphParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#stmt.
    def visitStmt(self, ctx:GraphParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#simpleStmt.
    def visitSimpleStmt(self, ctx:GraphParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#assignment.
    def visitAssignment(self, ctx:GraphParser.AssignmentContext):
        identifier = ctx.children[0].accept(self)
        value = ctx.children[1].accept(self)

        self.getCurrentScope().set(identifier, value.type, value.value)


    # Visit a parse tree produced by GraphParser#compoundStmt.
    def visitCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#ifStmt.
    def visitIfStmt(self, ctx:GraphParser.IfStmtContext):
        test = ctx.children[1].accept(self)

        if test.value:
            ctx.children[2].accept(self)
        else:
            ctx.children[3].accept(self)


    # Visit a parse tree produced by GraphParser#whileStmt.
    def visitWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        while ctx.children[1].accept(self).value:
            ctx.children[2].accept(self)


    # Visit a parse tree produced by GraphParser#foreachStmt.
    def visitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graphAssignment.
    def visitGraphAssignment(self, ctx:GraphParser.GraphAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#compOp.
    def visitCompOp(self, ctx:GraphParser.CompOpContext):
        return ctx.children[0].symbol.text

    def strSubVars(self, mobj):
        key = mobj.group(1)[1:-1]
        scope = self.getCurrentScope()
        return str(scope.get(key)['value'])


    # Visit a parse tree produced by GraphParser#expr.
    def visitExpr(self, ctx:GraphParser.ExprContext):
        if ctx.getChildCount() == 1:
            value = ctx.children[0].accept(self)
            if type(value) is str and '\'' in value:
                value = value[1:-1]  # stripping ' of both ends
                value = re.sub("(?<![\\\])({(?:[a-z]+[a-zA-Z0-9]*)\})", self.strSubVars, value)
                value = re.sub("(\\\)(?={(?:[a-z]+[a-zA-Z0-9]*)\})", '', value)
                value = ValueTypeTuple(value, 'string')
            return value
        else:
            operator = ctx.children[1]
            if hasattr(operator, 'symbol'):
                operator = operator.symbol.text
            else:
                operator = operator.children[0].symbol.text

            left = self.getValue(ctx.children[0])
            right = self.getValue(ctx.children[2])

            if operator == '+':
                exprType = 'number'

                if left.type != 'number' or right.type != 'number':
                    error = 'Types do not match in test on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                    raise TypeError(error)

                result = left.value + right.value
            elif operator == '>':
                exprType = 'bool'

                left = self.getValue(ctx.children[0])
                right = self.getValue(ctx.children[2])

                if left.type != 'number' or right.type != 'number':
                    error = 'Types do not match in test on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                    raise TypeError(error)

                result = left.value > right.value
            else:
                print('Det giver ikke mening')

        return ValueTypeTuple(result, exprType)

    def getValue(self, ctx):
        val = ctx.accept(self)
        return self.lookUp(val)


    # Visit a parse tree produced by GraphParser#setOp.
    def visitSetOp(self, ctx:GraphParser.SetOpContext):
        return ctx.children[0].symbol.text


    # Visit a parse tree produced by GraphParser#factorOp.
    def visitFactorOp(self, ctx:GraphParser.FactorOpContext):
        return ctx.children[0].symbol.text


    # Visit a parse tree produced by GraphParser#molecule.
    def visitMolecule(self, ctx:GraphParser.MoleculeContext):
        if ctx.getChildCount() > 1:
            identifier = ctx.children[0].accept(self)
            structure = self.lookUp(identifier)
            index = self.lookUp(ctx.children[1].children[0].accept(self))

            if index.type != 'number':
                error = 'Value is not of type number ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                raise TypeError(error)
            if structure.type != 'list':
                error = 'Value is not of type list ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                raise TypeError(error)

            value = structure.value[int(index.value)]

            return value

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#atom.
    def visitAtom(self, ctx:GraphParser.AtomContext):
        if hasattr(ctx.children[0], 'symbol'):
            return ctx.children[0].symbol.text
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#funcCall.
    def visitFuncCall(self, ctx:GraphParser.FuncCallContext):
        funcName = ctx.children[0].symbol.text

        if funcName == 'Print':
            input = ctx.children[1].accept(self)
            print(input.value)
        elif funcName in self.envF:
            result = self.visitDefinedFunction(ctx, funcName)

            return result
        else:
            raise ModuleNotFoundError('Function: ' + funcName + ' do not exist.')

    def visitDefinedFunction(self, ctx, funcName):
        funcBody = self.envF[funcName]

        actualParams = self.getActualParams(ctx)
        formalParams = self.getFormalParams(funcBody)

        if len(formalParams) != len(actualParams):
            raise ValueError('Formal parameters and actual parameters is not the same amount in function: ' + funcName)

        mappedParams = self.mapParams(formalParams, actualParams)

        self.newScope()

        self.insertParamsInNewScope(mappedParams)

        result = self.visitChildren(funcBody.children[funcBody.getChildCount() - 1])

        self.closeScope()

        return result

    def insertParamsInNewScope(self, paramsCollected):
        for i in range(0, len(paramsCollected.formal)):
            self.getCurrentScope().set(paramsCollected.formal[i], paramsCollected.actual[i].type, paramsCollected.actual[i].value)

    def mapParams(self, formalParams, actualParams):
        actualValues = []
        formalNames = []

        for i in range(0, len(actualParams)):
            actualVal = actualParams[i].accept(self)
            actualVal = self.lookUp(actualVal)
            actualValues.append(actualVal)

        for param in range(0, len(formalParams)):
            formalNames.append(formalParams[param].symbol.text)

        return FormalActualTuple(formalNames, actualValues)

    def getActualParams(self, ctx):
        if ctx.getChildCount() == 2:
            formalParams = ctx.children[1].children
        else:
            formalParams = []

        return formalParams

    def getFormalParams(self, ctx):
        if ctx.getChildCount() == 3:
            actualParams = ctx.children[1].children
        else:
            actualParams = []

        return actualParams

    # Visit a parse tree produced by GraphParser#actualParams.
    def visitActualParams(self, ctx:GraphParser.ActualParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#listStruct.
    def visitListStruct(self, ctx:GraphParser.ListStructContext):

        listStruct = []
        for expr in ctx.children:
            result = self.visitExpr(expr)
            listStruct.append(result)

        return ValueTypeTuple(listStruct, 'list')


    # Visit a parse tree produced by GraphParser#rangerStruct.
    def visitRangerStruct(self, ctx:GraphParser.RangerStructContext):

        start = self.visitExpr(ctx.children[0])
        end = self.visitExpr(ctx.children[1])

        if start.type != 'number' or end.type != 'number':
            error = 'Types do not match in test on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error)

        ranger = []
        for i in range(int(start.value), int(end.value)):
            ranger.append(ValueTypeTuple(i, 'number'))

        return ValueTypeTuple(ranger, 'list')


    # Visit a parse tree produced by GraphParser#graph.
    def visitGraph(self, ctx:GraphParser.GraphContext):
        graph = Graph()
        vertexDecls = self.visitChildren(ctx)

        for vDecl in vertexDecls:
            vertex = vDecl.vertex
            if vertex not in graph.vertices:
                dic = {'name': ValueTypeTuple(vertex, 'string')}
                graph.vertices.append(dic)
            for eDecl in vDecl.edges:
                if eDecl.vertex not in graph.vertices:
                    dic = {'name': ValueTypeTuple(eDecl.vertex, 'string')}
                    graph.vertices.append(dic)

                edge = Edge(vertex, eDecl.vertex, eDecl.directed)

                if eDecl.label is not None:
                    edge.labels['label'] = eDecl.label

                graph.edges.append(edge)

        return graph


    # Visit a parse tree produced by GraphParser#vertices.
    def visitVertices(self, ctx:GraphParser.VerticesContext):
        vertexDecls = []
        for decl in ctx.children:
            vertexDecls.append(decl.accept(self))

        return vertexDecls


    # Visit a parse tree produced by GraphParser#vertex.
    def visitVertex(self, ctx:GraphParser.VertexContext):
        if ctx.getChildCount() == 1:
            vertexDecl = VertexDecleration(ctx.children[0].symbol.text, [])
        else:
            vertexDecl = VertexDecleration(ctx.children[0].symbol.text, ctx.children[1].accept(self))
        return vertexDecl


    # Visit a parse tree produced by GraphParser#edges.
    def visitEdges(self, ctx:GraphParser.EdgesContext):
        edges = []
        for edge in ctx.children:
            edges.append(edge.accept(self))
        return edges


    # Visit a parse tree produced by GraphParser#edge.
    def visitEdge(self, ctx:GraphParser.EdgeContext):
        directed = False
        vertex = None
        label = None

        for child in ctx.children:
            if hasattr(child, 'symbol'):
                text = child.symbol.text
                if text == '->':
                    directed = True
                else:
                    vertex = text
            else:
                label = child.accept(self)

        return EdgeDecleration(directed, vertex, label)


    # Visit a parse tree produced by GraphParser#identifier.
    def visitIdentifier(self, ctx:GraphParser.IdentifierContext):
        return ctx.getText()


    # Visit a parse tree produced by GraphParser#number.
    def visitNumber(self, ctx:GraphParser.NumberContext):
        return ValueTypeTuple(self.isNumber(ctx.getText()), 'number')


    # Visit a parse tree produced by GraphParser#boolean.
    def visitBoolean(self, ctx:GraphParser.BooleanContext):
        return ValueTypeTuple(ctx.getText() == 'True', 'boolean')


    def isNumber(self, value):
        try:
            number = float(value)
            return number
        except ValueError:
            return False

    def lookUp(self, value):
        if type(value) is str:
            entry = self.getCurrentScope().get(value)
            value = ValueTypeTuple(entry['value'], entry['type'])

        return value

del GraphParser
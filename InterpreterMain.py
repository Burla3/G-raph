# Generated from Graph.g4 by ANTLR 4.7
import re

from InterpreterClasses import *
from antlr4 import *
from antlr4.tree import Tree

import copy
from InterpreterClasses.Edge import Edge
from SymTab.SymbolTable import SymbolTable

from Antlr.GraphParser import GraphParser

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

    def visitProgram(self, ctx:GraphParser.ProgramContext):
        self.symbolTableStack.push(SymbolTable())
        return self.visitChildren(ctx)

    def visitFuncDef(self, ctx:GraphParser.FuncDefContext):
        name = ctx.children[0].symbol.text
        self.envF[name] = ctx

    def visitFormalParams(self, ctx:GraphParser.FormalParamsContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx:GraphParser.BlockContext):
        for child in ctx.children:
            if child.start.text == 'return':
                retValue = self.visitChildren(child)
                if retValue is not None:
                    return retValue
                else:
                    return '\u0000'
                #return self.visitChildren(child)
            else:
                retValue = self.visitChildren(child)
                if retValue is not None:
                    return retValue

    def visitStmt(self, ctx:GraphParser.StmtContext):
        return self.visitChildren(ctx)

    def visitSimpleStmt(self, ctx:GraphParser.SimpleStmtContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx:GraphParser.AssignmentContext):
        identifier = ctx.children[0].accept(self)
        value = ctx.children[1].accept(self)

        if value == '\u0000' or value is None:  # void returned
            raise ValueError('Function has no return value that can be assigned', ctx)

        if hasattr(identifier, 'value') and isinstance(identifier.value, Molecule):
            molecule = identifier.value
            structure = self.lookUp(molecule.atom, ctx)

            if structure.type == Types.Edge:
                structure.value.labels[molecule.trailer] = value
            else:
                structure.value[molecule.trailer] = value
        else:
            #value = self.lookUp(value, ctx)
            self.getCurrentScope().set(identifier, value.type, value.value)

    def visitCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx:GraphParser.IfStmtContext):
        count = 0

        for child in ctx.children:
            if isinstance(child, GraphParser.ExprContext) and self.evaluateBool(child):
                return ctx.children[count + 1].accept(self)
            count += 1

        if isinstance(ctx.children[count - 2], GraphParser.BlockContext):
            return ctx.children[count - 1].accept(self)

    def visitWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        while self.evaluateBool(ctx.children[1]):
            retValue = ctx.children[2].accept(self)
            if retValue is not None:
                return retValue

    def evaluateBool(self, ctx):
        result = ctx.accept(self)
        result = self.lookUp(result, ctx)
        if result.type != Types.Bool:
            raise TypeError('Expr do not evaluate to a boolean.', ctx)
        return result.value

    def visitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        identifier = ctx.children[1].accept(self)
        structureName = ctx.children[2].accept(self)
        structure = self.lookUp(structureName, ctx)


        if structure.type not in [Types.Edge, Types.Vertex, Types.List]:
            raise ValueError('Type is wrong.', ctx)

        for i in range(0, len(structure.value)):
            self.getCurrentScope().set(identifier, structure.value[i].type, structure.value[i].value)
            retValue = ctx.children[3].accept(self)
            structure.value[i] = self.lookUp(identifier, ctx)
            if retValue is not None:
                self.getCurrentScope().delete(identifier)
                return retValue

        self.getCurrentScope().delete(identifier)

    def visitGraphAssignment(self, ctx:GraphParser.GraphAssignmentContext):
        identifier = ctx.children[0].symbol.text
        value = ctx.children[1].accept(self)

        self.getCurrentScope().set(identifier, value.type, value.value)

    def visitCompOp(self, ctx:GraphParser.CompOpContext):
        return ctx.children[0].symbol.text

    def strSubVars(self, mobj):
        key = mobj.group(1)[1:-1]
        return str(self.lookUp(key, None))

    def visitExpr(self, ctx:GraphParser.ExprContext):
        if ctx.getChildCount() == 1:
            value = ctx.children[0].accept(self)
            if type(value) is str and '\'' in value:
                value = value[1:-1]  # stripping ' of both ends
                try:
                    value = re.sub("(?<![\\\])({(?:[a-z]+[a-zA-Z0-9]*)\})", self.strSubVars, value)
                except KeyError:
                    raise KeyError('Variable name: {0} has not been declared in the scope.'.format(value), ctx)
                value = re.sub("(\\\)(?={(?:[a-z]+[a-zA-Z0-9]*)\})", '', value)
                value = ValueTypeTuple(value, Types.String)
            return value
        elif ctx.getChildCount() == 2:
            operator = ctx.children[0]

            if hasattr(operator, 'symbol'):
                operator = operator.symbol.text
            else:
                operator = operator.children[0].symbol.text

            right = self.getValue(ctx.children[1])

            if operator == '-':
                exprType = Types.Number

                self.checkType(ctx, right, Types.Number)

                result = -right.value
            elif operator == 'not':
                exprType = Types.Bool

                self.checkType(ctx, right, Types.Bool)

                result = not right.value

        elif ctx.getChildCount() == 3:
            operator = ctx.children[1]

            if hasattr(operator, 'symbol'):
                operator = operator.symbol.text
            else:
                operator = operator.children[0].symbol.text

            left = self.getValue(ctx.children[0])
            right = self.getValue(ctx.children[2])

            if operator == '+':
                exprType = Types.Number

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value + right.value
            elif operator == '-':
                exprType = Types.Number

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value - right.value
            elif operator == '*':
                exprType = Types.Number

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value * right.value
            elif operator == '/':
                exprType = Types.Number

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value / right.value
            elif operator == '%':
                exprType = Types.Number

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value % right.value
            elif operator == '^':
                exprType = Types.Number

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value**right.value
            elif operator == '<':
                exprType = Types.Bool

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value < right.value
            elif operator == '>':
                exprType = Types.Bool

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value > right.value
            elif operator == '<=':
                exprType = Types.Bool

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value <= right.value
            elif operator == '>=':
                exprType = Types.Bool

                self.checkTypes(ctx, left, right, Types.Number, Types.Number)

                result = left.value >= right.value
            elif operator == 'is':
                exprType = Types.Bool

                result = left.value == right.value
            elif operator == 'is not':
                exprType = Types.Bool

                result = left.value != right.value
            elif operator == 'and':
                exprType = Types.Bool

                self.checkTypes(ctx, left, right, Types.Bool, Types.Bool)

                result = left.value and right.value
            elif operator == 'or':
                exprType = Types.Bool

                self.checkTypes(ctx, left, right, Types.Bool, Types.Bool)

                result = left.value or right.value
            elif operator == 'in':
                exprType = Types.Bool

                self.checkType(ctx, right, Types.List)

                result = left.value in right.value
            elif operator == 'not in':
                exprType = Types.Bool

                self.checkType(ctx, right, Types.List)

                result = left.value not in right.value
            elif operator == 'union':
                exprType = Types.Graph

                self.checkTypes(ctx, left, right, Types.Graph, Types.Graph)

                result = self.union(left.value, right.value, ctx)
            elif operator == 'intersect':
                exprType = Types.Graph

                self.checkTypes(ctx, left, right, Types.Graph, Types.Graph)

                result = self.intersect(left.value, right.value, ctx)
            elif operator == 'diff':
                exprType = Types.Graph

                self.checkTypes(ctx, left, right, Types.Graph, Types.Graph)

                result = self.diff(left.value, right.value, ctx)
            elif operator == 'concat':
                exprType = Types.List

                self.checkTypes(ctx, left, right, Types.List, Types.List)

                result = left.value + right.value
            else:
                raise KeyError('Operator does not exist.', ctx)

        return ValueTypeTuple(result, exprType)

    def diff(self, left, right, ctx):
        graph = Graph()

        for vertex in left.vertices:
            if not self.vertexExistsInGraph(right, vertex, ctx):
                graph.vertices.append(vertex)

        for edge in left.edges:
            if not self.edgeExistsInGraph(right, edge):
                graph.edges.append(edge)

        return graph

    def intersect(self, left, right, ctx):
        graph = Graph()

        for vertex in left.vertices:
            if self.vertexExistsInGraph(right, vertex, ctx):
                graph.vertices.append(vertex)

        for edge in left.edges:
            if self.edgeExistsInGraph(right, edge):
                graph.edges.append(edge)

        return graph

    def union(self, left, right, ctx):
        graph = Graph()

        for vertex in left.vertices:
            graph.vertices.append(vertex)

        for vertex in right.vertices:
            if not self.vertexExistsInGraph(graph, vertex, ctx):
                graph.vertices.append(vertex)

        for edge in left.edges:
            graph.edges.append(edge)

        for edge in right.edges:
            if not self.edgeExistsInGraph(graph, edge):
                graph.edges.append(edge)

        return graph

    def vertexExistsInGraph(self, graph, vertex, ctx):
        for v in graph.vertices:
            if vertex.value['name'].value == v.value['name'].value:
                if vertex != v:
                    raise NameError('Vertices has the same name but is not equals.', ctx)
                return True
        return False

    def edgeExistsInGraph(self, graph, edge):
        for e in graph.edges:
            if edge == e:
                return True
        return False

    def checkTypes(self, ctx, left, right, leftType, rightType):
        if left.type != leftType or right.type != rightType:
            error = 'Types do not match in expression on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error, ctx)

    def checkType(self, ctx, val, valType):
        if val.type != valType:
            error = 'Incorrect type on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error, ctx)

    def checkTypeList(self, ctx, val, typeList):
        if val.type not in typeList:
            error = 'Incorrect type on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error, ctx)

    def getValue(self, ctx):
        val = ctx.accept(self)
        return self.lookUp(val, ctx)

    def visitSetOp(self, ctx:GraphParser.SetOpContext):
        return ctx.children[0].symbol.text

    def visitFactorOp(self, ctx:GraphParser.FactorOpContext):
        return ctx.children[0].symbol.text

    def visitMolecule(self, ctx:GraphParser.MoleculeContext):
        if ctx.getChildCount() > 1:
            identifier = ctx.children[0].accept(self)
            structure = self.lookUp(identifier, ctx)
            index = self.lookUp(ctx.children[1].children[0].accept(self), ctx)

            if structure.type == Types.List:
                if index.type != Types.Number:
                    error = 'Value is not of type number ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                    raise TypeError(error, ctx)
                if isinstance(ctx.parentCtx, GraphParser.AssignmentContext):
                    value = ValueTypeTuple(Molecule(identifier, index), Types.Molecule)
                else:
                    value = structure.value[int(index.value)]
            elif structure.type in ['vertex', 'edge']:
                if index.type != Types.String:
                    error = 'Value is not of type string ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                    raise TypeError(error, ctx)

                if isinstance(ctx.parentCtx, GraphParser.AssignmentContext):
                    if index.value == 'name':
                        raise KeyError('You can not rename a vertex.', ctx)
                    value = ValueTypeTuple(Molecule(identifier, index), Types.Molecule)
                else:
                    value = structure.value[index.value]
            else:
                error = 'Value is not of type edge or vertex ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                raise TypeError(error, ctx)

            return value

        return self.visitChildren(ctx)

    def visitAtom(self, ctx:GraphParser.AtomContext):
        if hasattr(ctx.children[0], 'symbol'):
            return ctx.children[0].symbol.text
        else:
            return self.visitChildren(ctx)

    def visitFuncCall(self, ctx:GraphParser.FuncCallContext):
        funcName = ctx.children[0].symbol.text

        if funcName == 'Print':
            input = ctx.children[1].accept(self)
            print(str(input.value))
        elif funcName == 'Length':
            result = self.getLength(ctx)

            return result
        elif funcName == 'GetVertex':
            result = copy.deepcopy(self.getVertex(ctx))

            return result
        elif funcName == 'GetVertices':
            result = copy.deepcopy(self.getVertices(ctx))

            return result
        elif funcName == 'GetEdges':
            result = copy.deepcopy(self.getEdges(ctx))

            return result
        elif funcName == 'GetEdgesFrom':
            result = copy.deepcopy(self.getEdgesFrom(ctx))

            return result
        elif funcName == 'GetEdgesTo':
            result = copy.deepcopy(self.getEdgesTo(ctx))

            return result
        elif funcName == 'GetEdgesFromTo':
            result = copy.deepcopy(self.getEdgesFromTo(ctx))

            return result
        elif funcName == 'VerticesAdjacentTo':
            result = copy.deepcopy(self.verticesAdjacentTo(ctx))

            return result
        elif funcName == 'SetVertex':
            result = copy.deepcopy(self.setVertex(ctx))

            return result
        elif funcName == 'SetVertices':
            result = copy.deepcopy(self.setVertices(ctx))

            return result
        elif funcName == 'SetEdges':
            result = copy.deepcopy(self.setEdges(ctx))

            return result
        elif funcName in self.envF:
            result = copy.deepcopy(self.visitDefinedFunction(ctx, funcName))

            if not isinstance(ctx.parentCtx, GraphParser.SimpleStmtContext):
                return result
        else:
            raise ModuleNotFoundError('Function: ' + funcName + ' do not exist.', ctx)

    def setVertex(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 2:
            raise ValueError('GetVertices requires 2 parameters. A graph and a list of vertices.', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[1].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[0].value.type != Types.Graph:
            raise TypeError('The second parameter has to be a graph.', ctx)
        if params[1].value.type != Types.Vertex:
            raise TypeError('The second parameter has to be a vertex.', ctx)

        graph = copy.deepcopy(params[0].value)
        vertex = copy.deepcopy(params[1].value)
        graph.value = graph.value.setVertex(vertex)

        return graph

    def setVertices(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 2:
            raise ValueError('GetVertices requires 2 parameters. A graph and a list of vertices.', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[1].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[0].value.type != Types.Graph:
            raise TypeError('The second parameter has to be a graph.', ctx)
        if params[1].value.type != Types.List:
            raise TypeError('The second parameter has to be a list.', ctx)

        for e in params[1].value.value:
            if e.type != Types.Vertex:
                raise TypeError('The second parameter has to be a list containing only vertices.', ctx)

        graph = copy.deepcopy(params[0].value)
        graph.value.vertices = params[1].value.value

        return graph

    def setEdges(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 2:
            raise ValueError('GetVertices requires 2 parameters. A graph and a list of edges.', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[1].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[0].value.type != Types.Graph:
            raise TypeError('The second parameter has to be a graph.', ctx)
        if params[1].value.type != Types.List:
            raise TypeError('The second parameter has to be a list.', ctx)

        for e in params[1].value.value:
            if e.type != Types.Edge:
                raise TypeError('The second parameter has to be a list containing only edges.', ctx)

        graph = copy.deepcopy(params[0].value)
        graph.value.edges = params[1].value.value

        return graph

    def getLength(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 1:
            raise ValueError('Length requires 1 parameter. A list, vertex, edge or a string.', ctx)

        input = params[0].value
        self.checkTypeList(ctx, input, [Types.Vertex, Types.List, Types.Edge, Types.String])

        return ValueTypeTuple(len(input.value), Types.Number)

    def verticesAdjacentTo(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 2:
            raise ValueError('GetVertex requires 2 parameters a graph and a name', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)

        graph = params[0].value
        self.checkType(ctx, graph, Types.Graph)

        vertex = params[1].value
        self.checkType(ctx, vertex, Types.String)

        vertices = graph.value.verticesAdjacentTo(vertex)

        return ValueTypeTuple(vertices, Types.List)

    def getVertex(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 2:
            raise ValueError('GetVertex requires 2 parameters a graph and a name', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)

        graph = params[0].value
        self.checkType(ctx, graph, Types.Graph)

        vertex = params[1].value
        self.checkType(ctx, vertex, Types.String)

        return graph.value.getVertex(vertex)

    def getVertices(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 1:
            raise ValueError('GetVertices requires 1 parameter. A graph.', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)

        graph = params[0].value
        self.checkType(ctx, graph, Types.Graph)

        return ValueTypeTuple(graph.value.vertices, Types.List)

    def getEdges(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 1:
            raise ValueError('GetEdges requires 1 parameter. A graph.', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)

        graph = params[0].value
        self.checkType(ctx, graph, Types.Graph)

        return ValueTypeTuple(graph.value.edges, Types.List)

    def getEdgesFrom(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 2:
            raise ValueError('GetVertex requires 2 parameters a graph and a name', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)


        graph = params[0].value
        self.checkType(ctx, graph, Types.Graph)

        vertex = params[1].value
        self.checkType(ctx, vertex, Types.String)

        edges = graph.value.getEdgesFrom(vertex)

        return ValueTypeTuple(edges, Types.List)

    def getEdgesTo(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 2:
            raise ValueError('GetVertex requires 2 parameters a graph and a name', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)

        graph = params[0].value
        self.checkType(ctx, graph, Types.Graph)

        vertex = params[1].value
        self.checkType(ctx, vertex, Types.String)

        edges = graph.value.getEdgesTo(vertex)

        return ValueTypeTuple(edges, Types.List)

    def getEdgesFromTo(self, ctx):
        params = self.getActualParams(ctx)
        if len(params) != 3:
            raise ValueError('GetVertex requires 3 parameters a graph and a name', ctx)
        if params[0].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[1].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[2].type != Types.Value:
            raise TypeError('This methods do not take a ref as input.', ctx)
        if params[0].value.type != Types.Graph:
            raise TypeError('The first parameter has to contain a graph', ctx)
        if params[1].value.type != Types.String:
            raise TypeError('The second and third parameter has to be vertices.', ctx)
        if params[2].value.type != Types.String:
            raise TypeError('The second and third parameter has to be vertices.', ctx)


        graph = params[0].value
        vertexFrom = params[1].value
        vertexTo = params[2].value

        edges = graph.value.getEdgesFromTo(vertexFrom, vertexTo)

        return ValueTypeTuple(edges, Types.List)

    def visitDefinedFunction(self, ctx, funcName):
        funcDef = self.envF[funcName]

        actualParams = self.getActualParams(ctx)
        formalParams = self.getFormalParams(funcDef)

        if len(formalParams) != len(actualParams):
            raise ValueError('Formal parameters and actual parameters is not the same amount in function: ' + funcName, ctx)

        mappedParams = self.mapParams(formalParams, actualParams)

        currentScope = self.getCurrentScope()

        self.newScope()

        self.insertParamsInNewScope(mappedParams, currentScope)

        blockCtx = funcDef.children[funcDef.getChildCount() - 1]
        result = self.visitBlock(blockCtx)

        result = self.lookUp(result, ctx)

        self.closeScope()

        return result

    def insertParamsInNewScope(self, params, oldScope):
        currentScope = self.getCurrentScope()
        for i in range(0, len(params.formal)):
            if params.actual[i].type == Types.Ref:
                currentScope.set(params.formal[i], params.actual[i].type, None, oldScope, params.actual[i].value)
            else:
                currentScope.set(params.formal[i], params.actual[i].value.type, params.actual[i].value.value)

    def mapParams(self, formalParams, actualParams):
        formalNames = []

        for param in range(0, len(formalParams)):
            formalNames.append(formalParams[param].symbol.text)

        return FormalActualTuple(formalNames, actualParams)

    def getActualParams(self, ctx):
        if ctx.getChildCount() == 2:
            actualParams = []
            params = ctx.children[1].children
            count = len(params)
            index = 0

            while index < count:
                if isinstance(params[index], Tree.TerminalNodeImpl) and params[index].symbol.text == 'ref':
                    index += 1
                    if not hasattr(params[index], 'symbol'):
                        raise TypeError('You can only ref variables.', ctx)

                    actualParam = params[index].symbol.text
                    actualParams.append(ValueTypeTuple(actualParam, Types.Ref))
                    index += 1
                else:
                    actualParam = self.lookUp(params[index].accept(self), ctx)
                    actualParams.append(ValueTypeTuple(actualParam, Types.Value))
                    index += 1
        else:
            actualParams = []

        return actualParams

    def getFormalParams(self, ctx):
        if ctx.getChildCount() == 3:
            formalParams = ctx.children[1].children
        else:
            formalParams = []

        return formalParams

    def visitActualParams(self, ctx:GraphParser.ActualParamsContext):
        return self.visitChildren(ctx)

    def visitListStruct(self, ctx:GraphParser.ListStructContext):

        listStruct = []
        for expr in ctx.children:
            result = self.visitExpr(expr)
            result = self.lookUp(result, ctx)
            listStruct.append(result)

        return ValueTypeTuple(listStruct, Types.List)

    def visitRangerStruct(self, ctx:GraphParser.RangerStructContext):

        start = self.visitExpr(ctx.children[0])
        end = self.visitExpr(ctx.children[1])

        if start.type != Types.Number or end.type != Types.Number:
            error = 'Types do not match in test on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error, ctx)

        lowStart = int(start.value)
        highEnd = int(end.value) + 1

        if lowStart == highEnd:
            elem = ValueTypeTuple(float(start.value), Types.Number)
            return ValueTypeTuple([elem], Types.List)

        shouldReverse = False

        if lowStart > highEnd:
            lowStart = highEnd - 1
            highEnd = int(start.value) + 1
            shouldReverse = True

        ranger = []
        for i in range(lowStart, highEnd):
            ranger.append(ValueTypeTuple(float(i), Types.Number))

        if shouldReverse:
            ranger.reverse()

        return ValueTypeTuple(ranger, Types.List)

    def visitGraph(self, ctx:GraphParser.GraphContext):
        graph = Graph()
        vertexDecls = self.visitChildren(ctx)

        for vDecl in vertexDecls:
            vertex = vDecl.vertex
            dic = {'name': ValueTypeTuple(vertex, Types.String)}
            v = ValueTypeTuple(dic, Types.Vertex)
            if not self.vertexExistsInGraph(graph, v, ctx):
                graph.vertices.append(v)
            for eDecl in vDecl.edges:
                dic = {'name': ValueTypeTuple(eDecl.vertex, Types.String)}
                v = ValueTypeTuple(dic, Types.Vertex)
                if not self.vertexExistsInGraph(graph, v, ctx):
                    graph.vertices.append(v)

                if not eDecl.directed and vertex > eDecl.vertex:
                    edge = Edge(eDecl.vertex, vertex, eDecl.directed)
                else:
                    edge = Edge(vertex, eDecl.vertex, eDecl.directed)

                if eDecl.label is not None:
                    edge.labels['label'] = eDecl.label

                graph.edges.append(ValueTypeTuple(edge, Types.Edge))

        return ValueTypeTuple(graph, Types.Graph)

    def visitVertices(self, ctx:GraphParser.VerticesContext):
        vertexDecls = []
        for decl in ctx.children:
            vertexDecls.append(decl.accept(self))

        return vertexDecls

    def visitVertex(self, ctx:GraphParser.VertexContext):
        vertex = ctx.children[0].accept(self)
        if vertex.type != Types.String:
            raise TypeError('Vertex name is not a string', ctx)

        if ctx.getChildCount() == 1:
            vertexDecl = VertexDecleration(vertex.value, [])
        else:
            vertexDecl = VertexDecleration(vertex.value, ctx.children[1].accept(self))
        return vertexDecl

    def visitEdges(self, ctx:GraphParser.EdgesContext):
        edges = []
        for edge in ctx.children:
            edges.append(edge.accept(self))
        return edges

    def visitEdge(self, ctx:GraphParser.EdgeContext):
        directed = False
        label = None

        count = ctx.getChildCount()

        if count == 1:
             vertex = self.getVertexName(ctx.children[0].accept(self), ctx)
        elif count == 2:
            if hasattr(ctx.children[0], 'symbol'):
                directed = True
                vertex = self.getVertexName(ctx.children[1].accept(self), ctx)
            else:
                vertex = self.getVertexName(ctx.children[0].accept(self), ctx)
                label = ctx.children[1].accept(self)
        else:
            directed = True
            vertex = self.getVertexName(ctx.children[1].accept(self), ctx)
            label = ctx.children[2].accept(self)

        return EdgeDecleration(directed, vertex, label)

    def getVertexName(self, vertex, ctx):
        if vertex.type != Types.String:
            raise TypeError('Edge name is not a string.', ctx)

        return vertex.value

    def visitIdentifier(self, ctx:GraphParser.IdentifierContext):
        return ctx.getText()

    def visitNumber(self, ctx:GraphParser.NumberContext):
        return ValueTypeTuple(self.isNumber(ctx.getText()), Types.Number)

    def visitBoolean(self, ctx:GraphParser.BooleanContext):
        return ValueTypeTuple(ctx.getText() == 'True', Types.Bool)

    def isNumber(self, value):
        number = float(value)
        return number


    def lookUp(self, value, ctx):
        if type(value) is str:
            try:
                entry = self.getCurrentScope().get(value)
            except Exception as e:
                raise KeyError('Variable name: {0} has not been declared in the scope.'.format(value), ctx)
            value = ValueTypeTuple(entry['value'], entry['type'])

        return value

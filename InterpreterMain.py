# Generated from Graph.g4 by ANTLR 4.7
import re

from InterpreterClasses import *
from antlr4 import *

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
            raise ValueError()

        if hasattr(identifier, 'value') and isinstance(identifier.value, Molecule):
            molecule = identifier.value
            list = self.getCurrentScope().get(molecule.atom)
            list['value'][molecule.trailer] = value
            print('Hallo')
        else:
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
        if result.type != Types.Bool:
            raise TypeError('Expr do not evaluate to a boolean.')
        return result.value


    def visitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        identifier = ctx.children[1].accept(self)
        structure = ctx.children[2].accept(self)
        structure = self.lookUp(structure)

        if structure.type not in [Types.Edge, Types.Vertex, Types.List]:
            raise ValueError('Type is wrong.')
        for ele in structure.value:
            self.getCurrentScope().set(identifier, ele.type, ele.value)
            retValue = ctx.children[3].accept(self)
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
        return str(self.lookUp(key))


    def visitExpr(self, ctx:GraphParser.ExprContext):
        if ctx.getChildCount() == 1:
            value = ctx.children[0].accept(self)
            if type(value) is str and '\'' in value:
                value = value[1:-1]  # stripping ' of both ends
                value = re.sub("(?<![\\\])({(?:[a-z]+[a-zA-Z0-9]*)\})", self.strSubVars, value)
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
            else:
                raise KeyError('Operator do not exist.')

        return ValueTypeTuple(result, exprType)


    def checkTypes(self, ctx, left, right, leftType, rightType):
        if left.type != leftType or right.type != rightType:
            error = 'Types do not match in expression on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error)

    def checkType(self, ctx, val, valType):
        if val.type != valType:
            error = 'Incorrect type on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error)

    def getValue(self, ctx):
        val = ctx.accept(self)
        return self.lookUp(val)


    def visitSetOp(self, ctx:GraphParser.SetOpContext):
        return ctx.children[0].symbol.text


    def visitFactorOp(self, ctx:GraphParser.FactorOpContext):
        return ctx.children[0].symbol.text


    def visitMolecule(self, ctx:GraphParser.MoleculeContext):
        if ctx.getChildCount() > 1:
            identifier = ctx.children[0].accept(self)
            structure = self.lookUp(identifier)
            index = self.lookUp(ctx.children[1].children[0].accept(self))

            if structure.type == Types.List:
                if index.type != Types.Number:
                    error = 'Value is not of type number ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                    raise TypeError(error)
                if isinstance(ctx.parentCtx, GraphParser.AssignmentContext):
                    value = ValueTypeTuple(Molecule(identifier, index), Types.Molecule)
                else:
                    value = structure.value[int(index.value)]
            elif structure.type in ['vertex', 'edge']:
                if index.type != Types.String:
                    error = 'Value is not of type string ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                    raise TypeError(error)

                if isinstance(ctx.parentCtx, GraphParser.AssignmentContext):
                    if index.value == 'name':
                        raise KeyError('You can not rename a vertex.')
                    value = ValueTypeTuple(Molecule(identifier, index), Types.Molecule)
                else:
                    value = structure.value[index.value]
            else:
                error = 'Value is not of type edge or vertex ' + str(ctx.start.line) + ':' + str(ctx.start.column)
                raise TypeError(error)

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
        elif funcName == 'GetVertex':
            params = self.getActualParams(ctx)
            if len(params) != 2:
                raise ValueError('GetVertex requires 2 parameters a graph and a name')

            graph = self.lookUp(params[0].accept(self))
            if graph.type != Types.Graph:
                raise TypeError('First parameter is not of type graph.')
            vertex = params[1].accept(self)
            if vertex.type != Types.String:
                raise TypeError('Second parameter is not of type string.')

            result = graph.value.getVertex(vertex)

            return result
        elif funcName in self.envF:
            result = self.visitDefinedFunction(ctx, funcName)

            if not isinstance(ctx.parentCtx, GraphParser.SimpleStmtContext):
                return result
        else:
            raise ModuleNotFoundError('Function: ' + funcName + ' do not exist.')


    def visitDefinedFunction(self, ctx, funcName):
        funcDef = self.envF[funcName]

        actualParams = self.getActualParams(ctx)
        formalParams = self.getFormalParams(funcDef)

        if len(formalParams) != len(actualParams):
            raise ValueError('Formal parameters and actual parameters is not the same amount in function: ' + funcName)

        mappedParams = self.mapParams(formalParams, actualParams)

        self.newScope()

        self.insertParamsInNewScope(mappedParams)

        blockCtx = funcDef.children[funcDef.getChildCount() - 1]
        result = self.visitBlock(blockCtx)

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


    def visitActualParams(self, ctx:GraphParser.ActualParamsContext):
        return self.visitChildren(ctx)


    def visitListStruct(self, ctx:GraphParser.ListStructContext):

        listStruct = []
        for expr in ctx.children:
            result = self.visitExpr(expr)
            listStruct.append(result)

        return ValueTypeTuple(listStruct, Types.List)


    def visitRangerStruct(self, ctx:GraphParser.RangerStructContext):

        start = self.visitExpr(ctx.children[0])
        end = self.visitExpr(ctx.children[1])

        if start.type != Types.Number or end.type != Types.Number:
            error = 'Types do not match in test on line ' + str(ctx.start.line) + ':' + str(ctx.start.column)
            raise TypeError(error)

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
            if not self.vertexExistsInGraph(graph, vertex):
                dic = {'name': ValueTypeTuple(vertex, Types.String)}
                graph.vertices.append(ValueTypeTuple(dic, Types.Vertex))
            for eDecl in vDecl.edges:
                if not self.vertexExistsInGraph(graph, eDecl.vertex):
                    dic = {'name': ValueTypeTuple(eDecl.vertex, Types.String)}
                    graph.vertices.append(ValueTypeTuple(dic, Types.Vertex))

                if not eDecl.directed and vertex > eDecl.vertex:
                    edge = Edge(eDecl.vertex, vertex, eDecl.directed)
                else:
                    edge = Edge(vertex, eDecl.vertex, eDecl.directed)

                if eDecl.label is not None:
                    edge.labels['label'] = eDecl.label

                graph.edges.append(ValueTypeTuple(edge, Types.Edge))

        return ValueTypeTuple(graph, Types.Graph)

    def vertexExistsInGraph(self, graph, vertex):
        for v in graph.vertices:
            if vertex == v.value['name'].value:
                return True
        return False

    def visitVertices(self, ctx:GraphParser.VerticesContext):
        vertexDecls = []
        for decl in ctx.children:
            vertexDecls.append(decl.accept(self))

        return vertexDecls


    def visitVertex(self, ctx:GraphParser.VertexContext):
        vertex = ctx.children[0].accept(self)
        if vertex.type != Types.String:
            raise TypeError('Vertex name is not a string')

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
             vertex = self.getVertexName(ctx.children[0].accept(self))
        elif count == 2:
            if hasattr(ctx.children[0], 'symbol'):
                directed = True
                vertex = self.getVertexName(ctx.children[1].accept(self))
            else:
                vertex = self.getVertexName(ctx.children[0].accept(self))
                label = ctx.children[1].accept(self)
        else:
            directed = True
            vertex = self.getVertexName(ctx.children[1].accept(self))
            label = ctx.children[2].accept(self)

        return EdgeDecleration(directed, vertex, label)


    def getVertexName(self, vertex):
        if vertex.type != Types.String:
            raise TypeError('Edge name is not a string.')

        return vertex.value


    def visitIdentifier(self, ctx:GraphParser.IdentifierContext):
        return ctx.getText()


    def visitNumber(self, ctx:GraphParser.NumberContext):
        return ValueTypeTuple(self.isNumber(ctx.getText()), Types.Number)


    def visitBoolean(self, ctx:GraphParser.BooleanContext):
        return ValueTypeTuple(ctx.getText() == 'True', Types.Bool)


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

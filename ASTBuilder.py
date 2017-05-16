# Generated from Graph.g4 by ANTLR 4.7
from antlr4 import *
from antlr4.tree import Tree
import copy
if __name__ is not None and "." in __name__:
    from Antlr.GraphParser import GraphParser
else:
    from Antlr.GraphParser import GraphParser

# This class defines a complete generic visitor for a parse tree produced by GraphParser.

class ASTBuilder(ParseTreeVisitor):

    # Visit a parse tree produced by GraphParser#program.
    def visitProgram(self, ctx:GraphParser.ProgramContext):
        children = ctx.children
        count = len(children)

        del children[count - 1]
        del children[count - 3]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#funcDef.
    def visitFuncDef(self, ctx:GraphParser.FuncDefContext):
        children = ctx.children
        count = len(children)

        if count == 6:
            del children[0]
            del children[0]
            del children[1]
            del children[1]
        elif count == 7:
            del children[0]
            del children[0]
            del children[1]
            del children[2]
        else:
            raise ValueError('Det giver ingen mening!')

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#formalParams.
    def visitFormalParams(self, ctx:GraphParser.FormalParamsContext):
        children = ctx.children
        count = len(children)

        if count > 1:
            times = int((count - 1) / 3)
            for i in range(0, times):
                del children[1 + i]
                del children[1 + i]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#block.
    def visitBlock(self, ctx:GraphParser.BlockContext):
        children = ctx.children
        count = len(children)

        del children[count - 1]
        del children[0]
        del children[0]
        del children[0]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#stmt.
    def visitStmt(self, ctx:GraphParser.StmtContext):
        children = ctx.children
        count = len(children)

        if count == 2:
            del children[1]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#simpleStmt.
    def visitSimpleStmt(self, ctx:GraphParser.SimpleStmtContext):
        if len(ctx.children) is 3:
            del ctx.children[1]  # [ ]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#assignment.
    def visitAssignment(self, ctx:GraphParser.AssignmentContext):
        children = ctx.children
        count = len(children)

        del children[1]
        del children[1]
        del children[1]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#compoundStmt.
    def visitCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#ifStmt.
    def visitIfStmt(self, ctx:GraphParser.IfStmtContext):
        children = copy.copy(ctx.children)
        counter = 0

        for child in children:
            if isinstance(child, Tree.TerminalNodeImpl):
                del ctx.children[counter]
            else:
                counter += 1

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#whileStmt.
    def visitWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        children = ctx.children
        count = len(children)

        del children[1]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#foreachStmt.
    def visitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        children = ctx.children
        count = len(children)

        del children[5]
        del children[4]
        del children[3]
        del children[1]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graphAssignment.
    def visitGraphAssignment(self, ctx:GraphParser.GraphAssignmentContext):
        children = ctx.children
        count = len(children)

        del children[1]
        del children[1]
        del children[1]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#compOp.
    def visitCompOp(self, ctx:GraphParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#expr.
    def visitExpr(self, ctx:GraphParser.ExprContext):
        children = ctx.children
        count = len(children)

        if count > 1:
            del children[3]
            del children[1]
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#setOp.
    def visitSetOp(self, ctx:GraphParser.SetOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#factorOp.
    def visitFactorOp(self, ctx:GraphParser.FactorOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#molecule.
    def visitMolecule(self, ctx:GraphParser.MoleculeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#atom.
    def visitAtom(self, ctx:GraphParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#funcCall.
    def visitFuncCall(self, ctx:GraphParser.FuncCallContext):
        children = ctx.children
        count = len(children)

        if count == 3:
            del children[1]
            del children[1]
        elif count == 4:
            del children[1]
            del children[2]
        else:
            raise Exception('Something is not right!')

        return self.visitChildren(ctx)



    # Visit a parse tree produced by GraphParser#actualParams.
    def visitActualParams(self, ctx:GraphParser.ActualParamsContext):
        children = ctx.children
        count = len(children)

        if count > 1:
            times = int((count - 1) / 3)
            for i in range(0, times):
                del children[1 + i]
                del children[1 + i]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#listStruct.
    def visitListStruct(self, ctx:GraphParser.ListStructContext):
        children = ctx.children
        count = len(children)

        del children[count - 1]
        del children[0]

        if count > 1:
            times = int((count - 1) / 3)
            for i in range(0, times):
                del children[1 + i]
                del children[1 + i]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#rangerStruct.
    def visitRangerStruct(self, ctx:GraphParser.RangerStructContext):
        children = ctx.children
        count = len(children)

        del children[4]
        del children[2]
        del children[0]
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graph.
    def visitGraph(self, ctx:GraphParser.GraphContext):
        children = ctx.children

        del children[0] # graph
        del children[0] # :
        del children[0] # \r\n
        del children[0] # \r\n
        del children[1] # \r\n

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#vertices.
    def visitVertices(self, ctx:GraphParser.VerticesContext):
        children = ctx.children
        count = len(children)

        i = 1
        while count / 2 < len(children):
            del children[i]  # \r\n
            i += 1

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#vertex.
    def visitVertex(self, ctx:GraphParser.VertexContext):
        if len(ctx.children) > 2:
            del ctx.children[1]  # [ ]

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#edges.
    def visitEdges(self, ctx:GraphParser.EdgesContext):
        children = ctx.children
        count = len(children)

        i = 1
        while count / 3 < len(children) - 2:
            del children[i] # ,
            del children[i] # [ ]
            i += 1

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#edge.
    def visitEdge(self, ctx:GraphParser.EdgeContext):
        children = ctx.children
        count = len(children)

        del ctx.children[0]  # (

        if count is 3:
            del ctx.children[1]  # )
        elif count is 4:
            del ctx.children[2]  # )
        elif count is 5:
            del ctx.children[1]  # [ ]
            del ctx.children[2]  # )
        elif count is 6:
            del ctx.children[2]  # [ ]
            del ctx.children[3]  # )

        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#identifier.
    def visitIdentifier(self, ctx:GraphParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#number.
    def visitNumber(self, ctx:GraphParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#boolean.
    def visitBoolean(self, ctx:GraphParser.BooleanContext):
        return self.visitChildren(ctx)



del GraphParser
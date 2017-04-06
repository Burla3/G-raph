# Generated from ./Graph.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete generic visitor for a parse tree produced by GraphParser.

class GraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphParser#program.
    def visitProgram(self, ctx:GraphParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#procDef.
    def visitProcDef(self, ctx:GraphParser.ProcDefContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by GraphParser#compoundStmt.
    def visitCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#actualParams.
    def visitActualParams(self, ctx:GraphParser.ActualParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#assignment.
    def visitAssignment(self, ctx:GraphParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#flowStmt.
    def visitFlowStmt(self, ctx:GraphParser.FlowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#printStmt.
    def visitPrintStmt(self, ctx:GraphParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#breakStmt.
    def visitBreakStmt(self, ctx:GraphParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#continueStmt.
    def visitContinueStmt(self, ctx:GraphParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#returnStmt.
    def visitReturnStmt(self, ctx:GraphParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#ifStmt.
    def visitIfStmt(self, ctx:GraphParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#whileStmt.
    def visitWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#foreachStmt.
    def visitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#test.
    def visitTest(self, ctx:GraphParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#orTest.
    def visitOrTest(self, ctx:GraphParser.OrTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#andTest.
    def visitAndTest(self, ctx:GraphParser.AndTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#notTest.
    def visitNotTest(self, ctx:GraphParser.NotTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#comparison.
    def visitComparison(self, ctx:GraphParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#compOp.
    def visitCompOp(self, ctx:GraphParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#expression.
    def visitExpression(self, ctx:GraphParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#arithExpr.
    def visitArithExpr(self, ctx:GraphParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#term.
    def visitTerm(self, ctx:GraphParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#factorOp.
    def visitFactorOp(self, ctx:GraphParser.FactorOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#factor.
    def visitFactor(self, ctx:GraphParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#exponent.
    def visitExponent(self, ctx:GraphParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#atom.
    def visitAtom(self, ctx:GraphParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#trailer.
    def visitTrailer(self, ctx:GraphParser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graph.
    def visitGraph(self, ctx:GraphParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#vertices.
    def visitVertices(self, ctx:GraphParser.VerticesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#vertex.
    def visitVertex(self, ctx:GraphParser.VertexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#edges.
    def visitEdges(self, ctx:GraphParser.EdgesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#edge.
    def visitEdge(self, ctx:GraphParser.EdgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#name.
    def visitName(self, ctx:GraphParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#varId.
    def visitVarId(self, ctx:GraphParser.VarIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#procId.
    def visitProcId(self, ctx:GraphParser.ProcIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#letter.
    def visitLetter(self, ctx:GraphParser.LetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#ranger.
    def visitRanger(self, ctx:GraphParser.RangerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#integer.
    def visitInteger(self, ctx:GraphParser.IntegerContext):
        return self.visitChildren(ctx)



del GraphParser
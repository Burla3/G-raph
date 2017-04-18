# Generated from Graph.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete listener for a parse tree produced by GraphParser.
class GraphListener(ParseTreeListener):

    # Enter a parse tree produced by GraphParser#program.
    def enterProgram(self, ctx:GraphParser.ProgramContext):
        pass

    # Exit a parse tree produced by GraphParser#program.
    def exitProgram(self, ctx:GraphParser.ProgramContext):
        pass


    # Enter a parse tree produced by GraphParser#procDef.
    def enterProcDef(self, ctx:GraphParser.ProcDefContext):
        pass

    # Exit a parse tree produced by GraphParser#procDef.
    def exitProcDef(self, ctx:GraphParser.ProcDefContext):
        pass


    # Enter a parse tree produced by GraphParser#formalParams.
    def enterFormalParams(self, ctx:GraphParser.FormalParamsContext):
        pass

    # Exit a parse tree produced by GraphParser#formalParams.
    def exitFormalParams(self, ctx:GraphParser.FormalParamsContext):
        pass


    # Enter a parse tree produced by GraphParser#block.
    def enterBlock(self, ctx:GraphParser.BlockContext):
        pass

    # Exit a parse tree produced by GraphParser#block.
    def exitBlock(self, ctx:GraphParser.BlockContext):
        pass


    # Enter a parse tree produced by GraphParser#stmt.
    def enterStmt(self, ctx:GraphParser.StmtContext):
        pass

    # Exit a parse tree produced by GraphParser#stmt.
    def exitStmt(self, ctx:GraphParser.StmtContext):
        pass


    # Enter a parse tree produced by GraphParser#simpleStmt.
    def enterSimpleStmt(self, ctx:GraphParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by GraphParser#simpleStmt.
    def exitSimpleStmt(self, ctx:GraphParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by GraphParser#assignment.
    def enterAssignment(self, ctx:GraphParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GraphParser#assignment.
    def exitAssignment(self, ctx:GraphParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GraphParser#compoundStmt.
    def enterCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by GraphParser#compoundStmt.
    def exitCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        pass


    # Enter a parse tree produced by GraphParser#ifStmt.
    def enterIfStmt(self, ctx:GraphParser.IfStmtContext):
        pass

    # Exit a parse tree produced by GraphParser#ifStmt.
    def exitIfStmt(self, ctx:GraphParser.IfStmtContext):
        pass


    # Enter a parse tree produced by GraphParser#whileStmt.
    def enterWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by GraphParser#whileStmt.
    def exitWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by GraphParser#foreachStmt.
    def enterForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        pass

    # Exit a parse tree produced by GraphParser#foreachStmt.
    def exitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        pass


    # Enter a parse tree produced by GraphParser#graphAssignment.
    def enterGraphAssignment(self, ctx:GraphParser.GraphAssignmentContext):
        pass

    # Exit a parse tree produced by GraphParser#graphAssignment.
    def exitGraphAssignment(self, ctx:GraphParser.GraphAssignmentContext):
        pass


    # Enter a parse tree produced by GraphParser#test.
    def enterTest(self, ctx:GraphParser.TestContext):
        pass

    # Exit a parse tree produced by GraphParser#test.
    def exitTest(self, ctx:GraphParser.TestContext):
        pass


    # Enter a parse tree produced by GraphParser#compOp.
    def enterCompOp(self, ctx:GraphParser.CompOpContext):
        pass

    # Exit a parse tree produced by GraphParser#compOp.
    def exitCompOp(self, ctx:GraphParser.CompOpContext):
        pass


    # Enter a parse tree produced by GraphParser#expr.
    def enterExpr(self, ctx:GraphParser.ExprContext):
        pass

    # Exit a parse tree produced by GraphParser#expr.
    def exitExpr(self, ctx:GraphParser.ExprContext):
        pass


    # Enter a parse tree produced by GraphParser#setOp.
    def enterSetOp(self, ctx:GraphParser.SetOpContext):
        pass

    # Exit a parse tree produced by GraphParser#setOp.
    def exitSetOp(self, ctx:GraphParser.SetOpContext):
        pass


    # Enter a parse tree produced by GraphParser#factorOp.
    def enterFactorOp(self, ctx:GraphParser.FactorOpContext):
        pass

    # Exit a parse tree produced by GraphParser#factorOp.
    def exitFactorOp(self, ctx:GraphParser.FactorOpContext):
        pass


    # Enter a parse tree produced by GraphParser#molecule.
    def enterMolecule(self, ctx:GraphParser.MoleculeContext):
        pass

    # Exit a parse tree produced by GraphParser#molecule.
    def exitMolecule(self, ctx:GraphParser.MoleculeContext):
        pass


    # Enter a parse tree produced by GraphParser#atom.
    def enterAtom(self, ctx:GraphParser.AtomContext):
        pass

    # Exit a parse tree produced by GraphParser#atom.
    def exitAtom(self, ctx:GraphParser.AtomContext):
        pass


    # Enter a parse tree produced by GraphParser#trailer.
    def enterTrailer(self, ctx:GraphParser.TrailerContext):
        pass

    # Exit a parse tree produced by GraphParser#trailer.
    def exitTrailer(self, ctx:GraphParser.TrailerContext):
        pass


    # Enter a parse tree produced by GraphParser#procCall.
    def enterProcCall(self, ctx:GraphParser.ProcCallContext):
        pass

    # Exit a parse tree produced by GraphParser#procCall.
    def exitProcCall(self, ctx:GraphParser.ProcCallContext):
        pass


    # Enter a parse tree produced by GraphParser#actualParams.
    def enterActualParams(self, ctx:GraphParser.ActualParamsContext):
        pass

    # Exit a parse tree produced by GraphParser#actualParams.
    def exitActualParams(self, ctx:GraphParser.ActualParamsContext):
        pass


    # Enter a parse tree produced by GraphParser#listStruct.
    def enterListStruct(self, ctx:GraphParser.ListStructContext):
        pass

    # Exit a parse tree produced by GraphParser#listStruct.
    def exitListStruct(self, ctx:GraphParser.ListStructContext):
        pass


    # Enter a parse tree produced by GraphParser#rangerStruct.
    def enterRangerStruct(self, ctx:GraphParser.RangerStructContext):
        pass

    # Exit a parse tree produced by GraphParser#rangerStruct.
    def exitRangerStruct(self, ctx:GraphParser.RangerStructContext):
        pass


    # Enter a parse tree produced by GraphParser#graph.
    def enterGraph(self, ctx:GraphParser.GraphContext):
        pass

    # Exit a parse tree produced by GraphParser#graph.
    def exitGraph(self, ctx:GraphParser.GraphContext):
        pass


    # Enter a parse tree produced by GraphParser#vertices.
    def enterVertices(self, ctx:GraphParser.VerticesContext):
        pass

    # Exit a parse tree produced by GraphParser#vertices.
    def exitVertices(self, ctx:GraphParser.VerticesContext):
        pass


    # Enter a parse tree produced by GraphParser#vertex.
    def enterVertex(self, ctx:GraphParser.VertexContext):
        pass

    # Exit a parse tree produced by GraphParser#vertex.
    def exitVertex(self, ctx:GraphParser.VertexContext):
        pass


    # Enter a parse tree produced by GraphParser#edges.
    def enterEdges(self, ctx:GraphParser.EdgesContext):
        pass

    # Exit a parse tree produced by GraphParser#edges.
    def exitEdges(self, ctx:GraphParser.EdgesContext):
        pass


    # Enter a parse tree produced by GraphParser#edge.
    def enterEdge(self, ctx:GraphParser.EdgeContext):
        pass

    # Exit a parse tree produced by GraphParser#edge.
    def exitEdge(self, ctx:GraphParser.EdgeContext):
        pass


    # Enter a parse tree produced by GraphParser#identifier.
    def enterIdentifier(self, ctx:GraphParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GraphParser#identifier.
    def exitIdentifier(self, ctx:GraphParser.IdentifierContext):
        pass


    # Enter a parse tree produced by GraphParser#number.
    def enterNumber(self, ctx:GraphParser.NumberContext):
        pass

    # Exit a parse tree produced by GraphParser#number.
    def exitNumber(self, ctx:GraphParser.NumberContext):
        pass


    # Enter a parse tree produced by GraphParser#boolean.
    def enterBoolean(self, ctx:GraphParser.BooleanContext):
        pass

    # Exit a parse tree produced by GraphParser#boolean.
    def exitBoolean(self, ctx:GraphParser.BooleanContext):
        pass



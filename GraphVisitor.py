from ContextualAnalysis import ScopeChecker
from ContextualAnalysis import TypeChecker
from CodeGeneration import CodeGenerator

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

class GraphVisitor(ParseTreeVisitor):

    def visitProgram(self, ctx:GraphParser.ProgramContext):
        ScopeChecker.checkProgram()
        TypeChecker.checkProgram()
        CodeGenerator.generateProgram()
        return self.visitChildren(ctx)

    def visitProcDef(self, ctx:GraphParser.ProcDefContext):
        ScopeChecker.checkProcDef()
        TypeChecker.checkProcDef()
        CodeGenerator.generateProcDef()
        return self.visitChildren(ctx)

    def visitFormalParams(self, ctx:GraphParser.FormalParamsContext):
        ScopeChecker.checkFormalParams()
        TypeChecker.checkFormalParams()
        CodeGenerator.generateFormalParams()
        return self.visitChildren(ctx)

    def visitBlock(self, ctx:GraphParser.BlockContext):
        ScopeChecker.checkBlock()
        TypeChecker.checkBlock()
        CodeGenerator.generateBlock()
        return self.visitChildren(ctx)

    def visitStmt(self, ctx:GraphParser.StmtContext):
        ScopeChecker.checkStmt()
        TypeChecker.checkStmt()
        CodeGenerator.generateStmt()
        return self.visitChildren(ctx)

    def visitSimpleStmt(self, ctx:GraphParser.SimpleStmtContext):
        ScopeChecker.checkSimpleStmt()
        TypeChecker.checkSimpleStmt()
        CodeGenerator.generateSimpleStmt()
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx:GraphParser.AssignmentContext):
        ScopeChecker.checkAssignment()
        TypeChecker.checkAssignment()
        CodeGenerator.generateAssignment()
        return self.visitChildren(ctx)

    def visitPrintStmt(self, ctx:GraphParser.PrintStmtContext):
        ScopeChecker.checkPrintStmt()
        TypeChecker.checkPrintStmt()
        CodeGenerator.generatePrintStmt()
        return self.visitChildren(ctx)

    def visitLengthStmt(self, ctx:GraphParser.LengthStmtContext):
        ScopeChecker.checkLengthStmt()
        TypeChecker.checkLengthStmt()
        CodeGenerator.generateLengthStmt()
        return self.visitChildren(ctx)

    def visitCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        ScopeChecker.checkCompoundStmt()
        TypeChecker.checkCompoundStmt()
        CodeGenerator.generateCompoundStmt()
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx:GraphParser.IfStmtContext):
        ScopeChecker.checkIfStmt()
        TypeChecker.checkIfStmt()
        CodeGenerator.generateIfStmt()
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        ScopeChecker.checkWhileStmt()
        TypeChecker.checkWhileStmt()
        CodeGenerator.generateWhileStmt()
        return self.visitChildren(ctx)

    def visitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        ScopeChecker.checkForeachStmt()
        TypeChecker.checkForeachStmt()
        CodeGenerator.generateForeachStmt()
        return self.visitChildren(ctx)

    def visitGraphAssignment(self, ctx:GraphParser.GraphAssignmentContext):
        ScopeChecker.checkGraphAssignment()
        TypeChecker.checkGraphAssignment()
        CodeGenerator.generateGraphAssignment()
        return self.visitChildren(ctx)

    def visitTest(self, ctx:GraphParser.TestContext):
        ScopeChecker.checkTest()
        TypeChecker.checkTest()
        CodeGenerator.generateTest()
        return self.visitChildren(ctx)

    def visitCompOp(self, ctx:GraphParser.CompOpContext):
        ScopeChecker.checkCompOp()
        TypeChecker.checkCompOp()
        CodeGenerator.generateCompOp()
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:GraphParser.ExprContext):
        ScopeChecker.checkExpr()
        TypeChecker.checkExpr()
        CodeGenerator.generateExpr()
        return self.visitChildren(ctx)

    def visitSetOp(self, ctx:GraphParser.SetOpContext):
        ScopeChecker.checkSetOp()
        TypeChecker.checkSetOp()
        CodeGenerator.generateSetOp()
        return self.visitChildren(ctx)

    def visitFactorOp(self, ctx:GraphParser.FactorOpContext):
        ScopeChecker.checkFactorOp()
        TypeChecker.checkFactorOp()
        CodeGenerator.generateFactorOp()
        return self.visitChildren(ctx)

    def visitMolecule(self, ctx:GraphParser.MoleculeContext):
        ScopeChecker.checkMolecule()
        TypeChecker.checkMolecule()
        CodeGenerator.generateMolecule()
        return self.visitChildren(ctx)

    def visitAtom(self, ctx:GraphParser.AtomContext):
        ScopeChecker.checkAtom()
        TypeChecker.checkAtom()
        CodeGenerator.generateAtom()
        return self.visitChildren(ctx)

    def visitTrailer(self, ctx:GraphParser.TrailerContext):
        ScopeChecker.checkTrailer()
        TypeChecker.checkTrailer()
        CodeGenerator.generateTrailer()
        return self.visitChildren(ctx)

    def visitFuncCall(self, ctx:GraphParser.FuncCallContext):
        ScopeChecker.checkFuncCall()
        TypeChecker.checkFuncCall()
        CodeGenerator.generateFuncCall()
        return self.visitChildren(ctx)

    def visitGraphKeyword(self, ctx:GraphParser.GraphKeywordContext):
        ScopeChecker.checkGraphKeyword()
        TypeChecker.checkGraphKeyword()
        CodeGenerator.generateGraphKeyword()
        return self.visitChildren(ctx)

    def visitActualParams(self, ctx:GraphParser.ActualParamsContext):
        ScopeChecker.checkActualParams()
        TypeChecker.checkActualParams()
        CodeGenerator.generateActualParams()
        return self.visitChildren(ctx)

    def visitListStruct(self, ctx:GraphParser.ListStructContext):
        ScopeChecker.checkListStruct()
        TypeChecker.checkListStruct()
        CodeGenerator.generateListStruct()
        return self.visitChildren(ctx)

    def visitGraph(self, ctx:GraphParser.GraphContext):
        ScopeChecker.checkGraph()
        TypeChecker.checkGraph()
        CodeGenerator.generateGraph()
        return self.visitChildren(ctx)

    def visitVertices(self, ctx:GraphParser.VerticesContext):
        ScopeChecker.checkVertices()
        TypeChecker.checkVertices()
        CodeGenerator.generateVertices()
        return self.visitChildren(ctx)

    def visitVertex(self, ctx:GraphParser.VertexContext):
        ScopeChecker.checkVertex()
        TypeChecker.checkVertex()
        CodeGenerator.generateVertex()
        return self.visitChildren(ctx)

    def visitEdges(self, ctx:GraphParser.EdgesContext):
        ScopeChecker.checkEdges()
        TypeChecker.checkEdges()
        CodeGenerator.generateEdges()
        return self.visitChildren(ctx)

    def visitEdge(self, ctx:GraphParser.EdgeContext):
        ScopeChecker.checkEdge()
        TypeChecker.checkEdge()
        CodeGenerator.generateEdge()
        return self.visitChildren(ctx)

    def visitIdentifier(self, ctx:GraphParser.IdentifierContext):
        ScopeChecker.checkIdentifier()
        TypeChecker.checkIdentifier()
        CodeGenerator.generateIdentifier()
        return self.visitChildren(ctx)

    def visitNumber(self, ctx:GraphParser.NumberContext):
        ScopeChecker.checkNumber()
        TypeChecker.checkNumber()
        CodeGenerator.generateNumber()
        return self.visitChildren(ctx)

    def visitBoolean(self, ctx:GraphParser.BooleanContext):
        ScopeChecker.checkBoolean()
        TypeChecker.checkBoolean()
        CodeGenerator.generateBoolean()
        return self.visitChildren(ctx)



del GraphParser
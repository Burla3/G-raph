from Template.CodeGenerator import CodeGenerator
from Template.DeclarationProcessor import DeclarationProcessor
from Template.ScopeChecker import ScopeChecker
from antlr4 import *

from MuligvisSkrald.Template.TypeChecker import TypeChecker

if __name__ is not None and "." in __name__:
    from Antlr.GraphParser import GraphParser
else:
    from Antlr.GraphParser import GraphParser

class GraphVisitor(ParseTreeVisitor):

    def visitProgram(self, ctx:GraphParser.ProgramContext):
        DeclarationProcessor.processProgram()
        ScopeChecker.checkProgram()
        TypeChecker.checkProgram()
        CodeGenerator.generateProgram()
        return self.visitChildren(ctx)

    def visitFuncDef(self, ctx:GraphParser.FuncDefContext):
        DeclarationProcessor.processFuncDef()
        ScopeChecker.checkFuncDef()
        TypeChecker.checkFuncDef()
        CodeGenerator.generateFuncDef()
        return self.visitChildren(ctx)

    def visitFormalParams(self, ctx:GraphParser.FormalParamsContext):
        DeclarationProcessor.processFormalParams()
        ScopeChecker.checkFormalParams()
        TypeChecker.checkFormalParams()
        CodeGenerator.generateFormalParams()
        return self.visitChildren(ctx)

    def visitBlock(self, ctx:GraphParser.BlockContext):
        DeclarationProcessor.processBlock()
        ScopeChecker.checkBlock()
        TypeChecker.checkBlock()
        CodeGenerator.generateBlock()
        return self.visitChildren(ctx)

    def visitStmt(self, ctx:GraphParser.StmtContext):
        DeclarationProcessor.processStmt()
        ScopeChecker.checkStmt()
        TypeChecker.checkStmt()
        CodeGenerator.generateStmt()
        return self.visitChildren(ctx)

    def visitSimpleStmt(self, ctx:GraphParser.SimpleStmtContext):
        DeclarationProcessor.processSimpleStmt()
        ScopeChecker.checkSimpleStmt()
        TypeChecker.checkSimpleStmt()
        CodeGenerator.generateSimpleStmt()
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx:GraphParser.AssignmentContext):
        DeclarationProcessor.processAssignment()
        ScopeChecker.checkAssignment()
        TypeChecker.checkAssignment()
        CodeGenerator.generateAssignment()
        return self.visitChildren(ctx)

    def visitCompoundStmt(self, ctx:GraphParser.CompoundStmtContext):
        DeclarationProcessor.processCompoundStmt()
        ScopeChecker.checkCompoundStmt()
        TypeChecker.checkCompoundStmt()
        CodeGenerator.generateCompoundStmt()
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx:GraphParser.IfStmtContext):
        DeclarationProcessor.processIfStmt()
        ScopeChecker.checkIfStmt()
        TypeChecker.checkIfStmt()
        CodeGenerator.generateIfStmt()
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx:GraphParser.WhileStmtContext):
        DeclarationProcessor.processWhileStmt()
        ScopeChecker.checkWhileStmt()
        TypeChecker.checkWhileStmt()
        CodeGenerator.generateWhileStmt()
        return self.visitChildren(ctx)

    def visitForeachStmt(self, ctx:GraphParser.ForeachStmtContext):
        DeclarationProcessor.processForeachStmt()
        ScopeChecker.checkForeachStmt()
        TypeChecker.checkForeachStmt()
        CodeGenerator.generateForeachStmt()
        return self.visitChildren(ctx)

    def visitGraphAssignment(self, ctx:GraphParser.GraphAssignmentContext):
        DeclarationProcessor.processGraphAssignment()
        ScopeChecker.checkGraphAssignment()
        TypeChecker.checkGraphAssignment()
        CodeGenerator.generateGraphAssignment()
        return self.visitChildren(ctx)

    def visitTest(self, ctx:GraphParser.TestContext):
        DeclarationProcessor.processTest()
        ScopeChecker.checkTest()
        TypeChecker.checkTest()
        CodeGenerator.generateTest()
        return self.visitChildren(ctx)

    def visitCompOp(self, ctx:GraphParser.CompOpContext):
        DeclarationProcessor.processCompOp()
        ScopeChecker.checkCompOp()
        TypeChecker.checkCompOp()
        CodeGenerator.generateCompOp()
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:GraphParser.ExprContext):
        DeclarationProcessor.processExpr()
        ScopeChecker.checkExpr()
        TypeChecker.checkExpr()
        CodeGenerator.generateExpr()
        return self.visitChildren(ctx)

    def visitSetOp(self, ctx:GraphParser.SetOpContext):
        DeclarationProcessor.processSetOp()
        ScopeChecker.checkSetOp()
        TypeChecker.checkSetOp()
        CodeGenerator.generateSetOp()
        return self.visitChildren(ctx)

    def visitFactorOp(self, ctx:GraphParser.FactorOpContext):
        DeclarationProcessor.processFactorOp()
        ScopeChecker.checkFactorOp()
        TypeChecker.checkFactorOp()
        CodeGenerator.generateFactorOp()
        return self.visitChildren(ctx)

    def visitMolecule(self, ctx:GraphParser.MoleculeContext):
        DeclarationProcessor.processMolecule()
        ScopeChecker.checkMolecule()
        TypeChecker.checkMolecule()
        CodeGenerator.generateMolecule()
        return self.visitChildren(ctx)

    def visitAtom(self, ctx:GraphParser.AtomContext):
        DeclarationProcessor.processAtom()
        ScopeChecker.checkAtom()
        TypeChecker.checkAtom()
        CodeGenerator.generateAtom()
        return self.visitChildren(ctx)

    def visitTrailer(self, ctx:GraphParser.TrailerContext):
        DeclarationProcessor.processTrailer()
        ScopeChecker.checkTrailer()
        TypeChecker.checkTrailer()
        CodeGenerator.generateTrailer()
        return self.visitChildren(ctx)

    def visitFuncCall(self, ctx:GraphParser.FuncCallContext):
        DeclarationProcessor.processFuncCall()
        ScopeChecker.checkFuncCall()
        TypeChecker.checkFuncCall()
        CodeGenerator.generateFuncCall()
        return self.visitChildren(ctx)

    def visitActualParams(self, ctx:GraphParser.ActualParamsContext):
        DeclarationProcessor.processActualParams()
        ScopeChecker.checkActualParams()
        TypeChecker.checkActualParams()
        CodeGenerator.generateActualParams()
        return self.visitChildren(ctx)

    def visitListStruct(self, ctx:GraphParser.ListStructContext):
        DeclarationProcessor.processListStruct()
        ScopeChecker.checkListStruct()
        TypeChecker.checkListStruct()
        CodeGenerator.generateListStruct()
        return self.visitChildren(ctx)

    def visitRangerStruct(self, ctx:GraphParser.RangerStructContext):
        DeclarationProcessor.processRangerStruct()
        ScopeChecker.checkRangerStruct()
        TypeChecker.checkRangerStruct()
        CodeGenerator.generateRangerStruct()
        return self.visitChildren(ctx)

    def visitGraph(self, ctx:GraphParser.GraphContext):
        DeclarationProcessor.processGraph()
        ScopeChecker.checkGraph()
        TypeChecker.checkGraph()
        CodeGenerator.generateGraph()
        return self.visitChildren(ctx)

    def visitVertices(self, ctx:GraphParser.VerticesContext):
        DeclarationProcessor.processVertices()
        ScopeChecker.checkVertices()
        TypeChecker.checkVertices()
        CodeGenerator.generateVertices()
        return self.visitChildren(ctx)

    def visitVertex(self, ctx:GraphParser.VertexContext):
        DeclarationProcessor.processVertex()
        ScopeChecker.checkVertex()
        TypeChecker.checkVertex()
        CodeGenerator.generateVertex()
        return self.visitChildren(ctx)

    def visitEdges(self, ctx:GraphParser.EdgesContext):
        DeclarationProcessor.processEdges()
        ScopeChecker.checkEdges()
        TypeChecker.checkEdges()
        CodeGenerator.generateEdges()
        return self.visitChildren(ctx)

    def visitEdge(self, ctx:GraphParser.EdgeContext):
        DeclarationProcessor.processEdge()
        ScopeChecker.checkEdge()
        TypeChecker.checkEdge()
        CodeGenerator.generateEdge()
        return self.visitChildren(ctx)

    def visitIdentifier(self, ctx:GraphParser.IdentifierContext):
        DeclarationProcessor.processIdentifier()
        ScopeChecker.checkIdentifier()
        TypeChecker.checkIdentifier()
        CodeGenerator.generateIdentifier()
        return self.visitChildren(ctx)

    def visitNumber(self, ctx:GraphParser.NumberContext):
        DeclarationProcessor.processNumber()
        ScopeChecker.checkNumber()
        TypeChecker.checkNumber()
        CodeGenerator.generateNumber()
        return self.visitChildren(ctx)

    def visitBoolean(self, ctx:GraphParser.BooleanContext):
        DeclarationProcessor.processBoolean()
        ScopeChecker.checkBoolean()
        TypeChecker.checkBoolean()
        CodeGenerator.generateBoolean()
        return self.visitChildren(ctx)



del GraphParser
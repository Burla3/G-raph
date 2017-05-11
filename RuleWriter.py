from Antlr.GraphListener import GraphListener
from StringContainer import StringContainer

class RuleWriter(GraphListener):
    def __init__(self, cont):
        self.cont = cont

    def enterProgram(self, kurt):
        self.cont.string += "\"Program\":"

    def enterFuncDef(self, kurt):
        self.cont.string += "\"FuncDef\":"

    def enterFormalParams(self, kurt):
        self.cont.string += "\"FormalParams\":"

    def enterBlock(self, kurt):
        self.cont.string += "\"Block\":"

    def enterStmt(self, kurt):
        self.cont.string += "\"Stmt\":"

    def enterSimpleStmt(self, kurt):
        self.cont.string += "\"SimpleStmt\":"

    def enterAssignment(self, kurt):
        self.cont.string += "\"Assignment\":"

    def enterCompoundStmt(self, kurt):
        self.cont.string += "\"CompoundStmt\":"

    def enterIfStmt(self, kurt):
        self.cont.string += "\"IfStmt\":"

    def enterWhileStmt(self, kurt):
        self.cont.string += "\"WhileStmt\":"

    def enterForeachStmt(self, kurt):
        self.cont.string += "\"ForeachStmt\":"

    def enterGraphAssignment(self, kurt):
        self.cont.string += "\"GraphAssignment\":"

    def enterTest(self, kurt):
        self.cont.string += "\"Test\":"

    def enterCompOp(self, kurt):
        self.cont.string += "\"CompOp\":"

    def enterExpr(self, kurt):
        self.cont.string += "\"Expr\":"

    def enterSetOp(self, kurt):
        self.cont.string += "\"SetOp\":"

    def enterFactorOp(self, kurt):
        self.cont.string += "\"FactorOp\":"

    def enterMolecule(self, kurt):
        self.cont.string += "\"Molecule\":"

    def enterAtom(self, kurt):
        self.cont.string += "\"Atom\":"

    def enterFuncCall(self, kurt):
        self.cont.string += "\"FuncCall\":"

    def enterActualParams(self, kurt):
        self.cont.string += "\"ActualParams\":"

    def enterListStruct(self, kurt):
        self.cont.string += "\"ListStruct\":"

    def enterRangerStruct(self, kurt):
        self.cont.string += "\"RangerStruct\":"

    def enterGraph(self, kurt):
        self.cont.string += "\"Graph\":"

    def enterVertices(self, kurt):
        self.cont.string += "\"Vertices\":"

    def enterVertex(self, kurt):
        self.cont.string += "\"Vertex\":"

    def enterEdges(self, kurt):
        self.cont.string += "\"Edges\":"

    def enterEdge(self, kurt):
        self.cont.string += "\"Edge\":"

    def enterIdentifier(self, kurt):
        self.cont.string += "\"Identifier\":"

    def enterNumber(self, kurt):
        self.cont.string += "\"Number\":"

    def enterBoolean(self, kurt):
        self.cont.string += "\"Boolean\":"


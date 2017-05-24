from RuleWriter import RuleWriter
from StringContainer import StringContainer
from Antlr.GraphParser import GraphParser

class JSONBuilder:
    def __init__(self, tree):
        self.tree = tree
        self.cont = StringContainer()
        self.printer = RuleWriter(self.cont)

    def BuildAST(self):
        self.RemoveRedundant(self.tree)

    def RemoveRedundant(self, tree):
        if tree.getChildCount() > 0:
            counter = 0
            for child in tree.children:
                if child.getChildCount() == 1 and child.children[0].getChildCount() > 0:
                    if not isinstance(child, GraphParser.ExprContext):
                        tree.children[counter] = child.children[0]
                        self.RemoveRedundant(tree)
                    else:
                        self.RemoveRedundant(child)
                elif child.getChildCount() > 1:
                    self.RemoveRedundant(child)
                counter += 1

    def ConvertToJSON(self):
        self.cont.string = ''
        self.NTreeWalk(self.cont, self.tree)

        return self.cont.string

    def NTreeWalk(self, json, tree):
        if hasattr(tree, 'enterRule'):
            json.string += '{'
            tree.enterRule(self.printer)

            if tree.getChildCount() > 0:
                json.string += '['

                first = True

                for child in tree.children:
                    if first:
                        first = False
                    elif hasattr(child, 'symbol') and child.symbol.text.isspace():
                        pass
                    else:
                        json.string += ','
                    self.NTreeWalk(json, child)
                json.string += ']'

            json.string += '}'
        else:
            if not tree.symbol.text.isspace():
                string = tree.symbol.text
                string = string.replace('\\', '\\\\')
                json.string += '"' + string + '"'

    def WTreeWalk(self, json, tree):
        if hasattr(tree, 'enterRule'):
            json.string += '{'
            tree.enterRule(self.printer)
            json.string += '['

            first = True;

            for child in tree.children:
                if first:
                    first = False
                else:
                    json.string += ','
                self.NTreeWalk(json, child)
            json.string += ']'

            json.string += '}'
        else:
            if tree.symbol.text.isspace():
                json.string += "Whitespace"
            else:
                json.string += '"' + tree.symbol.text + '"'
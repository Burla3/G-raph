# Dependencies
import re

# Class for holding data from the def in GraphVisitor
class Def:
    def __init__(self, header, body, footer, node):
        self.header = header
        self.body = body
        self.footer = footer
        self.node = node

# Class for holding data about the phases we want to generate
class Phase:
    def __init__(self, path, name, action):
        self.path = path
        self.name = name
        self.action = action

# Strings from GraphVisitor that are constant
fileHeader = """
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

class GraphVisitor(ParseTreeVisitor):

"""

returnLine = """        return self.visitChildren(ctx)

"""

fileFooter = """

del GraphParser"""

fourSpaces = "    "
eightSpaces = "        "

# Path and name of the phases and their actions
phases = [Phase("ContextualAnalysis", "ScopeChecker", "check"),
          Phase("ContextualAnalysis", "TypeChecker", "check"),
          Phase("CodeGeneration", "CodeGenerator", "generate")]

# Find defs in visitor
defs = []

with open("Antlr/GraphVisitor.py", "r") as file:
    for line in file:
        if "    def" in line:
            defs.append(Def(line, "", returnLine, ""))

# Prepare defs for writing
for d in defs:
    d.node = re.search("visit(.+)\(", d.header).group(1)
    for phase in phases:
        d.body += eightSpaces + phase.name + "." + phase.action + d.node + "()" + "\n"

# Write to the new GraphVisitor file
with open("GraphVisitor.py", "w") as file:
    for phase in phases:
        file.write("from " + phase.path + " import " + phase.name + "\n")
    file.write(fileHeader)
    for d in defs:
        file.write(d.header)
        file.write(d.body)
        file.write(d.footer)
    file.write(fileFooter)

# Write to the new phase files
for phase in phases:
    with open(phase.path + "/" + phase.name + ".py", "w") as file:
        file.write("class " + phase.name + ":\n\n")
        for d in defs:
            file.write(fourSpaces + "def " + phase.action + d.node + "(self):\n")
            file.write(eightSpaces + "pass\n\n")

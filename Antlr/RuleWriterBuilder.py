import re

importstmt = """from GraphParser import GraphParser
from GraphListener import GraphListener
from StringContainer import StringContainer

class RuleWriter(GraphListener):
    def __init__(self, cont):
        self.cont = cont

"""


class Defs:
    def __init__(self, head):
        self.head = head

    def BuildPrint(self):
        f = re.compile('def enter(.+)[(].+')
        return '        self.cont.string += "\\"' + f.search(self.head).group(1) + '\\":"\n\n'


GraphListener = open('GraphListener.py', 'r')
defs = []
for line in GraphListener:
    if '    def enter' in line:
        defs.append(Defs(line))

GraphMain = open('RuleWriter.py', 'w')

GraphMain.write(importstmt)

pattern = re.compile('\(.*\)')

for definition in defs:
    GraphMain.write(pattern.sub('(self, kurt)', definition.head))
    #GraphMain.write(definition.head)
    GraphMain.write(definition.BuildPrint())


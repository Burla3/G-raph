grammar Graph;

tokens { INDENT, DEDENT }

@lexer::header {
from antlr4.Token import CommonToken
from Antlr.GraphParser import GraphParser
}

@lexer::members {
import re

class Node :
  def __init__(self, data) :
    self.data = data
    self.next = None
    self.prev = None

class LinkedList :
  def __init__( self ) :
    self.head = None
    self.tail = None

  def offer(self, data) :
    node = GraphLexer.Node(data)
    if self.head == None :
      self.head = node
      self.tail = node
    else :
      node.prev = self.tail
      node.prev.next = node
      self.tail = node

  def remove( self, i, returnresult=False) :
    counter = 0
    result = self.head
    while counter < i:
      result = result.next

    if result.prev:
      result.prev.next = result.next
    else:
      self.head = result

    if result.next:
      result.next.prev = result.prev
    else:
      self.tail = result

    if returnresult:
      return result.data

  def poll(self):

    if self.head is None:
      return None
    else:
      elementData = self.head.data
      nextNode = self.head.next
      self.head.data = None
      self.head.next = None
      self.head = nextNode
      if nextNode is None:
          self.tail = None
      else:
          nextNode.prev = None
      return elementData

  def size(self):
    counter = 0
    currentNode = self.head
    while currentNode is not None:
      currentNode = currentNode.next
      counter += 1
    return counter

  def get(self, i):
    counter = 0
    result = self.head
    while counter < i:
      result = result.next
      counter += 1
    return result.data

  def isEmpty(self):
    return self.head is None

  def __str__( self ) :
    s = ""
    p = self.head
    if p is not None :
      while p.next is not None :
        s += str(p.data)
        p = p.next
      s += str(p.data)
    return s

tokens = LinkedList()

indentCount = 0

SPACES_PER_INDENT = 4

lastToken = None

def emitToken(self, token:Token):
  self._token = token
  self.tokens.offer(token)

def nextToken(self):
  #if self._input.LA(1) is Token.EOF and self.indentCount is not 0:
  #  i = self.tokens.size() - 1
  #  while i >= 0:
  #    if self.tokens.get(i).type is Token.EOF:
  #      self.tokens.remove(i)
  #    i -= 1

  #  self.emitToken(self.commonToken(GraphParser.NEWLINE, "\n"))

  #  while self.indentCount is not 0:
  #    self.emitToken(self.createDedent())
  #    self.indentCount -= 1

  #  self.emitToken(self.commonToken(GraphParser.EOF, "<EOF>"))

  if self._input.LA(1) is Token.EOF and self.indentCount is not 0:
    raise Exception('End of program must be an empty newline')

  next = super().nextToken()

  if next.channel == Token.DEFAULT_CHANNEL:
    self.lastToken = next

  return next if self.tokens.isEmpty() else self.tokens.poll()

def createDedent(self):
  dedent = self.commonToken(GraphParser.DEDENT, "")
  dedent.line = self.lastToken.line
  return dedent

def commonToken(self, type:int, text:str):
  stop = self.getCharIndex() - 1
  if not self.text:
    start = stop
  else:
    start = stop - len(self.text) + 1
  return CommonToken(self._tokenFactorySourcePair, type, self.DEFAULT_TOKEN_CHANNEL, start, stop)

def getIndentationCount(spaces:str):
  return len(str);

def atStartOfInput(self):
  return super().column is 0 and super().line is 1
}

//Parser rules
//_________________________________________________________________________

// Start
program : NEWLINE? procDef* RUN block EOF;

// Procedure definition
procDef : (GRAPH SPACE)? PROCEDURE SPACE PROC_ID OPEN_PAREN formalParams? CLOSE_PAREN block ;

formalParams : VAR_ID (COMMA SPACE VAR_ID)* ;

// Block
block : COLON NEWLINE INDENT stmt+ DEDENT ;

// Statements
stmt : simpleStmt NEWLINE
     | compoundStmt
     ;

// Simple statements
simpleStmt : assignment
           | RETURN (SPACE expr)?
           | printStmt
           | PASS
           | lengthStmt
           | funcCall
           ;

assignment : molecule SPACE ASSIGN SPACE (expr | test) ;
printStmt : PRINT OPEN_PAREN STRING CLOSE_PAREN ;
lengthStmt : LENGTH OPEN_PAREN expr CLOSE_PAREN ;

// Compound statements
compoundStmt : ifStmt
             | whileStmt
             | foreachStmt
             | graphAssignment
             ;

ifStmt : IF SPACE test block (ELSEIF SPACE test block)* (ELSE block)? ;
whileStmt : WHILE SPACE test block ;
foreachStmt : FOREACH SPACE identifier SPACE IN SPACE expr block ;
graphAssignment : VAR_ID SPACE ASSIGN SPACE graph ;

// Test
test : test SPACE compOp SPACE test
       | NOT SPACE test
       | test SPACE OR SPACE test
       | test SPACE AND SPACE test
       | OPEN_PAREN test CLOSE_PAREN
       | expr
       | boolean
       ;

compOp: LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL | IN | NOT_IN | IS | IS_NOT ;

// Expressions
expr : molecule (SPACE setOp SPACE molecule)+
       |<assoc=right> expr POWER expr
       | ROOT OPEN_PAREN expr CLOSE_PAREN SPACE expr
       | LOG OPEN_PAREN expr CLOSE_PAREN SPACE expr
       | expr SPACE factorOp SPACE expr
       | expr SPACE (PLUS | MINUS) SPACE expr
       | OPEN_PAREN expr CLOSE_PAREN
       | MINUS molecule
       | funcCall
       | molecule
       ;

setOp: UNION | INTERSECT | DIFF | CONCAT ;
factorOp : TIMES | DIVIDE | MODULO | FLOORDIVISION | CEILINGDIVISION ;

molecule :  identifier trailer+ | atom ;

atom : VAR_ID
     | number
     | STRING
     | rangerStruct
     | listStruct
     ;

trailer : listStruct | DOT (VAR_ID | graphKeyword | funcCall) ;
funcCall : PROC_ID OPEN_PAREN actualParams? CLOSE_PAREN ;
graphKeyword : EDGES_KEY | VERTICES_KEY ;
actualParams : (REF SPACE)? expr (COMMA SPACE (REF SPACE)? expr)* ;
listStruct : OPEN_SQ_BRACKET expr (COMMA SPACE expr)* CLOSE_SQ_BRACKET ;
rangerStruct : expr DOT DOT expr ;

// Graph
graph  : GRAPH COLON NEWLINE INDENT vertices DEDENT ;
vertices : (vertex NEWLINE)+ ;
vertex : VAR_ID (SPACE+ edges)? ;
edges : edge (COMMA SPACE+ edge)* ;
edge : OPEN_PAREN DIRECTED? VAR_ID (SPACE expr)? CLOSE_PAREN ;

// Identifier
identifier: VAR_ID | PROC_ID ;

// Types
number : INT | FLOAT ;
boolean : TRUE | FALSE ;

// Lexer rules
//_________________________________________________
// Types
STRING : '\'' .*? '\'' ; // .*? matches anything until the first '
INT : DIGIT+ ;
FLOAT : DIGIT+ DOT DIGIT+ ;
TRUE: 'true' ;
FALSE: 'false' ;

// Keywords
RUN: '@run' ;
GRAPH: 'graph' ;
PROCEDURE: 'procedure' ;
RETURN: 'return' ;
PASS: 'pass' ;
PRINT: 'Print' ;
LENGTH: 'Length' ;
IF: 'if' ;
ELSEIF: 'else if' ;
ELSE: 'else' ;
WHILE: 'while' ;
FOREACH: 'for each' ;
EDGES_KEY: 'edges' ;
VERTICES_KEY: 'vertices' ;
REF: 'ref' ;

// Operators
ASSIGN: '=' ;
OR: 'or' ;
AND: 'and' ;
NOT: 'not' ;
LESS_THAN: '<' ;
GREATER_THAN: '>' ;
LESS_EQUAL: '<=' ;
GREATER_EQUAL: '>=' ;
IN: 'in' ;
NOT_IN: 'not in' ;
IS: 'is' ;
IS_NOT: 'is not' ;
PLUS: '+' ;
MINUS: '-' ;
UNION: 'union' ;
INTERSECT: 'intersect' ;
DIFF: 'diff' ;
CONCAT: 'concat' ;
TIMES: '*' ;
DIVIDE: '/' ;
MODULO: '%' ;
FLOORDIVISION: '/-' ;
CEILINGDIVISION: '/+' ;
LOG: 'log' ;
POWER : '^' ;
ROOT : 'root' ;
DIRECTED: '->' ;

// identifiers
VAR_ID: LOWERLETTER (LETTER | DIGIT)* ;
PROC_ID: UPPERLETTER (LETTER | DIGIT)* ;

// Misc
OPEN_PAREN: '(' ;
CLOSE_PAREN: ')' ;
OPEN_SQ_BRACKET: '[' ;
CLOSE_SQ_BRACKET: ']' ;
COMMA: ',' ;
DOT: '.' ;
COLON: ':' ;

// Fragments
fragment LETTER : LOWERLETTER | UPPERLETTER ;
fragment DIGIT : [0-9] ;
fragment LOWERLETTER : [a-z] ;
fragment UPPERLETTER : [A-Z] ;
fragment SPACES: [ ]+ ;

SPACE : ' ' ;
fragment COMMENT : '/*' .*? '*/' ;

SKIP_ : (SPACES | COMMENT) -> skip ;

NEWLINE
 : ( {self.atStartOfInput()}?   SPACES
   | ( '\r'? '\n' | '\r' ) SPACES?
   )
   {
pattern = self.re.compile(r"[^\r\n]+")
newLine = pattern.sub(r'', super().text)
pattern = self.re.compile(r"[\r\n]+")
spaces = pattern.sub(r'', super().text)

next = self.inputStream.LA(1)

#Python does not compare int with chars as expected so we use the ascii value of \r and \n and /
if next is 13 or next is 10 or next is 47:
  self.skip()
else:
  self.emitToken(self.commonToken(self.NEWLINE, newLine))
  indent = len(spaces)

  error = False
  if indent % self.SPACES_PER_INDENT is not 0:
    error = True
    if indent > self.indentCount * self.SPACES_PER_INDENT:
      indent = (self.indentCount + 1) * self.SPACES_PER_INDENT
    else:
      indent = indent - indent % self.SPACES_PER_INDENT

  if indent is self.indentCount * self.SPACES_PER_INDENT:
    self.skip()
  elif indent is (self.indentCount + 1) * self.SPACES_PER_INDENT:
    self.indentCount += 1
    self.emitToken(self.commonToken(GraphParser.INDENT, spaces))
  else:
    while indent < self.indentCount * self.SPACES_PER_INDENT:
      self.emitToken(self.createDedent())
      self.indentCount -= 1

  if error:
    raise RecognitionException('Incorrect amount of spaces as indentation', None, super().inputStream)
   }
 ;
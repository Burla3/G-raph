@ECHO OFF
call ClassPathCmd
@ECHO ON
call antlr4 -Dlanguage=Python3 -visitor Graph.g4
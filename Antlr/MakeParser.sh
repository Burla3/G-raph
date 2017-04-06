#!/bin/bash

if [ $# -gt 0 ]; then
	java -Xmx500M -cp "/usr/local/lib/antlr-4.5.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool "$1" -Dlanguage=Python3 ./Graph.g4
else
	java -Xmx500M -cp "/usr/local/lib/antlr-4.5.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=Python3 ./Graph.g4
fi

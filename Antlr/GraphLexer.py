# Generated from ./Graph.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
from Antlr.GraphParser import GraphParser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01bf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\7\2\u0088\n\2\f\2\16\2\u008b\13\2\3\2\3\2\3\3\6\3\u0090")
        buf.write("\n\3\r\3\16\3\u0091\3\4\6\4\u0095\n\4\r\4\16\4\u0096\3")
        buf.write("\4\3\4\6\4\u009b\n\4\r\4\16\4\u009c\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\7")
        buf.write("\61\u0172\n\61\f\61\16\61\u0175\13\61\3\62\3\62\3\62\7")
        buf.write("\62\u017a\n\62\f\62\16\62\u017d\13\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\5")
        buf.write(":\u018f\n:\3;\3;\3<\3<\3=\3=\3>\6>\u0198\n>\r>\16>\u0199")
        buf.write("\3?\3?\3@\3@\3@\3@\7@\u01a2\n@\f@\16@\u01a5\13@\3@\3@")
        buf.write("\3@\3A\3A\5A\u01ac\nA\3A\3A\3B\3B\3B\5B\u01b3\nB\3B\3")
        buf.write("B\5B\u01b7\nB\3B\5B\u01ba\nB\5B\u01bc\nB\3B\3B\4\u0089")
        buf.write("\u01a3\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s\2u\2w\2y\2{\2};\177\2\u0081<\u0083=\3\2\6\3")
        buf.write("\2\62;\3\2c|\3\2C\\\3\2\"\"\2\u01c8\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u008f")
        buf.write("\3\2\2\2\7\u0094\3\2\2\2\t\u009e\3\2\2\2\13\u00a3\3\2")
        buf.write("\2\2\r\u00a9\3\2\2\2\17\u00ae\3\2\2\2\21\u00b4\3\2\2\2")
        buf.write("\23\u00be\3\2\2\2\25\u00c5\3\2\2\2\27\u00ca\3\2\2\2\31")
        buf.write("\u00d0\3\2\2\2\33\u00d7\3\2\2\2\35\u00da\3\2\2\2\37\u00e2")
        buf.write("\3\2\2\2!\u00e7\3\2\2\2#\u00ed\3\2\2\2%\u00f6\3\2\2\2")
        buf.write("\'\u00fc\3\2\2\2)\u0105\3\2\2\2+\u0109\3\2\2\2-\u010b")
        buf.write("\3\2\2\2/\u010e\3\2\2\2\61\u0112\3\2\2\2\63\u0116\3\2")
        buf.write("\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\29\u011d\3\2\2\2")
        buf.write(";\u0120\3\2\2\2=\u0123\3\2\2\2?\u012a\3\2\2\2A\u012d\3")
        buf.write("\2\2\2C\u0134\3\2\2\2E\u0136\3\2\2\2G\u0138\3\2\2\2I\u013e")
        buf.write("\3\2\2\2K\u0148\3\2\2\2M\u014d\3\2\2\2O\u0154\3\2\2\2")
        buf.write("Q\u0156\3\2\2\2S\u0158\3\2\2\2U\u015a\3\2\2\2W\u015d\3")
        buf.write("\2\2\2Y\u0160\3\2\2\2[\u0164\3\2\2\2]\u0166\3\2\2\2_\u016b")
        buf.write("\3\2\2\2a\u016e\3\2\2\2c\u0176\3\2\2\2e\u017e\3\2\2\2")
        buf.write("g\u0180\3\2\2\2i\u0182\3\2\2\2k\u0184\3\2\2\2m\u0186\3")
        buf.write("\2\2\2o\u0188\3\2\2\2q\u018a\3\2\2\2s\u018e\3\2\2\2u\u0190")
        buf.write("\3\2\2\2w\u0192\3\2\2\2y\u0194\3\2\2\2{\u0197\3\2\2\2")
        buf.write("}\u019b\3\2\2\2\177\u019d\3\2\2\2\u0081\u01ab\3\2\2\2")
        buf.write("\u0083\u01bb\3\2\2\2\u0085\u0089\7)\2\2\u0086\u0088\13")
        buf.write("\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008c\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008c\u008d\7)\2\2\u008d\4\3\2\2\2\u008e")
        buf.write("\u0090\5u;\2\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\6\3\2\2\2\u0093")
        buf.write("\u0095\5u;\2\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u009a\5o8\2\u0099\u009b\5u;\2\u009a\u0099\3\2\2")
        buf.write("\2\u009b\u009c\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\b\3\2\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7t\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7g\2\2\u00a2\n")
        buf.write("\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7n\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7g\2\2\u00a8\f")
        buf.write("\3\2\2\2\u00a9\u00aa\7B\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac")
        buf.write("\7w\2\2\u00ac\u00ad\7p\2\2\u00ad\16\3\2\2\2\u00ae\u00af")
        buf.write("\7i\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7r\2\2\u00b2\u00b3\7j\2\2\u00b3\20\3\2\2\2\u00b4\u00b5")
        buf.write("\7r\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7e\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7f\2\2\u00ba\u00bb")
        buf.write("\7w\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\22")
        buf.write("\3\2\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\24\3\2\2\2\u00c5\u00c6\7r\2\2\u00c6\u00c7")
        buf.write("\7c\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7u\2\2\u00c9\26")
        buf.write("\3\2\2\2\u00ca\u00cb\7R\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd")
        buf.write("\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\30")
        buf.write("\3\2\2\2\u00d0\u00d1\7N\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7i\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6")
        buf.write("\7j\2\2\u00d6\32\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7h\2\2\u00d9\34\3\2\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7\"\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7h\2\2\u00e1\36")
        buf.write("\3\2\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\u00e6\7g\2\2\u00e6 \3\2\2\2\u00e7\u00e8")
        buf.write("\7y\2\2\u00e8\u00e9\7j\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7n\2\2\u00eb\u00ec\7g\2\2\u00ec\"\3\2\2\2\u00ed\u00ee")
        buf.write("\7h\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7\"\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7e\2\2\u00f4\u00f5\7j\2\2\u00f5$\3\2\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\u00f8\7f\2\2\u00f8\u00f9\7i\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7u\2\2\u00fb&\3\2\2\2\u00fc\u00fd")
        buf.write("\7x\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100\u0101\7k\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7u\2\2\u0104(\3\2\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7g\2\2\u0107\u0108\7h\2\2\u0108*\3")
        buf.write("\2\2\2\u0109\u010a\7?\2\2\u010a,\3\2\2\2\u010b\u010c\7")
        buf.write("q\2\2\u010c\u010d\7t\2\2\u010d.\3\2\2\2\u010e\u010f\7")
        buf.write("c\2\2\u010f\u0110\7p\2\2\u0110\u0111\7f\2\2\u0111\60\3")
        buf.write("\2\2\2\u0112\u0113\7p\2\2\u0113\u0114\7q\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115\62\3\2\2\2\u0116\u0117\7>\2\2\u0117\64\3")
        buf.write("\2\2\2\u0118\u0119\7@\2\2\u0119\66\3\2\2\2\u011a\u011b")
        buf.write("\7>\2\2\u011b\u011c\7?\2\2\u011c8\3\2\2\2\u011d\u011e")
        buf.write("\7@\2\2\u011e\u011f\7?\2\2\u011f:\3\2\2\2\u0120\u0121")
        buf.write("\7k\2\2\u0121\u0122\7p\2\2\u0122<\3\2\2\2\u0123\u0124")
        buf.write("\7p\2\2\u0124\u0125\7q\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7\"\2\2\u0127\u0128\7k\2\2\u0128\u0129\7p\2\2\u0129>")
        buf.write("\3\2\2\2\u012a\u012b\7k\2\2\u012b\u012c\7u\2\2\u012c@")
        buf.write("\3\2\2\2\u012d\u012e\7k\2\2\u012e\u012f\7u\2\2\u012f\u0130")
        buf.write("\7\"\2\2\u0130\u0131\7p\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133B\3\2\2\2\u0134\u0135\7-\2\2\u0135D\3\2\2")
        buf.write("\2\u0136\u0137\7/\2\2\u0137F\3\2\2\2\u0138\u0139\7w\2")
        buf.write("\2\u0139\u013a\7p\2\2\u013a\u013b\7k\2\2\u013b\u013c\7")
        buf.write("q\2\2\u013c\u013d\7p\2\2\u013dH\3\2\2\2\u013e\u013f\7")
        buf.write("k\2\2\u013f\u0140\7p\2\2\u0140\u0141\7v\2\2\u0141\u0142")
        buf.write("\7g\2\2\u0142\u0143\7t\2\2\u0143\u0144\7u\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145\u0146\7e\2\2\u0146\u0147\7v\2\2\u0147J\3")
        buf.write("\2\2\2\u0148\u0149\7f\2\2\u0149\u014a\7k\2\2\u014a\u014b")
        buf.write("\7h\2\2\u014b\u014c\7h\2\2\u014cL\3\2\2\2\u014d\u014e")
        buf.write("\7e\2\2\u014e\u014f\7q\2\2\u014f\u0150\7p\2\2\u0150\u0151")
        buf.write("\7e\2\2\u0151\u0152\7c\2\2\u0152\u0153\7v\2\2\u0153N\3")
        buf.write("\2\2\2\u0154\u0155\7,\2\2\u0155P\3\2\2\2\u0156\u0157\7")
        buf.write("\61\2\2\u0157R\3\2\2\2\u0158\u0159\7\'\2\2\u0159T\3\2")
        buf.write("\2\2\u015a\u015b\7\61\2\2\u015b\u015c\7/\2\2\u015cV\3")
        buf.write("\2\2\2\u015d\u015e\7\61\2\2\u015e\u015f\7-\2\2\u015fX")
        buf.write("\3\2\2\2\u0160\u0161\7n\2\2\u0161\u0162\7q\2\2\u0162\u0163")
        buf.write("\7i\2\2\u0163Z\3\2\2\2\u0164\u0165\7`\2\2\u0165\\\3\2")
        buf.write("\2\2\u0166\u0167\7t\2\2\u0167\u0168\7q\2\2\u0168\u0169")
        buf.write("\7q\2\2\u0169\u016a\7v\2\2\u016a^\3\2\2\2\u016b\u016c")
        buf.write("\7/\2\2\u016c\u016d\7@\2\2\u016d`\3\2\2\2\u016e\u0173")
        buf.write("\5w<\2\u016f\u0172\5s:\2\u0170\u0172\5u;\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174b\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0176\u017b\5y=\2\u0177\u017a\5s:\2\u0178")
        buf.write("\u017a\5u;\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017cd\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\7*\2\2")
        buf.write("\u017ff\3\2\2\2\u0180\u0181\7+\2\2\u0181h\3\2\2\2\u0182")
        buf.write("\u0183\7]\2\2\u0183j\3\2\2\2\u0184\u0185\7_\2\2\u0185")
        buf.write("l\3\2\2\2\u0186\u0187\7.\2\2\u0187n\3\2\2\2\u0188\u0189")
        buf.write("\7\60\2\2\u0189p\3\2\2\2\u018a\u018b\7<\2\2\u018br\3\2")
        buf.write("\2\2\u018c\u018f\5w<\2\u018d\u018f\5y=\2\u018e\u018c\3")
        buf.write("\2\2\2\u018e\u018d\3\2\2\2\u018ft\3\2\2\2\u0190\u0191")
        buf.write("\t\2\2\2\u0191v\3\2\2\2\u0192\u0193\t\3\2\2\u0193x\3\2")
        buf.write("\2\2\u0194\u0195\t\4\2\2\u0195z\3\2\2\2\u0196\u0198\t")
        buf.write("\5\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a|\3\2\2\2\u019b\u019c")
        buf.write("\7\"\2\2\u019c~\3\2\2\2\u019d\u019e\7\61\2\2\u019e\u019f")
        buf.write("\7,\2\2\u019f\u01a3\3\2\2\2\u01a0\u01a2\13\2\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3")
        buf.write("\2\2\2\u01a6\u01a7\7,\2\2\u01a7\u01a8\7\61\2\2\u01a8\u0080")
        buf.write("\3\2\2\2\u01a9\u01ac\5{>\2\u01aa\u01ac\5\177@\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01ae\bA\2\2\u01ae\u0082\3\2\2\2\u01af\u01b0\6")
        buf.write("B\2\2\u01b0\u01bc\5{>\2\u01b1\u01b3\7\17\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b7\7\f\2\2\u01b5\u01b7\7\17\2\2\u01b6\u01b2\3\2\2")
        buf.write("\2\u01b6\u01b5\3\2\2\2\u01b7\u01b9\3\2\2\2\u01b8\u01ba")
        buf.write("\5{>\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc")
        buf.write("\3\2\2\2\u01bb\u01af\3\2\2\2\u01bb\u01b6\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\bB\3\2\u01be\u0084\3\2\2\2")
        buf.write("\23\2\u0089\u0091\u0096\u009c\u0171\u0173\u0179\u017b")
        buf.write("\u018e\u0199\u01a3\u01ab\u01b2\u01b6\u01b9\u01bb\4\b\2")
        buf.write("\2\3B\2")
        return buf.getvalue()


class GraphLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    INT = 2
    FLOAT = 3
    TRUE = 4
    FALSE = 5
    RUN = 6
    GRAPH = 7
    PROCEDURE = 8
    RETURN = 9
    PASS = 10
    PRINT = 11
    LENGTH = 12
    IF = 13
    ELSEIF = 14
    ELSE = 15
    WHILE = 16
    FOREACH = 17
    EDGES_KEY = 18
    VERTICES_KEY = 19
    REF = 20
    ASSIGN = 21
    OR = 22
    AND = 23
    NOT = 24
    LESS_THAN = 25
    GREATER_THAN = 26
    LESS_EQUAL = 27
    GREATER_EQUAL = 28
    IN = 29
    NOT_IN = 30
    IS = 31
    IS_NOT = 32
    PLUS = 33
    MINUS = 34
    UNION = 35
    INTERSECT = 36
    DIFF = 37
    CONCAT = 38
    TIMES = 39
    DIVIDE = 40
    MODULO = 41
    FLOORDIVISION = 42
    CEILINGDIVISION = 43
    LOG = 44
    POWER = 45
    ROOT = 46
    DIRECTED = 47
    VAR_ID = 48
    PROC_ID = 49
    OPEN_PAREN = 50
    CLOSE_PAREN = 51
    OPEN_SQ_BRACKET = 52
    CLOSE_SQ_BRACKET = 53
    COMMA = 54
    DOT = 55
    COLON = 56
    SPACE = 57
    SKIP_ = 58
    NEWLINE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'@run'", "'graph'", "'procedure'", "'return'", 
            "'pass'", "'Print'", "'Length'", "'if'", "'else if'", "'else'", 
            "'while'", "'for each'", "'edges'", "'vertices'", "'ref'", "'='", 
            "'or'", "'and'", "'not'", "'<'", "'>'", "'<='", "'>='", "'in'", 
            "'not in'", "'is'", "'is not'", "'+'", "'-'", "'union'", "'intersect'", 
            "'diff'", "'concat'", "'*'", "'/'", "'%'", "'/-'", "'/+'", "'log'", 
            "'^'", "'root'", "'->'", "'('", "')'", "'['", "']'", "','", 
            "'.'", "':'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", "PROCEDURE", 
            "RETURN", "PASS", "PRINT", "LENGTH", "IF", "ELSEIF", "ELSE", 
            "WHILE", "FOREACH", "EDGES_KEY", "VERTICES_KEY", "REF", "ASSIGN", 
            "OR", "AND", "NOT", "LESS_THAN", "GREATER_THAN", "LESS_EQUAL", 
            "GREATER_EQUAL", "IN", "NOT_IN", "IS", "IS_NOT", "PLUS", "MINUS", 
            "UNION", "INTERSECT", "DIFF", "CONCAT", "TIMES", "DIVIDE", "MODULO", 
            "FLOORDIVISION", "CEILINGDIVISION", "LOG", "POWER", "ROOT", 
            "DIRECTED", "VAR_ID", "PROC_ID", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", "COMMA", "DOT", "COLON", 
            "SPACE", "SKIP_", "NEWLINE" ]

    ruleNames = [ "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", 
                  "PROCEDURE", "RETURN", "PASS", "PRINT", "LENGTH", "IF", 
                  "ELSEIF", "ELSE", "WHILE", "FOREACH", "EDGES_KEY", "VERTICES_KEY", 
                  "REF", "ASSIGN", "OR", "AND", "NOT", "LESS_THAN", "GREATER_THAN", 
                  "LESS_EQUAL", "GREATER_EQUAL", "IN", "NOT_IN", "IS", "IS_NOT", 
                  "PLUS", "MINUS", "UNION", "INTERSECT", "DIFF", "CONCAT", 
                  "TIMES", "DIVIDE", "MODULO", "FLOORDIVISION", "CEILINGDIVISION", 
                  "LOG", "POWER", "ROOT", "DIRECTED", "VAR_ID", "PROC_ID", 
                  "OPEN_PAREN", "CLOSE_PAREN", "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", 
                  "COMMA", "DOT", "COLON", "LETTER", "DIGIT", "LOWERLETTER", 
                  "UPPERLETTER", "SPACES", "SPACE", "COMMENT", "SKIP_", 
                  "NEWLINE" ]

    grammarFileName = "Graph.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[64] = self.NEWLINE_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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
               
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[64] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         



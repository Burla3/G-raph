# Generated from Graph.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
from Antlr.GraphParser import GraphParser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\7\2")
        buf.write("\u0086\n\2\f\2\16\2\u0089\13\2\3\2\3\2\3\3\6\3\u008e\n")
        buf.write("\3\r\3\16\3\u008f\3\4\6\4\u0093\n\4\r\4\16\4\u0094\3\4")
        buf.write("\3\4\6\4\u0099\n\4\r\4\16\4\u009a\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\7/\u0161\n/\f/\16")
        buf.write("/\u0164\13/\3\60\3\60\3\60\7\60\u0169\n\60\f\60\16\60")
        buf.write("\u016c\13\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\3\67\38\38\39\39\59\u0181")
        buf.write("\n9\3:\3:\3;\3;\3<\3<\3=\6=\u018a\n=\r=\16=\u018b\3>\3")
        buf.write(">\3?\3?\3?\3?\7?\u0194\n?\f?\16?\u0197\13?\3?\3?\3?\3")
        buf.write("@\3@\5@\u019e\n@\3@\3@\3A\3A\3A\5A\u01a5\nA\3A\3A\5A\u01a9")
        buf.write("\nA\3A\5A\u01ac\nA\5A\u01ae\nA\3A\3A\4\u0087\u0195\2B")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s")
        buf.write("\2u\2w\2y\2{:}\2\177;\u0081<\3\2\6\3\2\62;\3\2c|\3\2C")
        buf.write("\\\3\2\"\"\2\u01ba\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\3\u0083\3\2\2\2\5\u008d\3\2\2\2\7\u0092\3\2\2\2\t\u009c")
        buf.write("\3\2\2\2\13\u00a1\3\2\2\2\r\u00a7\3\2\2\2\17\u00ac\3\2")
        buf.write("\2\2\21\u00b2\3\2\2\2\23\u00bc\3\2\2\2\25\u00c3\3\2\2")
        buf.write("\2\27\u00c8\3\2\2\2\31\u00ce\3\2\2\2\33\u00d5\3\2\2\2")
        buf.write("\35\u00d8\3\2\2\2\37\u00e0\3\2\2\2!\u00e5\3\2\2\2#\u00eb")
        buf.write("\3\2\2\2%\u00f4\3\2\2\2\'\u00f8\3\2\2\2)\u00fa\3\2\2\2")
        buf.write("+\u00fd\3\2\2\2-\u0101\3\2\2\2/\u0105\3\2\2\2\61\u0107")
        buf.write("\3\2\2\2\63\u0109\3\2\2\2\65\u010c\3\2\2\2\67\u010f\3")
        buf.write("\2\2\29\u0112\3\2\2\2;\u0119\3\2\2\2=\u011c\3\2\2\2?\u0123")
        buf.write("\3\2\2\2A\u0125\3\2\2\2C\u0127\3\2\2\2E\u012d\3\2\2\2")
        buf.write("G\u0137\3\2\2\2I\u013c\3\2\2\2K\u0143\3\2\2\2M\u0145\3")
        buf.write("\2\2\2O\u0147\3\2\2\2Q\u0149\3\2\2\2S\u014c\3\2\2\2U\u014f")
        buf.write("\3\2\2\2W\u0153\3\2\2\2Y\u0155\3\2\2\2[\u015a\3\2\2\2")
        buf.write("]\u015d\3\2\2\2_\u0165\3\2\2\2a\u016d\3\2\2\2c\u016f\3")
        buf.write("\2\2\2e\u0171\3\2\2\2g\u0173\3\2\2\2i\u0175\3\2\2\2k\u0177")
        buf.write("\3\2\2\2m\u0179\3\2\2\2o\u017c\3\2\2\2q\u0180\3\2\2\2")
        buf.write("s\u0182\3\2\2\2u\u0184\3\2\2\2w\u0186\3\2\2\2y\u0189\3")
        buf.write("\2\2\2{\u018d\3\2\2\2}\u018f\3\2\2\2\177\u019d\3\2\2\2")
        buf.write("\u0081\u01ad\3\2\2\2\u0083\u0087\7)\2\2\u0084\u0086\13")
        buf.write("\2\2\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u008a\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u008a\u008b\7)\2\2\u008b\4\3\2\2\2\u008c")
        buf.write("\u008e\5s:\2\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\6\3\2\2\2\u0091")
        buf.write("\u0093\5s:\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0098\5k\66\2\u0097\u0099\5s:\2\u0098\u0097\3\2")
        buf.write("\2\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\b\3\2\2\2\u009c\u009d\7v\2\2\u009d\u009e")
        buf.write("\7t\2\2\u009e\u009f\7w\2\2\u009f\u00a0\7g\2\2\u00a0\n")
        buf.write("\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6\7g\2\2\u00a6\f")
        buf.write("\3\2\2\2\u00a7\u00a8\7B\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa")
        buf.write("\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\16\3\2\2\2\u00ac\u00ad")
        buf.write("\7i\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7r\2\2\u00b0\u00b1\7j\2\2\u00b1\20\3\2\2\2\u00b2\u00b3")
        buf.write("\7r\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6")
        buf.write("\7e\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7f\2\2\u00b8\u00b9")
        buf.write("\7w\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\22")
        buf.write("\3\2\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7r\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7u\2\2\u00c7\26")
        buf.write("\3\2\2\2\u00c8\u00c9\7R\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7v\2\2\u00cd\30")
        buf.write("\3\2\2\2\u00ce\u00cf\7N\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7i\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7j\2\2\u00d4\32\3\2\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7\34\3\2\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7\"\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7h\2\2\u00df\36")
        buf.write("\3\2\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3")
        buf.write("\7u\2\2\u00e3\u00e4\7g\2\2\u00e4 \3\2\2\2\u00e5\u00e6")
        buf.write("\7y\2\2\u00e6\u00e7\7j\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7n\2\2\u00e9\u00ea\7g\2\2\u00ea\"\3\2\2\2\u00eb\u00ec")
        buf.write("\7h\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef")
        buf.write("\7\"\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7e\2\2\u00f2\u00f3\7j\2\2\u00f3$\3\2\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7h\2\2\u00f7&\3")
        buf.write("\2\2\2\u00f8\u00f9\7?\2\2\u00f9(\3\2\2\2\u00fa\u00fb\7")
        buf.write("q\2\2\u00fb\u00fc\7t\2\2\u00fc*\3\2\2\2\u00fd\u00fe\7")
        buf.write("c\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7f\2\2\u0100,\3\2")
        buf.write("\2\2\u0101\u0102\7p\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104.\3\2\2\2\u0105\u0106\7>\2\2\u0106\60\3\2")
        buf.write("\2\2\u0107\u0108\7@\2\2\u0108\62\3\2\2\2\u0109\u010a\7")
        buf.write(">\2\2\u010a\u010b\7?\2\2\u010b\64\3\2\2\2\u010c\u010d")
        buf.write("\7@\2\2\u010d\u010e\7?\2\2\u010e\66\3\2\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7p\2\2\u01118\3\2\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113\u0114\7q\2\2\u0114\u0115\7v\2\2\u0115\u0116")
        buf.write("\7\"\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118:")
        buf.write("\3\2\2\2\u0119\u011a\7k\2\2\u011a\u011b\7u\2\2\u011b<")
        buf.write("\3\2\2\2\u011c\u011d\7k\2\2\u011d\u011e\7u\2\2\u011e\u011f")
        buf.write("\7\"\2\2\u011f\u0120\7p\2\2\u0120\u0121\7q\2\2\u0121\u0122")
        buf.write("\7v\2\2\u0122>\3\2\2\2\u0123\u0124\7-\2\2\u0124@\3\2\2")
        buf.write("\2\u0125\u0126\7/\2\2\u0126B\3\2\2\2\u0127\u0128\7w\2")
        buf.write("\2\u0128\u0129\7p\2\2\u0129\u012a\7k\2\2\u012a\u012b\7")
        buf.write("q\2\2\u012b\u012c\7p\2\2\u012cD\3\2\2\2\u012d\u012e\7")
        buf.write("k\2\2\u012e\u012f\7p\2\2\u012f\u0130\7v\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\u0132\7t\2\2\u0132\u0133\7u\2\2\u0133\u0134")
        buf.write("\7g\2\2\u0134\u0135\7e\2\2\u0135\u0136\7v\2\2\u0136F\3")
        buf.write("\2\2\2\u0137\u0138\7f\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7h\2\2\u013a\u013b\7h\2\2\u013bH\3\2\2\2\u013c\u013d")
        buf.write("\7e\2\2\u013d\u013e\7q\2\2\u013e\u013f\7p\2\2\u013f\u0140")
        buf.write("\7e\2\2\u0140\u0141\7c\2\2\u0141\u0142\7v\2\2\u0142J\3")
        buf.write("\2\2\2\u0143\u0144\7,\2\2\u0144L\3\2\2\2\u0145\u0146\7")
        buf.write("\61\2\2\u0146N\3\2\2\2\u0147\u0148\7\'\2\2\u0148P\3\2")
        buf.write("\2\2\u0149\u014a\7\61\2\2\u014a\u014b\7/\2\2\u014bR\3")
        buf.write("\2\2\2\u014c\u014d\7\61\2\2\u014d\u014e\7-\2\2\u014eT")
        buf.write("\3\2\2\2\u014f\u0150\7n\2\2\u0150\u0151\7q\2\2\u0151\u0152")
        buf.write("\7i\2\2\u0152V\3\2\2\2\u0153\u0154\7`\2\2\u0154X\3\2\2")
        buf.write("\2\u0155\u0156\7t\2\2\u0156\u0157\7q\2\2\u0157\u0158\7")
        buf.write("q\2\2\u0158\u0159\7v\2\2\u0159Z\3\2\2\2\u015a\u015b\7")
        buf.write("/\2\2\u015b\u015c\7@\2\2\u015c\\\3\2\2\2\u015d\u0162\5")
        buf.write("u;\2\u015e\u0161\5q9\2\u015f\u0161\5s:\2\u0160\u015e\3")
        buf.write("\2\2\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163^\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0165\u016a\5w<\2\u0166\u0169\5q9\2\u0167\u0169")
        buf.write("\5s:\2\u0168\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016c")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("`\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\7*\2\2\u016e")
        buf.write("b\3\2\2\2\u016f\u0170\7+\2\2\u0170d\3\2\2\2\u0171\u0172")
        buf.write("\7]\2\2\u0172f\3\2\2\2\u0173\u0174\7_\2\2\u0174h\3\2\2")
        buf.write("\2\u0175\u0176\7.\2\2\u0176j\3\2\2\2\u0177\u0178\7\60")
        buf.write("\2\2\u0178l\3\2\2\2\u0179\u017a\7\60\2\2\u017a\u017b\7")
        buf.write("\60\2\2\u017bn\3\2\2\2\u017c\u017d\7<\2\2\u017dp\3\2\2")
        buf.write("\2\u017e\u0181\5u;\2\u017f\u0181\5w<\2\u0180\u017e\3\2")
        buf.write("\2\2\u0180\u017f\3\2\2\2\u0181r\3\2\2\2\u0182\u0183\t")
        buf.write("\2\2\2\u0183t\3\2\2\2\u0184\u0185\t\3\2\2\u0185v\3\2\2")
        buf.write("\2\u0186\u0187\t\4\2\2\u0187x\3\2\2\2\u0188\u018a\t\5")
        buf.write("\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018cz\3\2\2\2\u018d\u018e")
        buf.write("\7\"\2\2\u018e|\3\2\2\2\u018f\u0190\7\61\2\2\u0190\u0191")
        buf.write("\7,\2\2\u0191\u0195\3\2\2\2\u0192\u0194\13\2\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0198\u0199\7,\2\2\u0199\u019a\7\61\2\2\u019a~")
        buf.write("\3\2\2\2\u019b\u019e\5y=\2\u019c\u019e\5}?\2\u019d\u019b")
        buf.write("\3\2\2\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\u01a0\b@\2\2\u01a0\u0080\3\2\2\2\u01a1\u01a2\6A\2\2\u01a2")
        buf.write("\u01ae\5y=\2\u01a3\u01a5\7\17\2\2\u01a4\u01a3\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a9\7")
        buf.write("\f\2\2\u01a7\u01a9\7\17\2\2\u01a8\u01a4\3\2\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01ac\5y=\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2")
        buf.write("\u01ad\u01a1\3\2\2\2\u01ad\u01a8\3\2\2\2\u01ae\u01af\3")
        buf.write("\2\2\2\u01af\u01b0\bA\3\2\u01b0\u0082\3\2\2\2\23\2\u0087")
        buf.write("\u008f\u0094\u009a\u0160\u0162\u0168\u016a\u0180\u018b")
        buf.write("\u0195\u019d\u01a4\u01a8\u01ab\u01ad\4\b\2\2\3A\2")
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
    REF = 18
    ASSIGN = 19
    OR = 20
    AND = 21
    NOT = 22
    LESS_THAN = 23
    GREATER_THAN = 24
    LESS_EQUAL = 25
    GREATER_EQUAL = 26
    IN = 27
    NOT_IN = 28
    IS = 29
    IS_NOT = 30
    PLUS = 31
    MINUS = 32
    UNION = 33
    INTERSECT = 34
    DIFF = 35
    CONCAT = 36
    TIMES = 37
    DIVIDE = 38
    MODULO = 39
    FLOORDIVISION = 40
    CEILINGDIVISION = 41
    LOG = 42
    POWER = 43
    ROOT = 44
    DIRECTED = 45
    VAR_ID = 46
    PROC_ID = 47
    OPEN_PAREN = 48
    CLOSE_PAREN = 49
    OPEN_SQ_BRACKET = 50
    CLOSE_SQ_BRACKET = 51
    COMMA = 52
    DOT = 53
    DOTDOT = 54
    COLON = 55
    SPACE = 56
    SKIP_ = 57
    NEWLINE = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'@run'", "'graph'", "'procedure'", "'return'", 
            "'pass'", "'Print'", "'Length'", "'if'", "'else if'", "'else'", 
            "'while'", "'for each'", "'ref'", "'='", "'or'", "'and'", "'not'", 
            "'<'", "'>'", "'<='", "'>='", "'in'", "'not in'", "'is'", "'is not'", 
            "'+'", "'-'", "'union'", "'intersect'", "'diff'", "'concat'", 
            "'*'", "'/'", "'%'", "'/-'", "'/+'", "'log'", "'^'", "'root'", 
            "'->'", "'('", "')'", "'['", "']'", "','", "'.'", "'..'", "':'", 
            "' '" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", "PROCEDURE", 
            "RETURN", "PASS", "PRINT", "LENGTH", "IF", "ELSEIF", "ELSE", 
            "WHILE", "FOREACH", "REF", "ASSIGN", "OR", "AND", "NOT", "LESS_THAN", 
            "GREATER_THAN", "LESS_EQUAL", "GREATER_EQUAL", "IN", "NOT_IN", 
            "IS", "IS_NOT", "PLUS", "MINUS", "UNION", "INTERSECT", "DIFF", 
            "CONCAT", "TIMES", "DIVIDE", "MODULO", "FLOORDIVISION", "CEILINGDIVISION", 
            "LOG", "POWER", "ROOT", "DIRECTED", "VAR_ID", "PROC_ID", "OPEN_PAREN", 
            "CLOSE_PAREN", "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", "COMMA", 
            "DOT", "DOTDOT", "COLON", "SPACE", "SKIP_", "NEWLINE" ]

    ruleNames = [ "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", 
                  "PROCEDURE", "RETURN", "PASS", "PRINT", "LENGTH", "IF", 
                  "ELSEIF", "ELSE", "WHILE", "FOREACH", "REF", "ASSIGN", 
                  "OR", "AND", "NOT", "LESS_THAN", "GREATER_THAN", "LESS_EQUAL", 
                  "GREATER_EQUAL", "IN", "NOT_IN", "IS", "IS_NOT", "PLUS", 
                  "MINUS", "UNION", "INTERSECT", "DIFF", "CONCAT", "TIMES", 
                  "DIVIDE", "MODULO", "FLOORDIVISION", "CEILINGDIVISION", 
                  "LOG", "POWER", "ROOT", "DIRECTED", "VAR_ID", "PROC_ID", 
                  "OPEN_PAREN", "CLOSE_PAREN", "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", 
                  "COMMA", "DOT", "DOTDOT", "COLON", "LETTER", "DIGIT", 
                  "LOWERLETTER", "UPPERLETTER", "SPACES", "SPACE", "COMMENT", 
                  "SKIP_", "NEWLINE" ]

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
    		actions[63] = self.NEWLINE_action 
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
            preds[63] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         



# Generated from Graph.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
from Antlr.GraphParser import GraphParser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0188\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\3\6\3")
        buf.write("\u0082\n\3\r\3\16\3\u0083\3\4\6\4\u0087\n\4\r\4\16\4\u0088")
        buf.write("\3\4\3\4\6\4\u008d\n\4\r\4\16\4\u008e\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\7)\u0138\n")
        buf.write(")\f)\16)\u013b\13)\3*\3*\3*\7*\u0140\n*\f*\16*\u0143\13")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\5\63\u0158\n\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\6\67\u0161\n\67\r\67\16\67\u0162")
        buf.write("\38\38\39\39\39\39\79\u016b\n9\f9\169\u016e\139\39\39")
        buf.write("\39\3:\3:\5:\u0175\n:\3:\3:\3;\3;\3;\5;\u017c\n;\3;\3")
        buf.write(";\5;\u0180\n;\3;\5;\u0183\n;\5;\u0185\n;\3;\3;\4{\u016c")
        buf.write("\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\2m\2o\64q\2")
        buf.write("s\65u\66\3\2\6\3\2\62;\3\2c|\3\2C\\\3\2\"\"\2\u0191\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2o\3\2\2\2\2s\3")
        buf.write("\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5\u0081\3\2\2\2\7\u0086\3")
        buf.write("\2\2\2\t\u0090\3\2\2\2\13\u0095\3\2\2\2\r\u009b\3\2\2")
        buf.write("\2\17\u00a0\3\2\2\2\21\u00a6\3\2\2\2\23\u00af\3\2\2\2")
        buf.write("\25\u00b6\3\2\2\2\27\u00bb\3\2\2\2\31\u00be\3\2\2\2\33")
        buf.write("\u00c6\3\2\2\2\35\u00cb\3\2\2\2\37\u00d1\3\2\2\2!\u00da")
        buf.write("\3\2\2\2#\u00de\3\2\2\2%\u00e0\3\2\2\2\'\u00e3\3\2\2\2")
        buf.write(")\u00e7\3\2\2\2+\u00eb\3\2\2\2-\u00ed\3\2\2\2/\u00ef\3")
        buf.write("\2\2\2\61\u00f2\3\2\2\2\63\u00f5\3\2\2\2\65\u00f8\3\2")
        buf.write("\2\2\67\u00ff\3\2\2\29\u0102\3\2\2\2;\u0109\3\2\2\2=\u010b")
        buf.write("\3\2\2\2?\u010d\3\2\2\2A\u0113\3\2\2\2C\u011d\3\2\2\2")
        buf.write("E\u0122\3\2\2\2G\u0129\3\2\2\2I\u012b\3\2\2\2K\u012d\3")
        buf.write("\2\2\2M\u012f\3\2\2\2O\u0131\3\2\2\2Q\u0134\3\2\2\2S\u013c")
        buf.write("\3\2\2\2U\u0144\3\2\2\2W\u0146\3\2\2\2Y\u0148\3\2\2\2")
        buf.write("[\u014a\3\2\2\2]\u014c\3\2\2\2_\u014e\3\2\2\2a\u0150\3")
        buf.write("\2\2\2c\u0153\3\2\2\2e\u0157\3\2\2\2g\u0159\3\2\2\2i\u015b")
        buf.write("\3\2\2\2k\u015d\3\2\2\2m\u0160\3\2\2\2o\u0164\3\2\2\2")
        buf.write("q\u0166\3\2\2\2s\u0174\3\2\2\2u\u0184\3\2\2\2w{\7)\2\2")
        buf.write("xz\13\2\2\2yx\3\2\2\2z}\3\2\2\2{|\3\2\2\2{y\3\2\2\2|~")
        buf.write("\3\2\2\2}{\3\2\2\2~\177\7)\2\2\177\4\3\2\2\2\u0080\u0082")
        buf.write("\5g\64\2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\6\3\2\2\2\u0085")
        buf.write("\u0087\5g\64\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3")
        buf.write("\2\2\2\u008a\u008c\5_\60\2\u008b\u008d\5g\64\2\u008c\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\b\3\2\2\2\u0090\u0091\7V\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\u0093\7w\2\2\u0093\u0094\7g\2\2\u0094")
        buf.write("\n\3\2\2\2\u0095\u0096\7H\2\2\u0096\u0097\7c\2\2\u0097")
        buf.write("\u0098\7n\2\2\u0098\u0099\7u\2\2\u0099\u009a\7g\2\2\u009a")
        buf.write("\f\3\2\2\2\u009b\u009c\7B\2\2\u009c\u009d\7t\2\2\u009d")
        buf.write("\u009e\7w\2\2\u009e\u009f\7p\2\2\u009f\16\3\2\2\2\u00a0")
        buf.write("\u00a1\7i\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7c\2\2\u00a3")
        buf.write("\u00a4\7r\2\2\u00a4\u00a5\7j\2\2\u00a5\20\3\2\2\2\u00a6")
        buf.write("\u00a7\7h\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7e\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7k\2\2\u00ac")
        buf.write("\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\22\3\2\2\2\u00af")
        buf.write("\u00b0\7t\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7v\2\2\u00b2")
        buf.write("\u00b3\7w\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7p\2\2\u00b5")
        buf.write("\24\3\2\2\2\u00b6\u00b7\7r\2\2\u00b7\u00b8\7c\2\2\u00b8")
        buf.write("\u00b9\7u\2\2\u00b9\u00ba\7u\2\2\u00ba\26\3\2\2\2\u00bb")
        buf.write("\u00bc\7k\2\2\u00bc\u00bd\7h\2\2\u00bd\30\3\2\2\2\u00be")
        buf.write("\u00bf\7g\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7u\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\u00c3\7\"\2\2\u00c3\u00c4\7k\2\2\u00c4")
        buf.write("\u00c5\7h\2\2\u00c5\32\3\2\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\u00c8\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\34\3\2\2\2\u00cb\u00cc\7y\2\2\u00cc\u00cd\7j\2\2\u00cd")
        buf.write("\u00ce\7k\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7g\2\2\u00d0")
        buf.write("\36\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3\7q\2\2\u00d3")
        buf.write("\u00d4\7t\2\2\u00d4\u00d5\7\"\2\2\u00d5\u00d6\7g\2\2\u00d6")
        buf.write("\u00d7\7c\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7j\2\2\u00d9")
        buf.write(" \3\2\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7g\2\2\u00dc")
        buf.write("\u00dd\7h\2\2\u00dd\"\3\2\2\2\u00de\u00df\7?\2\2\u00df")
        buf.write("$\3\2\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2\7t\2\2\u00e2")
        buf.write("&\3\2\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7p\2\2\u00e5")
        buf.write("\u00e6\7f\2\2\u00e6(\3\2\2\2\u00e7\u00e8\7p\2\2\u00e8")
        buf.write("\u00e9\7q\2\2\u00e9\u00ea\7v\2\2\u00ea*\3\2\2\2\u00eb")
        buf.write("\u00ec\7>\2\2\u00ec,\3\2\2\2\u00ed\u00ee\7@\2\2\u00ee")
        buf.write(".\3\2\2\2\u00ef\u00f0\7>\2\2\u00f0\u00f1\7?\2\2\u00f1")
        buf.write("\60\3\2\2\2\u00f2\u00f3\7@\2\2\u00f3\u00f4\7?\2\2\u00f4")
        buf.write("\62\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\64\3\2\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7q\2\2\u00fa")
        buf.write("\u00fb\7v\2\2\u00fb\u00fc\7\"\2\2\u00fc\u00fd\7k\2\2\u00fd")
        buf.write("\u00fe\7p\2\2\u00fe\66\3\2\2\2\u00ff\u0100\7k\2\2\u0100")
        buf.write("\u0101\7u\2\2\u01018\3\2\2\2\u0102\u0103\7k\2\2\u0103")
        buf.write("\u0104\7u\2\2\u0104\u0105\7\"\2\2\u0105\u0106\7p\2\2\u0106")
        buf.write("\u0107\7q\2\2\u0107\u0108\7v\2\2\u0108:\3\2\2\2\u0109")
        buf.write("\u010a\7-\2\2\u010a<\3\2\2\2\u010b\u010c\7/\2\2\u010c")
        buf.write(">\3\2\2\2\u010d\u010e\7w\2\2\u010e\u010f\7p\2\2\u010f")
        buf.write("\u0110\7k\2\2\u0110\u0111\7q\2\2\u0111\u0112\7p\2\2\u0112")
        buf.write("@\3\2\2\2\u0113\u0114\7k\2\2\u0114\u0115\7p\2\2\u0115")
        buf.write("\u0116\7v\2\2\u0116\u0117\7g\2\2\u0117\u0118\7t\2\2\u0118")
        buf.write("\u0119\7u\2\2\u0119\u011a\7g\2\2\u011a\u011b\7e\2\2\u011b")
        buf.write("\u011c\7v\2\2\u011cB\3\2\2\2\u011d\u011e\7f\2\2\u011e")
        buf.write("\u011f\7k\2\2\u011f\u0120\7h\2\2\u0120\u0121\7h\2\2\u0121")
        buf.write("D\3\2\2\2\u0122\u0123\7e\2\2\u0123\u0124\7q\2\2\u0124")
        buf.write("\u0125\7p\2\2\u0125\u0126\7e\2\2\u0126\u0127\7c\2\2\u0127")
        buf.write("\u0128\7v\2\2\u0128F\3\2\2\2\u0129\u012a\7,\2\2\u012a")
        buf.write("H\3\2\2\2\u012b\u012c\7\61\2\2\u012cJ\3\2\2\2\u012d\u012e")
        buf.write("\7\'\2\2\u012eL\3\2\2\2\u012f\u0130\7`\2\2\u0130N\3\2")
        buf.write("\2\2\u0131\u0132\7/\2\2\u0132\u0133\7@\2\2\u0133P\3\2")
        buf.write("\2\2\u0134\u0139\5i\65\2\u0135\u0138\5e\63\2\u0136\u0138")
        buf.write("\5g\64\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138")
        buf.write("\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013aR\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u0141\5k\66")
        buf.write("\2\u013d\u0140\5e\63\2\u013e\u0140\5g\64\2\u013f\u013d")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142T\3\2\2\2\u0143")
        buf.write("\u0141\3\2\2\2\u0144\u0145\7*\2\2\u0145V\3\2\2\2\u0146")
        buf.write("\u0147\7+\2\2\u0147X\3\2\2\2\u0148\u0149\7]\2\2\u0149")
        buf.write("Z\3\2\2\2\u014a\u014b\7_\2\2\u014b\\\3\2\2\2\u014c\u014d")
        buf.write("\7.\2\2\u014d^\3\2\2\2\u014e\u014f\7\60\2\2\u014f`\3\2")
        buf.write("\2\2\u0150\u0151\7\60\2\2\u0151\u0152\7\60\2\2\u0152b")
        buf.write("\3\2\2\2\u0153\u0154\7<\2\2\u0154d\3\2\2\2\u0155\u0158")
        buf.write("\5i\65\2\u0156\u0158\5k\66\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158f\3\2\2\2\u0159\u015a\t\2\2\2\u015a")
        buf.write("h\3\2\2\2\u015b\u015c\t\3\2\2\u015cj\3\2\2\2\u015d\u015e")
        buf.write("\t\4\2\2\u015el\3\2\2\2\u015f\u0161\t\5\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163n\3\2\2\2\u0164\u0165\7\"\2\2\u0165")
        buf.write("p\3\2\2\2\u0166\u0167\7\61\2\2\u0167\u0168\7,\2\2\u0168")
        buf.write("\u016c\3\2\2\2\u0169\u016b\13\2\2\2\u016a\u0169\3\2\2")
        buf.write("\2\u016b\u016e\3\2\2\2\u016c\u016d\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f")
        buf.write("\u0170\7,\2\2\u0170\u0171\7\61\2\2\u0171r\3\2\2\2\u0172")
        buf.write("\u0175\5m\67\2\u0173\u0175\5q9\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b:\2\2")
        buf.write("\u0177t\3\2\2\2\u0178\u0179\6;\2\2\u0179\u0185\5m\67\2")
        buf.write("\u017a\u017c\7\17\2\2\u017b\u017a\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0180\7\f\2\2\u017e")
        buf.write("\u0180\7\17\2\2\u017f\u017b\3\2\2\2\u017f\u017e\3\2\2")
        buf.write("\2\u0180\u0182\3\2\2\2\u0181\u0183\5m\67\2\u0182\u0181")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184")
        buf.write("\u0178\3\2\2\2\u0184\u017f\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0187\b;\3\2\u0187v\3\2\2\2\23\2{\u0083\u0088\u008e")
        buf.write("\u0137\u0139\u013f\u0141\u0157\u0162\u016c\u0174\u017b")
        buf.write("\u017f\u0182\u0184\4\b\2\2\3;\2")
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
    FUNCTION = 8
    RETURN = 9
    PASS = 10
    IF = 11
    ELSEIF = 12
    ELSE = 13
    WHILE = 14
    FOREACH = 15
    REF = 16
    ASSIGN = 17
    OR = 18
    AND = 19
    NOT = 20
    LESS_THAN = 21
    GREATER_THAN = 22
    LESS_EQUAL = 23
    GREATER_EQUAL = 24
    IN = 25
    NOT_IN = 26
    IS = 27
    IS_NOT = 28
    PLUS = 29
    MINUS = 30
    UNION = 31
    INTERSECT = 32
    DIFF = 33
    CONCAT = 34
    TIMES = 35
    DIVIDE = 36
    MODULO = 37
    POWER = 38
    DIRECTED = 39
    VAR_ID = 40
    FUNC_ID = 41
    OPEN_PAREN = 42
    CLOSE_PAREN = 43
    OPEN_SQ_BRACKET = 44
    CLOSE_SQ_BRACKET = 45
    COMMA = 46
    DOT = 47
    DOTDOT = 48
    COLON = 49
    SPACE = 50
    SKIP_ = 51
    NEWLINE = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'True'", "'False'", "'@run'", "'graph'", "'function'", "'return'", 
            "'pass'", "'if'", "'else if'", "'else'", "'while'", "'for each'", 
            "'ref'", "'='", "'or'", "'and'", "'not'", "'<'", "'>'", "'<='", 
            "'>='", "'in'", "'not in'", "'is'", "'is not'", "'+'", "'-'", 
            "'union'", "'intersect'", "'diff'", "'concat'", "'*'", "'/'", 
            "'%'", "'^'", "'->'", "'('", "')'", "'['", "']'", "','", "'.'", 
            "'..'", "':'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", "FUNCTION", 
            "RETURN", "PASS", "IF", "ELSEIF", "ELSE", "WHILE", "FOREACH", 
            "REF", "ASSIGN", "OR", "AND", "NOT", "LESS_THAN", "GREATER_THAN", 
            "LESS_EQUAL", "GREATER_EQUAL", "IN", "NOT_IN", "IS", "IS_NOT", 
            "PLUS", "MINUS", "UNION", "INTERSECT", "DIFF", "CONCAT", "TIMES", 
            "DIVIDE", "MODULO", "POWER", "DIRECTED", "VAR_ID", "FUNC_ID", 
            "OPEN_PAREN", "CLOSE_PAREN", "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", 
            "COMMA", "DOT", "DOTDOT", "COLON", "SPACE", "SKIP_", "NEWLINE" ]

    ruleNames = [ "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", 
                  "FUNCTION", "RETURN", "PASS", "IF", "ELSEIF", "ELSE", 
                  "WHILE", "FOREACH", "REF", "ASSIGN", "OR", "AND", "NOT", 
                  "LESS_THAN", "GREATER_THAN", "LESS_EQUAL", "GREATER_EQUAL", 
                  "IN", "NOT_IN", "IS", "IS_NOT", "PLUS", "MINUS", "UNION", 
                  "INTERSECT", "DIFF", "CONCAT", "TIMES", "DIVIDE", "MODULO", 
                  "POWER", "DIRECTED", "VAR_ID", "FUNC_ID", "OPEN_PAREN", 
                  "CLOSE_PAREN", "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", 
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
    		actions[57] = self.NEWLINE_action 
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
            preds[57] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         



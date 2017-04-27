# Generated from Graph.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
from Antlr.GraphParser import GraphParser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u019f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\7\2\u0082\n\2\f")
        buf.write("\2\16\2\u0085\13\2\3\2\3\2\3\3\6\3\u008a\n\3\r\3\16\3")
        buf.write("\u008b\3\4\6\4\u008f\n\4\r\4\16\4\u0090\3\4\3\4\6\4\u0095")
        buf.write("\n\4\r\4\16\4\u0096\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\7-\u014f\n-\f-\16-\u0152\13-\3.\3")
        buf.write(".\3.\7.\u0157\n.\f.\16.\u015a\13.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\5\67\u016f\n\67\38\38\39\39\3:\3:\3;\6")
        buf.write(";\u0178\n;\r;\16;\u0179\3<\3<\3=\3=\3=\3=\7=\u0182\n=")
        buf.write("\f=\16=\u0185\13=\3=\3=\3=\3>\3>\5>\u018c\n>\3>\3>\3?")
        buf.write("\3?\3?\5?\u0193\n?\3?\3?\5?\u0197\n?\3?\5?\u019a\n?\5")
        buf.write("?\u019c\n?\3?\3?\4\u0083\u0183\2@\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2w8y\2{9}:\3\2\6")
        buf.write("\3\2\62;\3\2c|\3\2C\\\3\2\"\"\2\u01a8\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2w\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3")
        buf.write("\2\2\2\5\u0089\3\2\2\2\7\u008e\3\2\2\2\t\u0098\3\2\2\2")
        buf.write("\13\u009d\3\2\2\2\r\u00a3\3\2\2\2\17\u00a8\3\2\2\2\21")
        buf.write("\u00ae\3\2\2\2\23\u00b7\3\2\2\2\25\u00be\3\2\2\2\27\u00c3")
        buf.write("\3\2\2\2\31\u00c6\3\2\2\2\33\u00ce\3\2\2\2\35\u00d3\3")
        buf.write("\2\2\2\37\u00d9\3\2\2\2!\u00e2\3\2\2\2#\u00e6\3\2\2\2")
        buf.write("%\u00e8\3\2\2\2\'\u00eb\3\2\2\2)\u00ef\3\2\2\2+\u00f3")
        buf.write("\3\2\2\2-\u00f5\3\2\2\2/\u00f7\3\2\2\2\61\u00fa\3\2\2")
        buf.write("\2\63\u00fd\3\2\2\2\65\u0100\3\2\2\2\67\u0107\3\2\2\2")
        buf.write("9\u010a\3\2\2\2;\u0111\3\2\2\2=\u0113\3\2\2\2?\u0115\3")
        buf.write("\2\2\2A\u011b\3\2\2\2C\u0125\3\2\2\2E\u012a\3\2\2\2G\u0131")
        buf.write("\3\2\2\2I\u0133\3\2\2\2K\u0135\3\2\2\2M\u0137\3\2\2\2")
        buf.write("O\u013a\3\2\2\2Q\u013d\3\2\2\2S\u0141\3\2\2\2U\u0143\3")
        buf.write("\2\2\2W\u0148\3\2\2\2Y\u014b\3\2\2\2[\u0153\3\2\2\2]\u015b")
        buf.write("\3\2\2\2_\u015d\3\2\2\2a\u015f\3\2\2\2c\u0161\3\2\2\2")
        buf.write("e\u0163\3\2\2\2g\u0165\3\2\2\2i\u0167\3\2\2\2k\u016a\3")
        buf.write("\2\2\2m\u016e\3\2\2\2o\u0170\3\2\2\2q\u0172\3\2\2\2s\u0174")
        buf.write("\3\2\2\2u\u0177\3\2\2\2w\u017b\3\2\2\2y\u017d\3\2\2\2")
        buf.write("{\u018b\3\2\2\2}\u019b\3\2\2\2\177\u0083\7)\2\2\u0080")
        buf.write("\u0082\13\2\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2")
        buf.write("\2\u0083\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0086")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\7)\2\2\u0087")
        buf.write("\4\3\2\2\2\u0088\u008a\5o8\2\u0089\u0088\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\6\3\2\2\2\u008d\u008f\5o8\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\5g\64\2\u0093\u0095")
        buf.write("\5o8\2\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\b\3\2\2\2\u0098\u0099")
        buf.write("\7v\2\2\u0099\u009a\7t\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\n\3\2\2\2\u009d\u009e\7h\2\2\u009e\u009f")
        buf.write("\7c\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7u\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\f\3\2\2\2\u00a3\u00a4\7B\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\16")
        buf.write("\3\2\2\2\u00a8\u00a9\7i\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7r\2\2\u00ac\u00ad\7j\2\2\u00ad\20")
        buf.write("\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1\u00b2\7e\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7p\2\2\u00b6\22")
        buf.write("\3\2\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\24\3\2\2\2\u00be\u00bf\7r\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7u\2\2\u00c2\26")
        buf.write("\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7h\2\2\u00c5\30")
        buf.write("\3\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9")
        buf.write("\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7\"\2\2\u00cb\u00cc")
        buf.write("\7k\2\2\u00cc\u00cd\7h\2\2\u00cd\32\3\2\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\34\3\2\2\2\u00d3\u00d4\7y\2\2\u00d4\u00d5")
        buf.write("\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\36\3\2\2\2\u00d9\u00da\7h\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7\"\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1")
        buf.write("\7j\2\2\u00e1 \3\2\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\u00e5\7h\2\2\u00e5\"\3\2\2\2\u00e6\u00e7")
        buf.write("\7?\2\2\u00e7$\3\2\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea&\3\2\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7f\2\2\u00ee(\3\2\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7v\2\2\u00f2*\3")
        buf.write("\2\2\2\u00f3\u00f4\7>\2\2\u00f4,\3\2\2\2\u00f5\u00f6\7")
        buf.write("@\2\2\u00f6.\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8\u00f9\7")
        buf.write("?\2\2\u00f9\60\3\2\2\2\u00fa\u00fb\7@\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fc\62\3\2\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\64\3\2\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7q\2\2\u0102\u0103\7v\2\2\u0103\u0104\7\"\2\2\u0104\u0105")
        buf.write("\7k\2\2\u0105\u0106\7p\2\2\u0106\66\3\2\2\2\u0107\u0108")
        buf.write("\7k\2\2\u0108\u0109\7u\2\2\u01098\3\2\2\2\u010a\u010b")
        buf.write("\7k\2\2\u010b\u010c\7u\2\2\u010c\u010d\7\"\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e\u010f\7q\2\2\u010f\u0110\7v\2\2\u0110:\3")
        buf.write("\2\2\2\u0111\u0112\7-\2\2\u0112<\3\2\2\2\u0113\u0114\7")
        buf.write("/\2\2\u0114>\3\2\2\2\u0115\u0116\7w\2\2\u0116\u0117\7")
        buf.write("p\2\2\u0117\u0118\7k\2\2\u0118\u0119\7q\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a@\3\2\2\2\u011b\u011c\7k\2\2\u011c\u011d")
        buf.write("\7p\2\2\u011d\u011e\7v\2\2\u011e\u011f\7g\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120\u0121\7u\2\2\u0121\u0122\7g\2\2\u0122\u0123")
        buf.write("\7e\2\2\u0123\u0124\7v\2\2\u0124B\3\2\2\2\u0125\u0126")
        buf.write("\7f\2\2\u0126\u0127\7k\2\2\u0127\u0128\7h\2\2\u0128\u0129")
        buf.write("\7h\2\2\u0129D\3\2\2\2\u012a\u012b\7e\2\2\u012b\u012c")
        buf.write("\7q\2\2\u012c\u012d\7p\2\2\u012d\u012e\7e\2\2\u012e\u012f")
        buf.write("\7c\2\2\u012f\u0130\7v\2\2\u0130F\3\2\2\2\u0131\u0132")
        buf.write("\7,\2\2\u0132H\3\2\2\2\u0133\u0134\7\61\2\2\u0134J\3\2")
        buf.write("\2\2\u0135\u0136\7\'\2\2\u0136L\3\2\2\2\u0137\u0138\7")
        buf.write("\61\2\2\u0138\u0139\7/\2\2\u0139N\3\2\2\2\u013a\u013b")
        buf.write("\7\61\2\2\u013b\u013c\7-\2\2\u013cP\3\2\2\2\u013d\u013e")
        buf.write("\7n\2\2\u013e\u013f\7q\2\2\u013f\u0140\7i\2\2\u0140R\3")
        buf.write("\2\2\2\u0141\u0142\7`\2\2\u0142T\3\2\2\2\u0143\u0144\7")
        buf.write("t\2\2\u0144\u0145\7q\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147V\3\2\2\2\u0148\u0149\7/\2\2\u0149\u014a")
        buf.write("\7@\2\2\u014aX\3\2\2\2\u014b\u0150\5q9\2\u014c\u014f\5")
        buf.write("m\67\2\u014d\u014f\5o8\2\u014e\u014c\3\2\2\2\u014e\u014d")
        buf.write("\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151Z\3\2\2\2\u0152\u0150\3\2\2\2\u0153")
        buf.write("\u0158\5s:\2\u0154\u0157\5m\67\2\u0155\u0157\5o8\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\\\3\2\2")
        buf.write("\2\u015a\u0158\3\2\2\2\u015b\u015c\7*\2\2\u015c^\3\2\2")
        buf.write("\2\u015d\u015e\7+\2\2\u015e`\3\2\2\2\u015f\u0160\7]\2")
        buf.write("\2\u0160b\3\2\2\2\u0161\u0162\7_\2\2\u0162d\3\2\2\2\u0163")
        buf.write("\u0164\7.\2\2\u0164f\3\2\2\2\u0165\u0166\7\60\2\2\u0166")
        buf.write("h\3\2\2\2\u0167\u0168\7\60\2\2\u0168\u0169\7\60\2\2\u0169")
        buf.write("j\3\2\2\2\u016a\u016b\7<\2\2\u016bl\3\2\2\2\u016c\u016f")
        buf.write("\5q9\2\u016d\u016f\5s:\2\u016e\u016c\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016fn\3\2\2\2\u0170\u0171\t\2\2\2\u0171p\3\2")
        buf.write("\2\2\u0172\u0173\t\3\2\2\u0173r\3\2\2\2\u0174\u0175\t")
        buf.write("\4\2\2\u0175t\3\2\2\2\u0176\u0178\t\5\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017av\3\2\2\2\u017b\u017c\7\"\2\2\u017c")
        buf.write("x\3\2\2\2\u017d\u017e\7\61\2\2\u017e\u017f\7,\2\2\u017f")
        buf.write("\u0183\3\2\2\2\u0180\u0182\13\2\2\2\u0181\u0180\3\2\2")
        buf.write("\2\u0182\u0185\3\2\2\2\u0183\u0184\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u0183\3\2\2\2\u0186")
        buf.write("\u0187\7,\2\2\u0187\u0188\7\61\2\2\u0188z\3\2\2\2\u0189")
        buf.write("\u018c\5u;\2\u018a\u018c\5y=\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e\b>\2\2")
        buf.write("\u018e|\3\2\2\2\u018f\u0190\6?\2\2\u0190\u019c\5u;\2\u0191")
        buf.write("\u0193\7\17\2\2\u0192\u0191\3\2\2\2\u0192\u0193\3\2\2")
        buf.write("\2\u0193\u0194\3\2\2\2\u0194\u0197\7\f\2\2\u0195\u0197")
        buf.write("\7\17\2\2\u0196\u0192\3\2\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u0199\3\2\2\2\u0198\u019a\5u;\2\u0199\u0198\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019a\u019c\3\2\2\2\u019b\u018f\3\2\2\2")
        buf.write("\u019b\u0196\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\b")
        buf.write("?\3\2\u019e~\3\2\2\2\23\2\u0083\u008b\u0090\u0096\u014e")
        buf.write("\u0150\u0156\u0158\u016e\u0179\u0183\u018b\u0192\u0196")
        buf.write("\u0199\u019b\4\b\2\2\3?\2")
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
    FLOORDIVISION = 38
    CEILINGDIVISION = 39
    LOG = 40
    POWER = 41
    ROOT = 42
    DIRECTED = 43
    VAR_ID = 44
    FUNC_ID = 45
    OPEN_PAREN = 46
    CLOSE_PAREN = 47
    OPEN_SQ_BRACKET = 48
    CLOSE_SQ_BRACKET = 49
    COMMA = 50
    DOT = 51
    DOTDOT = 52
    COLON = 53
    SPACE = 54
    SKIP_ = 55
    NEWLINE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'@run'", "'graph'", "'function'", "'return'", 
            "'pass'", "'if'", "'else if'", "'else'", "'while'", "'for each'", 
            "'ref'", "'='", "'or'", "'and'", "'not'", "'<'", "'>'", "'<='", 
            "'>='", "'in'", "'not in'", "'is'", "'is not'", "'+'", "'-'", 
            "'union'", "'intersect'", "'diff'", "'concat'", "'*'", "'/'", 
            "'%'", "'/-'", "'/+'", "'log'", "'^'", "'root'", "'->'", "'('", 
            "')'", "'['", "']'", "','", "'.'", "'..'", "':'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", "FUNCTION", 
            "RETURN", "PASS", "IF", "ELSEIF", "ELSE", "WHILE", "FOREACH", 
            "REF", "ASSIGN", "OR", "AND", "NOT", "LESS_THAN", "GREATER_THAN", 
            "LESS_EQUAL", "GREATER_EQUAL", "IN", "NOT_IN", "IS", "IS_NOT", 
            "PLUS", "MINUS", "UNION", "INTERSECT", "DIFF", "CONCAT", "TIMES", 
            "DIVIDE", "MODULO", "FLOORDIVISION", "CEILINGDIVISION", "LOG", 
            "POWER", "ROOT", "DIRECTED", "VAR_ID", "FUNC_ID", "OPEN_PAREN", 
            "CLOSE_PAREN", "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", "COMMA", 
            "DOT", "DOTDOT", "COLON", "SPACE", "SKIP_", "NEWLINE" ]

    ruleNames = [ "STRING", "INT", "FLOAT", "TRUE", "FALSE", "RUN", "GRAPH", 
                  "FUNCTION", "RETURN", "PASS", "IF", "ELSEIF", "ELSE", 
                  "WHILE", "FOREACH", "REF", "ASSIGN", "OR", "AND", "NOT", 
                  "LESS_THAN", "GREATER_THAN", "LESS_EQUAL", "GREATER_EQUAL", 
                  "IN", "NOT_IN", "IS", "IS_NOT", "PLUS", "MINUS", "UNION", 
                  "INTERSECT", "DIFF", "CONCAT", "TIMES", "DIVIDE", "MODULO", 
                  "FLOORDIVISION", "CEILINGDIVISION", "LOG", "POWER", "ROOT", 
                  "DIRECTED", "VAR_ID", "FUNC_ID", "OPEN_PAREN", "CLOSE_PAREN", 
                  "OPEN_SQ_BRACKET", "CLOSE_SQ_BRACKET", "COMMA", "DOT", 
                  "DOTDOT", "COLON", "LETTER", "DIGIT", "LOWERLETTER", "UPPERLETTER", 
                  "SPACES", "SPACE", "COMMENT", "SKIP_", "NEWLINE" ]

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
    		actions[61] = self.NEWLINE_action 
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
            preds[61] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         



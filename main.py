from gen.SimplifiedJavaLexer import SimplifiedJavaLexer
from gen.SimplifiedJavaParser import SimplifiedJavaParser
from gen.SimplifiedJavaVisitor import SimplifiedJavaVisitor
from antlr4 import *


def main():
    lexer = SimplifiedJavaLexer(FileStream("test.txt"))
    stream = CommonTokenStream(lexer)
    parser = SimplifiedJavaParser(stream)
    tree = parser.prog()
    visitor = SimplifiedJavaVisitor()
    visitor.visit(tree)
    print(visitor.symbol_table)
    # print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main()

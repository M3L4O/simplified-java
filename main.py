from gen.SimplifiedJavaLexer import SimplifiedJavaLexer
from gen.SimplifiedJavaParser import SimplifiedJavaParser
from gen.SimplifiedJavaVisitor import SimplifiedJavaVisitor
from antlr4 import *
from rich import print

def main():
    lexer = SimplifiedJavaLexer(FileStream("test.txt"))
    stream = CommonTokenStream(lexer)
    parser = SimplifiedJavaParser(stream)
    tree = parser.prog()
    visitor = SimplifiedJavaVisitor()
    visitor.visit(tree)
    # print(tree.toStringTree(recog=parser))
    # print(visitor.symbol_table)


if __name__ == "__main__":
    main()

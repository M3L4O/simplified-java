from gen.SimplifiedJavaLexer import SimplifiedJavaLexer
from gen.SimplifiedJavaParser import SimplifiedJavaParser
from gen.SimplifiedJavaVisitor import SimplifiedJavaVisitor
from antlr4 import *
from rich import print


def main():
    lexer = SimplifiedJavaLexer(FileStream("test2.txt"))
    stream = CommonTokenStream(lexer)
    parser = SimplifiedJavaParser(stream)
    tree = parser.prog()
    visitor = SimplifiedJavaVisitor()
    visitor.visit(tree)
    # print(tree.toStringTree(recog=parser))
    # print(visitor.numeric_ids)
    # print(visitor.errors)
    # print(visitor.symbol_table)


if __name__ == "__main__":
    main()

from gen.SimplifiedJavaLexer import SimplifiedJavaLexer
from gen.SimplifiedJavaParser import SimplifiedJavaParser
from gen.SimplifiedJavaVisitor import SimplifiedJavaVisitor
from antlr4 import *
from rich import print
from os import path as ph

def main():
    file = "test2.txt"
    lexer = SimplifiedJavaLexer(FileStream(file))
    stream = CommonTokenStream(lexer)
    parser = SimplifiedJavaParser(stream)
    tree = parser.prog()
    visitor = SimplifiedJavaVisitor(ph.basename(file).split(".")[0])
    visitor.visit(tree)
    # print(tree.toStringTree(recog=parser))
    # print(visitor.numeric_ids)
    print(visitor.errors)
    # print(visitor.symbol_table)


if __name__ == "__main__":
    main()

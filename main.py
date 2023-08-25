from gen.SimplifiedJavaLexer import SimplifiedJavaLexer
from gen.SimplifiedJavaParser import SimplifiedJavaParser
from gen.SimplifiedJavaVisitor import SimplifiedJavaVisitor
from antlr4 import *
from rich import print
from os import path as ph
import os


def main():
    # file = input("Digite o caminho para o arquivo: ")
    file = "test2.txt"
    lexer = SimplifiedJavaLexer(FileStream(file, encoding="utf-8"))
    stream = CommonTokenStream(lexer)
    parser = SimplifiedJavaParser(stream)
    tree = parser.prog()
    # output_file = input("Digite o nome do arquivo de saída (sem extensão): ")
    output_file = "test"
    
    visitor = SimplifiedJavaVisitor(output_file)
    
    try:
        visitor.visit(tree)
        os.system(f"java -jar jasmin.jar {output_file}.j")
    except Exception as e:
        print("\nErrors:")
        print(e)
        
    # print(tree.toStringTree(recog=parser))
    # print(visitor.numeric_ids)
    # print(visitor.errors)
    # print(visitor.symbol_table)


if __name__ == "__main__":
    main()

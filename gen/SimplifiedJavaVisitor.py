# Generated from SimplifiedJava.g4 by ANTLR 4.13.0
from antlr4 import *

from gen.SimplifiedJavaParser import SimplifiedJavaParser

# This class defines a complete generic visitor for a parse tree produced by SimplifiedJavaParser.


class SimplifiedJavaVisitor(ParseTreeVisitor):
    symbol_table: dict = {}
    default_value: dict = {
        "int": 0,
        "float": 0.0,
        "bool": False,
        "str": "",
    }

    # Visit a parse tree produced by SimplifiedJavaParser#prog.
    def visitProg(self, ctx: SimplifiedJavaParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#main.
    def visitMain(self, ctx: SimplifiedJavaParser.MainContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#cmd.
    def visitCmd(self, ctx: SimplifiedJavaParser.CmdContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#print.
    def visitPrint(self, ctx: SimplifiedJavaParser.PrintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#scanf.
    def visitScanf(self, ctx: SimplifiedJavaParser.ScanfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#conditional.
    def visitConditional(self, ctx: SimplifiedJavaParser.ConditionalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#while.
    def visitWhile(self, ctx: SimplifiedJavaParser.WhileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#EvalTarget.
    def visitEvalTarget(self, ctx: SimplifiedJavaParser.EvalTargetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#Not.
    def visitNot(self, ctx: SimplifiedJavaParser.NotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#Mult.
    def visitMult(self, ctx: SimplifiedJavaParser.MultContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#Parens.
    def visitParens(self, ctx: SimplifiedJavaParser.ParensContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#Sum.
    def visitSum(self, ctx: SimplifiedJavaParser.SumContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#Logic.
    def visitLogic(self, ctx: SimplifiedJavaParser.LogicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#function.
    def visitFunction(self, ctx: SimplifiedJavaParser.FunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#functionCall.
    def visitFunctionCall(self, ctx: SimplifiedJavaParser.FunctionCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#return.
    def visitReturn(self, ctx: SimplifiedJavaParser.ReturnContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#break.
    def visitBreak(self, ctx: SimplifiedJavaParser.BreakContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#declScope.
    def visitDeclScope(self, ctx: SimplifiedJavaParser.DeclScopeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#constDeclaration.
    def visitConstDeclaration(self, ctx: SimplifiedJavaParser.ConstDeclarationContext):
        ids: list[str] = [id.getText() for id in ctx.ID()]
        values: list[SimplifiedJavaParser.ValuedExprContext] = [
            value for value in ctx.literal()
        ]
        for id, value in zip(ids, values):
            _type: str
            if value.String():
                _type = "str"
            elif value.Boolean():
                _type = "bool"
            elif value.Float():
                _type = "float"
            elif value.Int():
                _type = "int"
            else:
                raise Exception("Invalid type")

            self.symbol_table[id] = {
                "type": ("const", _type),
                "value": value.getText(),
            }
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#variableDeclaration.
    def visitVariableDeclaration(
        self, ctx: SimplifiedJavaParser.VariableDeclarationContext
    ):
        ids: list[str] = [id for id in ctx.ID()]
        _type = ctx.Type()

        if _type is None:
            raise Exception("Invalid type")
        
        _type = _type.getText()

        for id in ids:
            if id.getText() in self.symbol_table:
                raise Exception(f"Variable {id.getText()} already declared in this scope.")
            
            self.symbol_table[id.getText()] = {
                "type": ("var", _type),
                "value": self.default_value[_type],
            }

        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#assign.
    def visitAssign(self, ctx: SimplifiedJavaParser.AssignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#arith.
    def visitArith(self, ctx: SimplifiedJavaParser.ArithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#literal.
    def visitLiteral(self, ctx: SimplifiedJavaParser.LiteralContext):
        return self.visitChildren(ctx)


del SimplifiedJavaParser

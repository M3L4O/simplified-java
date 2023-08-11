# Generated from SimplifiedJava.g4 by ANTLR 4.13.0
from antlr4 import *
from gen.SimplifiedJavaParser import SimplifiedJavaParser
from gen.SimplifiedJavaParser import SimplifiedJavaParser as gambiarra

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

    # Visit a parse tree produced by SimplifiedJavaParser#break.
    def visitBreak(self, ctx: SimplifiedJavaParser.BreakContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#logicExpr.
    def visitLogicExpr(self, ctx: SimplifiedJavaParser.LogicExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#arithExpr.
    def visitArithExpr(self, ctx: SimplifiedJavaParser.ArithExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#binLogicOp.
    def visitBinLogicOp(self, ctx: SimplifiedJavaParser.BinLogicOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#unLogicOp.
    def visitUnLogicOp(self, ctx: SimplifiedJavaParser.UnLogicOpContext):
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

    # Visit a parse tree produced by SimplifiedJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx: SimplifiedJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#constDeclaration.
    def visitConstDeclaration(self, ctx: SimplifiedJavaParser.ConstDeclarationContext):
        ids: list[str] = [id.getText() for id in ctx.ID()]
        values: list[SimplifiedJavaParser.ValuedExprContext] = [
            value for value in ctx.valuedExpr()
        ]
        function_ctx = ctx.parentCtx.parentCtx
        scope: str

        match type(function_ctx):
            case gambiarra.MainContext:
                scope = "main"
            case gambiarra.FunctionContext:
                scope = function_ctx.ID()[0].getText()

        for id, value in zip(ids, values):
            _type: str
            value = value.value()
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
                "type": _type,
                "value": value.getText(),
                "scope": scope,
            }
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#variableDeclaration.
    def visitVariableDeclaration(
        self, ctx: SimplifiedJavaParser.VariableDeclarationContext
    ):

        function_ctx = ctx.parentCtx.parentCtx
        scope: str

        match type(function_ctx):
            case gambiarra.MainContext:
                scope = "main"
            case gambiarra.FunctionContext:
                scope = function_ctx.ID()[0].getText()

        _type = ctx.Type().getText()
        ids = [id.getText() for id in ctx.ID()]
        for id in ids:
            self.symbol_table[id] = {
                "type": _type,
                "value": self.default_value[_type],
                "scope": scope,
            }

        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#assign.
    def visitAssign(self, ctx: SimplifiedJavaParser.AssignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#valuedExpr.
    def visitValuedExpr(self, ctx: SimplifiedJavaParser.ValuedExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#comparable.
    def visitComparable(self, ctx: SimplifiedJavaParser.ComparableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#arith.
    def visitArith(self, ctx: SimplifiedJavaParser.ArithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#bool.
    def visitBool(self, ctx: SimplifiedJavaParser.BoolContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#numeric.
    def visitNumeric(self, ctx: SimplifiedJavaParser.NumericContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#value.
    def visitValue(self, ctx: SimplifiedJavaParser.ValueContext):
        return self.visitChildren(ctx)


del SimplifiedJavaParser

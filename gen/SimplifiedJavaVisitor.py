# Generated from SimplifiedJava.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .SimplifiedJavaParser import SimplifiedJavaParser
else:
    from SimplifiedJavaParser import SimplifiedJavaParser

from gen.SimplifiedJavaParser import SimplifiedJavaParser as parser

# This class defines a complete generic visitor for a parse tree produced by SimplifiedJavaParser.


class SimplifiedJavaVisitor(ParseTreeVisitor):
    symbol_table: dict = {}
    default_value: dict = {
        int: 0,
        float: 0.0,
        bool: False,
        str: "",
    }
    type_mapper: dict = {
        "int": int,
        "float": float,
        "bool": bool,
        "str": str,
        "void": None,
    }

    # Visit a parse tree produced by SimplifiedJavaParser#prog.
    def visitProg(self, ctx: SimplifiedJavaParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#main.
    def visitMain(self, ctx: SimplifiedJavaParser.MainContext):
        self.symbol_table["main"] = {
            "type" : "void",
            "args" : {},
            "const": {},
            "vars" : {},
        }

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
        function_type = self.type_mapper[ctx.functionType.text]

        function_id = ctx.ID()[0].getText()

        if function_id in self.symbol_table:
            print(f"Function {id} already declared in this scope.")
            ctx.visitChildren(self)

        else:
            self.symbol_table[function_id] = {
                "type": function_type,
                "args": {},
                "const": {},
                "vars": {},
            }

        types = [self.type_mapper[type.getText()] for type in ctx.Type()]
        ids = [id.getText() for id in ctx.ID()[1:]]

        for type, id in zip(types, ids):
            if (
                id
                in self.symbol_table[function_id]["const"].keys()
                | self.symbol_table[function_id]["vars"].keys()
                | self.symbol_table[function_id]["args"].keys()
                | self.symbol_table.keys()
            ):
                print(f"Variable {id} already declared in this scope.")
                continue
            else:
                self.symbol_table[function_id]["args"][id] = {
                    "type": type,
                    "value": self.default_value[type],
                }

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
        types: list = [
            self.visitLiteral(literal)[0] for literal in ctx.literal()
        ]
        values: list = [self.visitLiteral(literal)[1] for literal in ctx.literal()]
        scope = ctx.parentCtx.parentCtx

        if type(scope) == parser.MainContext:
            scope = "main"
        elif type(scope) == parser.FunctionContext:
            scope = scope.ID()[0].getText()

        for id, _type, value in zip(ids, types, values):
            if (
                id
                in self.symbol_table[scope]["const"].keys()
                | self.symbol_table[scope]["vars"].keys()
                | self.symbol_table[scope]["args"].keys()
                | self.symbol_table.keys()
            ):
                print(f"Variable {id} already declared in this scope.")
                continue

            self.symbol_table[scope]["const"][id] = {
                "type": _type,
                "value": value,
            }

        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#variableDeclaration.
    def visitVariableDeclaration(
        self, ctx: SimplifiedJavaParser.VariableDeclarationContext
    ):
        scope = ctx.parentCtx.parentCtx

        if type(scope) == parser.MainContext:
            scope = "main"
        elif type(scope) == parser.FunctionContext:
            scope = scope.ID()[0].getText()

        ids: list[str] = [id.getText() for id in ctx.ID()]

        _type = self.type_mapper[ctx.Type().getText()]

        for id in ids:
            if (
                id
                in self.symbol_table[scope]["const"].keys()
                | self.symbol_table[scope]["vars"].keys()
                | self.symbol_table[scope]["args"].keys()
                | self.symbol_table.keys()
            ):
                print(f"Variable {id} already declared in this scope.")
                continue
            self.symbol_table[scope]["vars"][id] = {
                "type": _type,
                "value": self.default_value[_type],
            }

        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#assign.
    def visitAssign(self, ctx: SimplifiedJavaParser.AssignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#arith.
    def visitArith(self, ctx: SimplifiedJavaParser.ArithContext):
        if ctx.functionCall():
            return self.visitFunctionCall(ctx.functionCall())
        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.ID():
            return ctx.ID().getText()

    # Visit a parse tree produced by SimplifiedJavaParser#literal.
    def visitLiteral(self, ctx: SimplifiedJavaParser.LiteralContext):
        if ctx.String():
            _type = str
            value = ctx.getText()[1:-1]
        elif ctx.Boolean():
            _type = bool
            value = ctx.getText() == "true"
        elif ctx.Float():
            _type = float
            value = float(ctx.getText())
        elif ctx.Int():
            _type = int
            value = int(ctx.getText())
        else:
            raise Exception("Invalid type")
        
        return _type, value

del SimplifiedJavaParser

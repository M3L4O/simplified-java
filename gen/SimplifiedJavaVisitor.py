# Generated from SimplifiedJava.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .SimplifiedJavaParser import SimplifiedJavaParser
else:
    from SimplifiedJavaParser import SimplifiedJavaParser

from seedwork.entity.nodes import Node, Node


class SimplifiedJavaVisitor(ParseTreeVisitor):
    def __init__(self):
        self.op_mapper = {
            SimplifiedJavaParser.SumContext: self.visitSum,
            SimplifiedJavaParser.MultContext: self.visitMult,
            SimplifiedJavaParser.LogicContext: self.visitLogic,
            SimplifiedJavaParser.NotContext: self.visitNot,
            SimplifiedJavaParser.ParensContext: self.visitParens,
            SimplifiedJavaParser.EvalTargetContext: self.visitEvalTarget,
        }

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

    def solveExpression(self, line: int, column: int, left: Node, op: str, right: Node):
        value = None
        if left.value and right.value:
            try:
                value = eval(f"{left.value} {op} {right.value}")
            except NameError:
                pass
        return Node(line=line, column=column, code="", type=left.type, value=value)

    # Visit a parse tree produced by SimplifiedJavaParser#prog.
    def visitProg(self, ctx: SimplifiedJavaParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#main.
    def visitMain(self, ctx: SimplifiedJavaParser.MainContext):
        self.symbol_table["main"] = {
            "type": "void",
            "args": {},
            "const": {},
            "vars": {},
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
        return self.visitArith(ctx.arith())

    # Visit a parse tree produced by SimplifiedJavaParser#Not.
    def visitNot(self, ctx: SimplifiedJavaParser.NotContext):
        operand = self.op_mapper[ctx.operand.__class__](ctx.operand)

        if ctx.op.text == "!" and operand.type == bool:
            return Node(
                line=ctx.start.line,
                column=ctx.start.column,
                code="",
                type=bool,
            )
        elif ctx.op.text == "-" and operand.type in (int, float):
            return Node(
                line=ctx.start.line,
                column=ctx.start.column,
                code="",
                type=operand.type,
            )
        else:
            print(f"Type mismatch: {ctx.op.text} and {operand.type}, {ctx.getText()}")

    # Visit a parse tree produced by SimplifiedJavaParser#Mult.
    def visitMult(self, ctx: SimplifiedJavaParser.MultContext):
        if ctx.left.__class__ is SimplifiedJavaParser.EvalTargetContext:
            left = self.visitEvalTarget(ctx.left)
        else:
            left = self.op_mapper[ctx.left.__class__](ctx.left)
        if ctx.right.__class__ is SimplifiedJavaParser.EvalTargetContext:
            right = self.visitEvalTarget(ctx.right)
        else:
            right = self.op_mapper[ctx.right.__class__](ctx.right)

        if (
            left.type not in (int, float)
            or right.type not in (int, float)
            or left.type != right.type
        ):
            print(f"Type mismatch: {left.type} and {right.type}, {ctx.getText()}")

        return self.solveExpression(
            ctx.start.line, ctx.start.column, left, ctx.op.text, right
        )

    # Visit a parse tree produced by SimplifiedJavaParser#Parens.
    def visitParens(self, ctx: SimplifiedJavaParser.ParensContext):
        node = self.op_mapper[ctx.expr().__class__](ctx.expr())
        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code="",
            type=node.type,
            value=node.value,
        )

    # Visit a parse tree produced by SimplifiedJavaParser#Sum.
    def visitSum(self, ctx: SimplifiedJavaParser.SumContext):
        if ctx.left.__class__ is SimplifiedJavaParser.EvalTargetContext:
            left = self.visitEvalTarget(ctx.left)
        else:
            left = self.op_mapper[ctx.left.__class__](ctx.left)
        if ctx.right.__class__ is SimplifiedJavaParser.EvalTargetContext:
            right = self.visitEvalTarget(ctx.right)
        else:
            right = self.op_mapper[ctx.right.__class__](ctx.right)

        if (
            left.type not in (int, float)
            or right.type not in (int, float)
            or left.type != right.type
        ):
            print(f"Type mismatch: {left.type} and {right.type}, {ctx.getText()}")

        return self.solveExpression(
            ctx.start.line, ctx.start.column, left, ctx.op.text, right
        )

    # Visit a parse tree produced by SimplifiedJavaParser#Logic.
    def visitLogic(self, ctx: SimplifiedJavaParser.LogicContext):
        if ctx.left.__class__ is SimplifiedJavaParser.EvalTargetContext:
            left = self.visitEvalTarget(ctx.left)
        else:
            left = self.op_mapper[ctx.left.__class__](ctx.left)
        if ctx.right.__class__ is SimplifiedJavaParser.EvalTargetContext:
            right = self.visitEvalTarget(ctx.right)

        if left.type not in (int, float, bool) or right.type not in (int, float, bool):
            print(f"Type mismatch: {left.type} and {right.type}, {ctx.getText()}")
        elif left.type != right.type:
            print(
                f"Type mismatch: {left.type} is not equal to {right.type}, {ctx.getText()}"
            )

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code="",
            type=bool,
        )

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
        terminals: list[Node] = [
            self.visitLiteral(literal) for literal in ctx.literal()
        ]
        scope = ctx.parentCtx.parentCtx

        if type(scope) == SimplifiedJavaParser.MainContext:
            scope = "main"
        elif type(scope) == SimplifiedJavaParser.FunctionContext:
            scope = scope.ID()[0].getText()

        for id, terminal in zip(ids, terminals):
            if (
                id
                in self.symbol_table[scope]["const"].keys()
                | self.symbol_table[scope]["vars"].keys()
                | self.symbol_table[scope]["args"].keys()
                | self.symbol_table.keys()
            ):
                print(f"Variable {id} already declared in this scope in line {ctx.start.line}")
                continue

            self.symbol_table[scope]["const"][id] = {
                "type": terminal.type,
                "value": terminal.value,
            }

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code="",
            type=None,
        )

    # Visit a parse tree produced by SimplifiedJavaParser#variableDeclaration.
    def visitVariableDeclaration(
        self, ctx: SimplifiedJavaParser.VariableDeclarationContext
    ):
        scope = ctx.parentCtx.parentCtx

        if type(scope) == SimplifiedJavaParser.MainContext:
            scope = "main"
        elif type(scope) == SimplifiedJavaParser.FunctionContext:
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
                print(f"Variable {id} already declared in this scope in line {ctx.start.line}")
                continue
            self.symbol_table[scope]["vars"][id] = {
                "type": _type,
                "value": self.default_value[_type],
            }

        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#assign.
    def visitAssign(self, ctx: SimplifiedJavaParser.AssignContext):
        parent = ctx.parentCtx.parentCtx
        scope = (
            "main"
            if parent.__class__ == SimplifiedJavaParser.MainContext
            else parent.ID()[0].getText()
        )
        expr = self.op_mapper[ctx.expr().__class__](ctx.expr())
        if self.symbol_table[scope]["const"].get(ctx.ID().getText()):
            print(
                f"Cannot assign to const {ctx.ID().getText()} in line {ctx.start.line}"
            )
        elif not self.symbol_table[scope]["vars"].get(ctx.ID().getText()):
            print(f"Variable {ctx.ID().getText()} not declared in this scope in line {ctx.start.line}")
        elif expr.type != self.symbol_table[scope]["vars"][ctx.ID().getText()]["type"]:
            print(
                f"Type mismatch: {self.symbol_table[scope]['vars'][ctx.ID().getText()]['type']} and {expr.type}, {ctx.getText()}"
            )


    # Visit a parse tree produced by SimplifiedJavaParser#arith.
    def visitArith(self, ctx: SimplifiedJavaParser.ArithContext):
        if ctx.functionCall():
            pass
            # return self.visitFunctionCall(ctx.functionCall())
        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.ID():
            parent = ctx.parentCtx
            while (
                parent.__class__ is not SimplifiedJavaParser.MainContext
                and parent.__class__ is not SimplifiedJavaParser.FunctionContext
            ):
                parent = parent.parentCtx

            scope = (
                "main"
                if parent.__class__ is SimplifiedJavaParser.MainContext
                else parent.ID()[0].getText()
            )
            if self.symbol_table[scope]["const"].get(ctx.ID().getText()):
                const = self.symbol_table[scope]["const"][ctx.ID().getText()]
                value = const["value"]
                _type = const["type"]
            elif self.symbol_table[scope]["vars"].get(ctx.ID().getText()):
                var = self.symbol_table[scope]["vars"][ctx.ID().getText()]
                value = None
                _type = var["type"]
            elif self.symbol_table[scope]["args"].get(ctx.ID().getText()):
                arg = self.symbol_table[scope]["args"][ctx.ID().getText()]
                value = None
                _type = arg["type"]
            else:
                print(f"Variable {ctx.ID().getText()} not declared in this scope.")
                return 
            
            return Node(
                line=ctx.ID(),
                column=ctx.ID(),
                code="",
                value=value,
                type=_type,
            )

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

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code="",
            value=value,
            type=_type,
        )

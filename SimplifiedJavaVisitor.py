# Generated from SimplifiedJava.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .SimplifiedJavaParser import SimplifiedJavaParser
    from .JasminMapper import JasminMapper
else:
    from SimplifiedJavaParser import SimplifiedJavaParser
    from JasminMapper import JasminMapper

from seedwork.entity.nodes import Node


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
        self.node_mapper = {
            SimplifiedJavaParser.MainContext: self.visitMain,
            SimplifiedJavaParser.FunctionContext: self.visitFunction,
            SimplifiedJavaParser.ConstDeclarationContext: self.visitConstDeclaration,
            SimplifiedJavaParser.VariableDeclarationContext: self.visitVariableDeclaration,
            SimplifiedJavaParser.AssignContext: self.visitAssign,
            SimplifiedJavaParser.PrintContext: self.visitPrint,
            SimplifiedJavaParser.ScanfContext: self.visitScanf,
            SimplifiedJavaParser.ConditionalContext: self.visitConditional,
            SimplifiedJavaParser.WhileContext: self.visitWhile,
            SimplifiedJavaParser.ReturnContext: self.visitReturn,
            SimplifiedJavaParser.BreakContext: self.visitBreak,
            SimplifiedJavaParser.DeclScopeContext: self.visitDeclScope,
            SimplifiedJavaParser.FunctionCallContext: self.visitFunctionCall,
            SimplifiedJavaParser.ArithContext: self.visitArith,
            SimplifiedJavaParser.LiteralContext: self.visitLiteral,
            SimplifiedJavaParser.CmdContext: self.visitCmd,
        }

    jasmin_mapper = JasminMapper()
    has_error: bool = False
    errors: list[str] = []
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

    def get_scope(self, ctx):
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
        return scope

    def error(self, message: str):
        self.errors.append(message)
        self.has_error = True

    # Visit a parse tree produced by SimplifiedJavaParser#prog.
    def visitProg(self, ctx: SimplifiedJavaParser.ProgContext):
        if ctx.function():
            functions = [
                self.node_mapper[function.__class__](function)
                for function in ctx.function()
            ]
            print("\n".join([function.code for function in functions]))
        if ctx.main():
            main = self.node_mapper[ctx.main().__class__](ctx.main())
            print(main.code)

    # Visit a parse tree produced by SimplifiedJavaParser#main.
    def visitMain(self, ctx: SimplifiedJavaParser.MainContext):
        self.symbol_table["main"] = {
            "type": "void",
            "args": {},
            "const": {},
            "vars": {},
        }

        self.jasmin_mapper.numeric_ids["main"] = {
            "const": {},
            "vars": {},
        }

        initial = ".method public static main([Ljava/lang/String;)V\n"
        decl = self.visitDeclScope(ctx.declScope()).code if ctx.declScope() else ""
        locals = f".limit stack 100\n.limit locals {len(self.symbol_table['main']['vars'].keys())}\n"
        cmds = "".join([self.node_mapper[cmd.__class__](cmd).code for cmd in ctx.cmd()])
        final = f".end method\n"

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code=initial + locals + decl + cmds + final,
        )

    # Visit a parse tree produced by SimplifiedJavaParser#cmd.
    def visitCmd(self, ctx: SimplifiedJavaParser.CmdContext):
        if ctx.assign():
            return self.node_mapper[ctx.assign().__class__](ctx.assign())
        elif ctx.functionCall():
            return self.node_mapper[ctx.functionCall().__class__](ctx.functionCall())
        elif ctx.conditional():
            return self.node_mapper[ctx.conditional().__class__](ctx.conditional())
        elif ctx.while_():
            return self.node_mapper[ctx.while_().__class__](ctx.while_())
        elif ctx.print():
            return self.node_mapper[ctx.print().__class__](ctx.print())
        elif ctx.scanf():
            return self.node_mapper[ctx.scanf().__class__](ctx.scanf())
        elif ctx.return_():
            return self.node_mapper[ctx.return_().__class__](ctx.return_())
        elif ctx.break_():
            return self.node_mapper[ctx.break_().__class__](ctx.break_())

    # Visit a parse tree produced by SimplifiedJavaParser#print.
    def visitPrint(self, ctx: SimplifiedJavaParser.PrintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#scanf.
    def visitScanf(self, ctx: SimplifiedJavaParser.ScanfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SimplifiedJavaParser#conditional.
    def visitConditional(self, ctx: SimplifiedJavaParser.ConditionalContext):
        expr = self.op_mapper[ctx.expr().__class__](ctx.expr())
        if expr.type != bool:
            self.error(
                f"Type mismatch: {expr.type} and bool in line {ctx.start.line}: {ctx.getText()}"
            )

        true_label = self.jasmin_mapper.increase_label()
        next_label = self.jasmin_mapper.increase_label()
        if_cmds = ""
        else_cmds = ""
        # if ctx.ifCmd:
        #     if_cmds = "".join([self.node_mapper[cmd.__class__](cmd).code for cmd in ctx.ifCmd])
        # if ctx.elseCmd:
        #     else_cmds = "".join([self.node_mapper[cmd.__class__](cmd).code for cmd in ctx.elseCmd])
        
        
        
        code = f"{expr.code}ifeq L{true_label}\n{else_cmds}goto L{next_label}\nL{true_label}:\n{if_cmds}\nL{next_label}:\n"



        return Node(line=ctx.start.line, column=ctx.start.column, code=code)

    # Visit a parse tree produced by SimplifiedJavaParser#while.
    def visitWhile(self, ctx: SimplifiedJavaParser.WhileContext):
        expr = self.op_mapper[ctx.expr().__class__](ctx.expr())

        if expr.type != bool:
            self.error(
                f"Type mismatch: {expr.type} and bool in line {ctx.start.line}: {ctx.getText()}"
            )

        external_label = self.jasmin_mapper.increase_label()
        internal_label = self.jasmin_mapper.increase_label()
        next_label = self.jasmin_mapper.increase_label()
        results = [self.node_mapper[cmd.__class__](cmd) for cmd in ctx.cmd()]

        code = f"L{external_label}: {expr.code}ifeq L{internal_label}\ngoto L{next_label}\nL{internal_label}:\n{''.join([result.code for result in results])}\ngoto L{external_label}\nL{next_label}:"

        return Node(line=ctx.start.line, column=ctx.start.column, code=code)

    # Visit a parse tree produced by SimplifiedJavaParser#EvalTarget.
    def visitEvalTarget(self, ctx: SimplifiedJavaParser.EvalTargetContext):
        return self.visitArith(ctx.arith())

    # Visit a parse tree produced by SimplifiedJavaParser#Not.
    def visitNot(self, ctx: SimplifiedJavaParser.NotContext):
        operand = self.op_mapper[ctx.operand.__class__](ctx.operand)

        if (
            ctx.op.text == "!"
            and operand.type == bool
            or ctx.op.text == "-"
            and operand.type in (int, float)
        ):
            return self.solveExpression(
                ctx.start.line, ctx.start.column, operand, ctx.op.text
            )
        else:
            self.error(
                f"Type mismatch: {ctx.op.text} and {operand.type} in line {ctx.start.line}: {ctx.getText()}"
            )

    # Visit a parse tree produced by SimplifiedJavaParser#Mult.
    def visitMult(self, ctx: SimplifiedJavaParser.MultContext):
        left = self.op_mapper[ctx.left.__class__](ctx.left)

        right = self.op_mapper[ctx.right.__class__](ctx.right)

        if (
            left.type not in (int, float)
            or right.type not in (int, float)
            or left.type != right.type
        ):
            self.error(
                f"Type mismatch: {left.type} and {right.type} in line {ctx.start.line}: {ctx.getText()}"
            )

        code = f"{left.code}{right.code}{self.jasmin_mapper.arith_op_mapping[ctx.op.text][left.type]}\n"

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            type=right.type,
            code=code,
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
        left = self.op_mapper[ctx.left.__class__](ctx.left)

        right = self.op_mapper[ctx.right.__class__](ctx.right)
        if (
            left.type not in (int, float)
            or right.type not in (int, float)
            or left.type != right.type
        ):
            self.error(
                f"Type mismatch: {left.type} and {right.type} in line {ctx.start.line}: {ctx.getText()}"
            )
        code = f"{left.code}{right.code}{self.jasmin_mapper.arith_op_mapping[ctx.op.text][left.type]}\n"

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            type=left.type,
            code=code,
        )

    def visitLogic(self, ctx: SimplifiedJavaParser.LogicContext):
        if ctx.left.__class__ is SimplifiedJavaParser.LogicContext:
            self.error(
                f"Nested logic expressions are not supported in line {ctx.start.line}: {ctx.getText()}"
            )
            return Node(
                line=ctx.start.line,
                column=ctx.start.column,
                code="",
                type=bool,
            )
        else:
            left = self.op_mapper[ctx.left.__class__](ctx.left)

            right = self.op_mapper[ctx.right.__class__](ctx.right)

        if left.type != right.type:
            self.error(
                f"Type mismatch: {left.type} is not equal to {right.type} in line {ctx.start.line}: {ctx.getText()}"
            )

        true_label = self.jasmin_mapper.increase_label()
        next_label = self.jasmin_mapper.increase_label()

        code = f"{left.code}{right.code}{self.jasmin_mapper.arith_op_mapping[ctx.op.text][left.type]} goto L{true_label}\n"
        code += f"ldc 1\ngoto L{next_label}\nL{true_label}:\nldc 0\nL{next_label}:\n"

        return Node(line=ctx.start.line, column=ctx.start.column, code=code)

    def visitFunction(self, ctx: SimplifiedJavaParser.FunctionContext):
        function_type = self.type_mapper[ctx.functionType.text]

        function_id = ctx.ID()[0].getText()

        self.jasmin_mapper.numeric_ids[function_id] = {
            "const": {},
            "vars": {},
        }

        if function_id in self.symbol_table:
            self.error(
                f"Function {id} already declared in this scope  in line {ctx.start.line}: {ctx.getText()}"
            )

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
                | self.symbol_table.keys()
            ):
                self.error(
                    f"Variable {id} already declared in this scope  in line {ctx.start.line}: {ctx.getText()}"
                )
                continue
            else:
                self.symbol_table[function_id]["args"][id] = {
                    "type": type,
                    "value": self.default_value[type],
                }
                self.symbol_table[function_id]["vars"][id] = {
                    "type": type,
                    "value": self.default_value[type],
                }

                self.jasmin_mapper.numeric_ids[function_id]["vars"][
                    id
                ] = self.jasmin_mapper.increase_nid(scope=function_id)

        initial = self.jasmin_mapper.generate_function(function_id, function_type)
        locals = f".limit stack 100\n.limit locals {len(self.symbol_table[function_id]['vars'].keys())}\n"
        decl = self.visitDeclScope(ctx.declScope()).code if ctx.declScope() else ""
        cmds = [self.node_mapper[cmd.__class__](cmd).code for cmd in ctx.cmd()]
        final = f".end method\n"

        code = f"{initial}{locals}{decl}{''.join([cmd for cmd in cmds])}{final}"
        return Node(line=ctx.start.line, column=ctx.start.column, code=code)

    def visitFunctionCall(self, ctx: SimplifiedJavaParser.FunctionCallContext):
        if ctx.ID().getText() not in self.symbol_table:
            self.error(
                f"Function {ctx.ID().getText()} not declared in this scope  in line {ctx.start.line}: {ctx.getText()}"
            )

        args = self.symbol_table[ctx.ID().getText()]["args"].keys()
        if len(args) != len(ctx.expr()):
            self.error(
                f"Expected {len(ctx.expr())} arguments, got {len(args)} in line {ctx.start.line}: {ctx.getText()}"
            )

        for arg, expr in zip(args, ctx.expr()):
            expr = self.op_mapper[expr.__class__](expr)
            if expr.type != self.symbol_table[ctx.ID().getText()]["args"][arg]["type"]:
                self.error(
                    f"Type mismatch: {expr.type} and {self.symbol_table[ctx.ID().getText()]['args'][arg]['type']} in line {ctx.start.line}: {ctx.getText()}"
                )

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code="",
            type=self.symbol_table[ctx.ID().getText()]["type"],
        )

    # Visit a parse tree produced by SimplifiedJavaParser#return.
    def visitReturn(self, ctx: SimplifiedJavaParser.ReturnContext):
        scope = self.get_scope(ctx)
        type_function = self.symbol_table[scope]["type"]
        if ctx.expr():
            expr = self.op_mapper[ctx.expr().__class__](ctx.expr())
            if expr:
                if expr.type != type_function:
                    self.error(
                        f"Type mismatch: {expr.type} and {type_function} in line {ctx.start.line}: {ctx.getText()}"
                    )

        else:
            if type_function != None:
                self.error(
                    f"Type mismatch: None and {type_function} in line {ctx.start.line}: {ctx.getText()}"
                )
            else:
                code = f"return\n"

        return Node(line=ctx.start.line, column=ctx.start.column, code="")

    # Visit a parse tree produced by SimplifiedJavaParser#break.
    def visitBreak(self, ctx: SimplifiedJavaParser.BreakContext):
        parent = ctx.parentCtx
        while (
            parent.__class__ is not SimplifiedJavaParser.WhileContext
            and parent.__class__ is not SimplifiedJavaParser.ProgContext
        ):
            parent = parent.parentCtx

        if parent.__class__ is SimplifiedJavaParser.ProgContext:
            self.error(
                f"Break statement outside of loop in line {ctx.start.line}: {ctx.getText()}"
            )
        return Node(line=ctx.start.line, column=ctx.start.column, code="")

    # Visit a parse tree produced by SimplifiedJavaParser#declScope.
    def visitDeclScope(self, ctx: SimplifiedJavaParser.DeclScopeContext):
        consts: list[Node] = []
        variables: list[Node] = []
        if ctx.constDeclaration():
            consts = [
                self.node_mapper[constDeclaration.__class__](constDeclaration)
                for constDeclaration in ctx.constDeclaration()
            ]

        elif ctx.variableDeclaration():
            variables = [
                self.node_mapper[variableDeclaration.__class__](variableDeclaration)
                for variableDeclaration in ctx.variableDeclaration()
            ]
        else:
            return None

        code = "".join([const.code for const in consts]) + "".join(
            [var.code for var in variables]
        )

        return Node(line=ctx.start.line, column=ctx.start.column, code=code)

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
                | self.symbol_table.keys()
            ):
                self.error(
                    f"Variable {id} already declared in this scope  in line {ctx.start.line}: {ctx.getText()}"
                )
                continue

            self.symbol_table[scope]["const"][id] = {
                "type": terminal.type,
                "value": terminal.value,
            }

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code="",
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
        codes: list[str] = []
        for id in ids:
            if (
                id
                in self.symbol_table[scope]["const"].keys()
                | self.symbol_table[scope]["vars"].keys()
                | self.symbol_table.keys()
            ):
                self.error(
                    f"Variable {id} already declared in this scope  in line {ctx.start.line}: {ctx.getText()}"
                )
                continue
            self.symbol_table[scope]["vars"][id] = {
                "type": _type,
                "value": self.default_value[_type],
            }

            nid = self.jasmin_mapper.increase_nid(scope)
            self.jasmin_mapper.numeric_ids[scope]["vars"][id] = nid
            codes.append(
                self.jasmin_mapper.generate_assign(
                    _type, nid, self.default_value[_type]
                )
            )

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code="".join(codes),
            type=None,
        )

    # Visit a parse tree produced by SimplifiedJavaParser#assign.
    def visitAssign(self, ctx: SimplifiedJavaParser.AssignContext):
        scope = self.get_scope(ctx)
        expr = self.op_mapper[ctx.expr().__class__](ctx.expr())

        if self.symbol_table[scope]["const"].get(ctx.ID().getText()):
            self.error(
                f"Cannot assign to const {ctx.ID().getText()} in line {ctx.start.line}: {ctx.getText()}"
            )
        elif not self.symbol_table[scope]["vars"].get(ctx.ID().getText()):
            self.error(
                f"Variable {ctx.ID().getText()} not declared in this scope in line {ctx.start.line}: {ctx.getText()}"
            )
        elif expr.type != self.symbol_table[scope]["vars"][ctx.ID().getText()]["type"]:
            self.error(
                f"Type mismatch: {self.symbol_table[scope]['vars'][ctx.ID().getText()]['type']} and {expr.type} in line {ctx.start.line}: {ctx.getText()}"
            )

        nid = self.jasmin_mapper.numeric_ids[scope]["vars"][ctx.ID().getText()]

        code = f"{expr.code}\n{self.jasmin_mapper.store_types[expr.type]} {nid}\n"

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code=code,
            type=None,
        )

    # Visit a parse tree produced by SimplifiedJavaParser#arith.
    def visitArith(self, ctx: SimplifiedJavaParser.ArithContext):
        if ctx.functionCall():
            return self.visitFunctionCall(ctx.functionCall())
        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.ID():
            scope = self.get_scope(ctx)
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
                self.error(
                    f"Variable {ctx.ID().getText()} not declared in this scope in line {ctx.start.line}: {ctx.getText()}"
                )
                return
            nid = self.jasmin_mapper.find_nid_in_scope(ctx.ID().getText(), scope)
            load_type = self.jasmin_mapper.load_types[_type]
            code = f"{load_type} {nid}\n"

            return Node(
                line=None,
                column=None,
                code=code,
                value=value,
                type=_type,
            )

    # Visit a parse tree produced by SimplifiedJavaParser#literal.
    def visitLiteral(self, ctx: SimplifiedJavaParser.LiteralContext):
        if ctx.String():
            _type = str
            value = ctx.getText()
            code = value
        elif ctx.Boolean():
            _type = bool
            value = ctx.getText() == "true"
            code = f"ldc {0 if value else 1}\n"
        elif ctx.Float():
            _type = float
            value = float(ctx.getText())
            code = f"ldc {value}\n"
        elif ctx.Int():
            _type = int
            value = int(ctx.getText())
            code = f"ldc {value}\n"
        else:
            raise Exception("Invalid type")

        code = f"ldc {value}\n"

        return Node(
            line=ctx.start.line,
            column=ctx.start.column,
            code=code,
            value=value,
            type=_type,
        )

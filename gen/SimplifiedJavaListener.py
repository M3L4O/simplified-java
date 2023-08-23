# Generated from SimplifiedJava.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimplifiedJavaParser import SimplifiedJavaParser
else:
    from SimplifiedJavaParser import SimplifiedJavaParser

# This class defines a complete listener for a parse tree produced by SimplifiedJavaParser.
class SimplifiedJavaListener(ParseTreeListener):

    # Enter a parse tree produced by SimplifiedJavaParser#prog.
    def enterProg(self, ctx:SimplifiedJavaParser.ProgContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#prog.
    def exitProg(self, ctx:SimplifiedJavaParser.ProgContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#main.
    def enterMain(self, ctx:SimplifiedJavaParser.MainContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#main.
    def exitMain(self, ctx:SimplifiedJavaParser.MainContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#cmds.
    def enterCmds(self, ctx:SimplifiedJavaParser.CmdsContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#cmds.
    def exitCmds(self, ctx:SimplifiedJavaParser.CmdsContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#cmd.
    def enterCmd(self, ctx:SimplifiedJavaParser.CmdContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#cmd.
    def exitCmd(self, ctx:SimplifiedJavaParser.CmdContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#print.
    def enterPrint(self, ctx:SimplifiedJavaParser.PrintContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#print.
    def exitPrint(self, ctx:SimplifiedJavaParser.PrintContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#scanf.
    def enterScanf(self, ctx:SimplifiedJavaParser.ScanfContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#scanf.
    def exitScanf(self, ctx:SimplifiedJavaParser.ScanfContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#conditional.
    def enterConditional(self, ctx:SimplifiedJavaParser.ConditionalContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#conditional.
    def exitConditional(self, ctx:SimplifiedJavaParser.ConditionalContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#while.
    def enterWhile(self, ctx:SimplifiedJavaParser.WhileContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#while.
    def exitWhile(self, ctx:SimplifiedJavaParser.WhileContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#EvalTarget.
    def enterEvalTarget(self, ctx:SimplifiedJavaParser.EvalTargetContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#EvalTarget.
    def exitEvalTarget(self, ctx:SimplifiedJavaParser.EvalTargetContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#Not.
    def enterNot(self, ctx:SimplifiedJavaParser.NotContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#Not.
    def exitNot(self, ctx:SimplifiedJavaParser.NotContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#Mult.
    def enterMult(self, ctx:SimplifiedJavaParser.MultContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#Mult.
    def exitMult(self, ctx:SimplifiedJavaParser.MultContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#Parens.
    def enterParens(self, ctx:SimplifiedJavaParser.ParensContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#Parens.
    def exitParens(self, ctx:SimplifiedJavaParser.ParensContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#Sum.
    def enterSum(self, ctx:SimplifiedJavaParser.SumContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#Sum.
    def exitSum(self, ctx:SimplifiedJavaParser.SumContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#Logic.
    def enterLogic(self, ctx:SimplifiedJavaParser.LogicContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#Logic.
    def exitLogic(self, ctx:SimplifiedJavaParser.LogicContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#function.
    def enterFunction(self, ctx:SimplifiedJavaParser.FunctionContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#function.
    def exitFunction(self, ctx:SimplifiedJavaParser.FunctionContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#functionCall.
    def enterFunctionCall(self, ctx:SimplifiedJavaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#functionCall.
    def exitFunctionCall(self, ctx:SimplifiedJavaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#return.
    def enterReturn(self, ctx:SimplifiedJavaParser.ReturnContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#return.
    def exitReturn(self, ctx:SimplifiedJavaParser.ReturnContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#break.
    def enterBreak(self, ctx:SimplifiedJavaParser.BreakContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#break.
    def exitBreak(self, ctx:SimplifiedJavaParser.BreakContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#declScope.
    def enterDeclScope(self, ctx:SimplifiedJavaParser.DeclScopeContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#declScope.
    def exitDeclScope(self, ctx:SimplifiedJavaParser.DeclScopeContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#constDeclaration.
    def enterConstDeclaration(self, ctx:SimplifiedJavaParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#constDeclaration.
    def exitConstDeclaration(self, ctx:SimplifiedJavaParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SimplifiedJavaParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SimplifiedJavaParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#assign.
    def enterAssign(self, ctx:SimplifiedJavaParser.AssignContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#assign.
    def exitAssign(self, ctx:SimplifiedJavaParser.AssignContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#arith.
    def enterArith(self, ctx:SimplifiedJavaParser.ArithContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#arith.
    def exitArith(self, ctx:SimplifiedJavaParser.ArithContext):
        pass


    # Enter a parse tree produced by SimplifiedJavaParser#literal.
    def enterLiteral(self, ctx:SimplifiedJavaParser.LiteralContext):
        pass

    # Exit a parse tree produced by SimplifiedJavaParser#literal.
    def exitLiteral(self, ctx:SimplifiedJavaParser.LiteralContext):
        pass



del SimplifiedJavaParser
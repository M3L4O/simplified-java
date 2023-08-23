grammar SimplifiedJava;

prog: function* main EOF;

main: 'main' ':' declScope? cmd* 'end';
cmds: cmd*;
cmd:
	(assign | functionCall | break | return) ';'
	| conditional
	| while
	| print
	| scanf;

print: 'print' '(' expr (',' expr)* ')' ';';
scanf: 'scanf' '(' ID (',' ID)* ')' ';';

conditional:
	'if' '(' expr ')' ':' ifCmds=cmds ('else' ':' elseCmds=cmds)? 'end';
while: 'while' '(' expr ')' ':' cmd* 'end';

expr:
	left = expr op = ('*' | '/') right = expr								# Mult
	| left = expr op = ('+' | '-') right = expr								# Sum
	| left = expr op = ('==' | '!=' | '>=' | '<=' | '>' | '<') right = expr	# Logic
	| op = ('!' | '-') operand = expr										# Not
	| eval = arith															# EvalTarget
	| '(' expr ')'															# Parens;

function:
	ID '(' (Type ID (',' Type ID)*)? ')' ':' functionType=(Type | 'void') declScope? cmd* 'end';

functionCall: ID '(' (expr (',' expr)*)? ')';

return: ('return' expr?);
break: 'break';

declScope:
	'var' ':' ((constDeclaration | variableDeclaration) ';')+;

constDeclaration: 'const' ID '=' literal (',' ID '=' literal)*;

variableDeclaration: ID (',' ID)* ':' Type;

assign: ID '=' expr;

arith: (ID | literal | functionCall);
literal: String | Int | Float | Boolean;

String: '"' (Char | UnicodeChar | EscapeSequence)* '"';
Int: '0' | [1-9] Digit* ('e' '-'? Digit*)?;
Float: ('0' | [1-9] Digit*) ('.' Digit+) ('e' '-'? Digit*)?;
Boolean: 'true' | 'false';

Type: 'int' | 'float' | 'str' | 'bool';

ID: Letter (Letter | Digit | '_')*;

COMMENT: ('//' .*? ('\n' | EOF) | '/*' .*? '*/') -> skip;
WHITESPACE: [ \r\n\t]+ -> skip;

fragment Char: Letter | Digit | Symbol | ~["\r\n];
fragment UnicodeChar:
	[\p{Alpha}\p{General_Category=Other_Letter}];
fragment EscapeSequence: '\\' ['"nrt\\];
fragment Digit: [0-9];
fragment Letter: [a-zA-Z];
fragment Symbol: '?' | '!' | ',' | '.';
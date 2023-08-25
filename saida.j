.class public saida
.super java/lang/Object
.method public static fatorial(I)I
.limit stack 100
.limit locals 2
iload 0
ldc 0
if_icmpgt L0
ldc 1
goto L1
L0:
ldc 0
L1:
ifeq L2
ldc 1

ireturn
goto L3
L2:
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 0
invokevirtual java/io/PrintStream/print(I)V

getstatic java/lang/System/out Ljava/io/PrintStream;
ldc "\n"
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

iload 0
iload 0
ldc 1
isub

invokestatic saida/fatorial(I)I
imul

ireturn

L3:
ireturn
.end method

.method public static media(II)I
.limit stack 100
.limit locals 4
ldc 0
istore 2
iload 0
iload 1
iadd
ldc 2
idiv

istore 2
iload 2

ireturn
.end method

.method public static mostrarMedia(II)V
.limit stack 100
.limit locals 6
ldc 0
istore 2
ldc 0
istore 3
ldc 0.0
fstore 4
ldc 5
ldc 5
ldc 3
imul
iadd

istore 2
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc "Resultado: "
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

getstatic java/lang/System/out Ljava/io/PrintStream;
iload 0
iload 1

invokestatic saida/media(II)I
invokevirtual java/io/PrintStream/print(I)V

return 
return
.end method

.method public static main([Ljava/lang/String;)V
.limit stack 100
.limit locals 5
ldc 0
istore 0
ldc 0
istore 1
ldc 0
istore 2
ldc 1
istore 3
ldc 1
ldc 0

isub
istore 3
getstatic java/lang/System/out Ljava/io/PrintStream;
ldc "Programa Fatorial. Digite o valor?"
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
astore 4
aload 4
invokevirtual java/util/Scanner/nextInt()I
istore 0
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 0

invokestatic saida/fatorial(I)I
invokevirtual java/io/PrintStream/print(I)V

getstatic java/lang/System/out Ljava/io/PrintStream;
ldc "\n"
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

getstatic java/lang/System/out Ljava/io/PrintStream;
ldc "Programa Media. Digite o valores?"
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
astore 4
aload 4
invokevirtual java/util/Scanner/nextInt()I
istore 1
aload 4
invokevirtual java/util/Scanner/nextInt()I
istore 2
iload 1
iload 2

invokestatic saida/mostrarMedia(II)V
return
.end method

#ler 3 valores para os lados de triangulo(a,b,c)
#verificar se formam um triangulo
#se a condição for verdadeira indicar qual triangulo é

A = int(input("Insira o valor do Lado A:" ))
B = int(input("Insira o valor do Lado B:" ))
C= int(input("Insira o valor do Lado C:" ))

if (A < B + C) and (B < A + C) and (C < A + B):
    if (A == B) and (A == C) and (B != C):
        print("Triangulo Isósceles ")
    if (A != B) and (A != C) and (B !=C):
        print("Triangulo Escaleno ")
    if (A == B) and (A == C) and (B == C):
        print("Triangulo Equilátero")
else:
    print("Não é um triangulo")

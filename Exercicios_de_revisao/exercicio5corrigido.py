A = float(input("Insira o valor do Lado A:" ))
B = float(input("Insira o valor do Lado B:" ))
C= float(input("Insira o valor do Lado C:" ))

if (A > B + C) or (B > A + C) or (C > A + B):
    print("ñ é um triangulo")
elif (A == B) or (A == C) or (B == C):
    print("Triangulo equilatero")
elif (A == B) or (A == C) or (B != C):
    print("É um triangulo isoceles")
elif (A != B) or (A != C) or (B != C):
    print("É um Triangulo escaleno")

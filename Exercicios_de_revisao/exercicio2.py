media1 = float(input("Nota do 1 semestre "))
media2 = float(input("Nota do 2 semestre "))

mediaFinal = (media1 + media2)/2

if mediaFinal>=6 and mediaFinal<=10:
    print("Aprovado")
elif mediaFinal >=4 and mediaFinal <6:
    print("Exame")
elif mediaFinal >= 0 and mediaFinal<4:
    print("Reprovado")
else: print("Valor invalido")

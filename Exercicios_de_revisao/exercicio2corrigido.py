#dados
#Cps 1 semestre
cp1 = float(input("Entre com a nota do primeiro CP: "))
cp2 = float(input("Entre com a nota do segundo CP: "))
cp3 = float(input("Entre com a nota do terceiro CP: "))

#Cps 2 Semestre
cp4 = float(input("Entre com a nota do primeiro CP: "))
cp5 = float(input("Entre com a nota do segundo CP: "))
cp6 = float(input("Entre com a nota do terceiro CP: "))

gs1=  float(input("Entre com a nota do GS primeiro semestre: "))
gs2=  float(input("Entre com a nota do GS segundo semestre: "))

challenge=float(input("Entre com a nota do Challenge: "))
#Processos
media_1s=((cp1+cp2+cp3)/3)*0.2  + challenge*0.2 + gs1*0.6 

media_2s=((cp4+cp5+cp6)/3)*0.2  + challenge*0.2 + gs2*0.6 

media_final = media_1s*0.4 + media_2s*0.6

#Saida
if media_final>=6 :
    print("Aprovado")
elif media_final in range(4,6):
    print("Exame")
elif media_final<4:
    print("Reprovado")
else: print("Valor invalido")
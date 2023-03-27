#prod pode aumentar ou diminuir o valor
#if qtdVenda ==500 and preçoAtual <=30.00 +10%
#elif (qtdVenda ==501 and <=1200) or (preçoAtual >=30.01 and <=80.00 +15%
#elif qtdVenda > 1200 and preçoAtual>80.00 -20%
#elif qtdVenda<0 or preçoAtual<0.0
#print ("F")
#else print("Quantidade ou preço Atual invalido")
qtdVenda= float(input("Insira a quantidade de vendas do produto: "))
preçoAtual = float(input("Insira o preço atual do produto: "))

if (qtdVenda <=500) or (preçoAtual <=30.00):
    preco_final = preçoAtual + (preçoAtual *0.1)
    print(preco_final)
elif (qtdVenda >500 and qtdVenda <=1200) or (preçoAtual >=30.01 and preçoAtual <=80.00):
    preco_final = preçoAtual + (preçoAtual*0.15)
    print(preco_final)
elif (qtdVenda > 1200) or (preçoAtual > 80.00):
    preco_final= preçoAtual - (preçoAtual * 0.2)
    print (preco_final)
#else:
   #print("o preço nao sera alterado")
   #preco_final = preçoAtual

nome = ["Notebook", "tv"]
preço = [4000, 2000]
qtd = [2, 1]

#len() calcula tamanho de um container de dados
#len(xx) pega o tamanho de elementos (no caso daqui é o mesmo tamanho em tudo)
for index in range(0, len(nome)):
    if qtd[index] >1:
        print("eu tenho " + str(qtd[index]) + " " + nome[index] + "s de " + str(preço[index]) + " reais")
    else:
        print("eu tenho " + str(qtd[index]) + " " + nome[index] + " de " + str(preço[index]) + " reais")
    # criar 


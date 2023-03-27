#analista junior
#analista pleno
#analista senior
#arquiteto
#gerente
#inserir o reajuste
#printar o reajuste |+bonus

cargo = str(input("Insira seu cargo: "))
reajuste = int(input("Insira seu reajuste: "))
salarioAtual = float(input("Insira seu salario: "))
if cargo in ("analista junior", "Analista junior","Analista Junior", "Analista jr", "Analista Jr", "Analista JR", "analista jr" ):
    SalarioReajuste = (salarioAtual * (reajuste/100))
    SalarioReajuste = salarioAtual + SalarioReajuste *1.02
    print(SalarioReajuste)
elif cargo in ("analista pleno", "Analista pleno", "Analista Pleno"):
    SalarioReajuste = (salarioAtual * (reajuste/100))
    SalarioReajuste = salarioAtual + SalarioReajuste *1.025
    print(SalarioReajuste)
elif cargo in ("analista senior", "Analista senior" ,"Analista Senior"):
    SalarioReajuste = (salarioAtual * (reajuste/100))
    SalarioReajuste = salarioAtual + SalarioReajuste *1.03
    print(SalarioReajuste)
elif cargo in ("arquiteto","Arquiteto"):
    SalarioReajuste = (salarioAtual * (reajuste/100))
    SalarioReajuste= salarioAtual + SalarioReajuste *1.04
    print(SalarioReajuste)
elif cargo in ("gerente", "Gerente" ):
    SalarioReajuste = (salarioAtual * (reajuste/100))
    SalarioReajuste = salarioAtual + SalarioReajuste * 1.045
    print(SalarioReajuste)
else:
    print("Dados invalidos tentar novamente ")   
 
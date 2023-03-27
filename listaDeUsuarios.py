#Crie duas listas com os dados te 3 usuarios, sendo os dados o nome do usuario e a senha.
#crie uma condição para que quando o nome e a senha certa de um usuaria sejam inseridos apareça uma mensagem de sucesso.
#lower força todos os valores a serem minusculos

usuarios = ["Joao", "Jose", "Maria"]
senhas = ["a123", "456", "789"]

usuario = input("Digite o nome do usúario: ")
senha = input("digite a senha: ")

for index in range(0, len(usuario)):
    if (usuario == usuarios[index]) and (senha == senhas[index]):
            print("Sucesso!")
    else:
          print("negado")
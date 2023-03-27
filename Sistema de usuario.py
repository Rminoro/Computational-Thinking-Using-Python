user = ["alberico", "pedro", "eduardo"]
senha =["abc", "123456", "1234567"]

input_user = input("entre com o usuario: ").lower()
input_senha = input ("entre com a senha: ").lower()

for index in range(0,len(user)):
    if (input_user == user[index]) and (input_senha == senha[index]):
        print("Sucesso")
    else:
        print("dados incorretos")

while True:
    nome = input("Digite o seu nome maior que 3 caracteres: ")
    if len(nome) >= 3:
        break

    print("Digite um nome válido")


while True:
    idade = int(input("Digite o sua idade entre 0 a 150: "))
    if idade >= 0 and idade <= 150:
        break
    print("Digite uma idade válida")


while True:
    salario = int(input("Digite o seu salário maior que 0: ")) 
    if salario > 0:
        break
    print("Digite um salário válido: ")


while True:
    sexo = input("Digite o seu sexo 'f' ou 'm': ").lower()
    if sexo == "f" or sexo == "m":
        break
    print("Digite um sexo válido")


while True:
    estado_civil = input("Digite o seu estado civil 's', 'c', 'v', 'd': ").lower()
    if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
        break
    print("Digite um estado civil válido")


print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)



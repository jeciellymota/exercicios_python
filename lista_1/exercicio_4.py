def error(msgError):
    print(f"Digite um(a) {msgError} valido(a)")



while True:
    nome = input("Digite o seu nome maior que 3 caracteres: ")
    if len(nome) >= 3:
        break

    error("nome")


while True:
    idade = int(input("Digite o sua idade entre 0 a 150: "))
    if idade >= 0 and idade <= 150:
        break
    error("idade")


while True:
    salario = int(input("Digite o seu salário maior que 0: ")) 
    if salario > 0:
        break
    error("salario")


while True:
    sexo = input("Digite o seu sexo 'f' ou 'm': ").lower()
    if sexo == "f" or sexo == "m":
        break
    error("sexo")


while True:
    estado_civil = input("Digite o seu estado civil 's', 'c', 'v', 'd': ").lower()
    if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
        break
    error("estado civil")


print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)



import os
from func import *

os.system("cls")


print("*******CALCULADORA*******")

operacao = int(input("Escolha qual tipo de operação deseja realizar \n 1-soma, 2-subtração, 3-multiplicação, 4-divisão "))

while operacao < 1 or operacao > 4:

    os.system("cls")

    print("Tipo de operação inválida")
    operacao = int(input("Escolha qual tipo de operação deseja realizar \n 1-soma, 2-subtração, 3-multiplicação, 4-divisão "))

num1 = int(input("Digite o primeiro número "))
num2 = int(input("Digite o segundo número "))

if operacao == 1:
    print(f"O resultado da soma é {soma(num1,num2)}")

if operacao == 2:
    print(f"O resultado da sua subtração é {subtracao(num1,num2)}")

if operacao == 3:
     print(f"O resultado da sua multiplicação é {multiplicacao(num1,num2)}")

if operacao == 4:
     print(f"O resultado da sua divisão é {divisao(num1,num2)}")


 

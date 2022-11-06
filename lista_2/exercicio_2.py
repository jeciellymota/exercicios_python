list = [10, 2, 3, 4, 5, 6, 7, 8, 9]
# def lista(soma):
#     return (sum(soma))

# print(lista(list))

def lista(array):
    soma = 0
    for valor in array:
        soma += valor # soma = soma + valor
        print(valor)
    return soma    

print(lista(list))

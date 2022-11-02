# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input("Qual o tamanho do arquivo em MB que você deseja calcular? "))
velocidade = float(input("Qual a velocidade da ua internet em Mbps? "))
temposeg = arquivo / (velocidade / 8)
tempomin = temposeg / 60

print(f"Seu arquivo levará {tempomin} minutos para ser baixado")
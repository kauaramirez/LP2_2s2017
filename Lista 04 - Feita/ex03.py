dicionario = {}
nome = 'nome'
media = 0

while len(nome) > 0:
    nome = input("Digite seu nome: ")
    if len(nome) == 0:
        del[nome]
        break
    else:
        n1 = float(input("Digite sua primeira nota: "))
        n2 = float(input("Digite sua segunda nota: "))
        media = (n1+n2)/2
        dicionario[nome] = media	

print(dicionario)
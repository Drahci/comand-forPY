def testarForAninhado():
    for numerador in range(1,11):
        print("Tabuada do número:",numerador)
        for multiplicador in range(1,11):
            print( numerador,"x",multiplicador," = ",numerador*multiplicador )

def testarCodigos():
    varA = 3
    varB = 0
    for num in range(varA):
        varB += num**2
        print(varB)

def testarLista(lista):
    for fruta in lista:
        qtdletras =0
        for letras in fruta:
            qtdletras += 1
        print(fruta,qtdletras)

def testarMatriz():
    tabela = []
    contador = 0
    for i in range(3):
        linha = []
        for j in range(3):
            contador += 1
            linha.append(contador)
        tabela.append(linha)
    print(tabela)

def testarOrdem():
    dados=[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    for linha in dados:
        for coluna in linha:
            print(coluna)

#programas rodando
testarForAninhado()
testarCodigos()
lista=["abacaxi", "maça", "uva", "melão"]
testarLista(lista)
testarMatriz()
testarOrdem()
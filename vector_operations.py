import math

def normalizar(v):
    """ Normaliza o vetor v """
    norma = math.sqrt(sum(coord ** 2 for coord in v))
    return [coord / norma for coord in v]

def produto_escalar(v1, v2):
    """ Produto escalar de dois vetores """
    return sum(a * b for a, b in zip(v1, v2))

def produto_vetorial(v1, v2):
    """ Produto vetorial de dois vetores 3D """
    x = v1[1] * v2[2] - v1[2] * v2[1]
    y = v1[2] * v2[0] - v1[0] * v2[2]
    z = v1[0] * v2[1] - v1[1] * v2[0]
    return [x, y, z]

def subtrair_vetores(v1, v2):
    """ Subtração de dois vetores """
    return [a - b for a, b in zip(v1, v2)]

def multiplicar_por_escalar(v, escalar):
    """ Multiplica cada elemento de v por um escalar """
    return [coord * escalar for coord in v]

def multiplicar_matriz_vetor(matriz, vetor):
    """ Multiplica uma matriz 3x3 por um vetor 3D """
    return [produto_escalar(linha, vetor) for linha in matriz]

def multiplicar_matrizes(m1, m2):
    """ Multiplicação de duas matrizes 3x3 """
    resultado = []
    for linha in m1:
        nova_linha = []
        for j in range(len(m2[0])):
            coluna = [m2[i][j] for i in range(len(m2))]
            nova_linha.append(produto_escalar(linha, coluna))
        resultado.append(nova_linha)
    return resultado

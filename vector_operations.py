import math

def normalizar(v):
    """ Normaliza o vetor v """
    norma = math.sqrt(sum(coord ** 2 for coord in v))
    return [coord / norma for coord in v] if norma != 0 else [0] * len(v)

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

def ceil(x):
    """ Retorna o menor inteiro maior ou igual a x """
    return int(x) if x == int(x) else int(x) + 1 if x > 0 else int(x)

def floor(x):
    """ Retorna o maior inteiro menor ou igual a x """
    return int(x) if x == int(x) else int(x) - 1 if x < 0 else int(x)

def round_num(x):
    """ Arredonda o número x para o inteiro mais próximo """
    return int(x + 0.5) if x > 0 else int(x - 0.5)

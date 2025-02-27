import vector_operations as vop
import tkinter as tk

def ordenar_vertices(triangulo):
    """ Ordena os vértices do triângulo por y. """
    return sorted(triangulo, key=lambda v: v[1])

def rasterizar_linha(y1, x1, y2, x2):
    """ Rasteriza uma linha de (x1, y1) para (x2, y2) usando o algoritmo de DDA. """
    pixels = []
    dy = y2 - y1
    dx = x2 - x1
    
    if abs(dx) > abs(dy):
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        m = dy / dx if dx != 0 else 0
        y = y1
        for x in range(vop.ceil(x1), vop.floor(x2) + 1):
            pixels.append((x, vop.round_num(y)))
            y += m
    else:
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        m = dx / dy if dy != 0 else 0
        x = x1
        for y in range(vop.ceil(y1), vop.floor(y2) + 1):
            pixels.append((vop.round_num(x), y))
            x += m
    return pixels

def scanline_triangle(vertices):
    """ Rasteriza um triângulo utilizando o algoritmo Scanline com coerência geométrica. """
    v1, v2, v3 = ordenar_vertices(vertices)
    pixels = set()

    # Rasteriza as duas bordas do triângulo
    borda1 = rasterizar_linha(v1[1], v1[0], v2[1], v2[0])
    borda2 = rasterizar_linha(v1[1], v1[0], v3[1], v3[0])
    borda3 = rasterizar_linha(v2[1], v2[0], v3[1], v3[0])
    
    # Junta as bordas
    bordas = borda1 + borda2 + borda3

    # Organiza as linhas para preenchimento
    linhas = {}
    for x, y in bordas:
        if y not in linhas:
            linhas[y] = [x, x]
        else:
            linhas[y][0] = min(linhas[y][0], x)
            linhas[y][1] = max(linhas[y][1], x)

    # Preenche as linhas entre os extremos esquerdo e direito
    for y in linhas:
        for x in range(linhas[y][0], linhas[y][1] + 1):  # Garante que a linha inteira seja preenchida
            pixels.add((x, y))
    return pixels

def calcular_iluminacao(phong_params, ponto, normal):
    """Calcula a cor resultante no ponto dado a iluminação de Phong."""
    N, V, C, Lamb, Ka, Ll, Pl, Kd, Od, Ks, η = phong_params

    N = vop.normalizar(normal)
    V = vop.normalizar(vop.subtrair_vetores(C, ponto))
    L = vop.normalizar(vop.subtrair_vetores(Pl, ponto))
    R = vop.subtrair_vetores(vop.multiplicar_por_escalar(N, 2 * vop.produto_escalar(N, L)), L)

    if max(Lamb) > 1 or max(Ll) > 1:
        Lamb = [min(1, max(0, c / 255)) for c in Lamb]
        Ll = [min(1, max(0, c / 255)) for c in Ll]

    Iamb = [Ka * Lamb[i] for i in range(3)]

    dot_NL = max(vop.produto_escalar(N, L), 0)
    Idif = [Kd[i] * Od[i] * Ll[i] * dot_NL for i in range(3)]

    dot_RV = max(vop.produto_escalar(R, V), 0) ** η
    Iesp = [Ks * Ll[i] * dot_RV for i in range(3)]

    cor = [min(255, int((Iamb[i] + Idif[i] + Iesp[i]) * 255)) for i in range(3)]
    return f'#{cor[0]:02x}{cor[1]:02x}{cor[2]:02x}'

def colorir_triangulo(triangulo, normal, phong_params):
    """Aplica iluminação de Phong no triângulo e retorna os pixels coloridos."""
    pixels = scanline_triangle(triangulo)
    colorized_pixels = set()

    for x, y in pixels:
        ponto = (x, y, 0)
        cor = calcular_iluminacao(phong_params, ponto, normal)
        colorized_pixels.add(((x, y), cor))

    return colorized_pixels

def scanline_mesh(triangulos, normal, phong_params):
    """Rasteriza todos os triângulos de uma malha com iluminação de Phong e texturização."""
    pixels = set()
    for triangulo in triangulos:
        pixels.update(colorir_triangulo(triangulo, normal, phong_params))
    return pixels

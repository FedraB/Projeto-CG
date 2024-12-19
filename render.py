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

def rasterizar_flat_bottom(v1, v2, v3, pixels):
    """ Preenche o triângulo com base plana inferior. """
    inv_slope1 = (v2[0] - v1[0]) / (v2[1] - v1[1])
    inv_slope2 = (v3[0] - v1[0]) / (v3[1] - v1[1])
    x1 = x2 = v1[0]
    
    for y in range(v1[1], v2[1] + 1):
        for x in range(vop.round_num(x1), vop.round_num(x2) + 1):
            pixels.add((x, y))
        x1 += inv_slope1
        x2 += inv_slope2

def rasterizar_flat_top(v1, v2, v3, pixels):
    """ Preenche o triângulo com base plana superior. """
    inv_slope1 = (v3[0] - v1[0]) / (v3[1] - v1[1])
    inv_slope2 = (v3[0] - v2[0]) / (v3[1] - v2[1])
    x1 = x2 = v3[0]
    
    for y in range(v3[1], v1[1] - 1, -1):
        for x in range(vop.round_num(x1), vop.round_num(x2) + 1):
            pixels.add((x, y))
        x1 -= inv_slope1
        x2 -= inv_slope2
    
def scanline_mesh(triangulos):
    """ Rasteriza todos os triângulos de uma malha. """
    pixels = set()
    for triangulo in triangulos:
        pixels.update(scanline_triangle(triangulo))
    return pixels

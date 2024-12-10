import numpy as np

def transformar_mundial_para_vista(vertices, N, V, C):
    N = np.array(N) / np.linalg.norm(N)
    V = np.array(V)
    U = np.cross(V, N)
    U = U / np.linalg.norm(U)
    V = np.cross(N, U)
    # Matriz de transformação
    Mv = np.array([U, V, N])
    T = np.array(C)
    vertices_vista = [Mv.dot(vertex - T) for vertex in vertices]
    return vertices_vista

def projecao_perspectiva(vertices_vista, d, hx, hy):
    vertices_projetados = []
    for x, y, z in vertices_vista:
        xp = (-d * x) / (z * hx)
        yp = (-d * y) / (z * hy)
        vertices_projetados.append((xp, yp))
    return vertices_projetados


def normalizar_para_tela(vertices_projetados, largura_tela, altura_tela):
    vertices_tela = []
    for x, y in vertices_projetados:
        x_tela = int((x + 1) * largura_tela / 2)
        y_tela = int((1 - y) * altura_tela / 2)
        vertices_tela.append((x_tela, y_tela))
    return vertices_tela

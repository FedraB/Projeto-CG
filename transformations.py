import vector_operations as vop

def transformar_mundial_para_vista(vertices, N, V, C):
    """ Transforma os vértices das coordenadas mundiais para a vista """
    # 1. Normalizar os vetores N, U e V
    N = vop.normalizar(N)
    V = vop.normalizar(V)
    U = vop.normalizar(vop.produto_vetorial(V, N))
    V = vop.produto_vetorial(N, U)  # Corrige V para ser ortogonal
    
    # 2. Criar a matriz de rotação (base da câmera)
    Mv = [
        U,  # primeira linha (vetor U)
        V,  # segunda linha (vetor V)
        N   # terceira linha (vetor N)
    ]
    
    # 3. Transformar os vértices
    vertices_vista = []
    for vertice in vertices:
        # Transladar o ponto com relação ao centro C
        v_transladado = vop.subtrair_vetores(vertice, C)
        # Multiplicar a matriz de rotação por esse vetor
        v_vista = vop.multiplicar_matriz_vetor(Mv, v_transladado)
        vertices_vista.append(v_vista)
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

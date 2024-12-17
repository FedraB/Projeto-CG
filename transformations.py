import vector_operations as vop

def transformar_mundial_para_vista(vertices, N, V, C):
    """ Transforma os vértices das coordenadas mundiais para a vista """
    # Normaliza N (normal) e corrige V para ser ortogonal a N
    N = vop.normalizar(N)
    V = vop.subtrair_vetores(V, vop.multiplicar_por_escalar(N, vop.produto_escalar(V, N)))
    V = vop.normalizar(V)
    U = vop.normalizar(vop.produto_vetorial(V, N))  # Vetor ortogonal a V e N
    
    # Cria a matriz de rotação (base da câmera)
    Mv = [U, V, N]  # U, V e N como linhas da matriz
    
    # Transforma os vértices
    vertices_vista = []
    for vertice in vertices:
        v_transladado = vop.subtrair_vetores(vertice, C)  # Translada para o centro C
        v_vista = vop.multiplicar_matriz_vetor(Mv, v_transladado)  # Aplica rotação
        vertices_vista.append(v_vista)
    return vertices_vista

def projecao_perspectiva(vertices_vista, d, hx, hy):
    vertices_projetados = []
    for x, y, z in vertices_vista:
        if z == 0:  # Evita divisão por zero
            continue
        xp = (-d * x) / (z * hx)
        yp = (-d * y) / (z * hy)
        vertices_projetados.append((xp, yp))
    return vertices_projetados

def normalizar_para_tela(vertices_projetados, largura_tela, altura_tela):
    vertices_tela = []
    for x, y in vertices_projetados:
        x_tela = int((x + 1) * largura_tela / 2)
        y_tela = int((1 - y) * altura_tela / 2)
        
        # Clamping para garantir que os valores estão na tela
        x_tela = max(0, min(largura_tela - 1, x_tela))
        y_tela = max(0, min(altura_tela - 1, y_tela))
        
        vertices_tela.append((x_tela, y_tela))
    return vertices_tela

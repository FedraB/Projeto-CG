import vector_operations as vop

def transformar_mundial_para_vista(vertices, N, V, C):
    """ Transforma os vértices das coordenadas mundiais para a vista """
    
    # Verifica se N e V não são vetores nulos para evitar erro na normalização
    if vop.produto_escalar(N, N) == 0:
        raise ValueError("O vetor normal N não pode ser o vetor nulo.")
    if vop.produto_escalar(V, V) == 0:
        raise ValueError("O vetor V não pode ser o vetor nulo.")
    
    # Normaliza N (normal) e corrige V para ser ortogonal a N
    N = vop.normalizar(N)
    V = vop.subtrair_vetores(V, vop.multiplicar_por_escalar(N, vop.produto_escalar(V, N)))
    
    if vop.produto_escalar(V, V) == 0:  # Após ortogonalização, V pode se tornar nulo
        raise ValueError("O vetor V é ortogonal a N e não pode ser nulo.")
    
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

def projecao_perspectiva(vertices_vista, d, hx, hy, epsilon=1e-8):
    """ Projeta os vértices da vista para o plano da tela usando projeção em perspectiva """
    vertices_projetados = []
    for x, y, z in vertices_vista:
        if abs(z) < epsilon:  # Evita divisão por zero
            continue
        xp = (-d * x) / (z * hx)  # Projeção em perspectiva no eixo X
        yp = (-d * y) / (z * hy)  # Projeção em perspectiva no eixo Y
        vertices_projetados.append((xp, yp))
    return vertices_projetados

def normalizar_para_tela(vertices_projetados, largura_tela, altura_tela):
    """ Normaliza os vértices projetados no plano da tela (2D) """
    vertices_tela = []
    for x, y in vertices_projetados:
        x_tela = round((x + 1) * largura_tela / 2)  # De [-1, 1] para [0, largura_tela]
        y_tela = round((1 - y) * altura_tela / 2)  # De [-1, 1] para [0, altura_tela]
        
        # Clamping para garantir que os valores estão dentro da tela
        x_tela = max(0, min(largura_tela - 1, x_tela))
        y_tela = max(0, min(altura_tela - 1, y_tela))
        
        vertices_tela.append((x_tela, y_tela))
    return vertices_tela

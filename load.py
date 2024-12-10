def carregar_malha(arquivo_malha):
    with open(arquivo_malha, 'r') as f:
        linhas = f.readlines()
    # Número de vértices e triângulos
    n_vertices, n_triangulos = map(int, linhas[0].split())
    # Coordenadas dos vértices
    vertices = [list(map(float, linha.split())) for linha in linhas[1:n_vertices + 1]]
    # print(vertices)
    
    # Índices dos triângulos
    triangulos = [list(map(int, linha.split())) for linha in linhas[n_vertices + 1:]]
    # print(vertices)
    
    return vertices, triangulos

def carregar_parametros_camera(arquivo_camera):
    with open(arquivo_camera, 'r') as f:
        linhas = f.readlines()
    # Parâmetros
    N = list(map(float, linhas[0].split('=').pop().strip().split()))
    V = list(map(float, linhas[1].split('=').pop().strip().split()))
    d = float(linhas[2].split('=').pop().strip())
    hx = float(linhas[3].split('=').pop().strip())
    hy = float(linhas[4].split('=').pop().strip())
    C = list(map(float, linhas[5].split('=').pop().strip().split()))
    
    # print("N:" + str(N) +
    #       "\nV: " + str(V) + 
    #       "\nd: " + str(d) + 
    #       "\nhx: " + str(hx) + 
    #       "\nhy: " + str(hy) + 
    #       "\nC: " + str(C))
    
    return N, V, d, hx, hy, C
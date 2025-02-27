def carregar_malha(arquivo_malha):
    with open(arquivo_malha, 'r') as f:
        linhas = f.readlines()

    # Número de vértices e triângulos
    n_vertices, n_triangulos = map(int, linhas[0].split())
    
    # Valida o formato do arquivo
    if len(linhas) != (1 + n_vertices + n_triangulos):
        raise ValueError("O formato do arquivo da malha está incorreto.")
    
    # Coordenadas dos vértices
    vertices = [list(map(float, linha.split())) for linha in linhas[1:n_vertices + 1]]
    
    # Índices dos triângulos
    triangulos = [list(map(lambda x: int(x) - 1, linha.split())) 
                  for linha in linhas[n_vertices + 1:]]
    
    return vertices, triangulos

def carregar_parametros_camera_lighting(arquivo_camera):
    with open(arquivo_camera, 'r') as f:
        linhas = f.readlines()
    
    # Valida o formato do arquivo
    if len(linhas) != 14:
        raise ValueError("O formato do arquivo de parâmetros da câmera está incorreto.")
    
    try:
        # Parâmetros
        N = list(map(float, linhas[0].split('=').pop().strip().split()))
        V = list(map(float, linhas[1].split('=').pop().strip().split()))
        d = float(linhas[2].split('=').pop().strip())
        hx = float(linhas[3].split('=').pop().strip())
        hy = float(linhas[4].split('=').pop().strip())
        C = list(map(float, linhas[5].split('=').pop().strip().split()))    
        Lamb = list(map(float, linhas[6].split('=').pop().strip().split()))   
        Ka = float(linhas[7].split('=').pop().strip())
        Ll = list(map(float, linhas[8].split('=').pop().strip().split()))   
        Pl = list(map(float, linhas[9].split('=').pop().strip().split()))   
        Kd = list(map(float, linhas[10].split('=').pop().strip().split()))   
        Od = list(map(float, linhas[11].split('=').pop().strip().split()))   
        Ks = float(linhas[12].split('=').pop().strip())
        η = float(linhas[13].split('=').pop().strip())
    except (IndexError, ValueError):
        raise ValueError("Erro ao ler os parâmetros da câmera. Verifique o formato do arquivo.")
    
    return N, V, d, hx, hy, C, Lamb, Ka, Ll, Pl, Kd, Od, Ks, η

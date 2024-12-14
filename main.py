import load
import transformations
import render

def main():
    vertices, triangulos = load.carregar_malha("objetos/triangulo.byu")
    N, V, d, hx, hy, C = load.carregar_parametros_camera("camera.byu")
    vertices_vista = transformations.transformar_mundial_para_vista(vertices, N, V, C)
    vertices_projetados = transformations.projecao_perspectiva(vertices_vista, d, hx, hy)
    vertices_norm_tela = transformations.normalizar_para_tela(vertices_projetados, 2040, 1920)
    print(vertices_norm_tela) # [(839, 960), (1020, 845), (1020, 833)]

if __name__ == "__main__":
    main()
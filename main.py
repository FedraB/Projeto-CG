import load
import transformations
import render

def main():
    vertices, triangulos = load.carregar_malha("objetos/maca.byu")
    N, V, d, hx, hy, C = load.carregar_parametros_camera("objetos/camera.byu")
    vertices_vista = transformations.transformar_mundial_para_vista(vertices, N, V, C)
    vertices_projetados = transformations.projecao_perspectiva(vertices_vista, d, hx, hy)
    screen_w = 500
    screen_h = 500
    vertices_norm_tela = transformations.normalizar_para_tela(vertices_projetados, screen_w, screen_h)
    # print("Triângulos: " + str(triangulos) + "\nVértices: " + str(vertices_norm_tela))

    pixels = render.scanline_mesh(vertices_norm_tela)
    print("Pixels preenchidos:", pixels)
    render.desenhar_pixels(pixels, screen_w, screen_h)

if __name__ == "__main__":
    main()
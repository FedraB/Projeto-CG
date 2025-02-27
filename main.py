import load
import transformations
import render
import tkinter as tk

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
OBJECT_FILE = "objetos/objeto.byu"
CAMERA_LIGHTING_FILE = "objetos/camera_lighting.byu"

def atualizar_imagem(canvas, screen_w, screen_h):
    # Carrega os parâmetros novamente
    vertices, triangulos = load.carregar_malha(OBJECT_FILE)
    N, V, d, hx, hy, C, Lamb, Ka, Ll, Pl, Kd, Od, Ks, η = load.carregar_parametros_camera_lighting(CAMERA_LIGHTING_FILE)

    # Realiza a transformação
    vertices_vista = transformations.transformar_mundial_para_vista(vertices, N, V, C)
    vertices_projetados = transformations.projecao_perspectiva(vertices_vista, d, hx, hy)
    vertices_norm_tela = transformations.normalizar_para_tela(vertices_projetados, screen_w, screen_h)
    
    # Prepara os triângulos para desenhar na tela
    triangulos_tela = [[vertices_norm_tela[i] for i in triangulo] for triangulo in triangulos]
    
    # Chama a função que colore os triângulos e retorna os pixels
    phong_params = (N, V, C, Lamb, Ka, Ll, Pl, Kd, Od, Ks, η)
    pixels = render.scanline_mesh(triangulos_tela, N, phong_params)
    
    # Limpa o canvas antes de desenhar
    canvas.delete("all")
    
    # Desenha os pixels coloridos na tela
    for (x, y), cor in pixels:
        if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
            y_invertido = SCREEN_HEIGHT - y - 1
            canvas.create_rectangle(x, y_invertido, x + 1, y_invertido + 1, outline=cor, fill=cor)

def main():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Desenho de Pixels")
    
    # Cria um canvas para desenhar os pixels
    canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="black")
    canvas.pack()
    
    # Inicializa a renderização
    atualizar_imagem(canvas, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Função que recarrega os parâmetros e redesenha o objeto
    def recarregar(event):
        atualizar_imagem(canvas, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Vincula a tecla 'r' para recarregar e redesenhar
    root.bind("<r>", recarregar)
    
    # Vincula a tecla ESC para fechar a janela
    def fechar_janela(event=None):
        root.destroy()
    
    root.bind("<Escape>", fechar_janela)
    
    # Inicia o loop de eventos do Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
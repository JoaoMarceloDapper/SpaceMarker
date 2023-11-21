import pygame
import json
from tkinter import Tk, simpledialog
from tkinter import messagebox
import os

#Joao Marcelo Dapper
#1135024

pygame.init()
WIDTH = 1000
HEIGHT = 563
WHITE = (255, 255, 255)
WHITE_LINHA = (30, 144, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Marker")

background_image = pygame.image.load("bg.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
icone_game = pygame.image.load("space.png")
pygame.display.set_icon(icone_game)
pygame.display.set_caption("Space Marker")
font = pygame.font.Font(None,20)

linha1 = font.render("Pressione F10 para salvar os pontos do jogo", True, WHITE)
linha2 = font.render("Pressione F11 para carregar os pontos do jogo", True, WHITE)
linha3 = font.render("Pressione F12 para apagar os pontos do jogo", True, WHITE)

linha1_pos = (0, 1)
linha2_pos = (0, linha1.get_height())
linha3_pos = (0, linha1.get_height() + linha2.get_height())

points = []

ajuda = {}

def render_points():
    window.blit(background_image, (0, 0))

    for i in range(len(points)):
        point, name = points[i]
        pygame.draw.circle(window, WHITE, point, 5)
        text = font.render(f"{name} - {point}", True, WHITE_LINHA)
        window.blit(text, (point[0] + 10, point[1] + 10))
        if i > 0:
            pygame.draw.line(window, WHITE_LINHA, points[i - 1][0], point, 2)
    window.blit(linha1, (10, 10))
    window.blit(linha2, (20, 25))
    window.blit(linha3, (30, 40))
    pygame.display.flip()

def open_dialog():
    root = Tk()
    root.withdraw()
    name = simpledialog.askstring("Nome do Ponto:", "Digite o nome do ponto:")
    root.destroy()
    if name:
        return name
    else:
        return "Desconhecido"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F10:
                with open("pontos.json", "w") as f:
                    json.dump(points, f)
                print("Seus pontos foram salvos com sucesso!")
            try:
                if event.key == pygame.K_F11:
                    with open("pontos.json", "r") as f:
                        points = json.load(f)
                    print("Seus pontos foram carregados com sucesso!")
            except:messagebox.showinfo("Não Existe Pontos Salvos")
            if event.key == pygame.K_F12:
                points = []
                print("Seus pontos foram excluídos com sucesso!")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                point = event.pos
                name = open_dialog()
                points.append((point, name))

    render_points()
pygame.quit()
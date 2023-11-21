import pygame
import json
from tkinter import Tk, simpledialog
from tkinter import messagebox
import os

pygame.init()
WIDTH = 1000
HEIGHT = 563
WHITE = (255, 255, 255)
BLU = (30, 144, 255)
BLU_LINHA = (30, 144, 255)
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
    
#Quit Pygame
pygame.quit()
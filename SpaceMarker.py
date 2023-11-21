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
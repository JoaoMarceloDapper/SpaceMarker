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
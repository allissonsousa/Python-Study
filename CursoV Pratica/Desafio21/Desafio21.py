""" Faça um programa em python que abra e reproduza o aúdio de um arquivo mp3"""
import pygame
""" Como eu fiz
from playsound import playsound
playsound('ohmygah.mp3')"""

# Correção
"""Existem varias bibliotecas e modulos de tocar audio, vamos usar um famoso usado para jogos"""

pygame.init()
pygame.mixer.music.load('ohmygah.mp3')
pygame.mixer.music.play()
pygame.event.wait()  # Aguarda o programa finalizar o audio antes de encerrar
"""NÃO FUNCIONOU POR ALGUM MOTIVO, ACHO Q ESSA BIBLIOTECA SO FUNCIONA NO PYTHON 2"""

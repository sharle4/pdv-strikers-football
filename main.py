import pygame as pyg

pyg.init() #initialitsation de pygame

#Ouverture de la fenêtre Pygame
fenetre = pyg.display.set_mode((1920, 1080)) #creation des dimensions
icone = pyg.image.load("pics/logo/logo.png").convert_alpha() #chargement de l'icone de la fenetre
pyg.display.set_icon(icone) #assimilation de l'icone de la fenetre
pyg.display.set_caption("Pont-de-Veyle Strikers Battle League Football") #titre de la fenetre

running = True
while running :
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
    
pyg.quit()

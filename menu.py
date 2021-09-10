from PPlay import sprite
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import main

file = open("rank.txt",'a')
file.close()
janela1 = Window(800, 600)
mouse = Window.get_mouse()
jogar = Sprite("jogar.png")
jogar.x = 295
jogar.y = 300
dif = Sprite("dificuldade.png")
dif.x = 435
dif.y = 310
rank = Sprite("rank.png")
rank.x = 295
rank.y = 360
sair = Sprite("sair.png")
sair.x = 435
sair.y = 360

#
#

while(True):
    if mouse.is_over_area([295,300],[365, 352]) and mouse.is_button_pressed(1):
        main.jogo()
    if mouse.is_over_area([435,310],[600, 352]) and mouse.is_button_pressed(1):
        main.dificuldade()
    if mouse.is_over_area([295,360],[365, 412]) and mouse.is_button_pressed(1):
        main.ranking()
    if mouse.is_over_area([435,360],[515, 412]) and mouse.is_button_pressed(1):
        janela1.close()
    

    janela1.set_background_color([255,0,0])
    
    jogar.draw()
    dif.draw()
    sair.draw()
    rank.draw()
    janela1.update()
    

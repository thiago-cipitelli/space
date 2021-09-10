from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import random


janela = Window(800,600)
teclado = Window.get_keyboard()


def configs():
    voltar = Sprite("play.png")
    voltar.x = 365
    voltar.y = 265
    janela.set_background_color([255,255,0])
    while True:
        if teclado.key_pressed("esc"):
            break
        janela.update()
        voltar.draw()
        

def ranking():
    file = open("rank.txt",'r') 
    rank = file.readlines()
    lista = []
    if len(rank)>5:
        for i in range(5):
            lista.append(rank[i])
    voltar = Sprite("sair.png")
    voltar.x = 365
    voltar.y = 265
    janela.set_background_color([0,0,0])
    while True:
        if teclado.key_pressed("esc"):
            break
        hight = 100
        if len(rank)>5:
            for i in lista:
                janela.draw_text(i[:-1], 275, hight, 40, (255,255,255), "Arial", True)
                hight += 50
        else:
            for i in rank:
                janela.draw_text(i[:-1], 275, hight, 40, (255,255,255), "Arial", True)
                hight += 50
        janela.update()
        #voltar.draw()
        janela.draw_text("RANKING", 250, 0, 60, (255,255,255), "Arial", True)

def dificuldade():
    voltar = Sprite("sair.png")
    voltar.x = 365
    voltar.y = 265
    janela.set_background_color([80,50,145])
    while True:
        if teclado.key_pressed("esc"):
            break
        janela.update()
        voltar.draw()

####### Monstro #######

def criamatrizmonstros(m, posx, posy, tam):
    
    for y in range(tam):
        array = []
        for x in range (tam+2):
            array.append(Sprite("alien.png"))
            array[x].x = (posx*(x+1))
            array[x].y = (posy*(y+1))
        for x in range (1,tam+2):
            array[x].x += 25*x
        m.append(array)

def movematriz(m, dire):
    for x in m:   
        for e in x:
            e.x += e.width*dire

def deslocaY(m):
    for x in m:   
        for e in x:
            e.y += e.width



##### Fim Monstro #####

def jogo():
    janela.set_background_color([0,0,0])
    player = Sprite("nave.png")
    player.x = 360
    player.y = 500
    muni = 10
    reload = 0
    size = 1
    vida = 3
    cont = 0 
    tiros = []
    m = []
    dire = 1
    colidiu = False
    posx = 50
    posy = 50
    vel = -200
    ammo = True
    enemyammo = True
    enemyTiros = []
    tempo = 0
    pontos = 0 
    timepoint = 0
    fps = 0
    loops = 0
    relogio = 0
    while vida > 0:
        if len(m) == 0:
            criamatrizmonstros(m, posx, posy, size)
        if teclado.key_pressed("right") and player.x <= janela.width-player.width:
            player.move_x(-1 * vel * janela.delta_time())
        if teclado.key_pressed("left") and player.x >= 0:
            player.move_x(vel * janela.delta_time())
        if teclado.key_pressed("space") and ammo == True and muni > 0:
            muni-=1
            tiros.append(Sprite("tiro.png"))
            tiros[-1].x = player.x + player.width/2 - tiros[-1].width/2
            tiros[-1].y = player.y
            ammo = False
        else:
            tempo += janela.delta_time()
        for t in tiros:
                t.draw()
                t.move_y(vel * janela.delta_time())
                if t.y <= 0:
                    tiros.remove(t)
        for x in m:
            for e in x:
                if e != 0:
                    e.draw()
                for t in tiros:
                    
                    if t.x < x[-1].x + e.width and t.x > x[0].x:
                        if t.collided(e):
                            print("colidiu") 
                            tiros.remove(t)
                            x.remove(e)
                            if len(m) == 0:
                                criamatrizmonstros(m, posx, posy, size)
                            pontos += int(1/timepoint * 500)
        if enemyammo:
            for i in range(len(m)-1, -1, -1):
                
                if len(m[i])>0:
                    pos = random.randint(0, len(m[i])-1)
                    enemyTiros.append(Sprite("tiro.png"))
                    enemyTiros[-1].x = m[i][pos].x + m[i][pos].width/2
                    enemyTiros[-1].y = m[i][pos].y + m[i][pos].height
                    enemyammo = False
                    break
                
        for t in enemyTiros:
            t.draw()
            t.move_y(-1* vel * janela.delta_time())
            if t.y > janela.height:
                enemyTiros.remove(t)
                enemyammo = True
            if t.y >= player.y:
                if t.collided(player):
                    enemyammo = True
                    enemyTiros.remove(t)
                    vida -= 1
                    player.x = janela.width/2
                    
        if tempo >= 1:
            timepoint += 1
            print(len(m))
            if colidiu:
                deslocaY(m)
                colidiu = False
            else:
                movematriz(m, dire)
                if len(m) == 0:
                    criamatrizmonstros(m, posx, posy, size)
                if m[0][-1].x + (m[0][-1].width * 2) >= janela.width or m[0][0].x - m[0][0].width <= 0:
                    dire *= -1
                    colidiu = True
            if muni > 0:
                ammo = True
            else:
                player.image = pygame.image.load("dogenave.png")
                reload += 1
            tempo = 0 
        if reload == 6:
            player.image = pygame.image.load("nave.png")
            reload = 0
            muni = 10
        janela.update()
        janela.set_background_color([0,0,0])
        janela.draw_text("vidas:"+str(vida), janela.width - 100 , 0, 20, (255,255,255), "Arial", True)
        janela.draw_text(str(pontos), janela.width/2, 0, 20, (255,255,255), "Arial", True)
        janela.draw_text(str(fps), 0, 0, 20, (255,255,255), "Arial", True)
        player.draw()
        if relogio >= 1:
            fps = int(loops/relogio)
            loops = 0
            relogio = 0
        else:
            relogio += janela.delta_time()
            loops += 1
    nome = input("entre com o nome: ")
    file = open("rank.txt",'r')
    rank = file.readlines()
    rank.append(str(nome)+'#'+str(pontos)+'\n')
    file = open("rank.txt",'w')
    for l in rank:
        file.write(l)
    file = open("rank.txt",'r')
    rank = file.readlines()
    aux = []
    for l in rank:
        aux.append(l.split('#')[1])
    aux.sort()
    aux.reverse()
    file.close()
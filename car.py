import pygame
import time
pygame.init()
root=pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
bg=pygame.image.load("bg.png")
gr=pygame.image.load("ground.png")
fin=pygame.image.load("finish.png")
player=pygame.image.load("player.png")
player2=pygame.image.load("player2.png")
player3=pygame.image.load("player3.png")
player4=pygame.image.load("player4.png")
mon=pygame.image.load("money.png")
ship=pygame.image.load("ship.png")
lava=[pygame.image.load("fire1.png"),pygame.image.load("fire2.png"),pygame.image.load("fire3.png")]



maxscore=open("maxscore.txt","r")
max=maxscore.readline()
maxscore.close()
maxscore=open("maxscore.txt","w")













fireint=0
v=0
playercos=0
score=0
left=0
right=0
jump=0
inertj=3
level=list("LLL________________SMMMM_____S__MM_S_____L___MMM__L__________MMM_____++++__M__L__M___++++++___L_____MMMMMM___SS__________LSL_________F______________________________________________")
pos=10
y=525
game=0
music=pygame.mixer.Sound("fm-freemusic-give-me-a-smile.mp3")
sad=pygame.mixer.Sound("7759cfb9003b104.mp3")
win=pygame.mixer.Sound("19f925ab5a5e735.mp3")
class Nadpis:
    def __init__(self,nadpis,color,root,textc,max,game):
        self.nadpis=nadpis
        self.color=color
        self.root=root
        self.textc=textc
        self.max=max
        self.game=game
    def place(self):
        pygame.draw.rect(self.root, self.color, (100, 100, 1070, 520))
        finishtxt = xont.render(self.nadpis, True, self.textc)
        self.root.blit(finishtxt, (150, 300))
        if self.color==(255, 250, 250):
            try:
                if int(self.max)<score:
                    self.max=score
                    maxscore.write(str(score))
                    maxscore.close()
                txt=xont.render("Max score: "+str(self.max),True,self.textc)
                self.root.blit(txt,(150,400))

            except:
                txt = xont.render("Max score: " + str(score), True, self.textc)
                self.root.blit(txt, (150, 400))
                maxscore.write(str(score))
                maxscore.close()

        pygame.display.update()
        time.sleep(5)
        self.game=0
        music.stop()
        music.play()

xont=pygame.font.Font('Pixeboy-z8XGD.ttf',40)
music.play()
while True:
    root.blit(bg, (0, 0))
    if not game:
        pygame.draw.rect(root,(255,255,255),(500,50,300,200))
        play=xont.render("Play",True,(0,0,0))
        root.blit(play,(615,125))
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                quit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                if i.button==1:
                    if i.pos[0]>500 and i.pos[0]<800:
                        if i.pos[1]>50 and i.pos[1]<250:
                            game=1
                            music.stop()
                            music.play()

    if game:
        fireint += 1
        if fireint==3:
            fireint = 0
        text=xont.render(str(score),False,(0,0,0))
        root.blit(text,(0,0))
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_RIGHT or i.key==pygame.K_d:
                    right=1
                    left=0

                if i.key==pygame.K_LEFT or i.key==pygame.K_a:
                    right=0
                    left=1
                if i.key==pygame.K_SPACE or i.key==pygame.K_UP or i.key==pygame.K_w:
                    if y==525:
                        jump=1
                if i.key==pygame.K_z:
                    music.stop()             #???????????????????????????? ????????????

            if i.type==pygame.KEYUP:
                right=0
                left=0
        if right:
            if level[pos-2]=="+":
                if y>450:
                    pos-=1
                    v-=50
            if pos+9!="F":
                v+=50
                pos +=1
        if left:
            if level[pos-3]=="+":
                if y>450:
                    pos+=1
                    v+=50
            if pos>=9:
                v-=50
                pos -= 1
        if jump:
            y-=45
            inertj-=1
            if inertj==0:
                jump=0
                inertj=3
        for i in range(-3,20):
            root.blit(gr,(i*108-v,720-96))
        for i in range(-10,10):
            if level[pos+i]=="+":
                root.blit(gr,(pos+i*108+850,500))
            if level[pos+i]=="M":
                root.blit(mon,(pos+i*108+850,500))
            if level[pos+i]=="S":
                root.blit(ship,(pos+i*108+850,550))
            if level[pos+i]=="L":
                root.blit(lava[fireint],(pos+i*108+850,590))
            if level[pos+i]=="F":
                root.blit(fin,(pos+i*108+850,525))
                if pos-3==pos+i:
                    music.stop()
                    win.play()
                    ses = Nadpis("You collected "+str(score)+" coins. Cool!", (255, 250, 250), root,(0,0,0),max,game)
                    ses.place()
                    fireint = 0
                    v = 0
                    playercos = 0
                    score = 0
                    left = 0
                    right = 0
                    jump = 0
                    inertj = 3
                    level = list(
                        "LLL________________SMMMM_____S__MM_S_____L___MMM__L__________MMM_____++++__M__L__M___++++++___L_____MMMMMM___SS__________LSL_________F______________________________________________")
                    pos = 10
                    y = 525
                    game = 0

        if level[pos-2]=="M":
            level[pos-2]="_"
            score+=1
        if right:
            if level[pos-3]=="S":
                if y>=500:
                    music.stop()
                    sad.play()
                    ses = Nadpis("You lose!!!!", (255, 100, 100), root,(255,255,255),max,game)
                    ses.place()
                    fireint = 0
                    v = 0
                    playercos = 0
                    score = 0
                    left = 0
                    right = 0
                    jump = 0
                    inertj = 3
                    level = list(
                        "LLL________________SMMMM_____S__MM_S_____L___MMM__L__________MMM_____++++__M__L__M___++++++___L_____MMMMMM___SS__________LSL_________F______________________________________________")
                    pos = 10
                    y = 525
                    game = 0
        if left:
            if level[pos-2]=="S":
                if y>=500:
                    music.stop()
                    sad.play()
                    ses = Nadpis("You lose!!!!", (255, 100, 100), root,(255,255,255),max,game)
                    ses.place()
                    fireint = 0
                    v = 0
                    playercos = 0
                    score = 0
                    left = 0
                    right = 0
                    jump = 0
                    inertj = 3
                    level = list(
                        "LLL________________SMMMM_____S__MM_S_____L___MMM__L__________MMM_____++++__M__L__M___++++++___L_____MMMMMM___SS__________LSL_________F______________________________________________")
                    pos = 10
                    y = 525
                    game = 0
        if v>=100 or v<=-100:
            v=0
        if level[pos-2]!="+" or level[pos-3]!="+":
            if jump==0:
                if y<520:
                    if level[pos - 3] != "+":
                        y+=40
        if level[pos-3]=="L":
            if y>=500:
                music.stop()
                sad.play()
                ses=Nadpis("You burn!!!!!!!!!",(255,150,150),root,(255,255,255),max,game)
                ses.place()
                fireint = 0
                v = 0
                playercos = 0
                score = 0
                left = 0
                right = 0
                jump = 0
                inertj = 3
                level = list(
                    "LLL________________SMMMM_____S__MM_S_____L___MMM__L__________MMM_____++++__M__L__M___++++++___L_____MMMMMM___SS__________LSL_________F______________________________________________")
                pos = 10
                y = 525
                game = 0

        if right:
            if playercos%2==0:
                root.blit(player2,(600,y))
                playercos+=1
            else:
                root.blit(player,(600,y))
                playercos+=1
        if left:
            if playercos%2==0:
                root.blit(player3,(600,y))
                playercos+=1
            else:
                root.blit(player4,(600,y))
                playercos+=1
        if y>480:
            y=525
        if not left and not right:
            root.blit(player,(600,y))
    pygame.display.update()
    clock.tick(12)
from pygame import *
from random import *
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
window=display.set_mode((700,500))
beg_graund = transform.scale(image.load("galaxy.jpg"),(700,500))   
run=True
class GameSprite(sprite.Sprite):
    def __init__(self,playerimage,player_x,player_y,size_x,size_y,speed_player):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(playerimage),(size_x,size_y))
        self.speed=speed_player
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys [K_LEFT]:
            self.rect.x=self.rect.x-self.speed
        if keys [K_RIGHT]:
            self.rect.x=self.rect.x+self.speed
        if keys [K_UP]:
            self.rect.y=self.rect.y-self.speed
        if keys [K_DOWN]:
            self.rect.y=self.rect.y+self.speed
    def fire(self):
        bullet=Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20,-10)
        bullets.add(bullet)

ship=Player("rocket.png",10,400,80,100,10)
lost = 0 #пропущено кораблей
class Enemy(GameSprite):
    def update(self):
        self.rect.y=self.rect.y+self.speed
        global lost
        if self.rect.y > 700:
            self.rect.x = randint(80,win_width - 80)
            self.rect.y = 0 
            lost = lost +1
class Bullet(GameSprite):
    def update(self):
        self.rect.y=self.rect.y+self.speed
        if self.rect.y<0:
            self.kill()
monsters=sprite.Group()
for i in range(6):
    monster=Enemy("ufo.png",randint(80,600),-80,80,60,randint (1,5))
    monsters.add(monster)
bullets=sprite.Group()
score=0
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        elif e.type==KEYDOWN:
            if e.key==K_SPACE:
                fire_sound.play()
                ship.fire()
        window.blit(beg_graund,(0,0))
        ship.update()
        monsters.update()
        bullets.update()
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        collides=sprite.groupcollide(monsters,bullets,True,True)
        for i in collides:
            score=score+1
            monster=Enemy("ufo.png",randint(80,600),-80,80,60,randint (1,5))
            monsters.add(monster) 
        if sprite.spritecollide(ship,monsters,False)  or lost>5:
            run=False
        display.update()
    time.delay(50)


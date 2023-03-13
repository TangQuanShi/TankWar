
from pygame.sprite import Sprite
import pygame,time,random
SCREEN_WEIGH = 1380
SCREEN_HEIGHT = 725
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR = pygame.Color(255,0,0)
class MainGame():
    window = None
    my_tank = None
    home = None
    enemy_tank = []
    mytank_bulltlist = []
    enemy_bulletlist = []
    wall_list = []
    wall2_list =[]
    glass_list = []
    explodelist = []
    def __init__(self):
        pass
    def startGame(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode([SCREEN_WEIGH,SCREEN_HEIGHT])
        self.Creat_mytank()
        self.Create_Wall()
        #self.Create_wall2()
        self.Create_home()
        self.Random_Wall2()
        #self.Create_glass()
        self.Creat_Enemy()
        self.Random_glass()
        pygame.display.set_caption("坦克大战")
        while True:
            time.sleep(0.02)
            MainGame.window.fill(BG_COLOR)
            self.getEvent()
            self.Display_home()
            self.Display_Wall()
            self.Display_Wall2()
            self.Display_Enemy()
            self.Display_bullet()
            self.Enemybullet_hit_Mytank()
            self.Display_explode()
            if MainGame.my_tank.live:
                MainGame.my_tank.show()
            MainGame.window.blit(self.getText('还剩下%d辆坦克'%len(MainGame.enemy_tank)),(10,10))
            if not MainGame.my_tank.stop and MainGame.home.live:
                MainGame.my_tank.move()
                MainGame.my_tank.tank_hit_wall()
                MainGame.my_tank.mytank_hit_enemytank()
            self.Display_glass()
            pygame.display.update()
    def endGame(self):
        print("欢迎使用")
        exit()
    def Create_home(self):
        MainGame.home = home()
        for i in range(3):
            wall2 = Wall_2(SCREEN_WEIGH/2-100,SCREEN_HEIGHT-i*55)
            MainGame.wall2_list.append(wall2)
        wall3 = Wall_2(SCREEN_WEIGH/2-32,SCREEN_HEIGHT-55*2)
        MainGame.wall2_list.append(wall3)
        for i in range(3):
            wall4 = Wall_2(SCREEN_WEIGH/2+36,SCREEN_HEIGHT-i*55)
            MainGame.wall2_list.append(wall4)
    def Display_home(self):
        MainGame.home.Display_home()
    def Create_glass(self):
        for i in range(6):
            Glass = glass(i*120,600)
            MainGame.glass_list.append(Glass)
    def Display_glass(self):
        for glass in MainGame.glass_list:
            if glass.live:
                glass.displayglass()
    def Random_glass(self):
        num = random.randint(10, 12)
        i = 0
        a = None
        self.left = self.Random_glass_leftrect()
        self.top = self.Random_glass_toprect()
        while i != num:
            hit = False
            a = random.randint(0,10)
            self.temp_left = self.left
            self.temp_top = self.top
            if a <= 3 :
                self.left = self.Random_glass_leftrect()
            elif a >= 6:
                self.top = self.Random_glass_toprect()
            else:
                self.top = self.Random_glass_toprect()
                self.left = self.Random_glass_leftrect()
            Glass = glass(self.left, self.top)
            for wall_2 in MainGame.wall2_list:
                if pygame.sprite.collide_rect(Glass, wall_2):
                    hit = True
            for glass_ in MainGame.glass_list:
                if pygame.sprite.collide_rect(Glass, glass_):
                    hit = True
            for wall in MainGame.wall_list:
                if pygame.sprite.collide_rect(Glass, wall):
                    hit = True
            for enemy in MainGame.enemy_tank:
                if pygame.sprite.collide_rect(Glass, enemy):
                    hit = True
            if pygame.sprite.collide_rect(Glass, MainGame.my_tank):
                hit = True
            if self.temp_left ==self.left and self.temp_top == self.top:
                hit = True
            if hit == False:
                MainGame.glass_list.append(Glass)
                i += 1
    def Create_wall2(self):
        for i in range(6):
            wall = Wall_2(i*120,400)
            MainGame.wall2_list.append(wall)
    def Display_Wall2(self):
        for wall in MainGame.wall2_list:
            if wall.hp <= 0:
                explode4 = explode(wall)
                MainGame.explodelist.append(explode4)
                wall.live = False
                MainGame.wall2_list.remove(wall)
            if wall.live:
                wall.displaywall2()
    def Random_Wall2(self):
        num = random.randint(20,22)
        i = 0
        a = None
        self.left = self.Random_wall2_leftrect()
        self.top = self.Random_wall2_toprect()
        while i != num:
            hit = False
            a = random.randint(0,10)
            self.temp_left = self.left
            self.temp_top = self.top
            if a <= 4:
                self.left = self.Random_wall2_leftrect()
            elif a >= 7:
                self.top = self.Random_wall2_toprect()
            else:
                self.left = self.Random_wall2_leftrect()
                self.top = self.Random_wall2_toprect()
            wall2 = Wall_2(self.left,self.top)
            for wall_2 in MainGame.wall2_list:
                if pygame.sprite.collide_rect(wall2,wall_2):
                    hit = True
            for wall in MainGame.wall_list:
                if pygame.sprite.collide_rect(wall2,wall):
                    hit = True
            for enemy in MainGame.enemy_tank:
                if pygame.sprite.collide_rect(wall2,enemy):
                    hit = True
            if pygame.sprite.collide_rect(wall2,MainGame.my_tank):
                hit = True
            if self.temp_left == self.left and self.temp_top == self.top:
                hit =True
            if hit == False:
                MainGame.wall2_list.append(wall2)
                i += 1
    def Random_wall2_leftrect(self):
        left = 69*random.randint(0,18)
        return left
    def Random_wall2_toprect(self):
        top =55*random.randint(0,12)
        return top
    def Random_glass_leftrect(self):
        left = 85*random.randint(0,10)
        return left
    def Random_glass_toprect(self):
        top =88*random.randint(0,7)
        return top
    def Create_Wall(self):
        # T
        for i in range(5):
            if i == 1:
                wall2 = Wall(80,80)
                wall3 = Wall(200,80)
                MainGame.wall_list.append(wall2)
                MainGame.wall_list.append(wall3)
            wall = Wall(140,60*i+80)
            MainGame.wall_list.append(wall)
        #Q
        for i in range(5):
            if i == 1:
                wall5 = Wall(400,80)
                MainGame.wall_list.append(wall5)
            wall4 = Wall(340,i*60+80)
            MainGame.wall_list.append(wall4)
        wall6 = Wall(400, 320)
        MainGame.wall_list.append(wall6)
        for i in range(5):
            wall7 = Wall(460, i * 60 + 80)
            MainGame.wall_list.append(wall7)
        wall8 = Wall(520, 320)
        MainGame.wall_list.append(wall8)
        #S
        for i in range(3):
            wall9 = Wall(660,i*60+80)
            MainGame.wall_list.append(wall9)
            if i >= 1:
                wall10 = Wall(660+60*i,80)
                MainGame.wall_list.append(wall10)
        for i in range(2):
            wall11 = Wall(720+i*60,200)
            MainGame.wall_list.append(wall11)
        for i in range(3):
            wall12 = Wall(660+i*60,320)
            MainGame.wall_list.append(wall12)
        wall13 = Wall(780,260)
        MainGame.wall_list.append(wall13)
    def Display_Wall(self):
        for wall in MainGame.wall_list:
            if wall.hp <= 0:
                print("墙死了")
                explode3 = explode(wall)
                MainGame.explodelist.append(explode3)
                wall.live = False
                MainGame.wall_list.remove(wall)
            if wall.live:
                wall.displaywall()
    def Creat_mytank(self):
        MainGame.my_tank = MyTank(SCREEN_WEIGH/2+50,SCREEN_HEIGHT/2+50)
        music = Music('img/start.wav')
        music.paly()
    def Enemybullet_hit_Mytank(self):
        for Bullet in MainGame.enemy_bulletlist:
            if pygame.sprite.collide_rect(Bullet,MainGame.my_tank):
                Explode_1 = explode(MainGame.my_tank)
                MainGame.explodelist.append(Explode_1)
                MainGame.my_tank.live = False
                MainGame.enemy_bulletlist.remove(Bullet)
    def Creat_Enemy(self):
        num = random.randint(4,6)
        i = 0
        a = None
        self.left = self.Random_enemy_leftrect()
        self.top = self.Random_enemy_toprect()
        while i != num:
            hit = False
            self.speed = random.randint(2,4)
            self.temp_left = self.left
            self.temp_top = self.top
            self.top = self.Random_glass_toprect()
            self.left = self.Random_glass_leftrect()
            enemy = EnemyTank(self.left, self.top,self.speed)
            for wall_2 in MainGame.wall2_list:
                if pygame.sprite.collide_rect(enemy, wall_2):
                    hit = True
            for glass_ in MainGame.glass_list:
                if pygame.sprite.collide_rect(enemy, glass_):
                    hit = True
            for wall in MainGame.wall_list:
                if pygame.sprite.collide_rect(enemy, wall):
                    hit = True
            if pygame.sprite.collide_rect(enemy,MainGame.home):
                hit = True
            if pygame.sprite.collide_rect(enemy, MainGame.my_tank):
                hit = True
            if self.temp_left == self.left and self.temp_top == self.top:
                hit = True
            if hit == False:
                MainGame.enemy_tank.append(enemy)
                i += 1
    def Random_enemy_toprect(self):
        top =60*random.randint(0,12)
        return top
    def Random_enemy_leftrect(self):
        left =60*random.randint(0,12)
        return left
    def Display_Enemy(self):
        for enemy in MainGame.enemy_tank:
            if enemy.live:
                enemy.show()
                enemy.tank_hit_wall()
                enemy.enemytank_hit_mytank()
                enemy_bullet = None
                if MainGame.home.live:
                    enemy.randomMove()
                    enemy_bullet = enemy.shot()
                enemy.myBullet_hit_enemyTank()
                if enemy_bullet:
                    MainGame.enemy_bulletlist.append(enemy_bullet)
    def getText(self,text):
        pygame.font.init()
        font = pygame.font.SysFont('kaiti',18)
        T = font.render(text,True,TEXT_COLOR)
        return T
    def getEvent(self):
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not MainGame.my_tank.live:
                    self.Creat_mytank()
                if MainGame.my_tank and MainGame.my_tank.live and MainGame.home.live:
                    if event.key == pygame.K_LEFT:
                        MainGame.my_tank.direction = 'L'
                        MainGame.my_tank.stop = False
                    elif event.key == pygame.K_RIGHT:
                        MainGame.my_tank.direction = 'R'
                        MainGame.my_tank.stop = False
                    elif event.key == pygame.K_UP:
                        MainGame.my_tank.direction = 'U'
                        MainGame.my_tank.stop = False
                    elif event.key == pygame.K_DOWN:
                        MainGame.my_tank.direction = 'D'
                        MainGame.my_tank.stop = False
                    elif event.key == pygame.K_SPACE:
                        if len(MainGame.mytank_bulltlist) <= 3:
                            myBullet = bullet(MainGame.my_tank)
                            MainGame.mytank_bulltlist.append(myBullet)
                            bullet_music = Music('img/fire.wav')
                            bullet_music.paly()
            if MainGame.my_tank and MainGame.my_tank.live and MainGame.home.live:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        MainGame.my_tank.stop = True
    def Display_bullet(self):
        for mybullet in MainGame.mytank_bulltlist:
            if mybullet.live:
                mybullet.move()
                mybullet.displaybullet()
                mybullet.bullet_hit_wall()
                mybullet.bullet_hit_home()
            else:
                MainGame.mytank_bulltlist.remove(mybullet)
        for enemybullet in MainGame.enemy_bulletlist:
            if enemybullet.live:
                enemybullet.move()
                enemybullet.displaybullet()
                enemybullet.bullet_hit_wall()
                enemybullet.bullet_hit_home()
            else:
                MainGame.enemy_bulletlist.remove(enemybullet)
    def Display_explode(self):
        for Explode in MainGame.explodelist:
            if Explode.live:
                Explode.display()
            else:
                MainGame.explodelist.remove(Explode)
class Tank(Sprite):
    def __init__(self,left,top):
        super().__init__()
        self.images = {
            'U':pygame.image.load('img/p1tankU.gif'),
            'D':pygame.image.load('img/p1tankD.gif'),
            'L':pygame.image.load('img/p1tankL.gif'),
            'R':pygame.image.load('img/p1tankR.gif')
            }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 5
        self.stop = True
        self.live = True
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
    def move(self):
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        if self.direction == 'U':
            if self.rect.top >0 :
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.bottom < SCREEN_HEIGHT :
                self.rect.bottom += self.speed
        elif self.direction == 'L':
            if self.rect.left >0 :
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.right <SCREEN_WEIGH :
                self.rect.right += self.speed

    def shot(self):
        return bullet(self)
    def show(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
    def tank_hit_wall(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self,wall):
                self.stay()
        for wall in MainGame.wall2_list:
            if pygame.sprite.collide_rect(self,wall):
                self.stay()
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)
    def mytank_hit_enemytank(self):
        for enemy in MainGame.enemy_tank:
            if pygame.sprite.collide_rect(self,enemy):
                self.stay()
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        super(EnemyTank,self).__init__(left,top)
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }
        self.direction = self.randomDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.step = random.randint(30,40)
    def randomDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'
    def randomMove(self):
        if self.step > 0:
            self.move()
            self.step -= 1
        else:
            self.direction = self.randomDirection()
            self.step = random.randint(30,40)
    def shot(self):
        num = random.randint(1,1000)
        if num <= 10:
            return bullet(self)
    def myBullet_hit_enemyTank(self):
        for Bullet in MainGame.mytank_bulltlist:
            if pygame.sprite.collide_rect(Bullet,self):
                Explode = explode(self)
                MainGame.explodelist.append(Explode)
                self.live = False
                MainGame.enemy_tank.remove(self)
                Bullet.live = False
    def enemytank_hit_mytank(self):
        if pygame.sprite.collide_rect(self,MainGame.my_tank):
            self.stay()
class bullet(Sprite):
    def __init__(self,tank):
        super().__init__()
        self.image = pygame.image.load('img/enemymissile.gif')
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        #子弹的速度
        self.speed=6
        self.live = True
    def move(self):
        if self.direction == 'U':
            if self.rect.top >= 0:
                self.rect.top -= 10
            else:
                self.live = False
        if self.direction == 'D':
            if self.rect.top < SCREEN_HEIGHT:
                self.rect.top += 10
            else:
                self.live = False
        if self.direction == 'R':
            if self.rect.right < SCREEN_WEIGH:
                self.rect.right += 10
            else:
                self.live = False
        if self.direction == 'L':
            if self.rect.left >= 0:
                self.rect.left -= 10
            else:
                self.live = False
    def bullet_hit_wall(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self,wall):
                wall.hp -= 1
                self.live = False
        for wall in MainGame.wall2_list:
            if pygame.sprite.collide_rect(self,wall):
                wall.hp -= 1
                self.live = False
    def bullet_hit_home(self):
        if pygame.sprite.collide_rect(self,MainGame.home):
            explode2 = explode(MainGame.home)
            MainGame.explodelist.append(explode2)
            MainGame.home.live = False
    def displaybullet(self):
        MainGame.window.blit(self.image,self.rect)
class Wall():
    def __init__(self,left,top):
        self.image = pygame.image.load('img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.hp = 3
    def displaywall(self):
        if self.live:
            MainGame.window.blit(self.image,self.rect)
class Wall_2(Sprite):
    def __init__(self,left,top):
        super().__init__()
        self.image = pygame.image.load('img/wall_2.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.hp = 3
    def displaywall2(self):
        if self.live:
            MainGame.window.blit(self.image,self.rect)
class glass(Sprite):
    def __init__(self,left,top):
        super().__init__()
        self.image = pygame.image.load('img/glass.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
    def displayglass(self):
        if self.live:
            MainGame.window.blit(self.image,self.rect)
class home(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/home.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WEIGH /2,SCREEN_HEIGHT+10)
        self.live = True
        self.hp = 1
    def Display_home(self):
        if self.live:
            MainGame.window.blit(self.image,self.rect)
class explode():
    def __init__(self,tank):
        self.images = [pygame.image.load('img/blast0.gif'),
                       pygame.image.load('img/blast1.gif'),
                       pygame.image.load('img/blast2.gif'),
                       pygame.image.load('img/blast3.gif'),
                       pygame.image.load('img/blast4.gif')
        ]
        self.step = 0
        self.rect = tank.rect
        self.image = self.images[self.step]
        self.live = True
    def display(self):
        if len(self.images) > self.step:
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0
class Music():
    def __init__(self,filename):
        pygame.mixer.init()
        self.filename = filename
        pygame.mixer.music.load(self.filename)
    def paly(self):
        pygame.mixer.music.play()
if __name__ == '__main__':
    MainGame().startGame()

import pygame
from random import choice
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_w,
    K_s,
    KEYDOWN,
    K_RETURN
)

screen_width,screen_height = 720,480
score,score_ai = 0,0
speed_x = [-1,1]
speed_y = [-1,1]

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super(Paddle,self).__init__()
        self.surf = pygame.Surface((25,100))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(left = 10, top = 210)

    def update(self,pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_s]:
            self.rect.move_ip(0,1)

        if self.rect.top <=0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

class Ai_Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super(Ai_Paddle,self).__init__()
        self.surf = pygame.Surface((25,100))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(left = 685,top = 210)

    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
        


        if self.rect.top <=0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball,self).__init__()
        self.surf = pygame.Surface((10,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(left = 360,top = 240)
        self.speed = [0,0]
       

    def update(self):
        global score,score_ai
        self.rect.move_ip(self.speed[0],self.speed[1])
        if self.rect.top <=0 or self.rect.bottom > screen_height:
            self.speed[1]= -self.speed[1]
        if self.rect.left <=0:
            score_ai += 1 
            self.rect = self.surf.get_rect(left = 360,top = 240)
            self.speed = [0,0]
        if self.rect.right > screen_width:
            score += 1
            self.rect = self.surf.get_rect(left = 360,top = 240)
            self.speed = [0,0]

def Score(score):
   font=pygame.font.SysFont(None,40)
   scoretext=font.render(str(score), 1,(255,255,255))
   screen.blit(scoretext, (330, 20))        

def Score_ai(score_ai):
   font=pygame.font.SysFont(None,40)
   scoretext=font.render(str(score_ai), 1,(255,255,255))
   screen.blit(scoretext, (390, 20)) 


pygame.init()

pygame.display.set_caption('PONG!!!')  

paddle = Paddle()
ai_paddle = Ai_Paddle()
ball = Ball()

all_sprites = pygame.sprite.Group()
ball_sprite = pygame.sprite.Group()
all_sprites.add(paddle)
all_sprites.add(ai_paddle)
all_sprites.add(ball)
ball_sprite.add(ball)

screen = pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                ball.speed = [choice(speed_x),choice(speed_y)]
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pressed_keys = pygame.key.get_pressed()
    paddle.update(pressed_keys)
    ai_paddle.update(pressed_keys)
    ball.update()

    screen.fill((0,0,0))
    
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)
    
    Score_ai(score_ai)
    Score(score)

    if pygame.sprite.spritecollideany(paddle,ball_sprite):
        ball.speed[0]= - ball.speed[0]
    
    if pygame.sprite.spritecollideany(ai_paddle,ball_sprite):
        ball.speed[0]= - ball.speed[0]
    
    clock.tick(500)
    pygame.display.flip() 
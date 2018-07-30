import pygame;
import os;
import random;
import math;

pygame.init();

grey = (105,105,105);

win = pygame.display.set_mode((500,500));
pygame.display.set_caption("Snake");

class Player_Head(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self);
        self.image = pygame.Surface((25,25));
        self.image.fill((0,255,0));
        self.rect = self.image.get_rect();
        self.rect.center = (37.5,37.5);
        self.x_speed = 3;
        self.y_speed = 3;
        self.dir = 2;
        self.tempx=37.5;
        self.tempy=37.5;

    def update(self):
        key_press = pygame.key.get_pressed();
        if key_press[pygame.K_LEFT]:
            self.dir = 1;
        if key_press[pygame.K_RIGHT]:
            self.dir = 2;
        if key_press[pygame.K_UP]:
            self.dir = 3;
        if key_press[pygame.K_DOWN]:
            self.dir = 4;
        if self.dir ==1:
            self.tempx = self.rect.x;
            self.rect.x -= self.x_speed;
        if self.dir ==2:
            self.tempx = self.rect.x;
            self.rect.x += self.x_speed;
        if self.dir ==3:
            self.tempy = self.rect.y;
            self.rect.y -= self.y_speed;
        if self.dir ==4:
            self.tempy = self.rect.y;
            self.rect.y += self.y_speed;


class Border(pygame.sprite.Sprite):
    def __init__(self,x,y,height,width):
        pygame.sprite.Sprite.__init__(self);
        self.image = pygame.Surface((width,height));
        self.image.fill(grey);
        self.rect = self.image.get_rect();
        self.rect.center = (x,y);

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self);
        self.image = pygame.Surface((25,25));
        self.image.fill((255,0,0));
        self.rect = self.image.get_rect();
        x = random.randrange(50,450);
        y = random.randrange(50,450);
        self.rect.center = (x,y);

class Player_Tail(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self);
        self.image = pygame.Surface((25,25));
        self.image.fill((0,0,255));
        self.rect = self.image.get_rect();
        x = head.tempx;
        y = head.tempy;
        self.rect.center = (x,y);

    def update(self):
        self.rect.x,self.rect.y = head.tempx,head.tempy;

all_sprites = pygame.sprite.Group();
walls = pygame.sprite.Group();
foods = pygame.sprite.Group();
tails = pygame.sprite.Group();

head = Player_Head();
food = Food();

wall1 = Border(250,12.5,25,500);
wall2 = Border(250,487.5,25,500);
wall3 = Border(12.5,250,500,25);
wall4 = Border(487.5,250,500,25);

all_sprites.add(wall1);
all_sprites.add(wall2);
all_sprites.add(wall3);
all_sprites.add(wall4);
all_sprites.add(head);
all_sprites.add(food);

walls.add(wall1);
walls.add(wall2);
walls.add(wall3);
walls.add(wall4);

foods.add(food);


run = True;
while run:
    pygame.time.delay(25);
    win.fill((255, 255, 255));
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;
    all_sprites.update();
    wall_hit = pygame.sprite.spritecollide(head, walls, False);
    if wall_hit:
        run = False;
    food_hit = pygame.sprite.spritecollide(head,foods,True);
    if food_hit:
        m = Food();
        foods.add(m);
        all_sprites.add(m);
        tail = Player_Tail();
        all_sprites.add(tail);
        tails.add(tail);
    all_sprites.draw(win);
    pygame.display.update();
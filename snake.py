import pygame;
import os;
import random;
import math;
from pygame.locals import *;

game_folder = os.path.dirname(__file__);

pygame.init();
pygame.font.init();

grey = (105,105,105);
length = 0;
points = 0;

win = pygame.display.set_mode((500,500));
pygame.display.set_caption("Snake");
font = pygame.font.SysFont('Sans Serif', 20,False);

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self);
        #self.image = pygame.Surface((25,25));
        #self.image.fill((0,255,0));
        self.image = pygame.image.load(os.path.join(game_folder,"head.png")).convert();
        self.image.set_colorkey((255,255,255));
        self.rect = self.image.get_rect();
        self.rect.center = (x,y);
        self.x_speed = 25;
        self.y_speed = 25;
        self.dir = 2;
        self.tempx = int();
        self.tempy = int();

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
            self.tempy = self.rect.y;
            self.rect.x -= self.x_speed;
        if self.dir ==2:
            self.tempx = self.rect.x;
            self.tempy = self.rect.y;
            self.rect.x += self.x_speed;
        if self.dir ==3:
            self.tempx = self.rect.x;
            self.tempy = self.rect.y;
            self.rect.y -= self.y_speed;
        if self.dir ==4:
            self.tempx = self.rect.x;
            self.tempy = self.rect.y;
            self.rect.y += self.y_speed;

    def refresh(self):
        print("REFRESH")
        self.image = pygame.image.load(os.path.join(game_folder,"tail.png")).convert();
        self.image.set_colorkey((255,255,255));
        temp1 = snake.tempx;
        temp2 = snake.tempy;
        snake.tempx = self.rect.x;
        snake.tempy = self.rect.y;
        self.rect.x = temp1;
        self.rect.y = temp2;


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
        #self.image = pygame.Surface((25,25));
        #self.image.fill((255,0,0));
        self.image = pygame.image.load(os.path.join(game_folder,"food.png")).convert();
        self.image.set_colorkey((255,255,255));
        self.rect = self.image.get_rect();
        x = random.randrange(50,450);
        y = random.randrange(50,450);
        self.rect.center = (x,y);


all_sprites = pygame.sprite.Group();
walls = pygame.sprite.Group();
foods = pygame.sprite.Group();
tails = pygame.sprite.Group();

snake = Player(37.5,37.5);
food = Food();

wall1 = Border(250,12.5,25,500);
wall2 = Border(250,487.5,25,500);
wall3 = Border(12.5,250,500,25);
wall4 = Border(487.5,250,500,25);

all_sprites.add(wall1);
all_sprites.add(wall2);
all_sprites.add(wall3);
all_sprites.add(wall4);
all_sprites.add(snake);
all_sprites.add(food);

walls.add(wall1);
walls.add(wall2);
walls.add(wall3);
walls.add(wall4);

foods.add(food);


run = True;
while run:
    pygame.time.delay(90);
    point_surf = font.render("Score: " + str(points), False, (0, 0, 0));
    win.fill((255, 255, 255));
    win.blit(point_surf,(25,25));
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;
    all_sprites.update();
    wall_hit = pygame.sprite.spritecollide(snake, walls, False);
    tail_hit = pygame.sprite.spritecollide(snake,tails,False);
    if wall_hit:
        run = False;
    if tail_hit:
        run = False;
    food_hit = pygame.sprite.spritecollide(snake,foods,True);
    if food_hit:
        length+=1;
        if length < 20:
            points+=100;
        if length >= 20 and length < 30:
            points += 200;
        if length >=30:
            points+=500;
        m = Food();
        foods.add(m);
        all_sprites.add(m);
        tail = Player(snake.tempx,snake.tempy);
        tails.add(tail);
    for t in tails:
        t.refresh();
    all_sprites.draw(win);
    tails.draw(win);
    print(points);
    pygame.display.update();
pygame.quit();
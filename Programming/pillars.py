import pygame
import random
from game.constants import Constants

class Pillars: 
    def __init__(self, sprite_group):
        self.sprite_group = sprite_group 
        self.pillar_sprites = pygame.sprite.Group() 
        self.spawn() 
        self.spawn_count = 0
    def reset(self): 
        for pillar in self.pillar_sprites:
            pillar.kill()
        self.spawn_count = 0 
        self.spawn()
    def spawn(self):
        offset = random.randint(0, 100)
        top = UpPillar(offset)
        bottom = DownPillar(offset)
        
        self.pillar_sprites.add(top,bottom)
        self.sprite_group.add(top,bottom)
    
    def update(self):
        self.spawn_count += 1
        if self.spawn_count > Constants.pillar_spam_rate:
            self.spawn()
            self.spawn_count = 0
    def player_did_collide(self,player):
        if pygame.sprite.spritecollide(player, self.pillar_sprites, False, collided= pygame.sprite.collide_mask):
            return True
        return False
        
        
class Pillar(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.delta = 1 
        self.x_pos = Constants.screen_width + 50 
        self.y_pos = 0

    def update(self):
        self.x_pos -= self.delta 
        if self.x_pos< -50:
            self.kill()
            
        self.rect.center = (self.x_pos,self.y_pos)
class UpPillar(Pillar):
    def __init__(self, offset=0): 
        super().__init__() 
        self.y_pos= Constants.screen_height - 110 + offset 
        self.image = pygame.image.load('assets/PNG/rockGrass.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image) 
        self.rect = self.image.get_rect() 
        self.rect.center = (self.x_pos, self.y_pos)
            
class DownPillar(Pillar):
    def __init__(self, offset=0): 
        super().__init__() 
        self.y_pos= offset 
        self.image = pygame.image.load('assets/PNG/rockGrassDown.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image) 
        self.rect = self.image.get_rect() 
        self.rect.center = (self.x_pos, self.y_pos)
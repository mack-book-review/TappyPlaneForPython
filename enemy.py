import pygame 
from constants import *
import random 
import math 

class Enemy(pygame.sprite.Sprite):

  ENEMY_TYPES = ["Bee","Bat"]

  def __init__(self,texture_paths):
    super().__init__()

    self.textures = [] 

    for path in texture_paths:
      self.textures.append(pygame.transform.scale(pygame.image.load(path),[30,30]))

    #Initialize timer variables
    self.texture_timer = 0 
    self.texture_change_interval = 500
    self.current_texture = 0

    #Get initial image
    self.image = self.textures[self.current_texture]
    self.image.set_colorkey(WHITE)
    
    #Get reference to rect
    self.rect = self.image.get_rect()

    #Adjust Size - Scale Down
    self.size = self.image.get_size()
        # create a 2x bigger image than self.image
    self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.5), int(self.size[1]*0.5)))

    #Initialize speed 
    self.speed = random.randint(5,20)
    #Initialize Position
    self.rect.x = DEFAULT_SCREEN_SIZE[0] + random.randint(0,100)
    self.rect.y = random.randint(0,DEFAULT_SCREEN_SIZE[1]*0.5)
  


  def update(self):
    print("Updating enemy")
    print(str(self))
    self.update_textures()
    super().update()

  def update_textures(self):
    ticks = pygame.time.get_ticks()
    ticks = math.floor(ticks/100)

    self.texture_timer += ticks 

    if self.texture_timer > self.texture_change_interval:
      self.current_texture += 1
      if self.current_texture >= len(self.textures):
        self.current_texture = 0 
      self.texture_timer = 0
    
    self.image = self.textures[self.current_texture]
 


  
  def update(self):
    self.rect.x -= self.speed
    if self.rect.x < 0:
      self.rect.y = random.randint(0,DEFAULT_SCREEN_SIZE[1]*0.5)
      self.rect.x = DEFAULT_SCREEN_SIZE[0] + 50
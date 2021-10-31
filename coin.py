import pygame 
from constants import *
import random 
import math 

class Coin(pygame.sprite.Sprite):

  

  def __init__(self,coin_type):
    super().__init__()

    texture_paths = None
    self.textures = [] 
    self.coin_type = coin_type

    if coin_type == "gold":
      texture_paths = [
        "assets/coins/gold_1.png",
        "assets/coins/gold_2.png",
        "assets/coins/gold_3.png",
      ]
    elif coin_type == "silver":
      texture_paths = [
        "assets/coins/silver_1.png",
        "assets/coins/silver_2.png",
        "assets/coins/silver_3.png",
      ]
    else:
      texture_paths = [
        "assets/coins/bronze_1.png",
        "assets/coins/bronze_2.png",
        "assets/coins/bronze_3.png",
      ]

    
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
    self.speed = random.randint(1,5)
    #Initialize Position
    self.rect.x = DEFAULT_SCREEN_SIZE[0] + random.randint(0,100)
    self.rect.y = random.randint(0,DEFAULT_SCREEN_SIZE[1]*0.5)
  


  def update(self):
    print("Updating coin")
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
 
  def get_point_value(self):
    if self.coin_type == "gold":
      return 3
    elif self.coin_type == "silver":
      return 2 
    else:
      return 1 
      
  def reset_position(self):
     self.rect.y = random.randint(0,DEFAULT_SCREEN_SIZE[1]*0.5)
     self.rect.x = DEFAULT_SCREEN_SIZE[0] + 50
    
  
  def update(self):
    self.rect.x -= self.speed
    if self.rect.x < 0:
      self.reset_position()
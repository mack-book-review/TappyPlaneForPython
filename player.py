import pygame 
from constants import *
import math 

class Player(pygame.sprite.Sprite):
  """
  This class represents the tappy plane used by the player; it derives from the "Sprite" cass in pygame
  """

  TEXTURES = [
     pygame.image.load("assets/planes/planeBlue1.png"),
    pygame.image.load("assets/planes/planeBlue2.png"),
    pygame.image.load("assets/planes/planeBlue3.png")
  ]
  def __init__(self):

    #Call the parent class (Sprite) constructor
    super().__init__()

    #Initialize player properties
    self.health = 20
    self.is_colliding = False

    #Load the default player image
    self.current_texture = 0
    self.image = Player.TEXTURES[self.current_texture]

    #Make image background is transparent
    self.image.set_colorkey(WHITE)

    #Store a reference to the 'rect' object, which holds information about player position and size
    self.rect = self.image.get_rect()
    self.size = self.image.get_size()
    self.width = self.size[0]
    self.height = self.size[1]
   

    #Initialize positions
    self.rect.x = 10
    self.rect.y = DEFAULT_SCREEN_SIZE[1]*0.5

    #Create timers
    self.texture_timer = 0 
    self.texture_change_interval = 1000 

    self.coin_debounce_timer = 0
    self.coin_debounce_interval = 3000

    self.enemy_debounce_timer = 0
    self.enemy_debounce_interval = 5000

    #Initialize debounce flags 
    self.is_colliding_coin = False
    self.is_colliding_enemy = False


  def update_timers(self):
    ticks = pygame.time.get_ticks()
    ticks = math.floor(ticks/100)

    self.enemy_debounce_timer += ticks 
    self.coin_debounce_timer += ticks 

    if self.enemy_debounce_timer > self.enemy_debounce_interval:
      self.is_colliding_enemy = False
      self.enemy_debounce_timer = 0
    
    if self.coin_debounce_timer > self.coin_debounce_interval:
      self.is_colliding_coin = False
      self.coin_debounce_timer = 0

  def update_textures(self):
    ticks = pygame.time.get_ticks()
    ticks = math.floor(ticks/100)

    self.texture_timer += ticks 

    if self.texture_timer > self.texture_change_interval:
      self.current_texture += 1
      if self.current_texture >= len(Player.TEXTURES):
        self.current_texture = 0 
      self.texture_timer = 0
    
    self.image = Player.TEXTURES[self.current_texture]
 
  
  #Getters and setters
  def get_size(self):
    return [self.rect.width,self.rect.height]

  def get_position(self):
    return [self.rect.x,self.rect.y]
  
  def set_position(self,x,y):
    self.rect.x = x 
    self.rect.y = y

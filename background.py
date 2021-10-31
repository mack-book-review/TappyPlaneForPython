import pygame 
from constants import *

class Background:

  def __init__(self,screen,img_path):
    self.screen = screen
    self.img_path = img_path 
  
    self.bg_image_set = [
      pygame.transform.scale(pygame.image.load(img_path),DEFAULT_SCREEN_SIZE), 
      pygame.transform.scale(pygame.image.load(img_path),DEFAULT_SCREEN_SIZE), 
      pygame.transform.scale(pygame.image.load(img_path),DEFAULT_SCREEN_SIZE)
      ]

    self.offset = 0
   

  def update(self):
    self.offset += 1

    if self.offset - DEFAULT_SCREEN_SIZE[0] >= 0:
      first_image = self.bg_image_set.pop(0)
      self.bg_image_set.append(first_image)
      self.offset = 0
     

    for i in range(len(self.bg_image_set)):
      x_pos = i*DEFAULT_SCREEN_SIZE[0] - self.offset
      y_pos = 0
      self.screen.blit(self.bg_image_set[i],[x_pos,y_pos])

    

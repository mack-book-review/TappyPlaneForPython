import pygame 
from constants import *

class HUD():

  def __init__(self,screen):
    pygame.font.init()
    self.hud_font = pygame.font.SysFont('Comic Sans MS',30)
    self.screen = screen
  
  
  def update(self,score,health):
    hud_text = self.hud_font.render(f'Score: {score}  Health: {health} ', False, BLACK)
      
    self.screen.blit(hud_text,(10,10))

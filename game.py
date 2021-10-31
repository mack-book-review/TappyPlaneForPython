import pygame
import random
from constants import *
import player 
import background
import hud
import enemy
import bee
import bat
import coin 

class Game(object):
 
  def __init__(self):
    pygame.init() 
  
    self.score = 0
    self.clock = pygame.time.Clock()

    #Create timers
    self.enemySpawnTimer = 0 
    self.enemySpawnInterval = 5000

    #Create screen
    self.screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE)
    pygame.display.set_caption("Tappy Plane Game")
    
    #Create sprite groups
    self.all_sprites_list = pygame.sprite.Group()
    self.enemy_list = pygame.sprite.Group()
    self.coin_list = pygame.sprite.Group()
    

    #Create player
    self.player = player.Player()
    self.all_sprites_list.add(self.player)

    #Create enemies 
    self.spawn_enemies(random.randint(1,4))

    #Create coins 
    self.spawn_coins(random.randint(1,3))
  
    #Create background
    self.background = background.Background(self.screen,"assets/backgrounds/colored_castle.png")

    #Create HUD
    self.hud = hud.HUD(self.screen)

  def spawn_coins(self,number_enemies):
   
    some_coin = None
    coin_types = ["gold","silver","bronze"]
    for _ in range(number_enemies):
      rand_type = random.randrange(0,len(coin_types))
    
      coin_type = coin_types[rand_type]
    
      if coin_type == "gold":
        some_coin = coin.Coin("gold")
      elif coin_type == "silver":
        some_coin = coin.Coin("silver") 
      else: 
        some_coin = coin.Coin("bronze")

      self.coin_list.add(some_coin)
      self.all_sprites_list.add(some_coin)
  
  def spawn_enemies(self,number_enemies):
   
    some_enemy = None
    for _ in range(number_enemies):
      rand_type = random.randrange(0,len(enemy.Enemy.ENEMY_TYPES))
    
      e_type = enemy.Enemy.ENEMY_TYPES[rand_type]
    
      if e_type == "Bee":
        some_enemy = bee.Bee()
      elif e_type == "Bat":
        some_enemy = bat.Bat() 

      self.enemy_list.add(some_enemy)
      self.all_sprites_list.add(some_enemy)

  def run_game(self):
    done = False 

    #Main game loop 
    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            self.player.rect.y -= 20
          elif event.key == pygame.K_DOWN: 
            self.player.rect.y += 20
      #Update background 
      self.background.update()
      
      #Update all the sprites
      self.all_sprites_list.draw(self.screen)
      self.player.update_textures()
      self.player.update_timers()
      self.enemy_list.update()
      self.coin_list.update()

      for an_enemy in self.enemy_list:
        an_enemy.update_textures()
      
      for some_coin in self.coin_list:
        some_coin.update_textures()
      

      #check collisions
      if not self.player.is_colliding_coin:
  
        coin = pygame.sprite.spritecollideany(self.player,self.coin_list,pygame.sprite.collide_rect_ratio(0.5))
        if coin:
          self.player.is_colliding_coin = True
          self.score += coin.get_point_value()
          coin.reset_position()
          self.player.coin_debounce_timer = 0

      if not self.player.is_colliding_enemy:
  
        player_hit = pygame.sprite.spritecollideany(self.player,self.enemy_list,pygame.sprite.collide_rect_ratio(0.5))
        if player_hit:
          self.player.is_colliding_enemy = True
          self.player.health -= 1
          self.player.enemy_debounce_timer = 0


      #Update HUD 
      self.hud.update(self.score,self.player.health)

      #update the screen
      pygame.display.flip()

      #set the frame rate
      self.clock.tick(60)
    
    pygame.quit()
    


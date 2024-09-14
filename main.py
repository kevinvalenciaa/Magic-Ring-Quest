
#double check overlap
#flowchart / list of events on how the game works

import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
    def __init__(self):
    
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Magic Ring Quest')
        self.clock = pygame.time.Clock()
    
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()                    pygame.quit()
                    sys.exit()
  
            self.screen.fill('black')
            self.level.run()

            #debug('test')
            pygame.display.update()
            self.clock.tick(FPS)
 
if __name__ == '__main__':
    game = Game()
    game.run()

                    if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

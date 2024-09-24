
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
        
        # Game state
        self.paused = False    
        self.show_fps = False        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                    if event.key == pygame.K_SPACE:
                    if event.key == pygame.K_F1:
                        self.show_fps = not self.show_fps                        self.paused = not self.paused                        pygame.quit()
                        sys.exit()                    pygame.quit()
                    sys.exit()
  
            self.screen.fill('black')
            if not self.paused:
                self.level.run()
            else:
                font = pygame.font.Font(None, 74)
                pause_text = font.render("PAUSED", True, "white")
                pause_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//2))
                self.screen.blit(pause_text, pause_rect)
            #debug('test')
            pygame.display.update()
            self.clock.tick(FPS)
 
if __name__ == '__main__':
    game = Game()
    game.run()

                    if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                    if event.key == pygame.K_SPACE:
                    if event.key == pygame.K_F1:
                        self.show_fps = not self.show_fps                        self.paused = not self.paused                        pygame.quit()
                        sys.exit()

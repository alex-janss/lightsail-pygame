import pygame
from pygame import event
import sys
from player import Player

WIDTH = 720
HEIGTH = 720
FPS = 60


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('LightSailer')
        self.clock = pygame.time.Clock()

        self.visible_sprites = pygame.sprite.Group()
        self.player = Player(self.screen.get_rect().center, self.visible_sprites)


    def run(self):
        while not event.get(eventtype=pygame.QUIT):
            self.screen.fill('black')
            #self.screen.blit(self.player.image, self.player.rect)
            self.visible_sprites.update()
            self.visible_sprites.draw(self.screen)
            pygame.display.update()
            event.clear()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    app = App()
    app.run()

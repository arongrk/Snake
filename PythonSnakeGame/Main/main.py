import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('ressources/schlangenkopf-sticker.jpg').convert()
        self.headup = pygame.image.load('ressources/snake_graphics/headup.png').convert()
        self.headdown = pygame.image.load('ressources/snake_graphics/headdown.png').convert()
        self.headright = pygame.image.load('ressources/snake_graphics/headright.png').convert()
        self.headleft = pygame.image.load('ressources/snake_graphics/headleft.png').convert()
        self.upright = pygame.image.load('ressources/snake_graphics/upright.png').convert()
        self.upleft = pygame.image.load('ressources/snake_graphics/upleft.png').convert()
        self.downright = pygame.image.load('ressources/snake_graphics/downright.png').convert()
        self.downleft = pygame.image.load('ressources/snake_graphics/downleft.png').convert()
        self.vertical = pygame.image.load('ressources/snake_graphics/vertical.png').convert()
        self.horizontal = pygame.image.load('ressources/snake_graphics/horizontal.png').convert()
        self.endup = pygame.image.load('ressources/snake_graphics/endup.png').convert()
        self.enddown = pygame.image.load('ressources/snake_graphics/enddown.png').convert()
        self.endright = pygame.image.load('ressources/snake_graphics/endright.png').convert()
        self.endleft = pygame.image.load('ressources/snake_graphics/endleft.png').convert()
        self.x = 330
        self.y = 330
        self.direction = 'right'
        self.snake_length = 10
        self.snake_x = [330]
        self.snake_y = [330]

    def draw_head(self):
        if self.direction == 'up':
            self.parent_screen.blit(self.headup, (self.x, self.y))
        if self.direction == 'down':
            self.parent_screen.blit(self.headdown, (self.x, self.y))
        if self.direction == 'right':
            self.parent_screen.blit(self.headright, (self.x, self.y))
        if self.direction == 'left':
            self.parent_screen.blit(self.headleft, (self.x, self.y))

    def draw_body(self):
        slen = self.snake_length
        for i in range(0, slen - 1):
            if self.snake_x[i-1] > self.snake_x[i]:
                if self.snake_x[i+1] < self.snake_x[i]:
                    self.parent_screen.blit(self.horizontal, (self.snake_x[i], self.snake_y[i]))
                if self.snake_y[i+1] > self.snake_y[i]:
                    self.parent_screen.blit(self.downright, (self.snake_x[i], self.snake_y[i]))
                if self.snake_y[i+1] < self.snake_y[i]:
                    self.parent_screen.blit(self.upright, (self.snake_x[i], self.snake_y[i]))
            if self.snake_x[i-1] < self.snake_x[i]:
                if self.snake_x[i+1] > self.snake_x[i]:
                    self.parent_screen.blit(self.horizontal, (self.snake_x[i], self.snake_y[i]))
                if self.snake_y[i+1] > self.snake_y[i]:
                    self.parent_screen.blit(self.downleft, (self.snake_x[i], self.snake_y[i]))
                if self.snake_y[i+1] < self.snake_y[i]:
                    self.parent_screen.blit(self.upleft, (self.snake_x[i], self.snake_y[i]))
            if self.snake_y[i-1] > self.snake_y[i]:
                if self.snake_y[i+1] < self.snake_y[i]:
                    self.parent_screen.blit(self.vertical, (self.snake_x[i], self.snake_y[i]))
                if self.snake_x[i+1] > self.snake_x[i]:
                    self.parent_screen.blit(self.downright, (self.snake_x[i], self.snake_y[i]))
                if self.snake_x[i+1] < self.snake_x[i]:
                    self.parent_screen.blit(self.downleft, (self.snake_x[i], self.snake_y[i]))
            if self.snake_y[i-1] < self.snake_y[i]:
                if self.snake_y[i+1] > self.snake_y[i]:
                    self.parent_screen.blit(self.vertical, (self.snake_x[i], self.snake_y[i]))
                if self.snake_x[i+1] > self.snake_x[i]:
                    self.parent_screen.blit(self.upright, (self.snake_x[i], self.snake_y[i]))
                if self.snake_x[i+1] < self.snake_x[i]:
                    self.parent_screen.blit(self.upleft, (self.snake_x[i], self.snake_y[i]))
        if slen > 1:
            if self.snake_x[slen - 2] > self.snake_x[slen - 1]:
                self.parent_screen.blit(self.endright, (self.snake_x[slen - 1], self.snake_y[slen - 1]))
            if self.snake_x[slen - 2] < self.snake_x[slen - 1]:
                self.parent_screen.blit(self.endleft, (self.snake_x[slen - 1], self.snake_y[slen - 1]))
            if self.snake_y[slen - 2] > self.snake_y[slen - 1]:
                self.parent_screen.blit(self.enddown, (self.snake_x[slen - 1], self.snake_y[slen - 1]))
            if self.snake_y[slen - 2] < self.snake_y[slen - 1]:
                self.parent_screen.blit(self.endup, (self.snake_x[slen - 1], self.snake_y[slen - 1]))

    def draw(self):
        self.parent_screen.fill((52, 117, 54))
        for i in range(self.snake_length - len(self.snake_x)):
            self.snake_x.append(0)
            self.snake_y.append(0)
        for i in range(self.snake_length - 1, 0, -1):
            self.snake_x[i] = self.snake_x[i-1]
            self.snake_y[i] = self.snake_y[i-1]
        self.snake_x[0] = self.x
        self.snake_y[0] = self.y
        self.draw_body()
        self.draw_head()
        pygame.display.flip()

    def check_collision(self):
        for i in range(1, self.snake_length):
            if self.snake_length > 1:
                if self.x == self.snake_x[i] and self.y == self.snake_y[i]:
                    return True
            if self.snake_x[0] > 990 or self.x < 0 or self.y > 660 or self.y < 0:
                return True

    def move_up(self):
        self.y -= 55
        self.draw()

    def move_down(self):
        self.y += 55
        self.draw()

    def move_right(self):
        self.x += 55
        self.draw()

    def move_left(self):
        self.x -= 55
        self.draw()

    def walk(self):
        if self.direction == 'down':
            self.move_down()
            col = self.check_collision()
            if not col:
                time.sleep(0.3)
            return col
        if self.direction == 'up':
            self.move_up()
            col = self.check_collision()
            if not col:
                time.sleep(0.3)
            return col
        if self.direction == 'right':
            self.move_right()
            col = self.check_collision()
            if not col:
                time.sleep(0.3)
            return col
        if self.direction == 'left':
            self.move_left()
            col = self.check_collision()
            if not col:
                time.sleep(0.3)
            return col


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1045, 715))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.col = False

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        self.snake.snake_length += 1

                    if event.key == K_UP:
                        self.snake.direction = 'up'
                    elif event.key == K_DOWN:
                        self.snake.direction = 'down'
                    elif event.key == K_LEFT:
                        self.snake.direction = 'left'
                    elif event.key == K_RIGHT:
                        self.snake.direction = 'right'

                if event.type == QUIT:
                    running = False
            self.col = self.snake.walk()
            if self.col:
                running = False


if __name__ == '__main__':
    game = Game()
    game.run()

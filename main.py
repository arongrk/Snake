import pygame
from pygame.locals import *
import time
import random


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('ressources/schlangenkopf-sticker.jpg').convert_alpha()
        self.headup = pygame.image.load('ressources/snake_graphics/headup.png').convert_alpha()
        self.headdown = pygame.image.load('ressources/snake_graphics/headdown.png').convert_alpha()
        self.headright = pygame.image.load('ressources/snake_graphics/headright.png').convert_alpha()
        self.headleft = pygame.image.load('ressources/snake_graphics/headleft.png').convert_alpha()
        self.upright = pygame.image.load('ressources/snake_graphics/upright.png').convert_alpha()
        self.upleft = pygame.image.load('ressources/snake_graphics/upleft.png').convert_alpha()
        self.downright = pygame.image.load('ressources/snake_graphics/downright.png').convert_alpha()
        self.downleft = pygame.image.load('ressources/snake_graphics/downleft.png').convert_alpha()
        self.vertical = pygame.image.load('ressources/snake_graphics/vertical.png').convert_alpha()
        self.horizontal = pygame.image.load('ressources/snake_graphics/horizontal.png').convert_alpha()
        self.endup = pygame.image.load('ressources/snake_graphics/endup.png').convert_alpha()
        self.enddown = pygame.image.load('ressources/snake_graphics/enddown.png').convert_alpha()
        self.endright = pygame.image.load('ressources/snake_graphics/endright.png').convert_alpha()
        self.endleft = pygame.image.load('ressources/snake_graphics/endleft.png').convert_alpha()
        self.x = 330
        self.y = 330
        self.direction = 'right'
        self.snake_length = 2
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
        for i in range(1, slen - 1):
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

    def check_collision(self):
        for i in range(1, self.snake_length):
            if self.snake_length > 1:
                if self.x == self.snake_x[i] and self.y == self.snake_y[i]:
                    return True
        if self.x > 990 or self.x < 0 or self.y > 660 or self.y < 0:
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
        if self.direction == 'up':
            self.move_up()
        if self.direction == 'right':
            self.move_right()
        if self.direction == 'left':
            self.move_left()


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = 110
        self.y = 110
        self.image = pygame.image.load('ressources/snake_graphics/apple.png').convert_alpha()

    def draw(self):
        self.parent_screen.fill((52, 117, 54))
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(0, 18) * 55
        self.y = random.randint(0, 12) * 55


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1045, 715))
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.snake.draw()
        self.game_lost = False
        self.speed = 0.3

    def apple_col(self):
        if self.apple.x == self.snake.x and self.apple.y == self.snake.y:
            return True
        return False

    def game_over(self):
        self.surface.fill((52, 117, 54))
        font = pygame.font.SysFont('leelawadeeui', 24)
        img = font.render('Game Over!', True, (0, 0, 0))
        self.surface.blit(img, (200, 200))
        pygame.display.flip()

    def play(self):
        self.apple.draw()
        self.snake.walk()
        if self.snake.check_collision():
            return True
        pygame.display.flip()

        # Check for Apple collision
        if self.apple_col():
            self.snake.snake_length += 1
            self.apple.move()

    def run(self):

        while not self.game_lost:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_lost = True
                    if event.key == K_RETURN:
                        self.snake.snake_length += 1

                    if event.key == K_UP and not self.snake.direction == 'down':
                        self.snake.direction = 'up'
                    elif event.key == K_DOWN and not self.snake.direction == 'up':
                        self.snake.direction = 'down'
                    elif event.key == K_LEFT and not self.snake.direction == 'right':
                        self.snake.direction = 'left'
                    elif event.key == K_RIGHT and not self.snake.direction == 'left':
                        self.snake.direction = 'right'

                # Speeding up the snake
                    if event.key == K_UP and self.snake.direction == 'up':
                        self.speed = 0.1
                    if event.key == K_DOWN and self.snake.direction == 'down':
                        self.speed = 0.1
                    if event.key == K_LEFT and self.snake.direction == 'left':
                        self.speed = 0.1
                    if event.key == K_RIGHT and self.snake.direction == 'right':
                        self.speed = 0.1

                # Slowing down the snake
                if event.type == KEYUP:
                    if event.key == K_UP and self.snake.direction == 'up':
                        self.speed = 0.3
                    if event.key == K_DOWN and self.snake.direction == 'down':
                        self.speed = 0.3
                    if event.key == K_LEFT and self.snake.direction == 'left':
                        self.speed = 0.3
                    if event.key == K_RIGHT and self.snake.direction == 'right':
                        self.speed = 0.3

                if event.type == QUIT:
                    self.game_lost = True

            if self.play():
                self.game_lost = True
            time.sleep(self.speed)

        self.game_over()
        time.sleep(5)







if __name__ == '__main__':
    game = Game()
    game.run()

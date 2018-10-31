import random
import operator
import pygame
import math

def generate_nums(difficulty):
    ops = ['+', '-', '*']
    num1 = random.randint(0, difficulty)
    num2 = random.randint(1, difficulty)
    op = random.choice(ops)
    nums = [num1, op, num2]
    return nums


def get_question_text(nums):
    return f"{nums[0]} {nums[1]} {nums[2]}"


def get_answer(nums):
    if nums[1] == '+':
        answer = nums[0] + nums[2]
    if nums[1] == '-':
        answer = nums[0] - nums[2]
    if nums[1] == '*':
        answer = nums[0] * nums[2]
    return answer


class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.is_clicked = False

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.is_clicked = True
                return True

            return False


class User:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)


def get_click(button):
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_over(pos):
                lives = 3
                dead = False

class Candy:
    def __init__(self, x, y, speed, angle, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.image = image

    def move(self, max_width, max_height):
        """ Update speed and position based on speed, angle """
        # for constant change in position values.
        if self.x > max_width or self.x < 0 or self.y > max_height or self.y < 0:
            self.speed *= -1
            self.angle = random.randint(0,360)

        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def draw(self, win):
        """ Draw the particle on screen"""
        win.blit(self.image, (self.x, self.y))
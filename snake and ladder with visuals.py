import pygame
import random
class SnakeLadder:
    def __init__(self):
        # Initialize the game board
        pygame.init()
        self.width = 720
        self.height = 480
        self.board_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.board_size)
        self.board_color = (240, 240, 240)
        self.snake_color = (255, 0, 0)
        self.ladder_color = (0, 255, 0)
        self.player_color = (0, 0, 255)
        self.snakes = {16: 4, 48: 26, 49: 11, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.pos = 0

    def draw_board(self):
        # Draw the game board
        self.screen.fill(self.board_color)
        for snake in self.snakes:
            pygame.draw.line(self.screen, self.snake_color,
                             (snake % 10 * 72, snake // 10 * 48),
                             (self.snakes[snake] % 10 * 72, self.snakes[snake] // 10 * 48), 5)
        for ladder in self.ladders:
            pygame.draw.line(self.screen, self.ladder_color,
                             (ladder % 10 * 72, ladder // 10 * 48),
                             (self.ladders[ladder] % 10 * 72, self.ladders[ladder] // 10 * 48), 5)
        pygame.draw.circle(self.screen, self.player_color, (self.pos % 10 * 72, self.pos // 10 * 48), 20)
        pygame.display.flip()

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self):
        roll = self.roll_dice()
        self.pos += roll
        print(f"You rolled a {roll}. You are now on {self.pos}.")

        if self.pos in self.snakes:
            print(f"Oops, you landed on a snake and went down to {self.snakes[self.pos]}.")
            self.pos = self.snakes[self.pos]

        elif self.pos in self.ladders:
            print(f"Yay, you landed on a ladder and went up to {self.ladders[self.pos]}.")
            self.pos = self.ladders[self.pos]

        self.draw_board()

        if self.pos == 100:
            print("Congratulations, you won!")
            return True
        else:
            return False


game = SnakeLadder()
game.draw_board()
while not game.move():
    pass

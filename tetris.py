import pygame
import sys
from random import choice

from pygame.event import EventType

pygame.init()


class TetrisApp:
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20
    TILE_SIZE = 30

    COLORS = [
        (0, 0, 255),  # blue
        (255, 165, 0),  # orange
        (0, 255, 255),  # cyan
        (255, 0, 255),  # magenta
        (255, 0, 0),  # red
        (0, 255, 0),  # green
        (255, 255, 0)  # yellow
    ]

    # (I, T, S, Z, O, L, J)
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1, 1],
         [0, 1, 0]],  # T
        [[0, 1, 1],
         [1, 1, 0]],  # S
        [[1, 1, 0],
         [0, 1, 1]],  # Z
        [[1, 1],
         [1, 1]],  # O
        [[1, 1, 1],
         [1, 0, 0]],  # L
        [[1, 1, 1],
         [0, 0, 1]],  # J
    ]

    def __init__(self):
        # Set up the display
        self.width = TetrisApp.BOARD_WIDTH * TetrisApp.TILE_SIZE
        self.height = TetrisApp.BOARD_HEIGHT * TetrisApp.TILE_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tetris')

        # Set up the clock for controlling game speed
        self.clock = pygame.time.Clock()

        # Game state
        # self.board = TODO
        self.board = [[0] * TetrisApp.BOARD_WIDTH for _ in range(TetrisApp.BOARD_HEIGHT)]
        self.current_piece = []
        self.current_piece_color = None
        self.current_piece_x = 0
        self.current_piece_y = 0
        self.game_over = False

        # Time for piece movement
        self.drop_time = 0
        self.drop_speed = 500  # 0.5 second

        # start with a new piece
        self.new_piece()

    def new_piece(self):
        # TODO
        self.current_piece = choice(TetrisApp.SHAPES)
        self.current_piece_color = choice(TetrisApp.COLORS)
        self.current_piece_x = 0
        self.current_piece_y = 0

    def draw_tile(self, x, y, color):
        # Calculate the rectangle position
        rect = pygame.Rect(
            x * TetrisApp.TILE_SIZE,
            y * TetrisApp.TILE_SIZE,
            TetrisApp.TILE_SIZE,
            TetrisApp.TILE_SIZE
        )

        # Draw the filled rectangle
        pygame.draw.rect(self.screen, color, rect)
        # Draw a graw border
        pygame.draw.rect(self.screen, (128, 128, 128), rect, 1)

    def draw(self):
        self.screen.fill((0, 216, 166))

        # Draw current piece!!!
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell == 1:
                    self.draw_tile(
                        x + self.current_piece_x,
                        y + self.current_piece_y,
                        self.current_piece_color
                    )

        pygame.display.flip()

    def check_collision(self, dx, dy):
        new_x = self.current_piece_x + dx
        new_y = self.current_piece_y + dy

        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell != 0:
                    board_x = new_x + x
                    board_y = new_y + y

                    if board_x < 0 or board_x >= TetrisApp.BOARD_WIDTH \
                            or board_y >= TetrisApp.BOARD_HEIGHT:
                        return True

                    if board_y >= 0 and self.board[board_y][board_x] != 0:
                        return True

        return False

    def move(self, dx, dy):
        if not self.check_collision(dx, dy):
            self.current_piece_x += dx
            self.current_piece_y += dy
            return True

        return False

    def rotate(self):
        rotated = [list(row) for row in zip(*reversed(self.current_piece))]
        self.current_piece = rotated

    def handle_events(self):
        # 이벤트 처리 (특히 창 닫기)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move(1, 0)
                elif event.key == pygame.K_UP:
                    self.rotate()
                elif event.key == pygame.K_DOWN:
                    self.move(0, 1)
                elif event.key == pygame.K_SPACE:
                    print("Space Bar Pressed")

    def run(self):
        """ Main game loop. """
        while not self.game_over:
            self.handle_events()
            self.draw()
            self.clock.tick(60)  # Limit to 60 FPS


def main():
    app = TetrisApp()
    app.run()


if __name__ == "__main__":
    main()
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
        self.drop_time = pygame.time.get_ticks()
        self.drop_speed = 500  # 0.5 second

        # start with a new piece
        self.new_piece()

    def new_piece(self):
        # TODO
        self.current_piece = choice(TetrisApp.SHAPES)
        self.current_piece_color = choice(TetrisApp.COLORS)
        self.current_piece_x = TetrisApp.BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_piece_y = 0

        if self.check_collision(self.current_piece_x, self.current_piece_y, self.current_piece):
            self.game_over = True
            print("Game Over (What a Skill Issue)")

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

        #draw the board
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    color = TetrisApp.COLORS[cell - 1]
                    self.draw_tile(x, y, color)


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


    def check_collision(self, px, py, piece):
        """Check if the piece collides with the board boundaries or other pieces."""
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                try:
                    # Check if the cell is filled and if it's outside boundaries or colliding
                    if cell and (
                            py + y >= TetrisApp.BOARD_HEIGHT or  # Bottom boundary
                            px + x < 0 or  # Left boundary
                            px + x >= TetrisApp.BOARD_WIDTH or  # Right boundary
                            self.board[py + y][px + x]  # Collision with existing blocks
                    ):
                        return True
                except IndexError:
                    return True
        return False

    def move(self, dx, dy):
        if not self.check_collision(self.current_piece_x + dx, self.current_piece_y + dy, self.current_piece):
            self.current_piece_x += dx
            self.current_piece_y += dy
            return True

        return False

    def rotate(self):
        rotated = [list(row) for row in zip(*reversed(self.current_piece))]
        if not self.check_collision(self.current_piece_x, self.current_piece_y, rotated):
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
                    while self.move(0, 1):
                        pass

    def clear_line(self):
        new_board = []

        for row in self.board:
            if 0 in row:
                new_board.append(row)
        num_of_cleared_lines = TetrisApp.BOARD_HEIGHT - len(new_board)
        for _ in range(num_of_cleared_lines):
            new_board.insert(0, [0] * TetrisApp.BOARD_WIDTH)
        self.board = new_board
    def freeze_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_piece_y + y][self.current_piece_x + x] = \
                        TetrisApp.COLORS.index(self.current_piece_color) + 1
        self.clear_line()
        self.new_piece()

    def update(self):
        # get current time
        current_time = pygame.time.get_ticks()
        if current_time - self.drop_time > self.drop_speed:
            if not self.move (0, 1):
                self.freeze_piece()

            self.drop_time = current_time

    def run(self):
        """ Main game loop. """
        while not self.game_over:
            self.handle_events()
            self.draw()
            self.update()
            self.clock.tick(60)  # Limit to 60 FPS


def main():
    app = TetrisApp()
    app.run()


if __name__ == "__main__":
    main()
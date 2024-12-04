import pygame
import random
import time
from src.models import GameModel
from src.views import GameView

class GameController:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Animal Shooter")
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.start_time = time.time()
        self.running = True
        self.showing_menu = True
        self.showing_end_screen = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.showing_menu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # Start game
                        self.showing_menu = False
                    elif event.key == pygame.K_q:  # Quit game
                        self.running = False

            elif self.showing_end_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart game
                        self.reset_game()
                    elif event.key == pygame.K_q:  # Quit game
                        self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and not self.showing_end_screen:
                if self.view.animal_rect.collidepoint(event.pos):
                    pygame.mixer.Sound("assets/click.wav").play()
                    self.model.score += 10
                    self.view.animal_rect.topleft = (random.randint(0, 750), random.randint(0, 550))

    def update(self):
        if not self.showing_menu and not self.showing_end_screen:
            elapsed_time = int(time.time() - self.start_time)
            self.model.timer = max(30 - elapsed_time, 0)
            if self.model.timer == 0:
                self.end_game()

    def reset_game(self):
        self.model.score = 0
        self.model.timer = 30
        self.start_time = time.time()
        self.showing_end_screen = False

    def end_game(self):
        self.showing_end_screen = True
        if self.model.score > self.model.high_score:
            self.model.high_score = self.model.score
            self.model.save_high_score()

    def run(self):
        while self.running:
            self.handle_events()
            if self.showing_menu:
                self.view.draw_menu()
            elif self.showing_end_screen:
                self.view.draw_end_screen(self.model.score, self.model.high_score)
            else:
                self.update()
                self.view.draw(self.model.score, self.model.timer, self.model.high_score)
            self.clock.tick(30)



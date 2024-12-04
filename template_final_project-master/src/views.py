import pygame

class GameView:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)
        self.background = pygame.image.load("assets/background.jpg")
        self.animal_image = pygame.image.load("assets/animal.png")
        self.animal_rect = self.animal_image.get_rect()

    def draw_menu(self):
        self.screen.fill((240, 230, 250))  
        black_color = (0, 0, 0)

        title_text = self.large_font.render("Animal Shooter", True, black_color)
        start_text = self.font.render("Press S to Start", True, black_color)
        quit_text = self.font.render("Press Q to Quit", True, black_color)

        self.screen.blit(title_text, (200, 200))
        self.screen.blit(start_text, (300, 300))
        self.screen.blit(quit_text, (300, 350))
        pygame.display.flip()

    def draw(self, score, timer, high_score):
        self.screen.blit(self.background, (0, 0))
        score_text = self.font.render(f"Score: {score}", True, (255,255,255))
        timer_text = self.font.render(f"Time: {timer}", True, (255,255,255))
        high_score_text = self.font.render(f"High Score: {high_score}", True, (255,255,255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(timer_text, (10, 50))
        self.screen.blit(high_score_text, (10, 90))
        self.screen.blit(self.animal_image, self.animal_rect)
        pygame.display.flip()

    def draw_end_screen(self, score, high_score):
        self.screen.fill((240, 230, 250))  
        black_color = (0, 0, 0)
        
        game_over_text = self.large_font.render("Game Over!", True, black_color)
        score_text = self.font.render(f"Your Score: {score}", True, black_color)
        high_score_text = self.font.render(f"High Score: {high_score}", True, black_color)
        replay_text = self.font.render("Press R to Play Again or Q to Quit", True, black_color)

        self.screen.blit(game_over_text, (250, 200))
        self.screen.blit(score_text, (300, 300))
        self.screen.blit(high_score_text, (300, 350))
        self.screen.blit(replay_text, (200, 450))
        pygame.display.flip()

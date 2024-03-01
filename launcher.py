import pygame
from tic_tac_toe import TicTacToe
from ultimate_tic_tac_toe import UltimateTicTacToe

class Launcher:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((474, 613))
        self.background_colour = (255, 255, 255)
        self.screen.fill(self.background_colour)
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.game = "Tic tac toe"
        self.game2 = "Ultimate tic tac toe"
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(self.game, True, (0, 0, 0))
        self.text2 = self.font.render(self.game2, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(237, 200))
        self.text_rect2 = self.text2.get_rect(center=(237, 400))
        
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.text_rect.collidepoint(event.pos):
                    self.screen.fill(self.background_colour)
                    self.tic_tac_toe = TicTacToe()
                    self.tic_tac_toe.run()
                if self.text_rect2.collidepoint(event.pos):
                    self.screen.fill(self.background_colour)
                    self.ultimate_tic_tac_toe = UltimateTicTacToe()
                    self.ultimate_tic_tac_toe.run()
    
    def display(self):
        self.screen.fill(self.background_colour)
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text2, self.text_rect2)
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.event_handler()
            self.display()
            self.clock.tick(60)
        pygame.quit()


game = Launcher()
game.run()
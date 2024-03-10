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
        self.text = self.font.render(self.game, True, (255,255,255), (0, 0, 0))
        self.text2 = self.font.render(self.game2, True, (255,255,255), (0, 0, 0))
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
                    self.tic_tac_toe.run_computer_vs_computer()
                if self.text_rect2.collidepoint(event.pos):
                    self.screen.fill(self.background_colour)
                    self.choice_ultimate()
                    
                    
    def choice_ultimate(self):
        self.screen.fill(self.background_colour)
        title = "You have chosen Ultimate Tic Tac Toe"
        question = "What do you want ?"
        answer1 = "1) Play with a friend"
        answer2 = "2) Play against the computer"
        back = "Back"
        
        self.title_text = self.font.render(title, True, (0, 0, 0))
        self.question_text = self.font.render(question, True, (0, 0, 0))
        self.answer1_text = self.font.render(answer1, True, (255,255,255), (0, 0, 0))
        self.answer2_text = self.font.render(answer2, True, (255,255,255), (0, 0, 0))
        self.back_text = self.font.render(back, True, (255,255,255), (0, 0, 0))
        
        self.title_rect = self.title_text.get_rect(center=(237, 100))
        self.question_rect = self.question_text.get_rect(center=(237, 150))
        self.answer1_rect = self.answer1_text.get_rect(center=(237, 300))
        self.answer2_rect = self.answer2_text.get_rect(center=(237, 400))
        self.back_rect = self.back_text.get_rect(center=(40, 40))
        
        while self.running:
            self.event_handler_ultimate()
            self.display_ultimate()
            self.clock.tick(60)
        
    def display_ultimate(self):
        self.screen.fill(self.background_colour)
        self.screen.blit(self.title_text, self.title_rect)
        self.screen.blit(self.question_text, self.question_rect)
        self.screen.blit(self.answer1_text, self.answer1_rect)
        self.screen.blit(self.answer2_text, self.answer2_rect)
        self.screen.blit(self.back_text, self.back_rect)
        pygame.display.flip()
        
    def event_handler_ultimate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.answer1_rect.collidepoint(event.pos):
                    self.screen.fill(self.background_colour)
                    self.ultimate_tic_tac_toe = UltimateTicTacToe()
                    self.ultimate_tic_tac_toe.run_without_computer()
                if self.answer2_rect.collidepoint(event.pos):
                    self.screen.fill(self.background_colour)
                    self.ultimate_tic_tac_toe = UltimateTicTacToe()
                    self.ultimate_tic_tac_toe.run_with_computer()
                if self.back_rect.collidepoint(event.pos):
                    self.screen.fill(self.background_colour)
                    self.run()
    
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
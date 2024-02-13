import pygame

class TicTacToe:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((474, 613))
        self.background_colour = (255, 255, 255)
        self.screen.fill(self.background_colour)
        self.background = pygame.image.load("OIP.jpeg")
        self.rect = self.background.get_rect(topleft=(0, 0))

        self.game_state = [['_'] * 3 for _ in range(3)]

        self.cross = pygame.image.load("cross.png")
        self.cross = pygame.transform.scale(self.cross, (150, 150))

        self.circle = pygame.image.load("circle.png")
        self.circle = pygame.transform.scale(self.circle, (150, 150))
        
        self.horiz_bar = pygame.image.load("horiz_bar.png")
        self.horiz_bar = pygame.transform.scale(self.horiz_bar, (474, 200))
        
        self.vert_bar = pygame.image.load("vert_bar.png")
        self.vert_bar = pygame.transform.scale(self.vert_bar, (200, 474))
        
        self.diag_right_bar = pygame.image.load("diag_right_bar.png")
        self.diag_right_bar = pygame.transform.scale(self.diag_right_bar, (474, 474))
        
        self.diag_left_bar = pygame.image.load("diag_left_bar.png")
        self.diag_left_bar = pygame.transform.scale(self.diag_left_bar, (474, 474))

        self.cell_rects = [
            pygame.Rect(0, 154, 150, 150),
            pygame.Rect(160, 154, 150, 150),
            pygame.Rect(320, 154, 150, 150),
            pygame.Rect(0, 309, 150, 150),
            pygame.Rect(160, 309, 150, 150),
            pygame.Rect(320, 309, 150, 150),
            pygame.Rect(0, 464, 150, 150),
            pygame.Rect(160, 464, 150, 150),
            pygame.Rect(320, 464, 150, 150)
        ]
        
        self.winning_conditions = {
            ((0, 0), (0, 1), (0, 2)): "horiz_bar1",
            ((1, 0), (1, 1), (1, 2)): "horiz_bar2",
            ((2, 0), (2, 1), (2, 2)): "horiz_bar3",
            ((0, 0), (1, 0), (2, 0)): "vert_bar1",
            ((0, 1), (1, 1), (2, 1)): "vert_bar2",
            ((0, 2), (1, 2), (2, 2)): "vert_bar3",
            ((0, 0), (1, 1), (2, 2)): "diag_left",
            ((0, 2), (1, 1), (2, 0)): "diag_right"
        }
        
        self.winning_bar = "empty"
        
        self.complete_bar_pos = None

        self.running = True
        self.turn = 0

    def display(self):
        self.screen.blit(self.background, self.rect.topleft)

        for i, rect in enumerate(self.cell_rects):
            x, y = rect.topleft
            if self.game_state[i // 3][i % 3] == 'X':
                self.screen.blit(self.cross, (x, y))
            elif self.game_state[i // 3][i % 3] == 'O':
                self.screen.blit(self.circle, (x, y))
                
        if self.complete_bar_pos is not None:
            self.display_complete_bar()

        pygame.display.flip()
        
    def display_complete_bar(self):
        if self.winning_bar != "empty":
            if self.winning_bar == "horiz_bar1" :
                self.screen.blit(self.horiz_bar, (0, 130))
            elif self.winning_bar == "horiz_bar2" :
                self.screen.blit(self.horiz_bar, (0, 290))
            elif self.winning_bar == "horiz_bar3" :
                self.screen.blit(self.horiz_bar, (0, 440))
            elif self.winning_bar == "vert_bar1" :
                self.screen.blit(self.vert_bar, (-20, 150))
            elif self.winning_bar == "vert_bar2" :
                self.screen.blit(self.vert_bar, (140, 150))
            elif self.winning_bar == "vert_bar3" :
                self.screen.blit(self.vert_bar, (290, 150))
            elif self.winning_bar == "diag_left" :
                self.screen.blit(self.diag_left_bar, (0, 150))
            elif self.winning_bar == "diag_right" :
                self.screen.blit(self.diag_right_bar, (0, 150))

    
    def display_result(self, result):
        phrase = "Victory for " + result if result != "Draw" else "Draw"
        
        pygame.time.wait(2000)
        self.screen.fill(self.background_colour)
        
        font = pygame.font.Font(None, 36)
        text = font.render(phrase, True, (0, 0, 0))
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, rect.topleft)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.turn == 0:
                    self.on_mouse_down()

    def on_mouse_down(self):
        x, y = pygame.mouse.get_pos()
        for i, rect in enumerate(self.cell_rects):
            if rect.collidepoint(x, y) and self.game_state[i // 3][i % 3] == '_':
                self.make_move(i)
                self.make_computer_move()
                return  

    def make_move(self, position):
        symbol = 'O' if self.turn == 1 else 'X'
        self.game_state[position // 3][position % 3] = symbol
        self.turn = (self.turn + 1) % 2
        self.display_game_state()
        

    def make_computer_move(self):
        best_score = float('-inf')
        best_action = None

        for i in range(9):
            if self.game_state[i // 3][i % 3] == '_':
                self.game_state[i // 3][i % 3] = 'O'
                score = self.minimax(False)
                self.game_state[i // 3][i % 3] = '_'

                if score > best_score:
                    best_score = score
                    best_action = i

        if best_action is not None:
            self.make_move(best_action)


    def evaluate(self):
        result = self.check_victory()
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        elif result == 'Draw':
            return 0
        else:
            return None

    
    def minimax(self, is_maximizing):
        score = self.evaluate()

        if score is not None:
            return score

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if self.game_state[i // 3][i % 3] == '_':
                    self.game_state[i // 3][i % 3] = 'O'
                    best_score = max(best_score, self.minimax(False))
                    self.game_state[i // 3][i % 3] = '_'
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.game_state[i // 3][i % 3] == '_':
                    self.game_state[i // 3][i % 3] = 'X'
                    best_score = min(best_score, self.minimax(True))
                    self.game_state[i // 3][i % 3] = '_'
            return best_score

    def check_victory(self):
        for positions, bar_name in self.winning_conditions.items():
            if all(self.game_state[i][j] == 'O' for i, j in positions):
                self.winning_bar = bar_name
                self.complete_bar_pos=(1,1)
                return 'O'
            elif all(self.game_state[i][j] == 'X' for i, j in positions):
                self.winning_bar = bar_name
                self.complete_bar_pos=(1,1)
                return 'X'

        if all(self.game_state[i][j] != '_' for i in range(3) for j in range(3)):
            return "Draw"

        self.winning_bar = "empty"
        return '_'

    
    def display_game_state(self):
        for i in range(3):
            print(self.game_state[i])
            
        print()
            

    def run(self):
        while self.running:
            self.events()
            result = self.check_victory()
            self.display()

            
            if result != "_":
                if result == "Draw":
                    print("Draw")
                else:
                    print("Victory for", result)
                self.display_result(result)
                
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            waiting = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            waiting = False
                
                self.__init__()
                
        pygame.quit()


game = TicTacToe()
game.run()

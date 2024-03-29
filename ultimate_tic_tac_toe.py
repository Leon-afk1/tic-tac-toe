import pygame


class UltimateTicTacToe:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((474, 613))
        self.background_colour = (255, 255, 255)
        self.screen.fill(self.background_colour)
        self.background = pygame.image.load("ultimate-tic-tac-toe.webp")
        self.background = pygame.transform.scale(self.background, (474, 613))
        self.rect = self.background.get_rect(topleft=(0, 0))
        
        self.computer = False

        self.game_state = [['_'] * 3 for _ in range(3)]
        
        self.game_state_cell1 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell2 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell3 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell4 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell5 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell6 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell7 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell8 = [['_'] * 3 for _ in range(3)]
        self.game_state_cell9 = [['_'] * 3 for _ in range(3)]
        
        self.game_small_boards_state = [self.game_state_cell1, self.game_state_cell2, self.game_state_cell3, self.game_state_cell4, self.game_state_cell5, self.game_state_cell6, self.game_state_cell7, self.game_state_cell8, self.game_state_cell9]

        self.cross = pygame.image.load("cross.png")
        self.cross = pygame.transform.scale(self.cross, (150, 200))
        
        self.small_cross = pygame.transform.scale(self.cross, (35, 40))

        self.circle = pygame.image.load("circle.png")
        self.circle = pygame.transform.scale(self.circle, (150, 200))

        self.small_circle = pygame.transform.scale(self.circle, (35, 40))
        
        self.horiz_bar = pygame.image.load("horiz_bar.png")
        self.horiz_bar = pygame.transform.scale(self.horiz_bar, (474, 200))
        
        self.small_horiz_bar = pygame.transform.scale(self.horiz_bar, (150, 40))
        
        self.vert_bar = pygame.image.load("vert_bar.png")
        self.vert_bar = pygame.transform.scale(self.vert_bar, (200, 570))
        
        self.diag_right_bar = pygame.image.load("diag_right_bar.png")
        self.diag_right_bar = pygame.transform.scale(self.diag_right_bar, (474, 600))
        
        self.diag_left_bar = pygame.image.load("diag_left_bar.png")
        self.diag_left_bar = pygame.transform.scale(self.diag_left_bar, (474, 600))

        self.cell_rects = [
            pygame.Rect(0, 0, 150, 200),
            pygame.Rect(160, 0, 150, 200),
            pygame.Rect(320, 0, 150, 200),
            pygame.Rect(0, 210, 150, 200),
            pygame.Rect(160, 210, 150, 200),
            pygame.Rect(320, 210, 150, 200),
            pygame.Rect(0, 413, 150, 200),
            pygame.Rect(160, 413, 150, 200),
            pygame.Rect(320, 413, 150, 200)
        ]
        
        self.cell1_rects = [
            pygame.Rect(39, 52, 35, 55),
            pygame.Rect(77, 52, 35, 55),
            pygame.Rect(117, 52, 35, 55),
            pygame.Rect(39, 102, 35, 55),
            pygame.Rect(77, 102, 35, 55),
            pygame.Rect(117, 102, 35, 55),
            pygame.Rect(39, 157, 35, 55),
            pygame.Rect(77, 157, 35, 55),
            pygame.Rect(117, 157, 35, 55)
        ]
        
        self.cell2_rects = [
            pygame.Rect(182, 52, 35, 55),
            pygame.Rect(220, 52, 35, 55),
            pygame.Rect(260, 52, 35, 55),
            pygame.Rect(182, 102, 35, 55),
            pygame.Rect(220, 102, 35, 55),
            pygame.Rect(260, 102, 35, 55),
            pygame.Rect(182, 157, 35, 55),
            pygame.Rect(220, 157, 35, 55),
            pygame.Rect(260, 157, 35, 55)
        ]
        
        self.cell3_rects = [
            pygame.Rect(322, 52, 35, 55),
            pygame.Rect(360, 52, 35, 55),
            pygame.Rect(400, 52, 35, 55),
            pygame.Rect(322, 102, 35, 55),
            pygame.Rect(360, 102, 35, 55),
            pygame.Rect(400, 102, 35, 55),
            pygame.Rect(322, 157, 35, 55),
            pygame.Rect(360, 157, 35, 55),
            pygame.Rect(400, 157, 35, 55)
        ]
        
        self.cell4_rects = [
            pygame.Rect(39, 235, 35, 55),
            pygame.Rect(77, 235, 35, 55),
            pygame.Rect(117, 235, 35, 55),
            pygame.Rect(39, 285, 35, 55),
            pygame.Rect(77, 285, 35, 55),
            pygame.Rect(117, 285, 35, 55),
            pygame.Rect(39, 340, 35, 55),
            pygame.Rect(77, 340, 35, 55),
            pygame.Rect(117, 340, 35, 55)
        ]
        
        self.cell5_rects = [
            pygame.Rect(182, 235, 35, 55),
            pygame.Rect(220, 235, 35, 55),
            pygame.Rect(260, 235, 35, 55),
            pygame.Rect(182, 285, 35, 55),
            pygame.Rect(220, 285, 35, 55),
            pygame.Rect(260, 285, 35, 55),
            pygame.Rect(182, 340, 35, 55),
            pygame.Rect(220, 340, 35, 55),
            pygame.Rect(260, 340, 35, 55)
        ]
        
        self.cell6_rects = [
            pygame.Rect(322, 235, 35, 55),
            pygame.Rect(360, 235, 35, 55),
            pygame.Rect(400, 235, 35, 55),
            pygame.Rect(322, 285, 35, 55),
            pygame.Rect(360, 285, 35, 55),
            pygame.Rect(400, 285, 35, 55),
            pygame.Rect(322, 340, 35, 55),
            pygame.Rect(360, 340, 35, 55),
            pygame.Rect(400, 340, 35, 55)
        ]
        
        self.cell7_rects = [
            pygame.Rect(39, 422, 35, 55),
            pygame.Rect(77, 422, 35, 55),
            pygame.Rect(117, 422, 35, 55),
            pygame.Rect(39, 472, 35, 55),
            pygame.Rect(77, 472, 35, 55),
            pygame.Rect(117, 472, 35, 55),
            pygame.Rect(39, 527, 35, 55),
            pygame.Rect(77, 527, 35, 55),
            pygame.Rect(117, 527, 35, 55)
        ]
        
        self.cell8_rects = [
            pygame.Rect(182, 422, 35, 55),
            pygame.Rect(220, 422, 35, 55),
            pygame.Rect(260, 422, 35, 55),
            pygame.Rect(182, 472, 35, 55),
            pygame.Rect(220, 472, 35, 55),
            pygame.Rect(260, 472, 35, 55),
            pygame.Rect(182, 527, 35, 55),
            pygame.Rect(220, 527, 35, 55),
            pygame.Rect(260, 527, 35, 55)
        ]
        
        self.cell9_rects = [
            pygame.Rect(322, 422, 35, 55),
            pygame.Rect(360, 422, 35, 55),
            pygame.Rect(400, 422, 35, 55),
            pygame.Rect(322, 472, 35, 55),
            pygame.Rect(360, 472, 35, 55),
            pygame.Rect(400, 472, 35, 55),
            pygame.Rect(322, 527, 35, 55),
            pygame.Rect(360, 527, 35, 55),
            pygame.Rect(400, 527, 35, 55)
        ]
        
        self.cells_rects = [self.cell1_rects, self.cell2_rects, self.cell3_rects, self.cell4_rects, self.cell5_rects, self.cell6_rects, self.cell7_rects, self.cell8_rects, self.cell9_rects]
        
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
        
        self.winning_condition_small_board = {
            ((0,0), (0,1), (0,2)),
            ((1,0), (1,1), (1,2)),
            ((2,0), (2,1), (2,2)),
            ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)),
            ((0,2), (1,2), (2,2)),
            ((0,0), (1,1), (2,2)),
            ((0,2), (1,1), (2,0))
        }
        
        self.winning_bar = "empty"
        
        self.complete_bar_pos = None

        self.running = True
        self.turn = 0
        
        self.choice_case = -1
        
    def display(self):
        self.screen.blit(self.background, self.rect.topleft)
        
        for i, rect in enumerate(self.cell_rects):
            for j, rect2 in enumerate(self.cells_rects[i]):
                x, y = rect2.topleft
                if self.game_small_boards_state[i][j // 3][j % 3] == 'X':
                    self.screen.blit(self.small_cross, (x, y))
                elif self.game_small_boards_state[i][j // 3][j % 3] == 'O':
                    self.screen.blit(self.small_circle, (x, y))

        for i, rect in enumerate(self.cell_rects):
            x, y = rect.topleft
            if self.game_state[i // 3][i % 3] == 'X':
                self.screen.blit(self.cross, (x, y))
            elif self.game_state[i // 3][i % 3] == 'O':
                self.screen.blit(self.circle, (x, y))
            elif self.game_state[i // 3][i % 3] == "Draw":
                self.screen.blit(self.cross, (x, y))
                self.screen.blit(self.circle, (x, y))
                
        if self.complete_bar_pos is not None:
            self.display_complete_bar()

        pygame.display.flip()
        
    def display_complete_bar(self):
        if self.winning_bar != "empty":
            if self.winning_bar == "horiz_bar1" :
                self.screen.blit(self.horiz_bar, (0, 45))
            elif self.winning_bar == "horiz_bar2" :
                self.screen.blit(self.horiz_bar, (0, 210))
            elif self.winning_bar == "horiz_bar3" :
                self.screen.blit(self.horiz_bar, (0, 390))
            elif self.winning_bar == "vert_bar1" :
                self.screen.blit(self.vert_bar, (-5, 45))
            elif self.winning_bar == "vert_bar2" :
                self.screen.blit(self.vert_bar, (140, 45))
            elif self.winning_bar == "vert_bar3" :
                self.screen.blit(self.vert_bar, (280, 45))
            elif self.winning_bar == "diag_left" :
                self.screen.blit(self.diag_left_bar, (0, 30))
            elif self.winning_bar == "diag_right" :
                self.screen.blit(self.diag_right_bar, (0, 30))

    
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
                if self.computer:
                    if self.turn == 0:
                        self.on_mouse_down()
                else:
                    self.on_mouse_down()

    def on_mouse_down(self):
        x, y = pygame.mouse.get_pos()
        print(x, y)
        
        for i, rect in enumerate(self.cell_rects):
            if rect.collidepoint(x, y) and self.game_state[i // 3][i % 3] == '_' and self.choice_case == -1:
                for j, rect2 in enumerate(self.cells_rects[i]):
                    if rect2.collidepoint(x, y) and self.game_small_boards_state[i][j // 3][j % 3] == '_':
                        self.make_move(j, i)
                        self.check_victory_small_board(self.game_small_boards_state[i])
                        if self.game_state[j // 3][j % 3] != '_':
                            self.choice_case = -1
                        else:
                            self.choice_case = j
                            
                        if self.computer:
                            if self.check_victory() == "_":
                                self.display()
                                self.make_computer_move()
                        break
                break
            elif rect.collidepoint(x, y) and self.game_state[i // 3][i % 3] == '_' and self.choice_case == i:
                for j, rect2 in enumerate(self.cells_rects[i]):
                    if rect2.collidepoint(x, y) and self.game_small_boards_state[i][j // 3][j % 3] == '_':
                        self.make_move(j, i)
                        if self.game_state[j // 3][j % 3] != '_':
                            self.choice_case = -1
                        else:
                            self.choice_case = j
                            
                        if self.computer:
                            if self.check_victory() == "_":
                                self.display()
                                self.make_computer_move()
                        break
                break
        print(self.choice_case)        

    def make_move(self, position, big_board):
        symbol = 'O' if self.turn == 1 else 'X'
        self.game_small_boards_state[big_board][position // 3][position % 3] = symbol
        result = self.check_victory_small_board(self.game_small_boards_state[big_board])
        if result != '_':
            if result != "Draw":
                self.game_state[big_board // 3][big_board % 3] = symbol
            else:
                self.game_state[big_board // 3][big_board % 3] = "Draw"
        self.turn = (self.turn + 1) % 2
        self.display_game_state()
        
    def make_computer_move(self):
        best_score, best_move = self.minimax(self.game_small_boards_state[self.choice_case], True, self.choice_case)

        if best_move is not None:
            self.make_move(best_move[1], self.choice_case)

        if self.game_state[best_move[1] // 3][best_move[1] % 3] != '_':
            self.choice_case = -1
        else:
            self.choice_case = best_move[1] // 3 * 3 + best_move[1] % 3


    def evaluate(self, small_board):
        result = self.check_victory_small_board(small_board)
        if result == 'O':
            return 1
        elif result == 'X':
            return -1
        elif result == 'Draw':
            return 0
        else:
            return None

    def minimax(self, small_board, is_maximizing, current_small_board_index):
        score = self.evaluate(small_board)

        if score is not None:
            return score

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if small_board[i][j] == '_':
                        small_board[i][j] = 'O'
                        current_score = self.minimax(small_board, False, current_small_board_index)
                        small_board[i][j] = '_'

                        if isinstance(current_score, tuple):
                            current_score = current_score[0]

                        if current_score > best_score:
                            best_score = current_score
                            best_move = (i, j)

            if best_score == float('-inf'):
                return None
            return best_score, best_move

        else:
            best_score = float('inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if small_board[i][j] == '_':
                        small_board[i][j] = 'X'
                        current_score = self.minimax(small_board, True, current_small_board_index)
                        small_board[i][j] = '_'

                        if isinstance(current_score, tuple):
                            current_score = current_score[0]

                        if current_score < best_score:
                            best_score = current_score
                            best_move = (i, j)

            if best_score == float('inf'):
                return None
            return best_score, best_move


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

    def check_victory_small_board(self, small_board):
        for positions in self.winning_condition_small_board:
            if all(small_board[i][j] == 'O' for i, j in positions):
                return 'O'
            elif all(small_board[i][j] == 'X' for i, j in positions):
                return 'X'
            
        if all(small_board[i][j] != '_' for i in range(3) for j in range(3)):
            return "Draw"
        
        return '_'

    def display_game_state(self):
        for i in range(3):
            print(self.game_state[i])
            
        print()
        
    def run_without_computer(self):
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
    
    def run_with_computer(self):
        self.computer = True
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

                
    
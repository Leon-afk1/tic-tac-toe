import pygame
import numpy as np
import tensorflow as tf
import random


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001
GAMMA = 0.9

class TicTacToe:
    def __init__(self):
        pygame.font.init()
        # Set the background
        self.screen = pygame.display.set_mode((474, 613))
        self.background_colour = (255, 255, 255)
        self.screen.fill(self.background_colour)
        
        # Load images
        self.background = pygame.image.load("OIP.jpeg")
        self.rect = self.background.get_rect(topleft=(0, 0))
        
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
        
        # Set the cells rects
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
        
        # Set the game state
        self.game_state = [['_'] * 3 for _ in range(3)]
        
        # Set winning condition
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
        self.turn = random.choice([0, 1])
        
        self.prev_game_state = [['_' for _ in range(3)] for _ in range(3)]
        self.prev_move = None
        
        self.computer=0
        
        self.model = self.build_q_model()
        
        self.memory = []

    def build_q_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(3, 3)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(9, activation='linear', kernel_initializer='random_uniform')  
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LR), loss='mse')
        self.model = model  # Store the model in class attribute
        return model

    def save_model(self):
        self.model.save('tic_tac_toe_model.keras')


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
        pygame.time.wait(500)
        self.screen.fill(self.background_colour)
        font = pygame.font.Font(None, 36)
        text = font.render(phrase, True, (0, 0, 0))
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, rect.topleft)
        pygame.display.flip()
        # Wait for user input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.computer>0:
                    self.model.save('tic_tac_toe_model')
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.computer==0: # Human vs Human
                    x, y = pygame.mouse.get_pos()
                    for i, rect in enumerate(self.cell_rects):
                        if rect.collidepoint(x, y) and self.game_state[i // 3][i % 3] == '_':
                            self.make_move(i)
                            return
                if self.computer==1: # Human vs Computer with miniMax algorithm
                    if self.turn == 0:
                        x, y = pygame.mouse.get_pos()
                        for i, rect in enumerate(self.cell_rects):
                            if rect.collidepoint(x, y) and self.game_state[i // 3][i % 3] == '_':
                                self.make_move(i)
                                
                        if self.check_victory() == '_':
                            self.make_computer_move_min_max()
                        return
                if self.computer==2: # Human vs Computer with neural network
                    if self.turn == 0:
                        x, y = pygame.mouse.get_pos()
                        for i, rect in enumerate(self.cell_rects):
                            if rect.collidepoint(x, y) and self.game_state[i // 3][i % 3] == '_':
                                self.make_move(i)
                                
                        if self.check_victory() == '_':
                            self.make_computer_move()
                            reward = self.evaluate()
                            next_state = self.convert_state(self.game_state)
                            state = self.convert_state(self.prev_game_state)
                            
                            self.remember(state, self.prev_move, reward, next_state, False)
                            
                            self.replay()
                        return
    
    def make_move(self, position):
        symbol = 'O' if self.turn == 1 else 'X'
        self.game_state[position // 3][position % 3] = symbol
        self.turn = (self.turn + 1) % 2
        
    def make_computer_move(self):
        if np.random.rand() < 0.1:
            available_moves = [i for i in range(9) if self.game_state[i // 3][i % 3] == '_']
            selected_move = np.random.choice(available_moves)
        else:
            q_values = self.model.predict(np.array([self.convert_state(self.game_state)]))[0]
            available_moves = [i for i in range(9) if self.game_state[i // 3][i % 3] == '_']
            selected_move = available_moves[np.argmax([q_values[i] for i in available_moves])]

        self.make_move(selected_move)
        
    def make_computer_move_min_max(self):
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
        
    # Convertir l'état du jeu en format adapté pour le modèle            
    def convert_state(self, state):
        return np.array([[self.convert_symbol(s) for s in row] for row in state], dtype='float32')
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
        if len(self.memory) > MAX_MEMORY:
            del self.memory[0]
            
    def replay(self):
        if len(self.memory) < BATCH_SIZE:
            return

        minibatch = np.random.choice(self.memory, BATCH_SIZE, replace=False)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + GAMMA * np.max(self.model.predict(np.array([next_state]))[0])

            target_f = self.model.predict(np.array([state]))
            target_f[0][action] = target

            self.model.fit(np.array([state]), target_f, epochs=1, verbose=0)
            
    def convert_symbol(self, symbol):
        if symbol == 'X':
            return 1.0
        elif symbol == 'O':
            return -1.0
        else:
            return 0.0

    def evaluate(self):
        result = self.check_victory()
        if result == 'X':
            return  1
        elif result == 'O':
            return -1 
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
        
    def run(self,computer_val):
        self.computer=computer_val
        if self.computer==0:
            while self.running: # Human vs Human
                self.events()
                result = self.check_victory()
                self.display()

                if result != "_":
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
        
        if self.computer==1: # Human vs Computer with miniMax algorithm
            while self.running:
                if self.turn == 1:
                    self.make_computer_move_min_max()
                self.events()
                result = self.check_victory()
                self.display()

                if result != "_":
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
                    
        if self.computer==2: # Human vs Computer with neural network
            win = 0
            lose = 0
            draw = 0
            while self.running:
                if self.turn == 1:
                    self.make_computer_move()
                    reward = self.evaluate()
                    next_state = self.convert_state(self.game_state)
                    state = self.convert_state(self.prev_game_state)
                    
                    self.remember(state, self.prev_move, reward, next_state, False)
                    
                    self.replay()
                self.events()
                result = self.check_victory()
                self.display()

                if result != "_":
                    self.display_result(result)
                    
                    if result == "X":
                        lose += 1
                    elif result == "O":
                        win += 1
                    else:
                        draw += 1
                        
                    print(f"Win: {win}, Lose: {lose}, Draw: {draw}")

                    self.model.save('tic_tac_toe_model')

                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.running = False
                                waiting = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                waiting = False

                    self.__init__()
                
        if self.computer==3: #Computer against Computer
            win = 0
            lose = 0
            draw = 0
            while self.running:
                if pygame.event.get(pygame.QUIT):
                    self.running = False
                if self.turn == 1:
                    self.make_computer_move()
                    reward = self.evaluate()
                    next_state = self.convert_state(self.game_state)
                    state = self.convert_state(self.prev_game_state)
                    
                    self.remember(state, self.prev_move, reward, next_state, False)
                    
                    self.replay()
                else:
                    self.make_computer_move_min_max()
                    reward = self.evaluate()
                    next_state = self.convert_state(self.game_state)
                    state = self.convert_state(self.prev_game_state)
                    
                    self.remember(state, self.prev_move, reward, next_state, False)
                    
                    self.replay()
                result = self.check_victory()
                self.display()

                if result != "_":
                    # self.display_result(result)
                    
                    if result == "X":
                        lose += 1
                    elif result == "O":
                        win += 1
                    else:
                        draw += 1
                        
                    print(f"Win: {win}, Lose: {lose}, Draw: {draw}")

                    self.save_model()

                    self.__init__()
            
            
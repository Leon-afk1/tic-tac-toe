import pygame
import heapq

class TicTacToe:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((474, 613))
        self.background_colour = (255, 255, 255)
        self.screen.fill(self.background_colour)
        self.background = pygame.image.load("OIP.jpeg")
        self.rect = self.background.get_rect(topleft=(0, 0))

        self.etat_jeu = [['_'] * 3 for _ in range(3)]

        self.croix = pygame.image.load("croix.png")
        self.croix = pygame.transform.scale(self.croix, (150, 150))

        self.cercle = pygame.image.load("cercle.png")
        self.cercle = pygame.transform.scale(self.cercle, (150, 150))

        self.cases_rect = [
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

        self.running = True
        self.tour = 0

    def afficher(self):
        self.screen.blit(self.background, self.rect.topleft)

        for i, rect in enumerate(self.cases_rect):
            x, y = rect.topleft
            if self.etat_jeu[i // 3][i % 3] == 'X':
                self.screen.blit(self.croix, (x, y))
            elif self.etat_jeu[i // 3][i % 3] == 'O':
                self.screen.blit(self.cercle, (x, y))

        pygame.display.flip()
    
    def afficher_resultat(self, resultat):
        phrase = "Victoire de " + resultat if resultat != "Match nul" else "Match nul"
        pygame.time.wait(2000)
        self.screen.fill(self.background_colour)
        
        font = pygame.font.Font(None, 36)
        texte = font.render(phrase, True, (0, 0, 0))
        rect = texte.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(texte, rect.topleft)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.tour == 0:
                    self.on_mouse_down()

    def on_mouse_down(self):
        x, y = pygame.mouse.get_pos()
        for i, rect in enumerate(self.cases_rect):
            if rect.collidepoint(x, y) and self.etat_jeu[i // 3][i % 3] == '_':
                self.jouer_coup(i)
                self.jouer_coup_ordinateur()
                return  

    def jouer_coup(self, position):
        interieur = 'O' if self.tour == 1 else 'X'
        self.etat_jeu[position // 3][position % 3] = interieur
        self.tour = (self.tour + 1) % 2
        self.afficher_etat_jeu()
        

    def jouer_coup_ordinateur(self):
        meilleur_score = float('-inf')
        meilleur_action = None

        for i in range(9):
            if self.etat_jeu[i // 3][i % 3] == '_':
                self.etat_jeu[i // 3][i % 3] = 'O'
                score = self.minimax(False)
                self.etat_jeu[i // 3][i % 3] = '_'

                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_action = i

        if meilleur_action is not None:
            self.jouer_coup(meilleur_action)


    def evaluer(self):
        resultat = self.check_victoire()
        if resultat == 'X':
            return -1
        elif resultat == 'O':
            return 1
        elif resultat == 'Match nul':
            return 0
        else:
            return None

    
    def minimax(self, est_maximisant):
        score = self.evaluer()

        if score is not None:
            return score

        if est_maximisant:
            meilleur_score = float('-inf')
            for i in range(9):
                if self.etat_jeu[i // 3][i % 3] == '_':
                    self.etat_jeu[i // 3][i % 3] = 'O'
                    meilleur_score = max(meilleur_score, self.minimax(False))
                    self.etat_jeu[i // 3][i % 3] = '_'
            return meilleur_score
        else:
            meilleur_score = float('inf')
            for i in range(9):
                if self.etat_jeu[i // 3][i % 3] == '_':
                    self.etat_jeu[i // 3][i % 3] = 'X'
                    meilleur_score = min(meilleur_score, self.minimax(True))
                    self.etat_jeu[i // 3][i % 3] = '_'
            return meilleur_score

    def check_victoire(self):
        for i in range(3):
            if self.etat_jeu[i][0] == self.etat_jeu[i][1] == self.etat_jeu[i][2] != '_':
                return self.etat_jeu[i][0]
            if self.etat_jeu[0][i] == self.etat_jeu[1][i] == self.etat_jeu[2][i] != '_':
                return self.etat_jeu[0][i]

        if self.etat_jeu[0][0] == self.etat_jeu[1][1] == self.etat_jeu[2][2] != '_':
            return self.etat_jeu[0][0]
        if self.etat_jeu[0][2] == self.etat_jeu[1][1] == self.etat_jeu[2][0] != '_':
            return self.etat_jeu[0][2]

        if all(self.etat_jeu[i][j] != '_' for i in range(3) for j in range(3)):
            return "Match nul"

        return '_'
    
    def afficher_etat_jeu(self):
        for i in range(3):
            print(self.etat_jeu[i])
            
        print()
            

    def run(self):
        while self.running:
            self.events()
            self.afficher()

            resultat = self.check_victoire()
            if resultat != "_":
                if resultat == "Match nul":
                    print("Match nul")
                else:
                    print("Victoire de", resultat)
                self.afficher_resultat(resultat)
                
                attente = True
                while attente:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            attente = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            attente = False
                
                self.__init__()
                
        pygame.quit()


jeu = TicTacToe()
jeu.run()

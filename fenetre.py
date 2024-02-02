import pygame

class fenetre:
    def __init__(self):
        self.screen = pygame.display.set_mode((474,613))
        self.background_colour = (255,255,255)
        self.screen.fill(self.background_colour)
        self.background = pygame.image.load("OIP.jpeg")
        self.rect= self.background.get_rect(topleft=(0,0))
        
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()
        
        self.croix = pygame.image.load("croix.png")
        self.croix = pygame.transform.scale(self.croix, (150,150))
        self.croix_rect = self.croix.get_rect(topleft=(0,0))
        
        self.cercle = pygame.image.load("cercle.png")
        self.cercle = pygame.transform.scale(self.cercle, (150,150))
        self.cercle_rect = self.cercle.get_rect(topleft=(0,0))
        
        self.case1 = pygame.Rect(0,154,150,150)
        self.case1_interior = "null"
        self.case2 = pygame.Rect(160,154,150,150)
        self.case2_interior = "null"
        self.case3 = pygame.Rect(320,154,150,150)
        self.case3_interior = "null"
        self.case4 = pygame.Rect(0,309,150,150)
        self.case4_interior = "null"
        self.case5 = pygame.Rect(160,309,150,150)
        self.case5_interior = "null"
        self.case6 = pygame.Rect(320,309,150,150)
        self.case6_interior = "null"
        self.case7 = pygame.Rect(0,464,150,150)
        self.case7_interior = "null"
        self.case8 = pygame.Rect(160,464,150,150)
        self.case8_interior = "null"
        self.case9 = pygame.Rect(320,464,150,150)
        self.case9_interior = "null"

        self.running = True
        
        self.tour = 0
        
    def afficher(self):
        self.screen.blit(self.background, self.rect.topleft)
        if self.case1_interior == "croix":
            self.screen.blit(self.croix, self.case1.topleft)
        if self.case1_interior == "cercle":
            self.screen.blit(self.cercle, self.case1.topleft)
        if self.case2_interior == "croix":
            self.screen.blit(self.croix, self.case2.topleft)
        if self.case2_interior == "cercle":
            self.screen.blit(self.cercle, self.case2.topleft)
        if self.case3_interior == "croix":
            self.screen.blit(self.croix, self.case3.topleft)
        if self.case3_interior == "cercle":
            self.screen.blit(self.cercle, self.case3.topleft)
        if self.case4_interior == "croix":
            self.screen.blit(self.croix, self.case4.topleft)
        if self.case4_interior == "cercle":
            self.screen.blit(self.cercle, self.case4.topleft)
        if self.case5_interior == "croix":
            self.screen.blit(self.croix, self.case5.topleft)
        if self.case5_interior == "cercle":
            self.screen.blit(self.cercle, self.case5.topleft)
        if self.case6_interior == "croix":
            self.screen.blit(self.croix, self.case6.topleft)
        if self.case6_interior == "cercle":
            self.screen.blit(self.cercle, self.case6.topleft)
        if self.case7_interior == "croix":
            self.screen.blit(self.croix, self.case7.topleft)
        if self.case7_interior == "cercle":
            self.screen.blit(self.cercle, self.case7.topleft)
        if self.case8_interior == "croix":
            self.screen.blit(self.croix, self.case8.topleft)
        if self.case8_interior == "cercle":
            self.screen.blit(self.cercle, self.case8.topleft)
        if self.case9_interior == "croix":
            self.screen.blit(self.croix, self.case9.topleft)
        if self.case9_interior == "cercle":
            self.screen.blit(self.cercle, self.case9.topleft)
        pygame.display.flip()
        
    def events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                    break
                case pygame.MOUSEBUTTONDOWN:
                    self.OnMouseDown()
        
    def OnMouseDown(self):
        (x,y) = pygame.mouse.get_pos()
        case = 150
        interieur = "null"
        # if (self.tour==1):
        if (self.tour==1):
            interieur = "cercle"
        else:
            interieur = "croix"
        
        if ((x>=0 and x<case) and (y>154 and y<154+case)):
            self.case1_interior = interieur
        if ((x>=160 and x<160+case) and (y>154 and y<154+case)):
            self.case2_interior = interieur
        if ((x>=320 and x<320+case) and (y>154 and y<154+case)):
            self.case3_interior = interieur
        if ((x>=0 and x<case) and (y>309 and y<309+case)):
            self.case4_interior = interieur
        if ((x>=160 and x<160+case) and (y>309 and y<309+case)):
            self.case5_interior = interieur
        if ((x>=320 and x<320+case) and (y>309 and y<309+case)):
            self.case6_interior = interieur
        if ((x>=0 and x<case) and (y>464 and y<464+case)):
            self.case7_interior = interieur
        if ((x>=160 and x<160+case) and (y>464 and y<464+case)):
            self.case8_interior = interieur
        if ((x>=320 and x<320+case) and (y>464 and y<464+case)):
            self.case9_interior = interieur
        
        self.tour = (self.tour+1)%2
    
    def ordinateur(self):
        if (self.tour==0):
            if (self.case1_interior == "null"):
                self.case1_interior = "cercle"
            elif (self.case2_interior == "null"):
                self.case2_interior = "cercle"
            elif (self.case3_interior == "null"):
                self.case3_interior = "cercle"
            elif (self.case4_interior == "null"):
                self.case4_interior = "cercle"
            elif (self.case5_interior == "null"):
                self.case5_interior = "cercle"
            elif (self.case6_interior == "null"):
                self.case6_interior = "cercle"
            elif (self.case7_interior == "null"):
                self.case7_interior = "cercle"
            elif (self.case8_interior == "null"):
                self.case8_interior = "cercle"
            elif (self.case9_interior == "null"):
                self.case9_interior = "cercle"
            self.tour = (self.tour+1)%2
        
    def check_victory(self):
        if (self.case1_interior == self.case2_interior and self.case2_interior == self.case3_interior and self.case1_interior != "null"):
            return self.case1_interior
        if (self.case4_interior == self.case5_interior and self.case5_interior == self.case6_interior and self.case4_interior != "null"):
            return self.case4_interior
        if (self.case7_interior == self.case8_interior and self.case8_interior == self.case9_interior and self.case7_interior != "null"):
            return self.case7_interior
        if (self.case1_interior == self.case4_interior and self.case4_interior == self.case7_interior and self.case1_interior != "null"):
            return self.case1_interior
        if (self.case2_interior == self.case5_interior and self.case5_interior == self.case8_interior and self.case2_interior != "null"):
            return self.case2_interior
        if (self.case3_interior == self.case6_interior and self.case6_interior == self.case9_interior and self.case3_interior != "null"):
            return self.case3_interior
        if (self.case1_interior == self.case5_interior and self.case5_interior == self.case9_interior and self.case1_interior != "null"):
            return self.case1_interior
        if (self.case3_interior == self.case5_interior and self.case5_interior == self.case7_interior and self.case3_interior != "null"):
            return self.case3_interior
        return "null"
    
    def run(self):
        while self.running:
            self.events()
            self.afficher()
            # self.ordinateur()
            if (self.check_victory() != "null"):
                print(self.check_victory())
                self.running = False
            
                    

    
fenetre = fenetre()

fenetre.run()

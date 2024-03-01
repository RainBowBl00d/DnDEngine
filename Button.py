import pygame
class button:
    def __init__(self, gameobject):
        self.gameobject = gameobject
        self.clicked = False

    def onClick(self, functions):
        if functions == None:
            print("No functions provided")
            return
        for function in functions:
            function()
        return

    def getClicking(self, functions):
        pos = pygame.mouse.get_pos()

        if self.gameobject.transform.rect.collidepoint(pos):
            if not self.clicked and pygame.mouse.get_pressed()[0]:
                self.clicked = True
                self.onClick(functions)
            else:
                self.clicked = False
        return

    def getClick(self, functions):
        pos = pygame.mouse.get_pos()

        if  self.gameobject.transform.rect.collidepoint(pos):
            if not self.clicked and pygame.mouse.get_pressed()[0]:
                self.clicked = True
                self.onClick(functions)
            elif self.clicked and not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        return

import pygame
import MouseInput
class button:
    def __init__(self, gameobject):
        self.gameobject = gameobject
        self.clicked = False

    def onClick(self, functions):
        if functions is None:
            print("No functions provided")
            return
        if callable(functions):
            functions()
        else:
            for function in functions:
                function()

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
            if not self.clicked and MouseInput.mouseInput.getButtonDown(pygame.BUTTON_LEFT):
                print("here")
                self.clicked = True
                self.onClick(functions)
        if self.clicked and MouseInput.mouseInput.getButtonUp(pygame.BUTTON_LEFT):
            self.clicked = False
        return

import MouseInput
import pygame
class dragnDrop():
    def __init__(self, gameobject):
        self.gameobject = gameobject
        self.file = None

    def hanleDrop(self, file):
        self.file = file

    def getFile(self):
        if self.file is not None:
            return self.file
        else:
            print("No file has been loaded")
    def reset(self):
        self.file = None
    def getDrop(self):
        if MouseInput.mouseInput.getButtonDown(0):
            if self.gameobject.transform.rect.collidepoint(MouseInput.mouseInput.mouse_position):
                file_path = pygame.filedialog.askopenfilename()
                if file_path:
                    self.hanleDrop(file_path)
    def update(self):
        if self.file is not None:
            self.getDrop()


import pygame
import MouseInput
import tkinter as tk
from tkinter import filedialog
class dragNDropField:
    def __init__(self, gameobject):
        self.gameobject = gameobject
        self.file_path = None
        self.image = None

    def getHover(self):
        if MouseInput.mouseInput.getButtonDown(pygame.BUTTON_LEFT):
            pos = pygame.mouse.get_pos()
            if self.gameobject.transform.rect.collidepoint(pos):
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename()
                if file_path:
                    self.file_path = file_path
                    self.updateImage()

    def updateImage(self):
        if self.image == None:
            print("No image has been referenced")
        else:
            self.image.spriterenderer.sprite = pygame.image.load(self.file_path)
    def getFilePath(self):
        if self.file_path == None:
            print("No file has been selected.")
        else:
            return self.file_path
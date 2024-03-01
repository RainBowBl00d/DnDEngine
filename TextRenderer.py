import pygame
class textrenderer:
    def __init__(self, gameobject, offset_x = 0, offeset_y = 0, text="Example text", color=(0, 0, 0), size=32, font=None):
        self.gameobject = gameobject
        self.text = text
        self.font = font or pygame.font.Font(None, size)
        self.color = color
        self.size = size
        self.offset_x = offset_x
        self.offset_y = offeset_y


    def setText(self, text):
        self.text = text

    def addText(self, text):
        self.text += text

    def setFont(self, font):
        self.font = font

    def setColor(self, color):
        self.color = color

    def setSize(self, size):
        self.size = size

    def setOffsetX(self, offset_x):
        self.offset_x = offset_x
    def setOffsetY(self, offset_y):
        self.offset_y = offset_y

    def addOffsetX(self, offset_x):
        self.offset_x += offset_x
    def addOffsetY(self, offset_y):
        self.offset_y -= offset_y


    def update(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.gameobject.transform.rect.centerx + self.offset_x, self.gameobject.transform.rect.centery - self.offset_y))


class textField:
    def __init__(self, gameobject, textrenderer):
        self.gameobject = gameobject
        self.textrenderer = textrenderer or textrenderer()

        self.clicked = False
        self.typing = False

    def input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.gameobject.transform.rect.collidepoint(event.pos):
                self.clicked = True
            else:
                self.clicked = False
        elif event.type == pygame.KEYDOWN:
            if self.clicked:
                if event.key == pygame.K_RETURN:
                    # Finish editing when Enter is pressed
                    self.clicked = False
                elif event.key == pygame.K_BACKSPACE:
                    self.textrenderer.text = self.textrenderer.text[:-1]
                else:
                    self.textrenderer.text += event.unicode

        return self.textrenderer.text
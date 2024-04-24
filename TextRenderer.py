import pygame

class textrenderer:
    def __init__(self, gameobject, offset_x = 0, offset_y = 0, text="Example text", color=(0, 0, 0), size=32, font=None, input_type="mixed"):
        self.gameobject = gameobject
        self.text = text
        self.font = font or pygame.font.Font(None, size)
        self.color = color
        self.size = size
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.input_type = input_type



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

    def setOffset(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y


    def addOffsetX(self, offset_x):
        self.offset_x += offset_x

    def addOffsetY(self, offset_y):
        self.offset_y -= offset_y

    def update(self, surface):
        text_surface = self.font.render(self.text, True, self.color)

        surface.blit(text_surface, (self.gameobject.transform.rect.centerx + self.offset_x
                                    , self.gameobject.transform.rect.centery - self.offset_y))

class textField:
    def __init__(self, gameobject, textrenderer):
        self.gameobject = gameobject
        self.textrenderer = textrenderer or textrenderer()

        self.clicked = False
        self.typing = False

    def input(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            if self.gameobject.transform.rect.collidepoint(mouse_x, mouse_y):
                self.clicked = True
            else:
                self.clicked = False

        if self.clicked and pygame.key.get_pressed()[pygame.K_RETURN]:
            self.clicked = False
        elif self.clicked and pygame.key.get_pressed()[pygame.K_BACKSPACE]:
            self.textrenderer.text = self.textrenderer.text[:-1]
        elif self.clicked:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.clicked = False
                elif event.key == pygame.K_BACKSPACE:
                    self.textrenderer.text = self.textrenderer.text[:-1]
                elif self.textrenderer.input_type == 'letters' and event.unicode.isalpha():
                    self.textrenderer.text += event.unicode
                elif self.textrenderer.input_type == 'numbers' and event.unicode.isdigit():
                    self.textrenderer.text += event.unicode
                elif self.textrenderer.input_type == 'mixed':
                    self.textrenderer.text += event.unicode

        return self.textrenderer.text
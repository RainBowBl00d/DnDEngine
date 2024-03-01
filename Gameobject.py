import pygame

class spriterenderer:
    def __init__(self, sprite=None, color=None):
        if sprite:
            self.sprite = pygame.image.load(sprite).convert_alpha()
            self.color = None
        elif color:
            self.sprite = None
            self.color = color
        else:
            raise ValueError("Either sprite or color must be provided")

    def setSprite(self, sprite):
        self.sprite = sprite

    def setColor(self, color):
        self.color = color

class transform:
    def __init__(self, x, y, spriterenderer, width=None, height=None, scale=1):
        if hasattr(spriterenderer, 'sprite') and spriterenderer.sprite:
            self.spriterenderer = spriterenderer
            self.sprite = spriterenderer.sprite
            self.rect = self.sprite.get_rect(topleft=(x, y))
            if width is not None and height is not None:
                self.rect.width = scale * width
                self.rect.height = scale * height
        else:
            self.spriterenderer = spriterenderer
            self.rect = pygame.Rect(x, y, width * scale, height * scale)

class gameobject:
    def __init__(self, window, transform):
        self.components = []
        self.transform = transform or transform()
        self.surface = window.display  # Assign display directly
        self.isActive = True
        window.gameobjects.append(self)

    def render(self):
        if self.isActive:
            if hasattr(self.transform, 'spriterenderer') and self.transform.spriterenderer:
                if self.transform.spriterenderer.sprite:
                    self.surface.blit(self.transform.spriterenderer.sprite, self.transform.rect)
                elif self.transform.spriterenderer.color:
                    pygame.draw.rect(self.surface, self.transform.spriterenderer.color, self.transform.rect)
            else:
                pygame.draw.rect(self.surface, (255, 0, 0), self.transform.rect)

            self.update()

    def setActive(self, isActive):
        self.isActive = isActive

    def addComponent(self, component):
        self.components.append(component)

    def get_component(self, component_type):
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    def update(self):
        for component in self.components:
            if hasattr(component, 'update'):
                component.update(self.surface)
import pygame
import Button, TextRenderer


class spriterenderer:
    def __init__(self, sprite, color):
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
    def __init__(self, gameobject, x, y, width, height, scale):
        self.gameobject = gameobject

        if self.gameobject.spriterenderer.sprite:
            self.rect = gameobject.spriterenderer.sprite.get_rect(topleft=(x, y))
            scaled_sprite = pygame.transform.scale(self.gameobject.spriterenderer.sprite,
                                                   (width * scale, height * scale))
            self.gameobject.spriterenderer.setSprite(scaled_sprite)
        else:
            self.rect = pygame.Rect(x, y, width * scale, height * scale)


class gameobject:
    def __init__(self, window,x, y, width=100, height=100, scale=1, sprite=None, color=None):
        self.components = []
        self.surface = window.display
        self.isActive = True
        self.spriterenderer = spriterenderer(sprite=sprite,color= color)
        self.transform = transform(self, x=x, y=y, width=width, height=height, scale=scale)
        window.gameobjects.append(self)

    def render(self):
        if self.isActive:
            if self.spriterenderer.sprite:
                self.surface.blit(source=self.spriterenderer.sprite, dest=self.transform.rect)
            else:
                pygame.draw.rect(surface=self.surface,color= self.spriterenderer.color,rect= self.transform.rect)
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

    @staticmethod
    def create_button(window, x, y, text="Button", size=32, sprite=None, color=None):
        # Create a game object
        button_obj = gameobject(window, x=x, y=y, height=100, width=200,sprite=sprite, color=color)

        button_obj.addComponent(button_obj.transform)
        button_obj.addComponent(button_obj.spriterenderer)

        # Create a button component and add it to the game object
        button = Button.button(button_obj)
        button_obj.addComponent(button)

        # Create a text renderer component and add it to the game object
        text_renderer = TextRenderer.textrenderer(button_obj, text=text, size=size, offset_y=0, offset_x=0)
        button_obj.addComponent(text_renderer)

        return button_obj

    @staticmethod
    def create_background(window, sprite, color, x, y, width, height, scale, text, size):
        background_obj = gameobject(window, sprite=sprite, color=None, x=x, y=y,
                                                    width=width, height=height, scale=scale)
        textrenderer = TextRenderer.textrenderer(background_obj, text=text, size=size,
                                                 color=color)
        background_obj.addComponent(textrenderer)

        return  background_obj
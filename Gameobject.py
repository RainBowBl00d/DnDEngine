import DragnDropField
import pygame
import Button, TextRenderer, Item


class spriterenderer:
    def __init__(self, sprite, color):
        if sprite:
            self.sprite = pygame.image.load(sprite).convert_alpha()
            self.color = None
        elif color:
            self.sprite = None
            self.color = color
        else:
            raise ValueError("Either sprite or color must be given")

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

        button_obj = gameobject(window, x=x, y=y, height=100, width=200,sprite=sprite, color=color)

        button_obj.addComponent(button_obj.transform)
        button_obj.addComponent(button_obj.spriterenderer)

        button = Button.button(button_obj)
        button_obj.addComponent(button)

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

        return background_obj
    @staticmethod
    def create_image(window, x, y, width, height, scale):
        image_obj = gameobject(window, sprite="defaultCharacterSprite.png", x=x, y=y,
                                                    width=width, height=height, scale=scale)
        return image_obj

    @staticmethod
    def create_textfield(window, x, y,width, heigth, text="enter text", size=32, sprite=None, color=None, input_type = "mixed"):
        textfield_obj = gameobject(window, x=x, y=y, height=heigth, width=width,sprite=sprite, color=color)

        textfield_obj.addComponent(textfield_obj.transform)
        textfield_obj.addComponent(textfield_obj.spriterenderer)

        text_renderer = TextRenderer.textrenderer(textfield_obj, text=text, size=size, offset_y=0, offset_x=0, input_type = input_type)
        textfield_obj.addComponent(text_renderer)

        button = TextRenderer.textField(textfield_obj, text_renderer )
        textfield_obj.addComponent(button)

        return textfield_obj

    @staticmethod
    def create_dragnDropfield(window, x, y, text, size, sprite=None,color=None):
        dragnDropfield_obj = gameobject(window, x=x, y=y, height=100, width=200,sprite=sprite, color=color )

        dragnDropfield_obj.addComponent(dragnDropfield_obj.transform)
        dragnDropfield_obj.addComponent(dragnDropfield_obj.spriterenderer)

        dragNDropField = DragnDropField.dragNDropField(dragnDropfield_obj)
        dragnDropfield_obj.addComponent(dragNDropField)

        text_renderer = TextRenderer.textrenderer(dragnDropfield_obj, text=text, size=size, offset_y=0, offset_x=0)
        dragnDropfield_obj.addComponent(text_renderer)
        return dragnDropfield_obj


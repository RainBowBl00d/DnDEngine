import pygame
import Gameobject
import Button
import TextRenderer

class window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.gameobjects = []
        self.isActive = True
        pygame.display.set_caption("Caption")

    def renderGameobjects(self):
        if(self.isActive):
            for gameobject in self.gameobjects:
                gameobject.render()

    def setActive(self, isActive):
        self.isActive = isActive

#<editor-fold desc="functions">
def start():
    startscreen.setActive(False)
    pickScreen.setActive(True)

def exit():
    global running
    running = False

def updateStartScreen():
    if startscreen.isActive:
        start_bt_obj.get_component(Button.button).getClick([start])
        exit_bt_obj.get_component(Button.button).getClick([exit])
#</editor-fold>

pygame.init()
clock = pygame.time.Clock()

startscreen = window(1440, 720)
pickScreen = window(1440, 720)

running = True

#<editor-fold desc="Start Menu creation">
#<editor-fold desc="Background creation">
startbackground_spriterenderer = Gameobject.spriterenderer("StartScreen.jpg", color=(0,0,0))
startbackground_transform = Gameobject.transform(0, 0, spriterenderer = startbackground_spriterenderer, width=1440, height=720, scale= 1)
startbackground_obj = Gameobject.gameobject(startscreen, transform=startbackground_transform)
textrenderer = TextRenderer.textrenderer(startbackground_obj, text="Dungeons, Dragons and an Engine", size=96, color=(0,0,0), offset_x=-600, offeset_y= 200)
startbackground_obj.addComponent(textrenderer)
startbackground_spriterenderer.sprite = pygame.transform.scale(startbackground_spriterenderer.sprite, (startscreen.display.get_width(), startscreen.display.get_height()))
#</editor-fold>
#<editor-fold desc="Start button">
start_bt_spriterenderer = Gameobject.spriterenderer(sprite="Button.png")
start_bt_transform = Gameobject.transform(600, 310, spriterenderer= start_bt_spriterenderer)
start_bt_obj = Gameobject.gameobject(startscreen, start_bt_transform)
start_bt_bt = Button.button(start_bt_obj)
start_bt_obj.addComponent(start_bt_bt)
start_bt_txtrenderer = TextRenderer.textrenderer(start_bt_obj, text="Start", size=64, offeset_y= 20, offset_x=-50)
start_bt_obj.addComponent(start_bt_txtrenderer)
#</editor-fold>
#<editor-fold desc="Exit button">
exit_bt_spriterenderer = Gameobject.spriterenderer(sprite="Button.png")
exit_bt_transform = Gameobject.transform(600, 420, spriterenderer= exit_bt_spriterenderer)
exit_bt_obj = Gameobject.gameobject(startscreen, exit_bt_transform)
exit_bt_bt = Button.button(exit_bt_obj)
exit_bt_obj.addComponent(exit_bt_bt)
exit_bt_txtrenderer = TextRenderer.textrenderer(exit_bt_obj, text="Exit", size=64, offeset_y= 20, offset_x=-50)
exit_bt_obj.addComponent(exit_bt_txtrenderer)
#</editor-fold>
#</editor-fold>
#<editor-fold desc="Pick Menu creation">
#<editor-fold desc="PickMenu">
pickmenubackground_spriterenderer = Gameobject.spriterenderer("StartScreen.jpg", color=(0,0,0))
pickmenubackground_transform = Gameobject.transform(0, 0, spriterenderer=pickmenubackground_spriterenderer, width=1440, height=720, scale= 1)
pickmenubackground_obj = Gameobject.gameobject(pickScreen, transform=pickmenubackground_transform)
pickmenubackground_spriterenderer.sprite = pygame.transform.scale(pickmenubackground_spriterenderer.sprite, (pickScreen.display.get_width(), pickScreen.display.get_height()))
#</editor-fold>
#<editor-fold desc="Play button">
play_bt_spriterenderer = Gameobject.spriterenderer(sprite="Button.png")
play_bt_transform = Gameobject.transform(600, 310, spriterenderer= play_bt_spriterenderer)
play_bt_obj = Gameobject.gameobject(pickScreen, play_bt_transform)
play_bt_bt = Button.button(play_bt_obj)
play_bt_obj.addComponent(start_bt_bt)
play_bt_txtrenderer = TextRenderer.textrenderer(play_bt_obj, text="Play", size=64, offeset_y= 20, offset_x=-50)
play_bt_obj.addComponent(play_bt_txtrenderer)
#</editor-fold>
#<editor-fold desc="Play button">
create_bt_spriterenderer = Gameobject.spriterenderer(sprite="Button.png")
create_bt_transform = Gameobject.transform(600, 420, spriterenderer= create_bt_spriterenderer)
create_bt_obj = Gameobject.gameobject(pickScreen, create_bt_transform)
create_bt_bt = Button.button(create_bt_obj)
create_bt_obj.addComponent(create_bt_bt)
create_bt_txtrenderer = TextRenderer.textrenderer(create_bt_obj, text="Create", size=64, offeset_y= 20, offset_x=-50)
create_bt_obj.addComponent(create_bt_txtrenderer)
#</editor-fold>
#</editor-fold>


while running:
    startscreen.display.fill((255, 255, 255))
    pickScreen.display.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updateStartScreen()

    pickScreen.renderGameobjects()
    startscreen.renderGameobjects()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()

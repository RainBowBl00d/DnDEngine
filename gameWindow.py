import pygame
import Gameobject
import Button
import MouseInput
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
        if (self.isActive):
            for gameobject in self.gameobjects:
                gameobject.render()

    def setActive(self, isActive):
        self.isActive = isActive


# <editor-fold desc="functions">
###################################################################

def exit():
    global running
    running = False

def switchScenes(setActiveScene, disableScene):
    disableScene.setActive(False)
    setActiveScene.setActive(True)

####################################################################
def updatepickScreen():
    if pickScreen.isActive:
        play_bt_obj.get_component(Button.button).getClick([lambda: switchScenes(characterScreen, pickScreen)])
        back_bt_obj.get_component(Button.button).getClick([lambda: switchScenes(startscreen, pickScreen)])

def updateStartScreen():
    if startscreen.isActive:
        start_bt_obj.get_component(Button.button).getClick(lambda: switchScenes(pickScreen, startscreen))
        exit_bt_obj.get_component(Button.button).getClick([exit])

pygame.init()
clock = pygame.time.Clock()
startscreen = window(1440, 720)
startscreen.setActive(True)
pickScreen = window(1440, 720)
pickScreen.setActive(False)
characterScreen = window(1440, 720)
characterScreen.setActive(False)

running = True

# <editor-fold desc="Start Menu creation">
#Background creation
startbackground_obj = Gameobject.gameobject.create_background(window=startscreen, sprite="StartScreen.jpg",color=(0, 0, 0), x=0, y=0,
                                                        width=1440, height=720, scale=1, text="Dungeons, Dragons and an Engine", size=96)
#Button creation
start_bt_obj = Gameobject.gameobject.create_button(window=startscreen, x=100, y=310, text="Start", size=64, sprite="Button.png")
exit_bt_obj = Gameobject.gameobject.create_button(window=startscreen, x=100, y=420, text="Exit", size=64, sprite="Button.png")
start_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-100, 20)
exit_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-90, 20)

# </editor-fold>
# <editor-fold desc="Pick Menu creation">
#Background creation
pickmenubackground_obj = Gameobject.gameobject.create_background(pickScreen, sprite="StartScreen.jpg", color=(0, 0, 0), x=0, y=0,
                                               width=1440, height=720, scale=1,text="",size=0)
#Button creation
play_bt_obj = Gameobject.gameobject.create_button(pickScreen, 600, 310, text="Play", size=64, sprite="Button.png")
create_bt_obj = Gameobject.gameobject.create_button(pickScreen, 600, 420, text="Create", size=64, sprite="Button.png")
back_bt_obj = Gameobject.gameobject.create_button(pickScreen, 600, 530, text="Back", size=64, sprite="Button.png")

create_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 20)
play_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-90, 20)
back_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-90, 20)
# </editor-fold>

# <editor-fold desc="Character creation">
# </editor-fold>

while running:
    startscreen.display.fill((255, 255, 255))
    pickScreen.display.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        MouseInput.mouseInput.update(event)

    updateStartScreen()
    updatepickScreen()

    startscreen.renderGameobjects()
    pickScreen.renderGameobjects()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

import DragnDropField
import pygame
import Gameobject
import Button
import MouseInput
import TextRenderer
import Character


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


#<editor-fold desc="functions">


def exit():
    global running
    running = False

def switchScenes(setActiveScene, disableScene):
    disableScene.setActive(False)
    setActiveScene.setActive(True)


def updatepickScreen():
    if pickScreen.isActive:
        create_bt_obj.get_component(Button.button).getClick([lambda: switchScenes(characterScreen, pickScreen)])
        back_bt_obj.get_component(Button.button).getClick([lambda: switchScenes(startscreen, pickScreen)])

def updateStartScreen():
    if startscreen.isActive:
        start_bt_obj.get_component(Button.button).getClick(lambda: switchScenes(pickScreen, startscreen))
        exit_bt_obj.get_component(Button.button).getClick([exit])

def updateCharacterScreen():
    if characterScreen.isActive:
        dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        characterBack_bt_obj.get_component(Button.button).getClick(lambda: switchScenes(pickScreen, characterScreen))

#</editor-fold>


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
#background
charactercreationbackground_obj = Gameobject.gameobject.create_background(characterScreen, sprite="StartScreen.jpg", color=(0, 0, 0), x=0, y=0,
                                               width=1440, height=720, scale=1,text="",size=0)

#select stuff
previewbackground_obj = Gameobject.gameobject.create_background(characterScreen, sprite="Button.png", color=(0, 0, 0), x=100, y=50,
                                               width=500, height=600, scale=1,text="Preview", size=36)

dragNDrop_obj = Gameobject.gameobject.create_dragnDropfield(characterScreen, 600, 310, text="Select character image", size=24,sprite="Button.png" )
characterpreview_obj = Gameobject.gameobject.create_image(characterScreen, x=150, y= 150,width=200, height=400, scale=1)
dragNDrop_obj.get_component(DragnDropField.dragNDropField).image = characterpreview_obj
dragNDrop_obj.get_component(TextRenderer.textrenderer).setOffset(-140, 20)

selectionInventory_obj = Gameobject.gameobject.create_textfield(characterScreen, 650, 20,heigth=50, width=50, sprite="Button.png", input_type="numbers")
selectionHealth_obj = Gameobject.gameobject.create_textfield(characterScreen, 650, 80,heigth=50, width=50, sprite="Button.png", input_type="numbers")
selectionMana_obj = Gameobject.gameobject.create_textfield(characterScreen, 650, 140,heigth=50, width=50, sprite="Button.png", input_type="numbers")
selectionArmor_obj = Gameobject.gameobject.create_textfield(characterScreen, 650, 200,heigth=50, width=50, sprite="Button.png", input_type="numbers")
selectionName_obj = Gameobject.gameobject.create_textfield(characterScreen, 650, 260,heigth=50, width=50, sprite="Button.png", input_type="letters")

# Buttons
characterBack_bt_obj = Gameobject.gameobject.create_button(characterScreen, 1200, 600, text="Back", size=64, sprite="Button.png")
characterBack_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-90, 20)

# </editor-fold>

while running:
    startscreen.display.fill((255, 255, 255))
    pickScreen.display.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        MouseInput.mouseInput.update(event)
        MouseInput.keyboardInput.update(event)
        selectionInventory_obj.get_component(TextRenderer.textField).input(event)
        selectionHealth_obj.get_component(TextRenderer.textField).input(event)
        selectionMana_obj.get_component(TextRenderer.textField).input(event)
        selectionName_obj.get_component(TextRenderer.textField).input(event)
        selectionArmor_obj.get_component(TextRenderer.textField).input(event)


    updateStartScreen()
    updatepickScreen()
    updateCharacterScreen()

    startscreen.renderGameobjects()
    pickScreen.renderGameobjects()
    characterScreen.renderGameobjects()



    clock.tick(60)
    pygame.display.flip()

pygame.quit()

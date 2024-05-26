import Character
import DragnDropField
import pygame
import Gameobject
import Button
import Map
import MouseInput
import TextRenderer
import Item

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
        mapcreator_bt_obj.get_component(Button.button).getClick([lambda: switchScenes(mapCreateScreen, pickScreen)])
        createItem_bt_obj.get_component(Button.button).getClick([lambda: switchScenes(ItemCreateScreen, pickScreen)])

def updateStartScreen():
    if startscreen.isActive:
        start_bt_obj.get_component(Button.button).getClick(lambda: switchScenes(pickScreen, startscreen))
        exit_bt_obj.get_component(Button.button).getClick([exit])

def updateCharacterScreen():
    if characterScreen.isActive:
        lambda_expression = lambda: saveCharacter(selectionName_obj.get_component(TextRenderer.textrenderer).text,
                                                            selectionHealth_obj.get_component(TextRenderer.textrenderer).text,
                                                            selectionMana_obj.get_component(TextRenderer.textrenderer).text,
                                                            selectionArmor_obj.get_component(TextRenderer.textrenderer).text,
                                                            selectionInventory_obj.get_component(TextRenderer.textrenderer).text)
        dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        characterBack_bt_obj.get_component(Button.button).getClick(lambda: switchScenes(pickScreen, characterScreen))
        characterCreate_bt_obj.get_component(Button.button).getClick(lambda_expression)

def updateItemScreen():
    if ItemCreateScreen.isActive:
        lambda_expression = lambda: saveItem(itemselectionName_obj.get_component(TextRenderer.textrenderer).text,
                                                            itemselectionHealth_obj.get_component(TextRenderer.textrenderer).text,
                                                           itemselectionMana_obj.get_component(TextRenderer.textrenderer).text,
                                                            itemselectionArmor_obj.get_component(TextRenderer.textrenderer).text)
        itemdragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        itemBack_bt_obj.get_component(Button.button).getClick(lambda: switchScenes(pickScreen, ItemCreateScreen))
        itemCreate_bt_obj.get_component(Button.button).getClick(lambda_expression)

def updateMapCreateScreen():
    if mapCreateScreen.isActive:
        mapBack_bt_obj.get_component(Button.button).getClick(lambda : switchScenes(pickScreen, mapCreateScreen))
        map_1_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_2_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_3_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_4_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_5_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_6_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_7_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_8_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        map_9_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getHover()
        mapCreate_bt_obj.get_component(Button.button).getClick(lambda : saveMap(selectionMapName_obj.get_component(TextRenderer.textrenderer).text,
        map_1_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_2_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_3_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_4_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_5_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_6_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_7_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_8_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath(),
        map_9_dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath()))

def saveCharacter(name, maxhealth, maxmana, maxarmor, maxinventoryslots):
    character = Character.character(name, maxhealth, maxmana, maxarmor, maxinventoryslots)
    character.spritePath = dragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath()
    Character.character.serializeCharacterData(character)
def saveItem(name, maxhealth, maxmana, maxarmor):
    item = Item.item(name, maxhealth, maxmana, maxarmor, itemdragNDrop_obj.get_component(DragnDropField.dragNDropField).getFilePath())
    Item.item.serializeItemData(item)

def saveMap(name,sprite_path_1, sprite_path_2,sprite_path_3,sprite_path_4,sprite_path_5,sprite_path_6,sprite_path_7,sprite_path_8, sprite_path_9):
    map= Map.worldMap(name, 3,3)
    map.add_segment(0,0,sprite_path_1)
    map.add_segment(0,1,sprite_path_2)
    map.add_segment(0,2,sprite_path_3)
    map.add_segment(1,0,sprite_path_4)
    map.add_segment(1,1,sprite_path_5)
    map.add_segment(1,2,sprite_path_6)
    map.add_segment(2,0,sprite_path_7)
    map.add_segment(2,1,sprite_path_8)
    map.add_segment(2,2,sprite_path_9)
    map.serializeMapData()






#</editor-fold>


pygame.init()
clock = pygame.time.Clock()
startscreen = window(1440, 720)
startscreen.setActive(True)



#Creation
pickScreen = window(1440, 720)
pickScreen.setActive(False)
characterScreen = window(1440, 720)
characterScreen.setActive(False)
mapCreateScreen = window(1440, 720)
mapCreateScreen.setActive(False)
ItemCreateScreen = window(1440, 720)
ItemCreateScreen.setActive(False)




running = True
# <editor-fold desc="Map  creation">
#Background creation
mapCreatebackground_obj = Gameobject.gameobject.create_background(window=mapCreateScreen, sprite="assets/StartScreen.jpg", color=(0, 0, 0), x=0, y=0,
                                                                  width=1440, height=720, scale=1, text="", size=96)
#Select stuff
preview_window_width = 130
preview_window_height = 130
dragNDrop_size = 24


def create_preview_and_dragndrop(mapCreateScreen, grid_x, grid_y, preview_window_width, preview_window_height):
    x_offset = 100
    y_offset = 100
    x = grid_x * preview_window_width + x_offset * (grid_x + 1)
    y = grid_y * preview_window_height + y_offset * (grid_y + 1) -100

    preview_background_obj = Gameobject.gameobject.create_background(
        mapCreateScreen, sprite="assets/Button.png", color=(0, 0, 0),
        x=x, y=y, width=preview_window_width, height=preview_window_height, scale=1, text="assets/Preview", size=36
    )
    preview_obj = Gameobject.gameobject.create_image(
        mapCreateScreen, x=x +15, y=y + 15, width=100, height=100, scale=1, sprite_path="assets/treasureMap.jpg"
    )

    dragNDrop_obj = Gameobject.gameobject.create_dragnDropfield(
        mapCreateScreen, x=x, y=y + preview_window_height , text="Select character image",
        size=dragNDrop_size, sprite="assets/Button.png"
    )

    dragNDrop_obj.get_component(DragnDropField.dragNDropField).image = preview_obj

    return preview_background_obj, dragNDrop_obj


# First row
map_1_previewbackground_obj, map_1_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 0, 0,
                                                                                preview_window_width,
                                                                                preview_window_height)
map_2_previewbackground_obj, map_2_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 1, 0,
                                                                                preview_window_width,
                                                                                preview_window_height)
map_3_previewbackground_obj, map_3_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 2, 0,
                                                                                preview_window_width,
                                                                                preview_window_height)

# Second row
map_4_previewbackground_obj, map_4_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 0, 1,
                                                                                preview_window_width,
                                                                                preview_window_height)
map_5_previewbackground_obj, map_5_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 1, 1,
                                                                                preview_window_width,
                                                                                preview_window_height)
map_6_previewbackground_obj, map_6_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 2, 1,
                                                                                preview_window_width,
                                                                                preview_window_height)

# Third row
map_7_previewbackground_obj, map_7_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 0, 2,
                                                                                preview_window_width,
                                                                                preview_window_height)
map_8_previewbackground_obj, map_8_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 1, 2,
                                                                                preview_window_width,
                                                                                preview_window_height)
map_9_previewbackground_obj, map_9_dragNDrop_obj = create_preview_and_dragndrop(mapCreateScreen, 2, 2,
                                                                                preview_window_width,
                                                                                preview_window_height)
# Buttons
mapCreate_bt_obj = Gameobject.gameobject.create_button(
    mapCreateScreen, x=950, y=500,width=200,
    text="Create", size=64, sprite="assets/Button.png"
)
mapCreate_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 20)
mapBack_bt_obj = Gameobject.gameobject.create_button(
    mapCreateScreen, x=950, y=600,width=200,
    text="Back", size=64, sprite="assets/Button.png"
)
mapBack_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 20)

selectionMapName_obj = Gameobject.gameobject.create_textfield(
    mapCreateScreen, x=950, y=400,
    heigth= 50, width=200, sprite="assets/Button.png", input_type="letters"
)
name_text = Gameobject.gameobject.create_text(mapCreateScreen, 1200, 400, width= 150, heigth=50,text=": Enter Name", color=(0,0,255))
name_text.get_component(TextRenderer.textrenderer).setOffset(-65, 0)
selectionMapName_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 30)

# </editor-fold>

# <editor-fold desc="Start Menu creation">
#Background creation
startbackground_obj = Gameobject.gameobject.create_background(window=startscreen, sprite="assets/StartScreen.jpg",color=(0, 0, 0), x=0, y=0,
                                                        width=1440, height=720, scale=1, text="Dungeons, Dragons and an Engine", size=96)
#Button creation
start_bt_obj = Gameobject.gameobject.create_button(window=startscreen, x=100, y=310, width=200,text="Start", size=64, sprite="assets/Button.png")
exit_bt_obj = Gameobject.gameobject.create_button(window=startscreen, x=100, y=420,width=200, text="Exit", size=64, sprite="assets/Button.png")
start_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-100, 20)
exit_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-90, 20)

# </editor-fold>
# <editor-fold desc="Pick Menu creation">
#Background creation
pickmenubackground_obj = Gameobject.gameobject.create_background(pickScreen, sprite="assets/StartScreen.jpg", color=(0, 0, 0), x=0, y=0,
                                               width=1440, height=720, scale=1,text="",size=0)
#Button creation
mapcreator_bt_obj = Gameobject.gameobject.create_button(pickScreen, 600, 230,width=350,height = 100, text="Map Creator", size=64, sprite="assets/Button.png")
create_bt_obj = Gameobject.gameobject.create_button(pickScreen, 600, 360,width=420,height = 100, text="Create Character", size=64, sprite="assets/Button.png")
createItem_bt_obj = Gameobject.gameobject.create_button(pickScreen, 600, 490,width=300,height = 100, text="Create Item", size=64, sprite="assets/Button.png")

back_bt_obj = Gameobject.gameobject.create_button(pickScreen, 600, 620, width=200,height = 100,text="Back", size=64, sprite="assets/Button.png")


create_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 20)
createItem_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 20)
mapcreator_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-90, 20)
back_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-90, 20)

# </editor-fold>
# <editor-fold desc="Character creation">
# Background
charactercreationbackground_obj = Gameobject.gameobject.create_background(
    characterScreen, sprite="assets/StartScreen.jpg", color=(0, 0, 0),
    x=0, y=0, width=1440, height=720, scale=1, text="", size=0
)

# Select stuff
previewbackground_obj = Gameobject.gameobject.create_background(
    characterScreen, sprite="assets/Button.png", color=(0, 0, 0),
    x=100, y=50, width=500, height=600, scale=1, text="Preview", size=36
)

dragNDrop_obj = Gameobject.gameobject.create_dragnDropfield(
    characterScreen, x=600, y=550, text="Select character image",
    size=24, sprite="assets/Button.png"
)

characterpreview_obj = Gameobject.gameobject.create_image(
    characterScreen, x=150, y=150, width=200, height=400, scale=1
)

dragNDrop_obj.get_component(DragnDropField.dragNDropField).image = characterpreview_obj
dragNDrop_obj.get_component(TextRenderer.textrenderer).setOffset(-140, 20)

# Text fields alignment
textfield_x = 650
textfield_width = 150
textfield_height = 50
textfield_padding = 50

text_offset_x = -140
text_offset_y = 35

selectionInventory_obj = Gameobject.gameobject.create_textfield(
    characterScreen, x=textfield_x, y=50, heigth=textfield_height,
    width=textfield_width, sprite="assets/Button.png", input_type="numbers", text="0"
)
selectionInventory_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
inventory_text = Gameobject.gameobject.create_text(characterScreen, textfield_x + 200, 50, width= 400, heigth=50,text=": Enter the amount of invetory slots", color=(0,0,255))
inventory_text.get_component(TextRenderer.textrenderer).setOffset(-200, 5)

selectionHealth_obj = Gameobject.gameobject.create_textfield(
    characterScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 1,
    heigth=textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="numbers", text="0"
)
selectionHealth_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
health_text = Gameobject.gameobject.create_text(characterScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 1, width= 300, heigth=50,text=": Enter the amount of health", color=(0,0,255))
health_text.get_component(TextRenderer.textrenderer).setOffset(-150, 5)

selectionMana_obj = Gameobject.gameobject.create_textfield(
    characterScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 2,
    heigth=textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="numbers", text="0"
)
selectionMana_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
mana_text = Gameobject.gameobject.create_text(characterScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 2, width= 300, heigth=50,text=": Enter the amount of mana", color=(0,0,255))
mana_text.get_component(TextRenderer.textrenderer).setOffset(-150, 5)

selectionArmor_obj = Gameobject.gameobject.create_textfield(
    characterScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 3,
    heigth=textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="numbers", text="0"
)
selectionArmor_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
armor_text = Gameobject.gameobject.create_text(characterScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 3, width= 300, heigth=50,text=": Enter the amount of armor", color=(0,0,255))
armor_text.get_component(TextRenderer.textrenderer).setOffset(-150, 5)

selectionName_obj = Gameobject.gameobject.create_textfield(
    characterScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 4,
    heigth= textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="letters", text="Example"
)
selectionName_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
name_text = Gameobject.gameobject.create_text(characterScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 4, width= 150, heigth=50,text=": Enter Name", color=(0,0,255))
name_text.get_component(TextRenderer.textrenderer).setOffset(-65, 5)

# Buttons alignment
button_y = 600
button_width = 200
button_height = 80
button_padding = 20

characterBack_bt_obj = Gameobject.gameobject.create_button(
    characterScreen, x=1200, y=button_y, width=200, text="Back", size=64, sprite="assets/Button.png"
)

characterBack_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-100, 20)

characterCreate_bt_obj = Gameobject.gameobject.create_button(
    characterScreen, x=1100 - (button_width + button_padding), y=button_y, width=200,
    text="Create", size=64, sprite="assets/Button.png"
)
characterCreate_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 20)
# </editor-fold
# <editor-fold desc="Item creation">
# Background
itemcreationbackground_obj = Gameobject.gameobject.create_background(
    ItemCreateScreen, sprite="assets/StartScreen.jpg", color=(0, 0, 0),
    x=0, y=0, width=1440, height=720, scale=1, text="", size=0
)

# Select stuff
itempreviewbackground_obj = Gameobject.gameobject.create_background(
    ItemCreateScreen, sprite="assets/Button.png", color=(0, 0, 0),
    x=100, y=50, width=500, height=600, scale=1, text="Preview", size=36
)

itemdragNDrop_obj = Gameobject.gameobject.create_dragnDropfield(
    ItemCreateScreen, x=600, y=600, text="Select character image",
    size=24, sprite="assets/Button.png"
)

itempreview_obj = Gameobject.gameobject.create_image(
    ItemCreateScreen, x=150, y=150, width=200, height=400, scale=1, sprite_path="assets/helmet.png"
)

itemdragNDrop_obj.get_component(DragnDropField.dragNDropField).image = characterpreview_obj
itemdragNDrop_obj.get_component(TextRenderer.textrenderer).setOffset(-140, 20)

# Text fields alignment
textfield_x = 650
textfield_width = 150
textfield_height = 50
textfield_padding = 50

text_offset_x = -140
text_offset_y = 35

itemselectionHealth_obj = Gameobject.gameobject.create_textfield(
    ItemCreateScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 1,
    heigth=textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="numbers", text="0"
)
itemselectionHealth_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
itemhealth_text = Gameobject.gameobject.create_text(ItemCreateScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 1, width= 300, heigth=50,text=": Enter the amount of health", color=(0,0,255))
itemhealth_text.get_component(TextRenderer.textrenderer).setOffset(-150, 5)

itemselectionMana_obj = Gameobject.gameobject.create_textfield(
    ItemCreateScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 2,
    heigth=textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="numbers",text="0"
)
itemselectionMana_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
itemmana_text = Gameobject.gameobject.create_text(ItemCreateScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 2, width= 300, heigth=50,text=": Enter the amount of mana", color=(0,0,255))
itemmana_text.get_component(TextRenderer.textrenderer).setOffset(-150, 5)

itemselectionArmor_obj = Gameobject.gameobject.create_textfield(
    ItemCreateScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 3,
    heigth=textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="numbers", text="0"
)
itemselectionArmor_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
itemarmor_text = Gameobject.gameobject.create_text(ItemCreateScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 3, width= 300, heigth=50,text=": Enter the amount of armor", color=(0,0,255))
itemarmor_text.get_component(TextRenderer.textrenderer).setOffset(-150, 5)

itemselectionName_obj = Gameobject.gameobject.create_textfield(
    ItemCreateScreen, x=textfield_x, y=50 + (textfield_height + textfield_padding) * 4,
    heigth= textfield_height, width=textfield_width, sprite="assets/Button.png", input_type="letters",text="Helmet"
)
itemselectionName_obj.get_component(TextRenderer.textrenderer).setOffset(text_offset_x, text_offset_y)
itemname_text = Gameobject.gameobject.create_text(ItemCreateScreen, textfield_x + 200, 50 + (textfield_height + textfield_padding) * 4, width= 150, heigth=50,text=": Enter Name", color=(0,0,255))
itemname_text.get_component(TextRenderer.textrenderer).setOffset(-65, 5)

# Buttons alignment
button_y = 600
button_width = 200
button_height = 80
button_padding = 20

itemBack_bt_obj = Gameobject.gameobject.create_button(
    ItemCreateScreen, x=1200, y=button_y,width= 200, text="Back", size=64, sprite="assets/Button.png"
)

itemBack_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-100, 20)

itemCreate_bt_obj = Gameobject.gameobject.create_button(
    ItemCreateScreen, x=1100 - (button_width + button_padding), y=button_y,width=200,
    text="Create", size=64, sprite="assets/Button.png"
)
itemCreate_bt_obj.get_component(TextRenderer.textrenderer).setOffset(-120, 20)
# </editor-fold

while running:
    startscreen.display.fill((255, 255, 255))
    pickScreen.display.fill((255, 255, 255))
    characterScreen.display.fill((255, 255, 255))
    mapCreateScreen.display.fill((255, 255, 255))
    ItemCreateScreen.display.fill((255, 255, 255))

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
        itemselectionHealth_obj.get_component(TextRenderer.textField).input(event)
        itemselectionMana_obj.get_component(TextRenderer.textField).input(event)
        itemselectionArmor_obj.get_component(TextRenderer.textField).input(event)
        itemselectionName_obj.get_component(TextRenderer.textField).input(event)


    updateStartScreen()
    updatepickScreen()
    updateCharacterScreen()
    updateMapCreateScreen()
    updateItemScreen()

    startscreen.renderGameobjects()
    pickScreen.renderGameobjects()
    characterScreen.renderGameobjects()
    mapCreateScreen.renderGameobjects()
    ItemCreateScreen.renderGameobjects()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

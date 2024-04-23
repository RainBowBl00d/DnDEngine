import pygame
class mouseInput:
    current_frame_buttons = {}
    last_frame_buttons = {}
    mousePos = [0,0]

    @staticmethod
    def update(event):
        mouseInput.last_frame_buttons = mouseInput.current_frame_buttons.copy()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseInput.current_frame_buttons[event.button] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseInput.current_frame_buttons[event.button] = False

    @staticmethod
    def getButtonDown(button):
        return mouseInput.current_frame_buttons.get(button, False) and not mouseInput.last_frame_buttons.get(button, False)

    @staticmethod
    def getButtonUp(button):
        return not mouseInput.current_frame_buttons.get(button, False) and mouseInput.last_frame_buttons.get(button, False)

class keyboardInput:
    current_frame_buttons = {}
    last_frame_buttons = {}

    @staticmethod
    def update(event):
        keyboardInput.last_frame_buttons = keyboardInput.current_frame_buttons.copy()
        if event.type == pygame.KEYDOWN:
            keyboardInput.current_frame_buttons[event.button] = True
        elif event.type == pygame.KEYUP:
            keyboardInput.current_frame_buttons[event.button] = False

    @staticmethod
    def getButtonDown(button):
        return keyboardInput.current_frame_buttons.get(button, False) and not keyboardInput.last_frame_buttons.get(button, False)

    @staticmethod
    def getButtonUp(button):
        return not keyboardInput.current_frame_buttons.get(button, False) and mouseInput.last_frame_buttons.get(button, False)
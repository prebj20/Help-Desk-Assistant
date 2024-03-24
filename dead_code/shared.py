import pyperclip
from pynput import mouse, keyboard

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle and pressed:
        # Simulate Ctrl+V to paste
        with keyboard_controller.pressed(keyboard.Key.ctrl):
            keyboard_controller.press('v')
            keyboard_controller.release('v')
        return False

# Prepare the keyboard controller
keyboard_controller = keyboard.Controller()

if __name__ == "__main__":
    pyperclip.copy("This is the template.")

    # Start listening for mouse events
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

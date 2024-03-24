import subprocess
import pyperclip
from pynput import mouse, keyboard
import os

import tkinter as tk

from GUI import Application

# Command Management
class Command():
        def __init__(self, name: str, type: object, args=None, data=None, data_2=None) -> None:
            self.name = name
            self.type = type
            self.args = args
            self.data = data
            self.data_2 = data_2
            
class Types:
    class Template:
        def function(app: Application, cmd: Command):
            if (cmd.data): 
                app.display.replace(cmd.data+"\n")
                app.q("Copy Description", cmd.data)
            if (cmd.data_2): 
                app.display.append(25*"_"+"\n\n"+cmd.data_2)
                app.q("Copy Resolution", cmd.data_2)
            if(cmd.data or cmd.data_2):
                app.paste_switch()

    class KnowledgeBase:
         def function(app: Application, cmd: Command):
            app.display.append("Not Implemented. Try another command.")

    class Windows:
        def function(app: Application, cmd: Command):
            cmd.args = list(cmd.args)
            cmd.args.pop(0)

            # Read STDOUT, create subprocess
            sout = subprocess.check_output(cmd.args, text=True, shell=True)

            app.display.append("\n"+os.getcwd())
            if(sout): app.display.append(f"\n{sout}")

def find_command(list: Command, data) -> Command:
    for cmd in list:
        if cmd.name == data: return cmd
        elif cmd.data == data: return cmd
        elif cmd.data_2 == data: return cmd

# turns string into set of args
def arguments(entry) -> list:
    # original
    entry = str(entry).lower().strip(' !@#$%^&*()_+<>,.?/-')
    entry = entry.split()
    return entry

def copy_paste(app: Application, data):
    def on_click(x, y, button, pressed):
        if button == mouse.Button.middle and pressed:
            # Simulate Ctrl+V to paste
            with kb_ctrlr.pressed(keyboard.Key.ctrl):
                kb_ctrlr.press('v')
                kb_ctrlr.release('v')
            return False
    pyperclip.copy(str(data))

    if(app.pasteMode.get()):
        # Prepare the keyboard controller
        kb_ctrlr = keyboard.Controller()

        # Start listening for mouse events
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
    else: return


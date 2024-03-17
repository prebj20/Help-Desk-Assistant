import pyperclip
import os

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
                app.display.replace(cmd.data)
                app.q("Copy Description", cmd.data)
            if (cmd.data_2): 
                app.display.append("\n\n"+cmd.data_2)
                app.q("Copy Resolution", cmd.data_2)

    class KnowledgeBase:
         def function(app, cmd: Command):
            app.display.append("Not Implemented. Try another command.")

    class Windows:
        def function(app, cmd: Command):
            cmd.args = list(cmd.args)
            cmd.args.pop(0)
            os.system(" ".join(cmd.args))

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
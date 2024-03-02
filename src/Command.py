import pyperclip
from Mod import AnsiColor
import os


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
        def function(cmd: Command):
            pyperclip.copy(cmd.data)
            print(AnsiColor.OKGREEN+"Copied to Clipboard\n"+AnsiColor.ENDC)

    class KnowledgeBase:
         def function(cmd: Command):
            print(f"Not Implemented. Entered -> {cmd.args}")

    class Windows:
        def function(cmd: Command):
            cmd.args = list(cmd.args)
            cmd.args.pop(0)
            os.system(" ".join(cmd.args))
        

def find_command(list: Command, data) -> Command:
    for cmd in list:
        if cmd.name == data: return cmd
        elif cmd.data == data: return cmd
        elif cmd.data_2 == data: return cmd
    return None  # This line is optional but makes the behavior explicit
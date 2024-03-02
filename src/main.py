# region IMPORTS ========================================
import os
#from templates.py import Subject
import pyperclip

from Command import Command, Types, find_command
from Mod import AnsiColor, arguments, help, copy_to_clipboard
# endregion ============================================= 

USER = os.getlogin().replace(" ", "-").strip().lower()
# -------------------------------------------------------

# Loading Preset commands
password_reset = Command(name="pr", type=Types.Template, 
        data="User is having trouble signing into their account. The user seems to have forgotten their password.",
        data_2="Verified: SSN, DOB, Home Address\nReset password\nCleared security questions")

ticket_template = Command(name="tt", type=Types.Template, 
        data="User is having trouble signing into their account. The user seems to have forgotten their password.",
        data_2="Verified: SSN, DOB, Home Address\nReset password\nCleared security questions")

kb_search = Command(name="kb", type=Types.KnowledgeBase)

windows = Command(name="win", type=Types.Windows)


preset_commands = []
preset_commands.append(password_reset)
preset_commands.append(ticket_template)
preset_commands.append(kb_search)
preset_commands.append(windows)

# Main Loop
def main():
    # cleanup
    os.system("cls")
    print(f"{AnsiColor.HEADER}Help Desk Assistant <TEST-VERSION>{AnsiColor.ENDC}")

    # main loop
    while True:

        # Get Command
        entry = input(f"{AnsiColor.OKCYAN}\n<{USER}> |>> {AnsiColor.ENDC}")
        args = arguments(entry)

        # Exit/Help Check
        if   args[0] == 'exit': break
        elif args[0] == "help": help()

        elif find_command(preset_commands, args[0]):
            command = find_command(preset_commands, args[0])
            command.args = args
            command.type.function(command)
            continue


        # Invalid command
        else: print(f"{AnsiColor.FAIL}Invalid command. Type 'help' for a list of commands.{AnsiColor.ENDC}") 

    







if __name__ == "__main__":
    main()







# region IMPORTS ========================================
import os
#from templates.py import Subject
import pyperclip
import requests

from Mod import AnsiColor
# bs4 import BeautifulSoup as BS

# endregion ============================================= 


class Template:

    class Descr:
        ticket_template = "INFORMATION\nUser: ()\nPhone:\nEmail:\nDept:\nRC:\n\nSUMMARY\nUser is calling because\n\n\nTROUBLESHOOTING\n-\n"

        password_reset = "User is having trouble signing into their account. The user seems to have forgotten their password."
        account_activation = "User is trying to activated their account but they are having trouble with the process.\nSome information could be incorrect or missing in our system."
        duo_add_device = "User has experienced an issue with adding a new device to their DUO mobile account. They need some guidance in adding their new phone."

    class Resol:
        password_reset = "Verified: SSN, DOB, Home Address\nReset password\nCleared security questions"
        account_activation = password_reset.replace("SSN", "Phone Number")
        duo_add_device = "Verified: SSN, DOB, Home Address\nAdded new device"
    
    #@classfield
    commands = {
        "tt": Descr.ticket_template,  

        "pr": Resol.password_reset,
        "pr -d": Descr.password_reset,

        "aa": Resol.account_activation,
        "aa -d": Descr.account_activation,

        "duo": Resol.account_activation,
        "duo -d": Descr.account_activation
    }

    @classmethod
    def get_command(self, cmd)-> str:
        return self.commands.get(cmd)


def main():
    # cleanup
    os.system("cls")

    # main loop
    while True:

        entry = input("|>>>>\t")

        if entry.endswith(" -v"):
            print(Template.get_command(entry.removesuffix(" -v")))
        elif entry.lower() == 'exit':
            break
        elif entry in Template.commands:
            template = Template.get_command(entry)
            pyperclip.copy(template)
            print(AnsiColor.OKGREEN+"Copied to Clipboard\n"+AnsiColor.ENDC)

        elif entry.startswith("rc" or "RC"):
            foo()
            #info = KnowledgeBase.searchRC()
            #print(info)

        else:
            print("Command not found. Type 'help' for a list of commands.") 

            
                       
main()











####################################################
# - - - - - M I S C.   F U N C T I O N S - - - - - #
####################################################

# Display for 'help' cmd

def print_help_menu():
    print(AnsiColor.OKBLUE+"""
    +------------------------------------------+
    |           TDX Template Helper            |
    |  --------------------------------------  |
    |  Preset Commands:                        |
    |  tt         - Display Ticket Template    |
    |  pr         - Password Reset Resolution  |
    |  pr -d      - Password Reset Description |
    |  aa         - Account Activation Resol.  |
    |  aa -d      - Account Activation Desc.   |
    |  duo        - DUO Add Device Resolution  |
    |  duo -d     - DUO Add Device Description |
    |                                          |
    |  Usage:                                  |
    |  Enter a command to retrieve the         |
    |  corresponding template. Add '-d' after  |
    |  a command code for the description      |
    |  template.                               |
    |                                          |
    |  Example:                                |
    |  >>>> pr                                 |
    |  (Retrieves the password reset resol.)   |
    |                                          |
    |  Additional Commands:                    |
    |  help       - Display this help menu     |
    |  exit       - Exit the program           |
    +------------------------------------------+
    """+AnsiColor.ENDC)

# Copy string to clipboard 
# and show success message to user
def copy_to_clipBoard(str):
    pyperclip.copy(str)
    print(AnsiColor.OKGREEN+"Copied to Clipboard\n"+AnsiColor.ENDC)






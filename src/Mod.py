'''
Mod.py is intended as a common file for misc imports and helper functions.
No functions allowed. Only classes with methods. 
'''
import pyperclip

# Display for 'help' cmd
def help():
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

# attempts to fix unformatted entry
def suggest(entry) -> str:
    # original
    entry = str(entry).lower()

    entry = entry.strip(' -')
    entry = "".join(entry.split())

    new_entry = str()

    for i in range(0, len(entry)):
        ch = entry[i]
        if ch.isalpha(): new_entry += ""+ch
        if ch == "-" and entry[i+1] and entry[i+1].isalpha():
            new_entry += ""+ch

    entry = new_entry.replace("-", " -")

    return entry

# turns string into set of args
def arguments(entry) -> list:
    # original
    entry = str(entry).lower().strip(' !@#$%^&*()_+<>,.?/-')

    
    entry = entry.split()

    return entry

# Copy string to clipboard 
# and show success message to user
def copy_to_clipboard(str):
    pyperclip.copy(str)
    print(AnsiColor.OKGREEN+"Copied to Clipboard\n"+AnsiColor.ENDC)

# Ansi Color codes for colored console printouts
class AnsiColor:
    HEADER = '\033[95m'     # Font Size
    OKBLUE = '\033[94m'     # Blue
    OKCYAN = '\033[96m'     # Cyan
    OKGREEN = '\033[92m'    # Green
    WARNING = '\033[93m'    #
    FAIL = '\033[91m'       # 
    ENDC = '\033[0m'        # Default (Usually White)
    BOLD = '\033[1m'        # Font Style
    UNDERLINE = '\033[4m'   # Font Style
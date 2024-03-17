'''
Mod.py is intended as a common file for misc imports and helper functions.
No functions allowed. Only classes with methods. 
'''
import pyperclip

# Display for 'help' cmd


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
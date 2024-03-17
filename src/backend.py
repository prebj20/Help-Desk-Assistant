# region IMPORTS ========================================
from Command import *
# endregion ============================================= 

USER = os.getlogin().replace(" ", "-").strip().lower()
# -------------------------------------------------------

# Loading Preset commands
reference = Command(name="info", type=Types.Template, 
               data="""Information for Reference

Sites:
	AWS Phone 	-> pi.tt/hdphone
	Admin Accounts 	-> https://admin.accounts.pitt.edu/
	TDX Ticketing 	-> pi.tt/TDNext

6 Points:
	1. User contact info (make sure to get extension if it's an office number)
	2. Device name, MAC and/or IP, OS version, + location and port address if needed
	3. Descriptive summary of the issue including time of occurrence and last successful use/access
	4. Troubleshooting steps YOU performed
	5. Results of troubleshooting with supporting screenshots
	6. Correct categorizations, including supported application.""")
password_reset = Command(name="pr", type=Types.Template, 
        data="User is having trouble signing into their account. The user seems to have forgotten their password.",
        data_2="Verified: SSN, DOB, Home Address\nReset password\nCleared security questions")
ticket_template = Command(
    name="tt", 
    type=Types.Template, 
    data="""INFORMATION
Caller:
Phone:
Email:
Department:
RC:


SUMMARY
User is calling because 


TROUBLESHOOTING""")
kb_search = Command(name="kb", type=Types.KnowledgeBase)
windows = Command(name="win", type=Types.Windows)

preset_commands = []
preset_commands.append(password_reset)
preset_commands.append(ticket_template)
preset_commands.append(kb_search)
preset_commands.append(windows)
preset_commands.append(reference)

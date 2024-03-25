import tkinter as tk
import GUIColors as c
from backend import *
import json as js


ROOT_WIDTH = 950
ROOT_HEIGHT = 1000

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Help Desk Assistant")
        self.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")
        self.config(bg=c.ROOT_BG)
        
        self.actv_btns = list() # For storing dynamic buttons
        self.pasteMode = tk.BooleanVar()
        self.pasteMode.set(False)

        self.custom_templates = []
        


        self.build_header()
        self.build_display()
        self.build_cmd_line()
        self.build_custom_menu()

        self.load_custom_templates()

        

    # Building Elements
    def build_header(self):
        #  HEADER 
        self.header = tk.Frame(self, width=ROOT_WIDTH, height=75, background=c.HEADER_BG)
        self.header.pack(fill=tk.X)
        self.header.pack_propagate(False)

        # HEADER BUTTONS
        self.add_header_btn("Logout", self.destroy)
        self.theme_button = self.add_header_btn("Dark Mode", self.toggle_theme)

        # CLEAR DISPLAY BTN
        self.clear_display = self.add_header_btn("Clear Display", None)
        

        # Function to set the command once display is available
        def set_clear_command():
            if hasattr(self, 'display') and callable(getattr(self.display, 'clear', None)):
                self.clear_display.config(command=self.display.clear)
            else: self.header.after(100, set_clear_command)

        self.header.after(100, set_clear_command)

    def build_display(self):
        # DISPLAY FRAME
        self.display_frame = tk.Frame(self, width=ROOT_WIDTH, height=300, bg='BLACK', relief='sunken', borderwidth=2)  # Height in pixels
        self.display_frame.pack(fill='both', expand=False)  # Fill and expand can be adjusted based on your layout needs
        self.display_frame.pack_propagate(False)  # Prevent the frame from resizing based on the Text widget

        # DISPLAY FRAME SCROLLBAR
        self.scrollbar = tk.Scrollbar(self.display_frame, orient='vertical', width=10, relief='solid')
        self.scrollbar.pack(side='right', fill='y')

        # ACTUAL DISPLAY
        self.display = Text(self.display_frame, width=100, height=15, relief='sunken', bg=c.DSPLY_LBG, bd=4, fg=c.DSPLY_LFG, font=("Segoe UI", 10), state="disabled")
        self.display.pack(side='left', fill='both', expand=True)  # Make the Text widget fill the display frame

        # HEADER TITLE
        self.title = tk.Label(self.header, fg='BLACK', bg=c.HEADER_BG, text="Pitt IT Help Desk", font=("Times New Roman",18))
        self.title.pack(side="left", anchor='n', fill='y', padx=150)

        self.display.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.display.yview)

        # Add some initial text to the Text widget
        self.display.append(f"Logged in as: <{os.getlogin()}>")
    def build_cmd_line(self):
        # CMD LINE FRAME
        self.cmd_line_frame = tk.Frame(self, borderwidth=0, relief="flat", height=35, bg=c.ROOT_BG)
        self.cmd_line_frame.pack(anchor="w", padx=3, pady=(3,25), fill="x")
        self.cmd_line_frame.pack_propagate(False)

        # CMD LINE LABEL
        self.cmd_line_label = tk.Label(self.cmd_line_frame, text=" CMD: ", bg=c.HEADER_BG, relief="flat", )
        self.cmd_line_label.pack(side="left", fill="y")

        # CMD LINE
        self.cmd_line = tk.Entry(master=self.cmd_line_frame, bg="BLACK", fg="LIME", font=("Consolas", 12), insertbackground="LIME")
        self.cmd_line.bind("<Return>", lambda e: self.process_cmd(self.cmd_line.get()))
        self.cmd_line.pack(side="left", fill="y")
    def build_custom_menu(self):
        self.cm_frame = tk.Frame(self, borderwidth=2, relief="raised", bg=c.ROOT_BG)
        self.cm_frame.pack(fill="both", expand=True)

        self.label_frame = tk.Frame(self.cm_frame, bg=c.ROOT_BG)
        self.label_frame.pack()

        self.label = tk.Label(master=self.label_frame, text="Custom Templates", fg='BLACK', bg=c.ROOT_BG, height=1)
        self.label.pack(side='left')

        self.add_custom_btn = tk.Button(self.label_frame, text="+", width=1, fg='LIME', bg='GRAY', relief='solid', command=self.customs_form, font=("Times New Roman", 8))
        self.add_custom_btn.pack(side='right')

        temp: Command
        for temp in self.custom_templates:
            btn = tk.Button(self.cm_frame, text=temp.name, width=10, height=2, background="SILVER", relief="raised", bd=3, command=lambda: Types.Template.function(self, temp), activebackground=c.BTN_BG_ACTV)
            btn.pack(side="top", anchor="w", padx=5, pady=5)
        #def load_customs(self):




    # HELPER METHODS
    def add_header_btn(self, text, command):
        btn = tk.Button(self.header, text=text, width=10, height=2, background="SILVER", relief="raised", bd=3, command=command, activebackground=c.BTN_BG_ACTV)
        btn.bind("<Enter>", lambda e: e.widget.config(bg=c.BTN_BG_HVR))
        btn.bind("<Leave>", lambda e: e.widget.config(bg=c.BTN_BG))
        btn.pack(side=tk.LEFT, pady=5, padx=5)
        return btn
    def toggle_theme(self):
        if self.display.cget('bg') == c.DSPLY_DBG:
            self.theme_button.config(text="Dark Mode")
            self.display.config(bg=c.DSPLY_LBG, fg=c.DSPLY_LFG)
        else:
            self.theme_button.config(text="Light Mode")
            self.display.config(bg=c.DSPLY_DBG, fg=c.DSPLY_DFG)
    def process_cmd(self, entry):
        args = arguments(entry)

        # Exit/Help Check
        if args[0] == "help": self.display.append(help()) 
        elif find_command(preset_commands, args[0]):
            cmd = find_command(preset_commands, args[0])
            cmd.args = args
            cmd.type.function(app, cmd)
        else:
            self.display.append("Invalid Command.")
        self.cmd_line.delete(0, tk.END)
    def destroy_actv_buttons(self):
        for btn in app.actv_btns:
            btn.destroy()

        self.cmd_line.delete(0, tk.END)
    def q(self, text, data):
        btn = tk.Button(self.cmd_line_frame, text=text, height=2, background="SILVER", relief="raised", bd=3, command=lambda d=data:copy_paste(app, d), activebackground=c.BTN_BG_ACTV)
        btn.bind("<Enter>", lambda e: e.widget.config(bg=c.BTN_BG_HVR))
        btn.bind("<Leave>", lambda e: e.widget.config(bg=c.BTN_BG))
        btn.pack(side="left", padx=(5,0))
        self.actv_btns.append(btn)
    
    def paste_switch(self):
        self.paste_lock = tk.Checkbutton(master=self.cmd_line_frame, text="Scroll-Wheel Paste", bg="SILVER", variable=self.pasteMode)
        self.paste_lock.pack(side="left", padx=(5,0))
        self.actv_btns.append(self.paste_lock)
    def customs_form(self):
        self.form = tk.Tk()
        self.form.title("Custom Template Form")
        self.form.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT//2}")
        self.form.config(bg=c.ROOT_BG)

        entry_frame = tk.Frame(self.form, bg=c.ROOT_BG); entry_frame.pack(pady=(10,0))
        entry_label = tk.Label(entry_frame, bg=c.HEADER_BG, fg='BLACK', text="Name: ")
        entry_label.pack(side="left")
        self.name = tk.Entry(entry_frame); self.name.pack()

        entry_frame = tk.Frame(self.form, bg=c.ROOT_BG); entry_frame.pack(pady=(10,0))
        entry_label = tk.Label(entry_frame, bg=c.HEADER_BG, fg='BLACK', text="Description: ")
        entry_label.pack(side="left")
        self.descr = tk.Text(entry_frame, height=10); self.descr.pack()

        entry_frame = tk.Frame(self.form, bg=c.ROOT_BG); entry_frame.pack(pady=(10,0))
        entry_label = tk.Label(entry_frame, bg=c.HEADER_BG, fg='BLACK', text="Resolution: ")
        entry_label.pack(side="left")
        self.resol = tk.Text(entry_frame, height=10); self.resol.pack()

        submit = tk.Button(self.form, text="Submit", width=10, height=2, background="SILVER", relief="raised", bd=3, command=self.create_custom, activebackground=c.BTN_BG_ACTV)
        submit.pack()

    def create_custom(self):
        

        template = Command(name=self.name.get(), data=self.descr.get("1.0", tk.END), data_2=self.resol.get("1.0", tk.END), type=Types.Template)
        if(template.name.strip() == ""): return

        self.custom_templates.append(template)
        data = self.command_to_dict()
        write_user_data(data, filename="user_data.json")
        self.form.destroy()

        submit = tk.Button(self.cm_frame, text=template.name, width=10, height=2, background="SILVER", relief="raised", bd=3, command=lambda: Types.Template.function(self, template), activebackground=c.BTN_BG_ACTV)
        submit.pack(side="top", anchor="w", padx=5, pady=5)


    def command_to_dict(self) -> list:
        dict_commands = []
        cmd: Command
        
        for cmd in self.custom_templates:
            d = {
                'name': cmd.name,
                'data': cmd.data,
                'data_2': cmd.data_2,
            }
            dict_commands.append(d)
        return dict_commands

    def load_custom_templates(self, filename="user_data.json"):
        try:
            with open(filename, "r") as file:
                data = js.load(file)  # It should be json.load, not js.load

                if not data or not isinstance(data, list):
                    return

                for entry in data:
                    command = Command(
                        name=entry["name"],
                        type=Types.Template,  # Assuming all commands are of this type
                        data=entry.get("data"),  # Use .get to avoid KeyError if the key is missing
                        data_2=entry.get("data_2")
                    )
                    self.custom_templates.append(command)

                    # Create a button for each command and ensure lambda captures the current command's value
                    button = tk.Button(self.cm_frame, text=command.name, width=10, height=2, background="SILVER", relief="raised", bd=3, command=lambda cmd=command: Types.Template.function(self, cmd), activebackground=c.BTN_BG_ACTV)
                    button.pack(side="top", anchor="w", padx=5, pady=5)

        except FileNotFoundError:
            print(f"File {filename} not found.")
        except js.JSONDecodeError:
            print("Error decoding JSON from file. The file may be empty or contain invalid JSON.")

def write_user_data(commands, filename="user_data.json"):
    with open(filename, "w") as user_data:
        data_to_write = [command for command in commands]
        js.dump(data_to_write, user_data, indent=4)

    



# Custom Textbox Object
class Text(tk.Text):
    def append(self, text):
        self.config(state="normal")
        self.insert("end", f"{text}\n")
        self.config(state="disabled")

    def clear(self):
        self.config(state="normal")
        self.delete('1.0', tk.END)
        self.config(state="disabled")
        for btn in app.actv_btns:
            btn.destroy()

    def replace(self, text):
        self.clear()
        self.append(text)

if __name__ == "__main__":
    app = Application()
    app.mainloop()

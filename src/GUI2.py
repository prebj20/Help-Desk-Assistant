import tkinter as tk
import os
import pyperclip
import GUIColors as c
from backend import preset_commands, find_command, arguments

ROOT_WIDTH = 1200
ROOT_HEIGHT = 1000

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Help Desk Assistant")
        self.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")
        self.config(bg=c.ROOT_BG)
        self.actv_btns = []

        self.create_header()
        self.create_display_frame()
        self.create_cmd_line_frame()
        self.display_initial_text()

    def create_header(self):
        self.header = tk.Frame(self, width=ROOT_WIDTH, height=75, background=c.HEADER_BG)
        self.header.pack(fill=tk.X)
        self.header.pack_propagate(False)

        self.add_header_btn("Logout", self.destroy)
        self.theme_button = self.add_header_btn("Dark Mode", self.toggle_theme)
        
        self.title = tk.Label(self.header, fg=c.ROOT_BG, bg=c.HEADER_BG, text="Pitt IT Help Desk", font=("Times New Roman", 18))
        self.title.pack(side="left", pady=25, padx=225)

    def create_display_frame(self):
        self.display_frame = tk.Frame(self, width=ROOT_WIDTH, height=300, bg="BLACK", relief="sunken", borderwidth=2)
        self.display_frame.pack(fill='both', expand=False)
        self.display_frame.pack_propagate(False)

        scrollbar = tk.Scrollbar(self.display_frame, orient='vertical', width=10, relief='solid')
        scrollbar.pack(side='right', fill='y')

        self.display = Text(self.display_frame, width=100, height=15, relief="sunken", bg=c.DSPLY_LBG, bd=4, fg=c.DSPLY_LFG, font=("Segoe UI", 10), state="disabled")
        self.display.pack(side='left', fill='both', expand=True)
        self.display.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.display.yview)

    def create_cmd_line_frame(self):
        self.cmd_line_frame = tk.Frame(self, borderwidth=0, relief="flat", height=35, bg=c.ROOT_BG)
        self.cmd_line_frame.pack(anchor="w", padx=3, pady=3, fill="x")
        self.cmd_line_frame.pack_propagate(False)

        self.cmd_line_label = tk.Label(self.cmd_line_frame, text=" CMD: ", bg=c.HEADER_BG, relief="flat")
        self.cmd_line_label.pack(side="left", fill="y")

        self.cmd_line = tk.Entry(master=self.cmd_line_frame, bg="BLACK", fg="LIME", font=("Consolas", 12), insertbackground="LIME")
        self.cmd_line.bind("<Return>", lambda e: self.process_cmd(self.cmd_line.get()))
        self.cmd_line.pack(side="left", fill="y")

    def display_initial_text(self):
        self.display.append(f"Logged in as: <{os.getlogin()}>")

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
        if args[0] == "help": 
            self.display.append(help()) 
        elif (cmd := find_command(preset_commands, args[0])):
            cmd.args = args
            cmd.type.function(self, cmd)
        else:
            self.display.append("Invalid Command.")
        self.cmd_line.delete(0, tk.END)
    
    def q(self, text, data):
        btn = tk.Button(self.cmd_line_frame, text=text, height=2, background="SILVER", relief="raised", bd=3, command=lambda d=data: pyperclip.copy(d), activebackground=c.BTN_BG_ACTV)
        btn.pack(side="left", padx=(5,0))
        self.actv_btns.append(btn)

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

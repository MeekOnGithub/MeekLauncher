import core.launch
import core.config
import core.versions
import os
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk


def main():
    print("load launch page")

    def start():
        """
        This function is used to launch a game,
        """
        command = core.launch.launch(core.config.read()[".mc"], launch_version.get(), core.config.read()["java"],
                                     core.config.read()["playername"], core.config.read()["ram"])
        print(command)
        if command == 0:
            tk.messagebox.showerror("Null.")
        elif command == 1:
            tk.messagebox.showerror("Error", "This is not a complete game.")
        else:
            if os.system(command) != 0:
                tk.messagebox.showerror("Error", "Unable to launch. \nPlease upload the logs to issue.")

    def drop():
        # refresh version choose
        launch_version["values"] = core.versions.local_version(core.config.read()[".mc"])

    launch_view = tk.ttk.Frame()
    launch_title = tk.ttk.Label(launch_view, text="FMCL", font=("Arial", 20))
    launch_title.place(x=20, y=5)

    launch_about = tk.ttk.Label(launch_view,
                                text="FMCL is a free minecraft launcher.\n" \
                                     "Version: Public preview 3\n" \
                                     "Author:  Sharll\n" \
                                     "Do not decompile or crack this software",

                                font=("Arial", 12))
    launch_about.place(x=20, y=35)
    launch_launch = tk.ttk.Button(launch_view, text="launch", width=20, command=start)
    launch_launch.place(x=200, y=200)
    launch_version = tk.ttk.Combobox(launch_view, postcommand=drop)
    launch_version.place(x=20, y=200)

    return launch_view

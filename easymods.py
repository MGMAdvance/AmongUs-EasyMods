from mods import TownOfUs
from tkinter import Tk, Label, Button, mainloop
import check
import uninstall

path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Among Us\\"
window = Tk(className="EasyMods - for fast install Among Us mods")

window.geometry("300x300")

def install_town():
    if check.check_amongus_exe(path):
        townBtn = Label(window, text="Installing Town of Us...")
        townBtn.pack()

        town = TownOfUs.TownOfUs(path)
        town.run()
        townBtn = Label(window, text="Town of Us installed!")
        townBtn.pack()

def remove_mods():
    if check.check_amongus_exe(path):
        uninstall.Uninstall(path).uninstall_mods()
        
        modsBtn = Label(window, text="Removed mods!")
        modsBtn.pack()

installButton = Button(window, 
            text="Install Town of Us", 
            command=install_town)
installButton.pack()

removeButton = Button(window, 
            text="Remove Mods", 
            command=remove_mods)
removeButton.pack()

window.mainloop()
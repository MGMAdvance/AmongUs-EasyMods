import shutil
import os.path

class Uninstall:
    def __init__(self, path):
        self.folder = path

    def uninstall_mods(self):
        if os.path.isdir(self.folder):
            try:
                shutil.rmtree(self.folder + "BepInEx")
                shutil.rmtree(self.folder + "Assets")
                shutil.rmtree(self.folder + "mono")

                os.remove(self.folder + "doorstop_config.ini")
                os.remove(self.folder + "winhttp.dll")
                
                print("Mods removed")
            except OSError as error:
                print(error)
                print("Not possible to remove mods")

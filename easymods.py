from mods import TownOfUs
import check

path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Among Us\\"

if check.check_amongus_exe(path):
    town = TownOfUs.TownOfUs(path)
    town.run()
import os.path

def check_amongus_exe(path):
    if os.path.isfile(path + '\\Among Us.exe'):
        print("Found Among Us.exe")
        return True
    else:
        print("Not found Among Us.exe")
        return False
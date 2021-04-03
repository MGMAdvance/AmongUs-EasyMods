import os.path
import requests
import zipfile

class TownOfUs:
    RELEASE_URL = "https://api.github.com/repos/slushiegoose/Town-Of-Us/releases"
    link = ""
    filename = "townofus.zip"

    def __init__(self, path):
        self.folder = path

    def latest_link(self):
        req = requests.get(self.RELEASE_URL)
        pack = req.json()
        self.link = pack[0]["assets"][0]["browser_download_url"]

    def clean_up(self):
        folder = self.folder + self.filename
        
        if os.path.isfile(folder):
            os.remove(folder)

    def download(self):
        req = requests.get(self.link)

        with open(self.folder + self.filename, 'wb') as file:
            file.write(req.content)

    def extract_zip(self):
        folder = self.folder + self.filename

        with zipfile.ZipFile(folder, 'r') as zip_ref:
            zip_ref.extractall(self.folder)

    def run(self):
        self.latest_link()
        self.clean_up()
        self.download()
        self.extract_zip()
        self.clean_up()
        print("Town of Us installed!")
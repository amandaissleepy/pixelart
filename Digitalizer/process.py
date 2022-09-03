import glob
import os
import shutil
from PIL import Image

class Digitizer:
    def __init__(self, filepath):
        self.filepath = filepath
    def make_upside_down(self):
        print("make upside down")
    def save(self, output_filepath):
        shutil.copyfile(self.filepath, output_filepath)
        print("this have saved")

inputs = glob.glob("inputs/*.jpg")

os.makedirs("outputs", exist_ok=True)

for filepath in inputs:
    output = filepath.replace("inputs", "outputs")
    image = Digitizer(filepath)
    image.make_upside_down()
    image.save(output)

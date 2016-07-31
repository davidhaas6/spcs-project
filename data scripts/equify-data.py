import os
from glob import glob

test_data = './test-data/'
data = './data/'
# Array of font files w/ paths
font_files = [y for x in os.walk(data) for y in glob(os.path.join(x[0], '*.png'))]

# Makes data folder
for font in font_files:
    if not os.path.exists(test_data + font[font.rfind('/'):]):
        print font
        os.remove(font)

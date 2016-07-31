from PIL import Image, ImageDraw, ImageFont, ImageChops
from string import ascii_uppercase
import os
from random import randint
from glob import glob

fontsize = 30
fontdirectory = './fonts/'
imgdirectory = './test-data/'
mode = 'L'  # Allows anti-aliasing for the fonts
char_img_dimensions = (50, 60)  # dimension of bounding box for each letter

# Array of font files w/ paths
font_files = [y for x in os.walk(fontdirectory) for y in glob(os.path.join(x[0], '*.ttf'))]

# Makes data folder
if not os.path.exists(imgdirectory):
    os.makedirs(imgdirectory)

for font_file in font_files:
    if font_file.endswith(".ttf"):
        # Load the font for printing
        font = ImageFont.truetype(font_file, fontsize)

        # Makes sure it's not an italic or bold font, as well as excluding a problematic font family
        if 'Regular' in font.getname()[1] and 'Lao' not in font.getname()[0]:

            # Generates a blank canvas in which the letters will be pasted onto
            alphabet_img = Image.new(mode, (char_img_dimensions[0] * 26, char_img_dimensions[1]), "white")

            try:
                # Cycles through each uppercase letter
                for i in range(len(ascii_uppercase)):
                    if i < 2 or randint(1, 4) != 2:
                        ltr = ascii_uppercase[i]

                        # Instantiates a blank image for the specific letter
                        img = Image.new(mode, char_img_dimensions, "white")
                        draw = ImageDraw.Draw(img)

                        # A tuple of the dimensions in pixels for the letter
                        ltr_size = font.getsize(ltr)

                        (x_dimension, y_dimension) = char_img_dimensions

                        # Offset for the letter... seems like it should be useful
                        (x_offset, y_offset) = font.getoffset(ltr)

                        # Makes the letter generally centered in it's bounding box
                        ltr_location = ((x_dimension - ltr_size[0]) / 2 - x_offset, (y_dimension - ltr_size[1]) / 2)

                        # Draws the letter to its blank image
                        draw.text(ltr_location, ltr, font=font)

                        # Pastes the letter image onto the bigger canvas in order
                        ltr_num = ascii_uppercase.index(ltr)
                        alphabet_img.paste(img, (x_dimension * ltr_num, 0))

                # first condition makes sure the picture isn't blank
                # second condition makes sure the letters aren't just boxes
                if ImageChops.invert(alphabet_img).getbbox() and alphabet_img.histogram()[1] is not 0:
                    alphabet_img.save(imgdirectory + font.getname()[0] + '_' + font.getname()[1] + '.png')
            except IOError as e:
                print('IOError on font:', font.getname()[0] + '. Woops!\t\t', e)

# set font directory
# for-each for each ttf file
#   for loop A-Z all caps for each file
#       make a Image for each letter
#           center each letter in img based of off font.getsize(txt)
#   concatenate each image to form a long image of each letter in the font A-Z
#   save image as fontname.png

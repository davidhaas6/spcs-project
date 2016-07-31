from PIL import Image, ImageDraw, ImageFont, ImageChops
from string import ascii_uppercase
import os
from glob import glob

# http://stackoverflow.com/questions/10647311/how-do-you-merge-images-using-pil-pillow
fontsize = 30
fontdirectory = './fonts/'
imgdirectory = './data/'
mode = 'L'
char_img_dimensions = (50, 60)

font_files = [y for x in os.walk(fontdirectory) for y in glob(os.path.join(x[0], '*.ttf'))]
# font_files = font_files[:1500]

for font_file in font_files:
    if font_file.endswith(".ttf"):
        font = ImageFont.truetype(font_file, fontsize)
        if 'Regular' in font.getname()[1] and 'Lao' not in font.getname()[0]:
            alphabet_img = Image.new(mode, (char_img_dimensions[0] * 26, char_img_dimensions[1]), "white")
            ltr_img_arr = []
            try:
                for ltr in ascii_uppercase:
                    img = Image.new(mode, char_img_dimensions, "white")
                    draw = ImageDraw.Draw(img)
                    ltr_size = font.getsize(ltr)
                    (x_dimension, y_dimension) = char_img_dimensions
                    (x_offset, y_offset) = font.getoffset(ltr)
                    ltr_location = ((x_dimension - ltr_size[0]) / 2 - x_offset, (y_dimension - ltr_size[1]) / 2)
                    draw.text(ltr_location, ltr, font=font)

                    ltr_img_arr.append(img)
                    ltr_num = ascii_uppercase.index(ltr)
                    alphabet_img.paste(img, (x_dimension * ltr_num, 0))
                # first condition makes sure the picture isn't blank
                # second condition makes sure the letters aren't just boxes (maybeee :])
                if ImageChops.invert(alphabet_img).getbbox() and alphabet_img.histogram()[1] is not 0:
                    alphabet_img.save(imgdirectory + font.getname()[0] + '_' + font.getname()[1] + '.png')
            except IOError:
                print 'IOError on font:', font.getname()[0] + '. Woops!'

'''
font = ImageFont.truetype(fontname, fontsize)
img = Image.new("RGBA", (14, 22), "white")
draw = ImageDraw.Draw(img)
draw.text((0, -0), txt, (0, 0, 0), font=font)
# draw = ImageDraw.Draw(img)
print font.getsize(txt)
img.save("a_test.png")
'''

# set font directory
# for-each for each ttf file
#   for loop A-Z all caps for each file
#       make a Image for each letter
#           center each letter in img based of off font.getsize(txt)
#   concatenate each image to form a long image of each letter in the font A-Z
#   save image as fontname.png

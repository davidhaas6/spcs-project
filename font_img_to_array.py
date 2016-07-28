from PIL import Image
import numpy as np
import glob
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def img_to_brightness(imgname):
    # Takes in the image and converts it to greyscale
    im = Image.open(imgname).convert('LA')

    im.show()
    # Converts PIL image into a np array consisting of [brightness, alpha] values
    data = np.asarray(im)
    print(data[0])
    print('Data shape:', data.shape)

    # The 2d array which will hold the brightness values
    pic = []

    for row in data:
        new_row = []
        for val in row:
            # Only adds the brightness value to the new row
            new_row.append(val[0]/255.)
        # Appends the new row to the picture
        pic.append(new_row)
    print(pic)
    return pic


data_path = 'test-data/'
images = glob.glob(data_path + "*.png")
total_img_count = len(images)
(img_width, img_height) = Image.open(images[0]).getdata().size

x = np.ndarray(shape=(total_img_count, 1, img_height, img_width), dtype=np.float32)

# how to add new indices: x[pic_index, channel_num (should always be 0), 0:img_height,0:img_width] = img_0
for i in range(len(images)):
    x[i, 0, :img_height, :img_width] = img_to_brightness(images[i])
    if i % 10 == 0:
        print(float(i)/total_img_count * 100, '%')
np.save('test_font_arr', x)

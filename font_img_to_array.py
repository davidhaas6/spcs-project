from PIL import Image
import numpy as np
import glob


def img_to_brightness(imgname):
    im = Image.open(imgname).convert('LA')
    data = np.asarray(im)
    pic1 = []
    for row in data:
        new_row = []
        for val in row:
            new_row.append(val[0]/255.)
        pic1.append(new_row)
    return pic1

b_vals = []
b_vals.append(img_to_brightness('a_test.png'))
b_vals = np.asarray(b_vals)

data_path = 'data/'
images = glob.glob(data_path + "*.png")
total_img_count = len(images)
(img_width, img_height) = Image.open(images[0]).getdata().size

x = np.ndarray(shape=(total_img_count, 1, img_height, img_width), dtype=np.float32)


# how to add new indices: x[pic_index, channel_num (should always be 0), 0:img_height,0:img_width] = img_0
for i in range(len(images)):
    x[i, 0, :img_height, :img_width] = img_to_brightness(images[i])
    if i % 10 == 0:
        print float(i)/total_img_count * 100, '%'
np.save('font_arr', x)
print(img_to_brightness('a_test.png'))

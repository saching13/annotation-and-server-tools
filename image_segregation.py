from __future__ import division
import time
import cv2
import pickle
import glob
import os

input_folder = '/Users/harshkn/datasets/New_Images'

# folder name, key press
types = [
    ('yawning', 'y'),
    ('with_tray', 'w'),
    ('eye_closed', 'c'),
    ('eye_opened', 'o')
]

req_width = 1000
fn_i = 0
key_i = 1

files = glob.glob(input_folder + '/*')
just_keys = [ord(keys[key_i]) for keys in types]


def write_text(img, loc, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, loc, font, 1, (255, 255, 255), 2)


for each_type in types:
    full_folder = os.path.join(input_folder, each_type[fn_i])
    if not os.path.exists(full_folder):
        os.makedirs(full_folder)

for each_file in files:
    pro_image = cv2.imread(each_file)
    just_file_name = os.path.basename(each_file)
    # full_path = os.path.join(input_folder, just_file_name)

    if pro_image.shape[1] > req_width:
        resize_scale = req_width / pro_image.shape[1]
        resize_h = int(resize_scale * pro_image.shape[0])
        resize_w = int(resize_scale * pro_image.shape[1])
        resized_image = cv2.resize(pro_image, (resize_w, resize_h))

        # cv2.imwrite(full_path, resized_image)
        # cv2.imwrite(full_path_flipped, flipped_image)

        print(just_file_name)
    else:
        resized_image = pro_image
    # show the frame
    for ind, each_type in enumerate(types):
        loc_ind = ind + 1
        write_text(resized_image, (10, loc_ind * 25), (each_type[key_i] + '  ' + each_type[fn_i]))

    cv2.imshow("Frame", resized_image)
    key = cv2.waitKey(5000) & 0xFF
    while key not in just_keys:
        key = cv2.waitKey(1000) & 0xFF

    ind = just_keys.index(key)
    full_image_path = os.path.join(input_folder, types[ind][fn_i], just_file_name)
    print(full_image_path)
    cv2.imwrite(full_image_path, pro_image)




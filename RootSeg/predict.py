import copy
import os
import numpy as np
from PIL import Image
from RootSeg.RootSeg import RootSeg

if __name__ == "__main__":
    class_colors = [[0, 0, 0], [0, 255, 0]]
    # input image size
    HEIGHT = 512
    WIDTH = 512
    # background + root = 2
    NCLASSES = 2
    # example: logs/ep059-loss0.005-val_loss0.029.h5
    weight_path = ""
    test_img_path = ""
    predict_out_path = ""

    model = RootSeg(n_classes=NCLASSES, input_height=HEIGHT, input_width=WIDTH)
    model.load_weights(weight_path)

    imgs = os.listdir(test_img_path)
    for jpg in imgs:
        img = Image.open(test_img_path + jpg)

        old_img = copy.deepcopy(img)
        orininal_h = np.array(img).shape[0]
        orininal_w = np.array(img).shape[1]

        img = img.resize((WIDTH, HEIGHT), Image.BICUBIC)
        img = np.array(img) / 255
        img = img.reshape(-1, HEIGHT, WIDTH, 3)

        pr = model.predict(img)[0]
        pr = pr.reshape((int(HEIGHT), int(WIDTH), NCLASSES)).argmax(axis=-1)

        seg_img = np.zeros((int(HEIGHT), int(WIDTH), 3))
        for c in range(NCLASSES):
            seg_img[:, :, 0] += ((pr[:, :] == c) *
                                 class_colors[c][0]).astype('uint8')
            seg_img[:, :, 1] += ((pr[:, :] == c) *
                                 class_colors[c][1]).astype('uint8')
            seg_img[:, :, 2] += ((pr[:, :] == c) *
                                 class_colors[c][2]).astype('uint8')

        seg_img = Image.fromarray(np.uint8(seg_img)).resize(
            (orininal_w, orininal_h))
        image = Image.blend(old_img, seg_img, 0.3)

        image.save(predict_out_path + jpg)

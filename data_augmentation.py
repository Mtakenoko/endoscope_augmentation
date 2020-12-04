import os
import shutil
import cv2
import numpy as np

path = "eyemodel_train"
path_raw = "eyemodel_train_raw"

if os.path.exists(path):
    print('delete directory...')
    shutil.rmtree(path)
os.mkdir(path)

files = os.listdir(path_raw)
files_dir = [f for f in files if os.path.isdir(os.path.join(path_raw, f))]

for count, dir in enumerate(files_dir, 1):
    print('creating /'+ dir +' Images...'+ '  (' + str(count) + '/' + str(len(files_dir)) + ')')
    if not os.path.exists(path + '/' + dir):
        os.mkdir(path + '/' + dir)
    images = os.listdir(path_raw+'/'+ dir)
    images_files = [i for i in images if os.path.isfile(os.path.join(path_raw +'/'+ dir, i))]

    for i in images_files:
        base, ext = os.path.splitext(i)
        if ext == '.jpg':
            color_img = cv2.imread(path_raw + '/' + dir +'/' + base +'.jpg')
            depth_img = cv2.imread(path_raw + '/' + dir +'/' + base +'.png')
            
            # 画像の回転
            color_img_rotate_90_clockwise = cv2.rotate(color_img, cv2.ROTATE_90_CLOCKWISE)
            depth_img_rotate_90_clockwise = cv2.rotate(depth_img, cv2.ROTATE_90_CLOCKWISE)
            color_img_rotate_180_clockwise = cv2.rotate(color_img, cv2.ROTATE_180)
            depth_img_rotate_180_clockwise = cv2.rotate(depth_img, cv2.ROTATE_180)
            color_img_rotate_270_clockwise = cv2.rotate(color_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            depth_img_rotate_270_clockwise = cv2.rotate(depth_img, cv2.ROTATE_90_COUNTERCLOCKWISE)

            # 画像の上下左右反転
            color_img_flip_ud = cv2.flip(color_img, 0)
            depth_img_flip_ud = cv2.flip(depth_img, 0)
            color_img_flip_lr = cv2.flip(color_img, 1)
            depth_img_flip_lr = cv2.flip(depth_img, 1)
            color_img_flip_udlr = cv2.flip(color_img, -1)
            depth_img_flip_udlr = cv2.flip(depth_img, -1)

            # 画像の色彩変更
            hsv_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
            img_h, img_s, img_v = cv2.split(hsv_img)
            stride = 8
            hsv_img_1 = cv2.merge(((img_h + stride*1) % 255, img_s, img_v))
            hsv_img_2 = cv2.merge(((img_h + stride*2) % 255, img_s, img_v))
            hsv_img_3 = cv2.merge(((img_h + stride*3) % 255, img_s, img_v))
            hsv_img_4 = cv2.merge(((img_h + stride*4) % 255, img_s, img_v))
            hsv_img_5 = cv2.merge(((img_h + stride*5) % 255, img_s, img_v))
            hsv_img_6 = cv2.merge(((img_h + stride*6) % 255, img_s, img_v))
            hsv_img_7 = cv2.merge(((img_h + stride*7) % 255, img_s, img_v))
            hsv_img_8 = cv2.merge(((img_h + stride*8) % 255, img_s, img_v))
            hsv_img_9 = cv2.merge(((img_h + stride*9) % 255, img_s, img_v))
            hsv_img_10 = cv2.merge(((img_h + stride*10) % 255, img_s, img_v))
            color_img_1 = cv2.cvtColor(hsv_img_1, cv2.COLOR_HSV2BGR)
            color_img_2 = cv2.cvtColor(hsv_img_2, cv2.COLOR_HSV2BGR)
            color_img_3 = cv2.cvtColor(hsv_img_3, cv2.COLOR_HSV2BGR)
            color_img_4 = cv2.cvtColor(hsv_img_4, cv2.COLOR_HSV2BGR)
            color_img_5 = cv2.cvtColor(hsv_img_5, cv2.COLOR_HSV2BGR)
            color_img_6 = cv2.cvtColor(hsv_img_6, cv2.COLOR_HSV2BGR)
            color_img_7 = cv2.cvtColor(hsv_img_7, cv2.COLOR_HSV2BGR)
            color_img_8 = cv2.cvtColor(hsv_img_8, cv2.COLOR_HSV2BGR)
            color_img_9 = cv2.cvtColor(hsv_img_9, cv2.COLOR_HSV2BGR)
            color_img_10 = cv2.cvtColor(hsv_img_10, cv2.COLOR_HSV2BGR)

            # GrayScaleに変換
            depth_img = cv2.cvtColor(depth_img, cv2.COLOR_BGR2GRAY)
            depth_img_rotate_90_clockwise = cv2.cvtColor(depth_img_rotate_90_clockwise, cv2.COLOR_BGR2GRAY)
            depth_img_rotate_180_clockwise = cv2.cvtColor(depth_img_rotate_180_clockwise, cv2.COLOR_BGR2GRAY)
            depth_img_rotate_270_clockwise = cv2.cvtColor(depth_img_rotate_270_clockwise, cv2.COLOR_BGR2GRAY)
            depth_img_flip_ud = cv2.cvtColor(depth_img_flip_ud, cv2.COLOR_BGR2GRAY)
            depth_img_flip_lr = cv2.cvtColor(depth_img_flip_lr, cv2.COLOR_BGR2GRAY)
            depth_img_flip_udlr = cv2.cvtColor(depth_img_flip_udlr, cv2.COLOR_BGR2GRAY)

            # eyemodel_trainディレクトリに全て格納
            cv2.imwrite(path + '/' + dir + '/' + base +'.jpg', color_img)
            cv2.imwrite(path + '/' + dir + '/' + base +'.png', depth_img)
            cv2.imwrite(path + '/' + dir + '/' + base + '_90' +'.jpg', color_img_rotate_90_clockwise)
            cv2.imwrite(path + '/' + dir + '/' + base + '_90' +'.png', depth_img_rotate_90_clockwise)
            cv2.imwrite(path + '/' + dir + '/' + base + '_180' +'.jpg', color_img_rotate_180_clockwise)
            cv2.imwrite(path + '/' + dir + '/' + base + '_180' +'.png', depth_img_rotate_180_clockwise)
            cv2.imwrite(path + '/' + dir + '/' + base + '_270' +'.jpg', color_img_rotate_270_clockwise)
            cv2.imwrite(path + '/' + dir + '/' + base + '_270' +'.png', depth_img_rotate_270_clockwise)
            cv2.imwrite(path + '/' + dir + '/' + base + '_flip_ud' +'.jpg', color_img_flip_ud)
            cv2.imwrite(path + '/' + dir + '/' + base + '_flip_ud' +'.png', depth_img_flip_ud)
            cv2.imwrite(path + '/' + dir + '/' + base + '_flip_lr' +'.jpg', color_img_flip_lr)
            cv2.imwrite(path + '/' + dir + '/' + base + '_flip_lr' +'.png', depth_img_flip_lr)
            cv2.imwrite(path + '/' + dir + '/' + base + '_flip_udlr' +'.jpg', color_img_flip_udlr)
            cv2.imwrite(path + '/' + dir + '/' + base + '_flip_udlr' +'.png', depth_img_flip_udlr)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(1) + '.jpg', color_img_1)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(1) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(2) + '.jpg', color_img_2)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(2) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(3) + '.jpg', color_img_3)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(3) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(4) + '.jpg', color_img_4)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(4) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(5) + '.jpg', color_img_5)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(5) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(6) + '.jpg', color_img_6)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(6) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(7) + '.jpg', color_img_7)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(7) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(8) + '.jpg', color_img_8)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(8) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(9) + '.jpg', color_img_9)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(9) + '.png', depth_img)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(10) + '.jpg', color_img_10)
            # cv2.imwrite(path + '/' + dir + '/' + base + '_hue' + str(10) + '.png', depth_img)


            
print('Finished data augmentation!')
import os
import cv2

path = "eyemodel_train"
path_raw = "eyemodel_train_raw"

if not os.path.exists(path):
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
print('Finished data augmentation!')
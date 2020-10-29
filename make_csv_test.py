import os
import csv

def csv_test():
    path = "eyemodel_test"
    files = os.listdir(path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]

    with open(path + '.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for dir in files_dir:
            images = os.listdir(path+'/'+ dir)
            images_files = [i for i in images if os.path.isfile(os.path.join(path +'/'+ dir, i))]
            for i in images_files:
                base, ext = os.path.splitext(i)
                if ext == '.jpg':
                    writer.writerow(['data/'+ path + '/' + dir +'/' + base +'.jpg', 'data/'+ path + '/' + dir +'/' + base +'.png'])
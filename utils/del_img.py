import cv2
import os

root_path = '/data1/siyue/Code/label_dataset'
train_path = os.path.join(root_path, 'train.txt')
val_path = os.path.join(root_path, 'val.txt')

new_train_path = os.path.join(root_path, 'new_train.txt')
new_val_path = os.path.join(root_path, 'new_val.txt')

with open(val_path) as f, open(new_val_path, 'w') as out:
    for line in f:
        info = line.strip().split('\t')
        img_path = info[0]
        img = cv2.imread(img_path)
        if img is None:
            continue
        if img.shape[-1] != 3:
            continue
        out.write(line)



import matplotlib.pyplot as plt
import cv2
import numpy as py
import os

def image_comparison(image1, image2):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    # 计算图img的直方图
    H1 = cv2.calcHist([img1], [1], None, [256],[0,256])
    H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1) # 对图片进行归一化处理
 
    # 计算图img2的直方图
    H2 = cv2.calcHist([img2], [1], None, [256],[0,256])
    H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)
 
    # 利用compareHist（）进行比较相似度
    similarity = cv2.compareHist(H1, H2,0)
    return similarity
 

seed = "d:\\yangben\helmet\seed\\"
source = "d:\\yangben\helmet\current\\"
i=0
seed_names = os.listdir(seed)
source_names = os.listdir(source)
for seed_name in seed_names:
    for src_name in source_names:
        i=i+1
        if i>50:
            break
        similarity = image_comparison(seed+seed_name, source+src_name)
        print(source+src_name)        
        if similarity>0.9:
            print("-----------------delete--------")
            os.remove(source+src_name)





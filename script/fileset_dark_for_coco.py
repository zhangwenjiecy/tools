import os
import random
# 1. 获取一个要重命名的文件夹的名字
in_name_train = "d:\\work\\coco\\old\\train2017.txt"
in_name_val = "d:\\work\\coco\\old\\val2017.txt"
in_name_test = "d:\\work\\coco\\old\\test2017.txt"


out_name_train = "d:\\work\\coco\\train.txt"
out_name_val = "d:\\work\\coco\\val.txt"
out_name_test = "d:\\work\\coco\\test.txt"
prefix = "/data4/zwj/data/coco/yolo/JPEGImages/"



# 2. 获取那个文件夹中所有的文件名字
f_in_train=open(in_name_train, 'r')

f_train=open(out_name_train, 'w')


for line in f_in_train.readlines():
    name = line.strip("\n")
    img_file = prefix+name+'.jpg\n'
    f_train.write(img_file)


         
f_in_train.close()
f_train.close()


f_in_train=open(in_name_val, 'r')

f_train=open(out_name_val, 'w')


for line in f_in_train.readlines():
    name = line.strip("\n")
    img_file = prefix+name+'.jpg\n'
    f_train.write(img_file)


         
f_in_train.close()
f_train.close()


f_in_train=open(in_name_test, 'r')
f_train=open(out_name_test, 'w')


for line in f_in_train.readlines():
    name = line.strip("\n")
    img_file = prefix+name+'.jpg\n'
    f_train.write(img_file)

         
f_in_train.close()
f_train.close()





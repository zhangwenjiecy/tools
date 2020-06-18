import os
import random
# 1. 获取一个要重命名的文件夹的名字
folder_name = "D:\\work\\jueyuanzi\\JPEGImages"
testseed=0.2
valseed=0.1

out_name_train = "d:\\work\\train.txt"
out_name_val = "d:\\work\\val.txt"
out_name_trainval = "d:\\work\\trainval.txt"
out_name_test = "d:\\work\\test.txt"
prefix = "/data4/zwj/data/jueyuanzi/staticcut/JPEGImages/"
#prefix = ""



# 2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)

f_train=open(out_name_train, 'w')
f_trainval=open(out_name_trainval, 'w')
f_val=open(out_name_val, 'w')
f_test=open(out_name_test, 'w')

# 第1中方法
# os.chdir(folder_name)

# 3. 对获取的名字进行重命名即可
# for name in file_names:
#    print(name)
#    os.rename(name,"[京东出品]-"+name)
i = 1 # 可以让每个文件名字都不一样


for name in file_names:
    name2=name[0:10]
    i=random.randint(0,9)
    if i<=6:       
        f_train.write(prefix+name2+"\n")
        f_trainval.write(prefix+name2+"\n")
    elif i<=7:
        f_val.write(prefix+name2+"\n")
        f_trainval.write(prefix+name2+"\n")
    else:
        f_test.write(prefix+name2+"\n")
       
    

f_train.close()
f_trainval.close()
f_val.close()
f_test.close()
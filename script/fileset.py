import os
import random
# 1. 获取一个要重命名的文件夹的名字
folder_name = "D:\yangben\helmet\Annotations"
prefix = "D:\\yangben\\helmet\\Annotations\\"
out_name = "d:\\work\\filelist.txt"


# 2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)

out_names=open(out_name, 'w')


# 第1中方法
# os.chdir(folder_name)

# 3. 对获取的名字进行重命名即可
# for name in file_names:
#    print(name)
#    os.rename(name,"[京东出品]-"+name)
i = 1 # 可以让每个文件名字都不一样


for name in file_names:
    name2=name[0:8]
    out_names.write(prefix+name2+"\n")
          

out_names.close()

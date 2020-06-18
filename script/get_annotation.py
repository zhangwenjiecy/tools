import os,shutil
import random

# 1. 获取一个要重命名的文件夹的名字
jpg_dir = "D:\\yangben\\helmet\\dest_99"
anno_dir = "D:\\yangben\helmet\Annotations\\"
anno_dest = "D:\\yangben\helmet\\anno_99\\"



# 2. 获取那个文件夹中所有的文件名字
jpg_names = os.listdir(jpg_dir)
anno_names = os.listdir(jpg_dir)


# 第1中方法
# os.chdir(folder_name)

# 3. 对获取的名字进行重命名即可
# for name in file_names:
#    print(name)
#    os.rename(name,"[京东出品]-"+name)
i = 1 # 可以让每个文件名字都不一样


for name in jpg_names:
    name = name[0:8] + ".xml"
    shutil.copy( anno_dir+name, anno_dest+name)
    print(name)
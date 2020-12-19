#！/usr/bin/env python
# -*-coding:utf-8-*-
# coding: Youan Zhang
# 2020/12/18


import os;


def rename():
    '''
    函数作用：用python批量修改文件夹中的文件名：后六位依次叠加
    举例：
        文件夹中文件名：2007_000001.jpg
                        2007_000006.jpg
                        2007_000009.jpg
        输出：          000001.jpg
                        000002.jpg
                        000003.jpg
    '''
    # path = 'C:/yolov4-tf2-master/VOCdevkit/VOC2007/JPEGImages' # 这里存放需要修改的文件夹的路径
    path = 'C:/yolov4-tf2-master/VOCdevkit/VOC2007/Annotations' # 这里修改的是xml文件的文件名
    filelist = os.listdir(path) # 读取该文件夹下所有的文件和文件夹的名字

    count = 1
    for files_name in filelist: # 遍历所有的文件
        old_dir = os.path.join(path, files_name) # 原来文件的路径
        if os.path.isdir(old_dir): # 如果是文件夹，则跳过
            continue
        filename = os.path.splitext(files_name)[0] # 文件名
        filetype = os.path.splitext(files_name)[1] # 文件扩展名

        new_file_name = filename[-6:]  # 保留原来文件名的后6位
        new_dir = os.path.join(path, str(count).zfill(6) + filetype) #新的文件路径
        os.rename(old_dir, new_dir) # 重命名
        count = count+1

if __name__ == '__main__':
    rename()
    
    

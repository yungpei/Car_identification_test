def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.mkdir(dirname)

def dirResize(src, dst):
    myfiles = glob.glob(src + '/*.JPG')     # 讀取資料夾全部的 jpg 檔案
    emptydir(dst)
    print(src + ' 資料夾：')
    print('開始轉換圖形尺寸！')
    for f in myfiles:
        fname = f.split("\\")[-1]
        img = Image.open(f)
        img_new = img.resize((300, 225), Image.Resampling.LANCZOS)

        img_new.save(dst + '/' + fname)
    print('轉換圖形尺寸完成！ \n')

import PIL  
from PIL import Image
import glob
import shutil, os
from time import sleep

dirResize('predictPlate_sr', 'predictPlate')
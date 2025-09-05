def emptydir(dirname):  #清空資料夾
    if os.path.isdir(dirname):  #資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(2)  #需延遲,否則會出錯
    os.mkdir(dirname)  #建立資料夾

import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep

myfiles = glob.glob("carNegative_sr/*.JPG")
emptydir('carNegative')
print(' 開始轉換尺寸及灰階！ ')
for i, f in enumerate(myfiles):
    img = Image.open(f)
    img_new = img.resize((300, 225), Image.Resampling.LANCZOS)
    img_new = img_new.convert('L')
    outname = str("negGray") + str('{:0>3d}').format(i+1) + '.jpg'
    img_new.save('carNegative/' + outname)

print('轉換圖形尺寸完成！\n')
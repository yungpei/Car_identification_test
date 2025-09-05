from PIL import Image
import glob
import os

myfiles = glob.glob("carPlate/*.JPG")
print(' 開始轉換圖形格式！ ')
for f in myfiles:
    namespilt = f.split("\\")
    img = Image.open(f)
    outname = namespilt[1].replace('resizejpg', 'bmpraw')   # 置換檔案名稱
    outname = outname.replace('.jpg', '.bmp')               # 置換附加檔名
    img.save('carPlate/' + outname, 'bmp')                  # 以 bmp 格式存檔
    os.remove(f)
print(' 轉換圖形格式結束！ ')
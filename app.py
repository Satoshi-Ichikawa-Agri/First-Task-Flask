""" 要件
1. pillowを用いて、ランダムの色のRGB形式の画像を作成
2. Flaskと連携して、以下のgifのように「画像を表示ボタン」を押すたびに画像が表示される
"""
import numpy as np
from PIL import Image


row_data = np.arange(256)
hue_data = np.tile(row_data, (256, 1))
sat_data = np.transpose(hue_data)
val_data = np.full_like(hue_data, 255)
mat_data = np.stack([hue_data, sat_data, val_data], 2)

im = Image.fromarray(np.uint8(mat_data), "HSV")
im_rgh = im.convert("RGB")
im_rgh.show()

# Conduct
# if __name__ == "__main__":

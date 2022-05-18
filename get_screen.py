import subprocess
import numpy
import cv2
import datetime

ADB_PATH = '../platform-tools/adb'

def capture_screen_1():
    '''
    スクリーンキャプチャを取るための関数。Rawデータを処理

    Returns
    ----------
    img : opencv Mat
        OpenCV形式のイメージ

    '''
    result = []

    # adb exec-out screencap
    try:
        result = subprocess.check_output([ADB_PATH, 'exec-out', 'screencap'])
    except:
        return None

    # wigth, heightを取得。
    wigth = int.from_bytes(result[0:4], 'little')
    height = int.from_bytes(result[4:8], 'little')
    _ = int.from_bytes(result[8:12], 'little')
    #何かが4バイト追加されている

    # ここのCopyは必須。そうでないと、編集が出来ない
    tmp = numpy.frombuffer(result[16:], numpy.uint8, -1, 0).copy() 

    # 配列の形状変換。
    # 1つの要素がRGBAである、height * widthの行列を作る。
    img = numpy.reshape(tmp, (height, wigth, 4))    

    # 要素入れ替え。
    # RawDataはRGB、OpenCVはBGRなので、0番目の要素と、2番目の要素を入れ替える必要がある。
    b = img[:, :, 0].copy()               # ここのコピーも必須
    img[:, :, 0] = img[:, :, 2]
    img[:, :, 2] = b

    # alpha値を削除。alpha値が必要な場合は、下記行は消しても良いかも？
    img2 = numpy.delete(img, 3, 2)

    return img2

# 検証用コード
if __name__ == "__main__":
    img = capture_screen_1()
    now = datetime.datetime.now()
    filename = './img/temp//screen_' + now.strftime('%Y%m%d_%H%M%S') + '.png'
    cv2.imwrite(filename, img)
import subprocess
import random
import time

ADB_PATH = '../platform-tools/adb'

def range_tap(x1,y1,x2,y2):
    _x1 = random.randint(x1,x2)
    _y1 = random.randint(y1,y2)
    _x2 = _x1 + random.randint(-3,3)
    _y2 = _y1 + random.randint(-3,3)
    _msec = random.randint(100,200)
    try:
        #subprocess.check_output([ADB_PATH, 'shell', 'input','touchscreen', 'tap', str(_x), str(_y)])
        subprocess.check_output([ADB_PATH, 'shell', 'input','swipe', str(_x1), str(_y1), str(_x2), str(_y2), str(_msec)])
    except:
        print("ADBで通信エラー")
        quit()

def get_jitter_time():
    f = random.random()/100
    return round(0.5+f, 3)

def main():
    print("終了する場合はCntrl+C")
    phase = "rematch"
    counter = 0

    while True:
        # 早送りボタンは常にタップ
        print(phase,counter)
        if phase=="rematch":
            if counter < 3:
                range_tap(334,1827,744,1911)

            if counter >= 15:
                phase = "battle1"
                counter = 0
            else:
                counter += 1

        elif phase=="battle1":
            if counter < 4:
                range_tap(12,1192,166,1340)

            if counter >= 12:
                phase = "battle2"
                counter = 0
            else:
                counter += 1

        elif phase=="battle2":
            if counter < 4:
                range_tap(190,1192,346,1340)

            if counter >= 12:
                phase = "battle3"
                counter = 0
            else:
                counter += 1

        elif phase=="battle3":
            
            if counter < 4:
                range_tap(366,1192,524,1340)

            if counter >= 12:
                phase = "battle4"
                counter = 0
            else:
                counter += 1

        elif phase=="battle4":
            
            if counter < 4:
                range_tap(549,1192,702,1340)

            if counter >= 10:
                phase = "battle5"
                counter = 0
            else:
                counter += 1

        elif phase=="battle5":
            
            if counter < 4:
                range_tap(727,1192,888,1340)

            if counter >= 10:
                phase = "battle6"
                counter = 0
            else:
                counter += 1

        elif phase=="battle6":
            
            if counter < 4:
                range_tap(906,1192,1065,1340)

            if counter >= 10:
                phase = "clear"
                counter = 0
            else:
                counter += 1

        elif phase=="clear":
            if counter < 4:
                range_tap(424,2039,657,2118)

            if counter >= 5:
                phase = "get_wait"
                counter = 0
            else:
                counter += 1

        elif phase=="get_wait":
            ## 長押し処理やがめんどい
            if counter < 4:
                range_tap(906,1192,1065,1340)

            if counter >= 15:
                phase = "rematch"
                counter = 0
            else:
                counter += 1

        ##elif phase=="get_complete":
        
        time.sleep(get_jitter_time())



if __name__ == "__main__":
    main()
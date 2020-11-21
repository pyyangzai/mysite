import os
import cv2
import pyautogui
import uiautomation
# import pymouse, pykeyboard
#
#
# def f():
#     uiautomation.WindowControl()
#     pm = pymouse.PyMouse()
#     kb = pykeyboard.PyKeyboard()


def get_items(path):
    file_list = []
    for file in os.listdir(path):
        if not os.path.isdir(os.path.join(path, file)):
            file_list.append(file)
    return file_list


def pic_path(picture):
    return os.path.join(os.getcwd(), 'test_data', '{}'.format(picture))


def compare_pic(pic):
    print(pic)
    pyautogui.screenshot(pic_path('tmp.png'))
    img = cv2.imread(pic_path('tmp.png'))
    temp_img = cv2.imread(pic)
    t = cv2.matchTemplate(img, temp_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(t)
    print(max_val)
    print(max_loc)
    if max_val > 0.9:
        size = temp_img.shape
        print(size)
        return (max_loc[0]+size[0]/2, max_loc[1]+size[1]/2), size
    else:
        return


def start(name, cycle=2):
    path = pic_path(name)
    for i in range(cycle):
        if os.path.isdir(path):
            for item in get_items(path):
                return compare_pic(os.path.join(path, item))
        else:
            return compare_pic(path)

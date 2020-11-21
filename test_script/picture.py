import os
import time
from PIL import Image, ImageGrab


def shot_cut(name):
    im = ImageGrab.grab()
    im.save(os.path.join(os.getcwd(), 'test_data', '{}.png'.format(name)))


def open_pic(pic_name):
    pic_path = os.path.join(os.getcwd(), 'test_data', '{}'.format(pic_name))
    img_src = Image.open(pic_path)
    size = img_src.size
    print(size)
    return img_src, size


def fun(size, size1=()):
    x, y = size[0], size[1]
    if size1:
        X, Y = size1[0], size1[1]
        print([(X/2-x*(y/Y)/3/2-50, Y/3-50), (X/2+x*(y/Y)/3/2+50, Y/3-50),
                (X/2-x*(y/Y)/3/2-50, Y*2/3+50), (X/2+x*(y/Y)/3/2+50, Y*2/3+50)])
        return [(X/2-x*(y/Y)/3/2-50, Y/3-50), (X/2+x*(y/Y)/3/2+50, Y/3-50),
                (X/2-x*(y/Y)/3/2-50, Y*2/3+50), (X/2+x*(y/Y)/3/2+50, Y*2/3+50)]
    else:
        print([(x/3-50, y/3-50), (x*2/3+50, y/3-50),
                (x/3-50, y*2/3+50), (x*2/3+50, y*2/3+50)])
        return [(x/3-50, y/3-50), (x*2/3+50, y/3-50),
                (x/3-50, y*2/3+50), (x*2/3+50, y*2/3+50)]


def get_pic_color(img, lis):
    img_src = img.convert('RGBA')
    src_strlist = img_src.load()
    data1 = src_strlist[lis[0][0], lis[0][1]]
    data2 = src_strlist[lis[1][0], lis[1][1]]
    data3 = src_strlist[lis[2][0], lis[2][1]]
    data4 = src_strlist[lis[3][0], lis[3][1]]
    return [data1, data2, data3, data4]


if __name__ == '__main__':

    time.sleep(5)
    shot_cut('tmp')
    time.sleep(1)
    exit()

    img_obj, pic_size = open_pic('pic.JPG')
    print(get_pic_color(img_obj, fun(pic_size)))
    img_obj1, pic_size1 = open_pic('pi.PNG')
    print(get_pic_color(img_obj1, fun(pic_size1)))
    # img_obj1, pic_size1 = open_pic('pp.PNG')
    # print(get_pic_color(img_obj1, fun(pic_size1)))

    print(get_pic_color(img_obj1, fun(pic_size, pic_size1)))

    # img_obj2, pic_size2 = open_pic('pic1.PNG')
    # print(get_pic_color(img_obj2, fun(pic_size2)))
    # img_obj2, pic_size2 = open_pic('pi1.PNG')
    # print(get_pic_color(img_obj2, fun(pic_size2)))
    # img_obj3, pic_size3 = open_pic('pp1.PNG')
    # print(get_pic_color(img_obj3, fun(pic_size3)))


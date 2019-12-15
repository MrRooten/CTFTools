import cv2
import numpy as np
def get_binary_image(img):
    th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,1)
    return th1

def clear_border(img):
    h,w = img.shape[:2]
    for y in range(0,w):
        for x in range(0,h):
            if y < 2 or y > w -2:
                img[x,y] = 255
            if x < 2 or x > h - 2:
                img[x,y] = 255

    return img

def interference_line(img):
  h, w = img.shape[:2]
  # ！！！opencv矩阵点是反的
  # img[1,2] 1:图片的高度，2：图片的宽度
  for y in range(1, w - 1):
    for x in range(1, h - 1):
      count = 0
      if img[x, y - 1] > 245:
        count = count + 1
      if img[x, y + 1] > 245:
        count = count + 1
      if img[x - 1, y] > 245:
        count = count + 1
      if img[x + 1, y] > 245:
        count = count + 1
      if count > 2:
        img[x, y] = 255
  return img

def interference_point(img):
    """
    9邻域框,以当前点为中心的田字框,黑点个数
    :param x:
    :param y:
    :return:
    """
    filename =  './out_img/' + img_name.split('.')[0] + '-interferencePoint.jpg'
    # todo 判断图片的长宽度下限
    cur_pixel = img[x,y]# 当前像素点的值
    height,width = img.shape[:2]
    for y in range(0, width - 1):
      for x in range(0, height - 1):
        if y == 0:  # 第一行
            if x == 0:  # 左上顶点,4邻域
                # 中心点旁边3个点
                sum = int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右上顶点
                sum = int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            else:  # 最上非顶点,6邻域
                sum = int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
        elif y == width - 1:  # 最下面一行
            if x == 0:  # 左下顶点
                # 中心点旁边3个点
                sum = int(cur_pixel) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x, y - 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右下顶点
                sum = int(cur_pixel) \
                      + int(img[x, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y - 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            else:  # 最下非顶点,6邻域
                sum = int(cur_pixel) \
                      + int(img[x - 1, y]) \
                      + int(img[x + 1, y]) \
                      + int(img[x, y - 1]) \
                      + int(img[x - 1, y - 1]) \
                      + int(img[x + 1, y - 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
        else:  # y不在边界
            if x == 0:  # 左边非顶点
                sum = int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右边非顶点
                sum = int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x - 1, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
            else:  # 具备9领域条件的
                sum = int(img[x - 1, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1]) \
                      + int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 4 * 245:
                  img[x, y] = 0
    cv2.imwrite(filename,img)
    return img


from predict import predict, trim
import cv2
from PIL import Image
import sys
from math import floor
import numpy as np
import time


def reader(filename):
        img = cv2.imread(filename)
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh, blackAndWhiteImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        cv2.imwrite('ok.jpg', blackAndWhiteImage)
        img1 = Image.open("ok.jpg")
        img = trim(img1)
        img2, _ = trim(img1, Image.open(filename))
        img.save("ok.jpg")
        img2 = img2.convert('RGB')
        img2.save("colored.jpg")
        width, height = img.size

        cell_w = width/9
        cell_h = height/9

        top = 0
        left = 0
        bottom = cell_h
        right = cell_w
        r_top, r_left, r_bottom, r_right = round(top), round(left), round(bottom), round(right)
        f_w = cell_w/10
        f_h = cell_h/10
        grid = []
        rects = []
        for i in range(9):
                row = []
                rect = []
                for j in range(9):
                        crop_rectangle = (r_top + f_h, r_left + f_w, r_bottom - f_h, r_right - f_w)
                        crop_im = img.crop(crop_rectangle)
                        rect.append(crop_rectangle)
                        cell = f"{i}, {j}.jpg"
                        crop_im.save(cell)
                        num = predict(cell)
                        row.append(num)
                        top += cell_w
                        bottom += cell_w
                        r_top, r_left, r_bottom, r_right = round(top), round(left), round(bottom), round(right)
                grid.append(row)
                rects.append(rect)
                top = 0
                bottom = cell_w
                left += cell_h
                right += cell_h
                r_top, r_left, r_bottom, r_right = round(top), round(left), round(bottom), round(right)
        return grid, rects

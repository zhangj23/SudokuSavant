from solver import Solver
from sudoku_reader import reader
import sys
from PIL import Image, ImageFont, ImageDraw 
import numpy as np
import os
if len(sys.argv) != 3:
        sys.exit("Usage: python sudoku_reader.py image_filename/filefolder outfile_folder")

grid = None
if sys.argv[1][-4:] == '.jpg':
        empty = []
        grid, rects = reader(sys.argv[1])
        for i in range(9):
                for j in range(9):
                        if grid[i][j] == 0:
                                empty.append((i, j))
        rect = rects[0][0]
        font_size = -1.5 * ((rect[1] - rect[3])/2)
        print(font_size)
        model = Solver(grid)
        model.solve()
        my_image = Image.open("colored.jpg")
        img = my_image
        title_font = ImageFont.truetype('OpenSans-Regular.ttf', int(round(font_size)))
        image_editable = ImageDraw.Draw(my_image)
        n= 0
        for char in sys.argv[1]:
                if char == '/':
                        n += 1
                        break
                n += 1
        for solved in model.solutions:
                for i, j in empty:
                        num = solved[i][j]
                        rect = rects[i][j]
                        placement = (((rect[0] + rect[2])/2) + (rect[0] - rect[2])/2, (rect[1] + rect[3])/2 + (rect[1] - rect[3])/2)
                        image_editable.text(placement, str(num), fill=0, font=title_font)
                my_image.save(sys.argv[2] + '/' + sys.argv[1][n:-4] + "_solved.jpg")
else:
        for file in os.listdir(sys.argv[1]):
                empty = []
                file_path = os.path.join(sys.argv[1], file)
                grid, rects = reader(file_path)
                for i in range(9):
                        for j in range(9):
                                if grid[i][j] == 0:
                                        empty.append((i, j))
                rect = rects[0][0]
                font_size = -1.5 * ((rect[1] - rect[3])/2)

                model = Solver(grid)
                model.solve()
                my_image = Image.open("colored.jpg")
                img = my_image
                title_font = ImageFont.truetype('OpenSans-Regular.ttf', int(round(font_size)))
                image_editable = ImageDraw.Draw(my_image)
                for i, j in empty:
                        num = model.solutions[0][i][j]
                        rect = rects[i][j]
                        placement = (((rect[0] + rect[2])/2) + (rect[0] - rect[2])/2, (rect[1] + rect[3])/2 + (rect[1] - rect[3])/2)
                        image_editable.text(placement, str(num), fill=0, font=title_font)
                my_image.save(sys.argv[2] + '/' + file[:-4] + "_solved.jpg")

from PIL import Image

from PIL import ImageFont
from PIL import ImageDraw
import os

for folder in os.listdir("fonts"):
        path = os.path.join("fonts", folder)
        for file in os.listdir(path):
            if file[-3:] == "ttf":
                file_path = os.path.join(path, file)
                for ele in file:
                    if ele.isdigit():
                        file = file.replace(ele, 't')
                for i in range(1, 10):
                    img = Image.new('RGB', (500,500), (250,250,250))
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype(file_path, 400)
                    draw.text((150, -30),str(i),(0,0,0),font=font)
                    img.save('images/'+file[:-3]+"_"+str(i)+'.jpg')
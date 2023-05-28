from PIL import Image
import os 
from predict import trim
for file in os.listdir("images"):
    num = 0
    file_path = os.path.join("images", file)
    n = 20
    img = Image.open(file_path)
    w, h = img.size
    trim_img, box = trim(img, img)
    eleft, etop, eright, ebottom = box
    rotated = img.rotate(5, fillcolor = (255, 255, 255))
    rotated.save("images/fiverot_" + file)
    trim(rotated).save("images/trim_fiverot_" + file)
    rotated = img.rotate(-5, fillcolor=(255, 255, 255))
    rotated.save("images/-fiverot_" + file)
    trim(rotated).save("images/trim_-fiverot_" + file)
    left = 0
    top = 0
    right = w
    bottom = h
    while left < eleft - n:
        while top < etop - n:
            while right > eright + n:
                while bottom > ebottom + n:
                    bottom -= n
                    im1 = img.crop((left, top, right, bottom))
                    im1.save(file_path[:-4]+str(num)+'.jpg')
                    num += 1
                right -= n
                bottom = h
            top += n
            right = w
        left += n
        top = 0
    #     img_crop = img.crop((0, 0, w-n, h))
    #     img_crop.save("images/right_trim_"+file)
    #     img_crop = img.crop((0, 0, w-n, h-n))
    #     img_crop.save("images/bottom_right_trim_"+file)
    #     img_crop = img.crop((0, n, w-n, h))
    #     img_crop.save("images/top_right_trim_"+file)
    #     img_crop = img.crop((0, 0, w, h-n))
    #     img_crop.save("images/botttom_trim_"+file)
    #     img_crop = img.crop((n, 0, w, h))
    #     img_crop.save("images/left_trim_"+file)
    #     img_crop = img.crop((n, 0, w, h-n))
    #     img_crop.save("images/bottom_left_trim_"+file)
    #     img_crop = img.crop((n, n, w, h))
    #     img_crop.save("images/top_left_trim_"+file)
    #     img_crop = img.crop((0, n, w, h))
    #     img_crop.save("images/top_trim_"+file)
    #     n = 20
    # else:
    #     img = Image.open(file_path)
    #     w, h = img.size
    #     # trim(img).save("images/trim_"+file)
    #     rotated = img.rotate(5, fillcolor = (255, 255, 255))
    #     rotated.save("images/5rot_" + file)
    #     # trim(rotated).save("images/trim_20rot_" + file)
    #     rotated = img.rotate(-5, fillcolor=(255, 255, 255))
    #     rotated.save("images/-5rot_" + file)
    #     # trim(rotated).save("images/trim_-20rot_" + file)
    #     img_crop = img.crop((0, 0, w-n, h))
    #     img_crop.save("images/right_trim_"+file)
    #     img_crop = img.crop((0, 0, w-n, h-n))
    #     img_crop.save("images/bottom_right_trim_"+file)
    #     img_crop = img.crop((0, n, w-n, h))
    #     img_crop.save("images/top_right_trim_"+file)
    #     img_crop = img.crop((0, 0, w, h-n))
    #     img_crop.save("images/botttom_trim_"+file)
    #     img_crop = img.crop((n, 0, w, h))
    #     img_crop.save("images/left_trim_"+file)
    #     img_crop = img.crop((n, 0, w, h-n))
    #     img_crop.save("images/bottom_left_trim_"+file)
    #     img_crop = img.crop((n, n, w, h))
    #     img_crop.save("images/top_left_trim_"+file)
    #     img_crop = img.crop((0, n, w, h))
    #     img_crop.save("images/top_trim_"+file)
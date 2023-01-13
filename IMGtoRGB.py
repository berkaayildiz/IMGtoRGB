from PIL import Image

im = Image.open("image.png")    # This could be any type of image, not strictly png.

width = im.width
height = im.height

def IMGtoRGB(im):
    RGBim = im.convert('RGB')
    text = open('imagergb.txt', 'a')

    for y in range(height):
        tempRow = []
        
        for x in range(width):
            r, g, b = RGBim.getpixel((x, y))
            tempRow.append((r,g,b))

        text.write(str(tempRow) + 2*'\n')   # 2*'\n' was added to make file easier to read.
    return text

IMGtoRGB(im)
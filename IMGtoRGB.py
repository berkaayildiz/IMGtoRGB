from PIL import Image as Im
import pickle


def IMGtoRGB(path, outfileName='image'):
    
    image = Im.open(path)
 
    height = image.height
    width = image.width

    RGBimage = image.convert("RGB")
    
    outfileText = open(outfileName + '.txt', 'a')

    rowList = []

    # This list stores all of the data in a row-major order.

    for y in range(height):
        tempRow = []

        # This list stores the data of the current row.

        for x in range(width):
            r, g, b = RGBimage.getpixel((x,y))
            tempRow.append((r, g, b))
        
        rowList.append(tempRow)
        outfileText.write(str(tempRow) + 2*'\n')
        
        # "2*'\n'" is added to make file easier to read.

    return outfileText

def main():
    IMGtoRGB('image.png', 'image')


main()
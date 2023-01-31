import os
import pickle
from PIL import Image as Im


def IMGtoRGB(path):
    
    image = Im.open(path)
 
    height = image.height
    width = image.width

    RGBimage = image.convert("RGB")

    outfileName = os.path.splitext(path)[0]

    # Names the outfiles according to name of the image file.

    outfileText = open(f'{outfileName}Text.txt', 'w')
    outfilePickle = open(f'{outfileName}Pickle.txt', 'wb')

    # Creates two txt file to store both
    # serialized and non-serialized version of the file.

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
        
        # "2*'\n'" is added to make non-serialized file easier to read.

    pickle.dump(rowList, outfilePickle)

    outfileText.close()
    outfilePickle.close()
    
    return outfileText, outfilePickle

def main():
    IMGtoRGB('image.png')

    # Enter the path to your image file.
    # Other formats besides .png are possible.


main()

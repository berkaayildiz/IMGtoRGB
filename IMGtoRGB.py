from PIL import Image as Im
import pickle


def IMGtoRGB(path, outfileName='image'):
    
    image = Im.open(path)
 
    height = image.height
    width = image.width

    RGBimage = image.convert("RGB")
    
    outfileText = open(outfileName + 'Text.txt', 'a')
    outfilePickle = open(outfileName + 'Pickle.txt', 'wb')

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
    IMGtoRGB('image.png', 'image')

    # Enter the path to your image file.
    # Other formats besides .png are possible.


main()
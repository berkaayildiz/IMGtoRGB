import os
import pickle
from PIL import Image as Im

def IMGtoRGB(path, format):
    
    """
    Converts an image file to RGB format and returns the data in the desired format.

    Parameters:
    path (str): The file path of the image to be converted.
    format (str): The desired format of the returned data. Can be 'list', 'text', or 'pickle'.

    Returns:
    list/str/file: The data in the desired format. Returns `None` if the format is invalid.
    """

    try:
        # Open the image file
        image = Im.open(path)
    
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None

    # Get the height and width of the image
    height = image.height
    width = image.width

    # Convert the image to RGB format
    RGBimage = image.convert("RGB")

    # Create a list to store the image data in row-major order
    rows_list = []

    for y in range(height):
        # Create a list to store the data of the current row temporarily
        row = []

        for x in range(width):
            # Get the RGB values of the current pixel
            r, g, b = RGBimage.getpixel((x, y))
            row.append((r, g, b))
        
        rows_list.append(row)

    if format == 'list':
        return rows_list
    
    elif format == 'text':
        # Create a text file to store the data
        outfile_name = os.path.splitext(path)[0]
        outfile_path = f'{outfile_name}.txt'
        
        with open(outfile_path, 'w') as outfile:
            for row in rows_list:
                outfile.write(str(row) + 2 * '\n')
                # "2*'\n'" is added to make non-serialized file easier to read
        return outfile_path
    
    elif format == 'pickle':
        # Create a pickle file to store the data
        outfile_name = os.path.splitext(path)[0]
        outfile_path = f'{outfile_name}.pickle'
        
        with open(outfile_path, 'wb') as outfile:
            pickle.dump(rows_list, outfile)
        return outfile_path
    
    else:
        print("Error: Invalid format")
        return None

def main():
    IMGtoRGB('image.png', 'list')
    IMGtoRGB('image.png', 'text')
    IMGtoRGB('image.png', 'pickle')

if __name__ == '__main__':
    main()

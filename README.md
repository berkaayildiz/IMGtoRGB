# IMGtoRGB

A python script to convert an image to RGB format and return the data in the desired format.

## Requirements

- Python 3
- PIL (Pillow)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pillow.
To install the required packages, run the following command:

```bash
pip install Pillow
```

## Usage

The script can be run from the command line using the following syntax:

```bash
python IMGtoRGB.py [image_file] [format]
```

where `[image_file]` is the path to the image file to be converted, and `[format]` is the desired format of the returned data. The `[format]` argument can be one of the following:

- `list`: Returns the data as a list in memory.
- `text`: Writes the data to a text file.
- `pickle`: Writes the data to a pickle file.

## Example

```bash
python IMGtoRGB.py [image.png] [text]
```

This will convert the 'image.png' file to RGB format and write the data to a text file 'image.txt'.

This example run of the code was tried with the the famous painting “La Reproduction interdite” by René Magritte.

![example](https://user-images.githubusercontent.com/37070272/216344785-3cc831e0-76bc-4815-af32-fbe6bad6b628.PNG)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


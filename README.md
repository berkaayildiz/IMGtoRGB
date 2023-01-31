
# IMGtoRGB
A function that records the RGB values of each pixel of a picture in a file by creating two-dimensional lists in row-major order.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pillow, required for this program.

```bash
pip install Pillow
```
## Usage
An example run of this program.
```python
from PIL import Image

IMGtoRGB('image.png', 'imagergb')
```
The first parameter of the function is the path of the image file.
The second parameter of the function is the name of the outfile.

## Output
An example run of the code tried with the the famous painting “La Reproduction interdite” by René Magritte.
![example](https://user-images.githubusercontent.com/37070272/212308534-cfb00a62-90c5-424d-946f-798b02bac994.PNG)

With the new feature, now you can get the serialized version of the file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

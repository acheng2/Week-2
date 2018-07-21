from PIL import Image

def crop(image_path, coords):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.show()


if __name__ == '__main__':
    image = 'C:\\Users\\train916\\Desktop\\DukeTIP 2018\\Week 2\\W2D1\\vases.png'
    crop(image, (161, 166, 706, 1050))

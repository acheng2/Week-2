from PIL import Image
from PIL import ImageFilter
def PhotoShop():
    print("Welcome to Angela's Photoshop!")
    location = input("What picture do you want to edit? PLease enter the location of the file. Delete the quotes and switch the backslashes with forwardslashes")
    action = input("What do you want to do to that picture? Your choices are: crop, blur, sharpen, invert, darken, brighten, gray_scale, posterize, and solarize." )
    input_file = location
    image = input_file

    def sharpen(input_file, r, p, th):
        sharper_image = Image.open(input_file)
        sharper_image = sharper_image.filter(ImageFilter.UnsharpMask(radius = r, percent = p, threshold = th))
        sharper_image.show()

    def blur(input_file, r):
        blurred_image = Image.open(input_file)
        blurred_image = blurred_image.filter(ImageFilter.GaussianBlur(radius = r))
        blurred_image.show()

    if action == "sharpen":
        r = input("How many pixels do you want to sharpen?")
        r = int(r)
        p = input("What percentage do you want it to be sharpened by?")
        p = int(p)
        th = input("What do you want your threshold to be?")
        th = int(th)
        sharpen(input_file, r, p, th)

    if action == "blur":
        r = input("What radius of blur do you want? Put a value greater than 2.")
        r = int(r)
        blur(input_file, r)

    if action == "crop":
        input_file = location
        image = input_file
        im = Image.open(input_file)
        width, height = im.size
        print("Your picture's bit size, width by height, is")
        print(im.size)
        print("If your picture is colored, multiply the bits by 24 to find the pixel size. If your picture is black and white, multiply the bits by 3 to find the pixel size.")
        i = 0
        ii = []
        while i < 4:
            coords = input("PLease input the coordinates you want: left, upper, right, lower.")
            ii.append(int(coords))
            i = i + 1
        coords = (ii[0], ii[1], ii[2], ii[3])


    def apply_filter(image, filter):
        '''
        Create and return a NEW image, based on a
        transform of each pixel in the given image using the given filter
        image is an open Image object
        filter is a function to apply to each pixel in image
        return new image, same size, to which filter has been applied to each pixel of image
        '''
        pixels = [ filter(p) for p in image.getdata() ]
        nim = Image.new("RGB",image.size)
        nim.putdata(pixels)
        return nim

    def open_image(filename):
        '''
        opens the given image and converts it to RGB format
        returns a default image if the given one cannot be opened
        filename is the name of a PNG, JPG, or GIF image file
        '''
        image = Image.open(filename)
        if image == None:
            print("Specified input file " + filename + " cannot be opened.")
            return Image.new("RGB", (400, 400))
        else:
            print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
            return image.convert("RGB")


    '''
    During this lab a pixel is a tuple of 3 values (R, G, B)
    representing the red, green, and blue components of a color
    that each range from [0-255] inclusive.
    The filter functions:
        - take one pixel as an argument,
        - modify the channels of the pixel and
        - return the transformed pixel
    '''
    def identity(pixel):
        '''
        returns a pixel that is unchanged from the original
        '''
        r,g,b = pixel
        return (r,g,b)

    def crop(image_path, coords):
        '''
        crops an image
        '''
        image_obj = Image.open(image_path)
        cropped_image = image_obj.crop(coords)
        cropped_image.show()



    def invert(pixel):
        '''
        returns a pixel where every pixel channel is 255 minus its value
        '''
        r,g,b = pixel
        return (255-r, 255-g, 255-b)

    def darken(pixel):
        """
        returns a pixel whose red, green, and blue values are all 90% of those given
        """

        r,g,b = pixel
        return (int((9/10) * r), int((9/10) * g), int((9/10)* b))

    def brighten(pixel):
        """
        returns a pixel whose red, green, and blue values are all 110% of those given
        but not over 255 (the maximum value).
        """
        r,g,b = pixel
        return (int((1000000/10) * r), int((1000000/10) * g), int((100000/10)* b))


    def gray_scale(pixel):
        '''
        returns a pixel whose red, green, and blue values are all set to the same value:
          the average of the original channels
        '''
        r,g,b = pixel
        gry = (r + g + b) / 3
        return (int(gry), int(gry), int(gry))


    def posterize(pixel):
        """
        returns a pixel whose red, green, and blue values are all changed in
        the following way:
         - divide channel's range into 4 equal pieces (i.e., 0-63, 64-127, 128-191, 192-255)
         - set the channel's value to a fixed value within that range (i.e., 50, 100, 150, 200)
        """
        r,g,b = pixel
        if r >= 0 and r <= 63:
            r = 50
        if r >= 64 and r <= 127:
            r = 100
        if r >= 128 and r <= 191:
            r = 150
        if r >= 192 and r <= 255:
            r = 200
        if g >= 0 and g <= 63:
            g = 50
        if g >= 64 and g <= 127:
            g = 100
        if g >= 128 and g <= 191:
            g = 150
        if g >= 192 and g <= 255:
            g = 200
        if b >= 0 and b <= 63:
            b = 50
        if b >= 64 and b <= 127:
            b = 100
        if b >= 128 and b <= 191:
            b = 150
        if b >= 192 and b <= 255:
            b = 200
        return (r,g,b)

    def solarize(pixel):
        """
        returns a pixel whose red, green, and blue values are all changed in
        the following way:
         - if the value is less than 128, set it to 255 - the original value.
         - if the value is 128 or greater, don't change it.
        """
        r,g,b = pixel
        if r < 128:
            r = 255
        if g < 128:
            g = 255
        if b < 128:
            b = 255
        return (r,g,b)

    def load_and_go(fname,filterfunc):
        image = open_image(fname)
        nimage = apply_filter(image,filterfunc)
        image.show()
        nimage.show()
        '''
        processedImage.jpg is the name of the file
        the image is saved in. The first time you do
        this you may have to refresh to see it.
        '''
        nimage.save("processedImage.jpg")

    if __name__ == "__main__":
        input_file = location
        image = input_file
        crop(image, coords)
        if action == "invert":
            load_and_go(input_file, invert)
        if action == "darken":
            load_and_go(input_file, darken)
        if action == "brighten":
            load_and_go(input_file, brighten)
        if action == "gray_scale":
            load_and_go(input_file, gray_scale)
        if action == "posterize":
            load_and_go(input_file, posterize)
        if action == "solarize":
            load_and_go(input_file, solarize)
        if action == "crop":
            crop()
        if action == "blur":
            blur()
        if action == "sharpen":
            sharpen()
PhotoShop()

"""
# Problem Set 5
# Name:
# Collaborators:
"""

from PIL import Image, ImageFont, ImageDraw
import numpy


def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == "red":
        c = [[0.567, 0.433, 0], [0.558, 0.442, 0], [0, 0.242, 0.758]]
    elif color == "green":
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == "blue":
        c = [[0.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, 0.525]]
    elif color == "none":
        c = [[1, 0.0, 0], [0, 1, 0.0], [0, 0.0, 1]]
    return c


def matrix_multiply(m1, m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """
    # Use numpy.matmul for efficient matrix multiplication
    product = numpy.matmul(m1, m2)

    # Check if the result is a scalar (single number)
    if type(product) == numpy.int64:
        return float(product)  # Convert scalar to float
    else:
        # Convert the resulting numpy array/list back to a standard Python list
        result = list(product)
        return result


def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of representing pixels.

    For RGB images, each pixel is a tuple containing (R,G,B) values.
    For BW images, each pixel is an integer.

    # Note: Don't worry about determining if an image is RGB or BW.
            The PIL library functions you use will return the
            correct pixel values for either image mode.

    Returns the list of pixels.

    Inputs:
        filename: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values
                 in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image
                 in form L such as [60,66,72...] for BW image
    """
    # Open the image file using PIL
    img = Image.open(filename)

    # Get pixel data as a sequence and convert it to a standard list
    return list(img.getdata())


def pix_to_img(pixels_list, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels_list: a list of pixels such as the output of
                img_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a
              BW image, respectively
    returns:
        img: Image object made from list of pixels
    """
    # Create a new blank image with the specified mode and size
    image = Image.new(mode, size)

    # Load the pixel data into the new image
    image.putdata(pixels_list)

    # Save the generated image to a temporary file for viewing/submission
    image.save("RN_Image.png")
    return image


def filter(pixels_list, color):
    """
    pixels_list: a list of pixels in RGB form, such as
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing
           the color deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """
    # Get the 3x3 transformation matrix for the specified color deficiency

    M_c = numpy.array(make_matrix(color), dtype=numpy.float32)
    pixels_list_modif = []

    # Iterate through each pixel tuple (R, G, B)
    for p in pixels_list:
        # Convert the pixel tuple to a 1x3 NumPy array (vector) for multiplication
        pixel_initial = numpy.array(p, dtype=numpy.float32)

        # Perform matrix multiplication: M_c * pixel_initial_vector
        pixel_modif = numpy.matmul(M_c, pixel_initial)

        # Clip the resulting R, G, B values to the valid range [0, 255]
        # and cast them to integers before converting back to a tuple
        pixel_modif_tuple = tuple(numpy.clip(pixel_modif, 0, 255).astype(int))

        # Append the filtered pixel to the new list
        pixels_list_modif.append(pixel_modif_tuple)

    return pixels_list_modif


def extract_end_bits(num_end_bits, pixel):
    """
    Extracts the last num_end_bits of each value of a given pixel.

    example for BW pixel:
        num_end_bits = 5
        pixel = 214

        214 in binary is 11010110.
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_end_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_end_bits: the number of end bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The num_end_bits of pixel, as an integer (BW) or tuple of integers (RGB).
    """

    # Case for BW (Grayscale) pixel (integer)
    if isinstance(pixel, int):
        # Convert integer pixel to its binary string representation (removing '0b' prefix)
        pix_bin = bin(pixel)[2:]

        # Convert binary string characters to a list of integers (0s and 1s)
        pix_bin_int = list(map(int, pix_bin))
        pix_bin_short = []

        # Reverse the list of bits so the LSBs are at the beginning
        pix_bin_int.reverse()

        # Pad with zeros if the binary representation is shorter than num_end_bits
        while len(pix_bin_int) < num_end_bits:
            pix_bin_int.append(0)

        # Extract the required number of bits from the start of the reversed list
        for p in range(0, num_end_bits):
            pix_bin_short.append(pix_bin_int[p])

        # Reverse the extracted bits back to the correct order (MSB to LSB)
        pix_bin_short.reverse()

        # Join the list of integers back into a single binary string
        pix_bin_string = "".join(map(str, pix_bin_short))

        # Convert the final binary string back to an integer
        num_end_decimal = int(pix_bin_string, 2)

    # Case for RGB pixel (tuple)
    else:
        pix_bin_RGB = []

        # Iterate through the three color components (R, G, B)
        for i in range(0, 3):

            # Process each component identically to the BW case
            pix_bin = bin(pixel[i])[2:]
            pix_bin_int = list(map(int, pix_bin))
            pix_bin_short = []
            pix_bin_int.reverse()
            while len(pix_bin_int) < num_end_bits:
                pix_bin_int.append(0)
            for p in range(0, num_end_bits):
                pix_bin_short.append(pix_bin_int[p])
            pix_bin_short.reverse()
            pix_bin_string = "".join(map(str, pix_bin_short))

            # Store the integer result for the current component
            pix_bin_RGB.append(int(pix_bin_string, 2))

        # Return the extracted bits for all three components as a tuple
        num_end_decimal = tuple(pix_bin_RGB)
    return num_end_decimal


def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image.
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    # Convert image to list of pixels (integers)
    img_pxl = img_to_pix(filename)

    # Open image to get size information
    img = Image.open(filename)
    width, height = img.size
    hid_img_pxl = []

    # Extract 1 LSB from each pixel
    for pix in img_pxl:
        hid_img_pxl.append(extract_end_bits(1, pix))

    # Create a new image from the extracted LSBs (mode 'L' for Grayscale)
    new_img = pix_to_img(hid_img_pxl, (width, height), "L")

    # Rescaling block for visibility: LSB images are often very dim (0 or 1)
    np_new_img = numpy.array(new_img, dtype=numpy.float32)
    min_val = numpy.min(np_new_img)
    max_val = numpy.max(np_new_img)
    val_range = max_val - min_val
    if val_range == 0:

        # Handle case where all pixels are the same (e.g., all 0 or all 1)
        rescaled_np_new_img = numpy.full_like(np_new_img, 127.5)
    else:

        # Normalize the range [min_val, max_val] to [0, 1]
        normaliz_np_new_img = (np_new_img - min_val) / val_range

        # Rescale the normalized values to the full [0, 255] range
        rescaled_np_new_img = normaliz_np_new_img * 255

    # Convert the rescaled NumPy array back into a PIL Image object
    rescaled_new_img = Image.fromarray(rescaled_np_new_img.astype(numpy.uint8))

    # Save the final rescaled hidden image
    rescaled_new_img.save("RN_BW_Image_RESCALE.png")
    return rescaled_new_img


def reveal_color_image(filename):
    """
    Extracts the 3 LSBs for each pixel in the RGB input image.
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    # Convert image to list of pixels (tuples)
    img_pxl = img_to_pix(filename)

    # Open image to get size information
    img = Image.open(filename)
    width, height = img.size
    hid_img_pxl = []

    # Extract 3 LSBs from each RGB pixel tuple
    for pix in img_pxl:
        hid_img_pxl.append(extract_end_bits(3, pix))

    # Create a new image from the extracted LSBs (mode 'RGB')
    new_img = pix_to_img(hid_img_pxl, (width, height), "RGB")

    # Rescaling block: Identical logic to reveal_bw_image but applied to RGB channels
    np_new_img = numpy.array(new_img, dtype=numpy.float32)
    min_val = numpy.min(np_new_img)
    max_val = numpy.max(np_new_img)
    val_range = max_val - min_val
    if val_range == 0:
        rescaled_np_new_img = numpy.full_like(np_new_img, 127.5)
    else:
        normaliz_np_new_img = (np_new_img - min_val) / val_range
        rescaled_np_new_img = normaliz_np_new_img * 255
    rescaled_new_img = Image.fromarray(rescaled_np_new_img.astype(numpy.uint8))
    rescaled_new_img.save("RN_RGB_Image_RESCALE.png")
    return rescaled_new_img


def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)
    if im.mode == "1" or im.mode == "L":
        return reveal_bw_image(filename)
    elif im.mode == "RGB":
        return reveal_color_image(filename)
    else:
        raise Exception("Invalid mode %s" % im.mode)


def draw_kerb(filename, kerb):
    """
    Draws the text "kerb" onto the image located at "filename" and returns a PDF.
    Inputs:
        filename: string, input BW or RGB file
        kerb: string, your kerberos
    Output:
        Saves output image to "filename_kerb.xxx"
    """
    im = Image.open(filename)
    font = ImageFont.truetype("noto-sans-mono.ttf", 40)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), kerb, "white", font=font)
    idx = filename.find(".")
    new_filename = filename[:idx] + "_kerb" + filename[idx:]
    im.save(new_filename)
    return


def main():
    pass

    # Uncomment the following lines to test part 1


# im = Image.open("image_15.png")
# width, height = im.size
# pixels = img_to_pix("image_15.png")

# non_filtered_pixels = filter(pixels, "none")
# im = pix_to_img(non_filtered_pixels, (width, height), "RGB")
# im.show()

# red_filtered_pixels = filter(pixels, "red")
# im2 = pix_to_img(red_filtered_pixels, (width, height), "RGB")
# im2.show()

# Uncomment the following lines to test part 2
# im = reveal_bw_image("hidden1.bmp")
# im.show()

# im2 = reveal_color_image("hidden2.bmp")
# im2.show()


if __name__ == "__main__":
    main()

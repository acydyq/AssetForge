from PIL import Image

def apply_pixelation(image, pixel_size):
    small = image.resize((image.width // pixel_size, image.height // pixel_size), Image.NEAREST)
    return small.resize((image.width, image.height), Image.NEAREST)

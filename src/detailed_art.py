from PIL import Image

def generate_detailed_art(image):
    image = image.convert("P", palette=Image.ADAPTIVE, colors=16)
    return image

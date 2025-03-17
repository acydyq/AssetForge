from PIL import Image

def resize_image(image, width, height):
    return image.resize((width, height), Image.LANCZOS)

def convert_image(image, format):
    image = image.convert("RGB")
    return image.save(f"output/converted.{format.lower()}", format=format)

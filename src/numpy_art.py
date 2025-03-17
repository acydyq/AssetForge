import numpy as np
import matplotlib.pyplot as plt
import json
import random

# Load keyword settings from the file
def load_keywords():
    keyword_mapping = {}
    try:
        with open("keywords.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() and not line.startswith("#"):  # Ignore empty lines and comments
                    keyword, settings = line.strip().split("=")
                    colors, pattern, resolution = settings.split(";")
                    keyword_mapping[keyword.strip().lower()] = {
                        "colors": [c.strip() for c in colors.split(",")],
                        "pattern": pattern.strip(),
                        "resolution": resolution.strip()
                    }
    except FileNotFoundError:
        print("Error: keywords.txt not found.")
    return keyword_mapping

# Load user settings
def load_settings():
    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Settings file not found. Using defaults.")
        return {"default_resolution": "medium", "default_colors": ["black", "white", "gray"], "pattern_intensity": "normal"}

# Convert color names to RGB values
def get_rgb_from_name(color_name):
    color_dict = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 128, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "purple": (128, 0, 128),
        "orange": (255, 165, 0),
        "pink": (255, 192, 203),
        "gray": (128, 128, 128),
        "brown": (139, 69, 19),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "gold": (255, 215, 0),
        "silver": (192, 192, 192),
        "neon blue": (30, 144, 255)
    }
    return color_dict.get(color_name.lower(), (255, 255, 255))  # Default to white

# Generate pixel art based on description
def generate_numpy_art(description):
    keyword_data = load_keywords()
    user_settings = load_settings()
    
    selected_keyword = None
    for keyword in keyword_data:
        if keyword in description.lower():
            selected_keyword = keyword
            break

    if not selected_keyword:
        print("No matching keyword found. Using default settings.")
        settings = {
            "colors": user_settings["default_colors"],
            "pattern": "grid",
            "resolution": user_settings["default_resolution"]
        }
    else:
        settings = keyword_data[selected_keyword]

    colors = settings["colors"]
    resolution = settings["resolution"]

    res_map = {"low": 16, "medium": 32, "high": 64}
    grid_size = res_map.get(resolution, 32)

    data = np.zeros((grid_size, grid_size, 3))
    for i in range(grid_size):
        for j in range(grid_size):
            color = random.choice(colors)
            r, g, b = get_rgb_from_name(color)
            data[i, j] = [r / 255, g / 255, b / 255]

    plt.imshow(data)
    plt.axis("off")
    plt.show()

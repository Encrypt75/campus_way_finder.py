import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Load image
original_image = Image.open("campus_way_finder.py/final_map.png")

# Resize proportionally to fit screen
MAX_WIDTH, MAX_HEIGHT = 1000, 700
scale = min(MAX_WIDTH / original_image.width, MAX_HEIGHT / original_image.height)
new_size = (int(original_image.width * scale), int(original_image.height * scale))
resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)

# Coordinates scaled to resized image
location_coords = {
    "Main": (500, 100),
    "CEA": (350, 250),
    "COC": (200, 300),
    "I-Tech": (600, 350),
    "Hasmine": (800, 500)
}

# Draw on the image
draw = ImageDraw.Draw(resized_image)
font = ImageFont.load_default()  # Optional: load a more stylish font

for name, (x, y) in location_coords.items():
    draw.ellipse((x-5, y-5, x+5, y+5), fill="red")  # Red pin
    draw.text((x + 10, y - 5), name, fill="black", font=font)

# Create window and canvas
root = tk.Tk()
root.title("Campus Map with Pins")
root.geometry(f"{new_size[0]}x{new_size[1]}")

# Convert to Tkinter image
map_photo = ImageTk.PhotoImage(resized_image)

canvas = tk.Canvas(root, width=new_size[0], height=new_size[1])
canvas.pack()
canvas.create_image(0, 0, image=map_photo, anchor="nw")

root.mainloop()
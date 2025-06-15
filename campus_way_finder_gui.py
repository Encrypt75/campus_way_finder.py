import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Campus Way Finder")
root.geometry("1300x700")  # Adjust depending on your image size

# Load the map image
map_image = Image.open("campus_way_finder.py/final_map.png")
map_photo = ImageTk.PhotoImage(map_image)

# Create a canvas to draw on
canvas = tk.Canvas(root, width=map_photo.width(), height=map_photo.height())
canvas.pack(fill="both", expand=True)

# Add the map image as background
canvas.create_image(0, 0, image=map_photo, anchor="nw")

root.mainloop()
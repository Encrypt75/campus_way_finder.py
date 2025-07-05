import tkinter as tk
from PIL import Image, ImageTk

# Resize proportions
MAX_WIDTH, MAX_HEIGHT = 1000, 700

# Coordinates (x, y)
location_coords = {
    "Main": (815, 428),
    "CEA": (345, 350),
    "COC": (470, 355),
    "I-Tech": (250, 300),
    "Hasmine": (50, 200)
}

def show_map_with_path(path=None):
    root = tk.Tk()
    root.title("Campus Map")

    # Load and resize
    img = Image.open("campus_way_finder.py/final_map.png")
    scale = min(MAX_WIDTH / img.width, MAX_HEIGHT / img.height)
    new_size = (int(img.width * scale), int(img.height * scale))
    img = img.resize(new_size, Image.Resampling.LANCZOS)

    tk_img = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(root, width=new_size[0], height=new_size[1])
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=tk_img)
    canvas.image = tk_img

    # Draw pins and labels
    for name, (x, y) in location_coords.items():
        canvas.create_oval(x-6, y-6, x+6, y+6, fill="red")
        canvas.create_text(x + 10, y - 10, text=name, fill="black", font=("Arial", 10, "bold"))

    # If a path is provided, draw it
    if path:
        for i in range(len(path)-1):
            x1, y1 = location_coords[path[i]]
            x2, y2 = location_coords[path[i+1]]
            canvas.create_line(x1, y1, x2, y2, fill="blue", width=3)

    root.mainloop()
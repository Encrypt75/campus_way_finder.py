point_locations = [
    "a.) College of Engineering and Architecture (CEA)",
    "b.) College of Communication (COC)",
    "c.) College of Information Technology (I-Tech)",
    "d.) Hasmine Building",
    "e.) Main Building"
]

location_str = "\n".join(point_locations)
location = input(f"Select your current location:\n \n{location_str}").strip()
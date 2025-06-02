point_locations = [
    "a.) College of Engineering and Architecture (CEA)",
    "b.) College of Communication (COC)",
    "c.) College of Information Technology (I-Tech)",
    "d.) Hasmine Building",
    "e.) Main Building"
]

main_building_points = [
    "a.) Main Entrance",
    "b.) Gymnasium",
    "c.) Swimming Pool",
    "d.) Chappel",
    "e.) Main Academic Building",
    "f.) Lagoon",
    "g.) Obelisk",
    "h.) Ninoy Aquino Learning Resource Center (Library)",
    "i.) Oval",
    "j.) Ferry Station",
]

location_str = "\n".join(point_locations)
current_location = input(f"{location_str}\n\nSelect your current location: ").strip()

destination = input(f"\n{location_str}\n\nWhere do you want to go?: ").strip()

if destination == "e":
    destination_points_str = "\n".join(main_building_points)
    destination_point = input(f"\n{destination_points_str}\n\nSelect your destination point: ").strip()
    
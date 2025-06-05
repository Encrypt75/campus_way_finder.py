point_locations = {
    "a": "College of Engineering and Architecture (CEA)",
    "b": "College of Communication (COC)",
    "c": "College of Information Technology (I-Tech)",
    "d": "Hasmine Building",
    "e": "Main Building"
}

location_lines = []

for letter, building_name in point_locations.items():
    line = (f"{letter}.) {building_name}")
    location_lines.append(line)
 
#converts list into a string
location_str = "\n".join(location_lines)

def get_location_input(prompt):
    while True:
        print(location_str)
        choice = input(f"{prompt} (enter letter only): ").strip().lower()
        #check if the letter is in the point_location keys
        if choice in point_locations:
            return choice
        else:
            print("Invalid input. Please choose a valid letter.\n")

#asks user for current location and destination
current_location = get_location_input("\nSelect your current location")
destination = get_location_input("\nWhere do you want to go?")
point_locations = {
    "1": "College of Engineering and Architecture (CEA)",
    "2": "College of Communication (COC)",
    "3": "College of Information Technology (I-Tech)",
    "4": "Hasmine Building",
    "5": "Main Building"
}

location_lines = []

for number, building_name in point_locations.items():
    line = (f"{number}.) {building_name}")
    location_lines.append(line)
 
#converts list into a string
location_str = "\n".join(location_lines)

def get_location_input(prompt):
    while True:
        print(location_str)
        choice = input(f"{prompt} (enter number only): ").strip().lower()
        #check if the letter is in the point_location keys
        if choice in point_locations:
            return choice
        else:
            print("Invalid input. Please choose a valid option.\n")

#asks user for current location and destination
current_location = get_location_input("\nSelect your current location")
destination = get_location_input("\nWhere do you want to go?")
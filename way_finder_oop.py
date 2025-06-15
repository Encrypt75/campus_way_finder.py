#built in heapq module for Djikstra's algorithm
import heapq

#class name
class CampusMap:
    def __init__(self):
        self.graph = {}  #stores the location name and its destination

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_path(self, from_loc, to_loc, distance):
        self.add_location(from_loc)
        self.add_location(to_loc)
        self.graph[from_loc].append((to_loc, distance))
        self.graph[to_loc].append((from_loc, distance))

    def find_shortest_path(self, start, end):
        #Dijkstra's Algorithm
        short_cut = [(0, start, [])]
        visited = set()

        while short_cut:
            (dist, current, path) = heapq.heappop(short_cut)
            if current in visited:
                continue
            visited.add(current)
            path = path + [current]

            if current == end:
                return dist, path

            for neighbor, cost in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(short_cut, (dist + cost, neighbor, path))

        return float("inf"), []

 
campus = CampusMap()

# Add all paths from your data
paths = [
    ("Main", "CEA", 750),
    ("Main", "COC", 650),
    ("Main", "I-Tech", 1000), 
    ("Main", "Hasmine", 1300),
    ("CEA", "COC", 150),
    ("CEA", "I-Tech", 230),
    ("CEA", "Hasmine", 800),  # Option 1
    ("CEA", "Hasmine", 700),  # Option 2 (shorter)
    ("COC", "I-Tech", 230),
    ("COC", "Hasmine", 950),
    ("COC", "Hasmine", 850),
    ("I-Tech", "Hasmine", 650)
]

for from_loc, to_loc, distance in paths:
    campus.add_path(from_loc, to_loc, distance)

location_menu = {
    "a": "Main",
    "b": "COC",
    "c": "CEA",
    "d": "I-Tech",
    "e": "Hasmine"
}

def display_menu():
    print("Locations: ")
    for key, name in location_menu.items():
        print(f"{key}. {name}")

while True: 
    display_menu()
    start = input("\nEnter letter of your current location: ").strip()
    end = input("Enter letter of your destination: ")

    if start not in location_menu and end not in location_menu:
        print("Location not found, try again\n")
        continue

    start = location_menu[start]
    end = location_menu[end]

    if start == end:
        print("⚠️ You are already at your destination!")
        continue

    distance, path = campus.find_shortest_path(start, end)

    print(f"\nFastest path from {start} to {end}:")
    print(" => ".join(path))
    print(f"Total distance: {distance} meters")

    again = input("\nDo you want to find another path? (y/n): ").strip().lower()
    if again != 'y':
        print("Exiting Campus Way Finder. Goodbye!")
        break

        
    


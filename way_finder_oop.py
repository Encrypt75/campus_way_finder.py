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

 
start = input("Enter your current location: ").strip()
end = input("Enter your destination: ").strip()

if start in campus.graph and end in campus.graph:
    dist, route = campus.find_shortest_path(start, end)
    print(f"\ntake route from {start} to {end}:")
    print(" => ".join(route))
    print(f"total distance: {dist} meters")
else:
    print("One or both locations not found.")
# Write your solution here
# Import the math module for mathematical calculations
import math

# Function to read bike station data from a file
def parse_bike(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Skip the header line and remove any empty or whitespace-only lines
        return [line.strip() for line in lines[1:] if line.strip()]

# Function to convert bike station lines into a dictionary of station names and coordinates
def get_station_data(filename: str):
    data = parse_bike(filename)  # Read cleaned data lines
    locations = {}  # Dictionary to store station name → (longitude, latitude)
    for line in data:
        fields = line.strip().split(';')  # Split line into fields using semicolon as the delimiter
        # Convert the coordinate strings to float for math operations
        lon = float(fields[0])  # Longitude is the first field
        lat = float(fields[1])  # Latitude is the second field
        name = fields[3]        # Station name is the fourth field
        locations[name] = (lon, lat)  # Store coordinates keyed by station name
    return locations

# Function to calculate distance in kilometers between two stations using Pythagorean theorem
def distance(stations: dict, station1: str, station2: str) -> float:
    # Get the coordinates for each station
    lon1, lat1 = stations[station1]
    lon2, lat2 = stations[station2]

    # Ensure coordinate values are floats
    lon1, lat1 = float(lon1), float(lat1)
    lon2, lat2 = float(lon2), float(lat2)

    # Approximate conversions for degrees to kilometers in Helsinki region
    x_km = (lon1 - lon2) * 55.26
    y_km = (lat1 - lat2) * 111.2

    # Calculate and return straight-line distance
    return math.sqrt(x_km**2 + y_km**2)

# Function to find the two stations with the greatest distance between them
def greatest_distance(stations: dict) -> tuple:
    from itertools import combinations  # Efficient pair generator
    import math

    # Local helper to calculate distance between two coordinate pairs
    def distance(p1, p2):
        lon1, lat1 = map(float, p1)
        lon2, lat2 = map(float, p2)
        x_km = (lon1 - lon2) * 55.26
        y_km = (lat1 - lat2) * 111.2
        return math.hypot(x_km, y_km)  # Equivalent to sqrt(x² + y²)

    # Use combinations to create unique station pairs, then find the pair with the largest distance
    max_pair = max(
        combinations(stations.items(), 2),
        key=lambda pair: distance(pair[0][1], pair[1][1])
    )

    # Extract station names and coordinates from result
    name1, coords1 = max_pair[0]
    name2, coords2 = max_pair[1]
    dist = distance(coords1, coords2)

    return name1, name2, dist

# Main execution block to demonstrate usage
if __name__ == "__main__":
    # Load station coordinates from file
    stations = get_station_data('stations1.csv')

    # Calculate and print distance between two example stations
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)

    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    # Find and print the pair of stations with the greatest separation
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

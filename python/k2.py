from levenshtein import levenshtein
cities = []
with open("data/city_names.txt") as fh:
    for line in fh:
        city = line.strip()
        if " " in city:
            # like Freiburg im Breisgau add city only as well
            cities.append(city.split()[0])
        cities.append(city)
#cities = cities[:20]
for city in ["Freiburg", "Frieburg", "Freiborg", 
             "Hamborg", "Sahrluis"]:
    neighbors = get_neighbors(cities, 
                              cities, 
                              city, 
                              2,
                              distance=levenshtein)
    print("vote_distance_weights: ", vote_distance_weights(neighbors))


destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[] for destination in destinations]

def get_destination_index(destination):
  count = 0
  for location in destinations:
    if location == destination:
      destination_index = count
      break
    count += 1
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return attractions_for_destination

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  i = 0
  while i < len(attractions_in_city):
    location = attractions_in_city[i]
    for interest in interests:
      j = 0
      while j < len(location[1]):
        if interest == location[1][j]:
          attractions_with_interest.append(location[0])
        j += 1
    i += 1

  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  travler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(travler_destination, traveler_interests)

  interests_string = "Hi "
  interests_string += traveler[0]
  interests_string += ", we think you'll like these places around " + traveler[1] + ": "
  attractions_string = ""
  last_index = traveler_attractions[-1]
  for attraction in traveler_attractions:
    interests_string += attraction
    if attraction != last_index:
      interests_string += ", "
  
  interests_string += "."
  return interests_string

# Adding attractions
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Start of Code
print(get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]]))
print(get_attractions_for_traveler(["John Doe", "Cairo, Egypt", ["historical site"]]))
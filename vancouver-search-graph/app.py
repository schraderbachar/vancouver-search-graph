from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)


#35
stations_under_construction = []


def greet():
  if stations_under_construction != None:
    for station in stations_under_construction:
      if station in landmark_choices.values():
        landmark_choices.pop(station)

    print("Hi there and welcome to SkyRoute! We'll help you find the shrotest route between the following Vancouver landmarks: \n" + landmark_string)
  else:
    print("Hi there and welcome to SkyRoute! We'll help you find the shrotest route between the following Vancouver landmarks: \n" + landmark_string)
def skyroute():
  add_down_station()
  greet()
  #27
  new_route()
  #34
  goodbye()

#50 add a function to easily add maintance stations
def add_down_station():
  down_list = []
  q = input("Do you wish to add stations that are down for maintenance? y/n:")
  if q == "y":
    num = int(input("How many?"))
    for i in range(0,num):
      station = input("Which station()?:")
      down_list.append(station)
  elif q == "n":
    print("Ok. Moving on!")
    return down_list
  else:
    print("You didn't enter y/n for yes or no please try again." + add_down_station)
  stations_under_construction = down_list
  return stations_under_construction
  #4
def set_start_and_end(start_point,end_point):
  #5
  if start_point is not None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    #7
    if change_point == "b":
      start_point, end_point = get_start(), get_end()
    elif change_point == "o":
      start_point = get_start()
    elif change_point == "d":
      end_point = get_end()
    else:
      print("Oops, that isnt 'o','d', or 'b'...")
      set_start_and_end(start_point,end_point)
    #6
  else:
    start_point = get_start()
    end_point = get_end()
  return start_point, end_point
def get_start():
  #requests origin from user
  #9
  start_point_letter = input("Where are you coming from? Type in the corresponding letter:")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point
  #10
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_start()
def get_end():
  #reuqests endpoint from user
  #11
  end_point_letter = input("Where are you going to? Type in the corresponding letter:")
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]
    return end_point
  #10
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_end()
  #13
def new_route(start_point=None,end_point=None):
  #14
  start_point, end_point = set_start_and_end(start_point,end_point)
  #24

  shortest_route = get_route(start_point,end_point)
    #25, #36 for the if
  if shortest_route is not None:
    shortest_route_string = '\n'.join(shortest_route)
    #26
    print(f"The shortest metro route from {start_point} to {end_point} is: \n{shortest_route_string}")
    #37
  else:
    print(f"Unfortunately, there is currently no path between {start_point} and {end_point} due to maintenance")
  #28
  again = input("Would you like to see another route? Enter y/n:")
  #29
  if again == "y":
    #30
    show_landmarks()
    new_route(start_point,end_point)
def show_landmarks():
  #31
  see_landmarks = input("Would you like to see another route? Enter y/n:")
  #32
  if see_landmarks == "y":
    print(landmark_string)

def get_route(start_point,end_point):
  #16,17
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  #44
  metro_system = get_active_stations() if stations_under_construction else vc_metro
  #45
  if stations_under_construction:
    #46
    possible_route = dfs(metro_system,start_staton,end_station)
    #47
    if not possible_route:
      return None
  #18,
  routes = []
  #19
  for start_station in start_stations:
    for end_station in end_stations:
      #20, 48 changed vc metro to metro station to get the shortest route for whichever metro graph is currently in place
      route = bfs(metro_system,start_station,end_station)
      #21
      if route:
        routes.append(route)
        #22
  shortest_route = min(routes, key=len)
  return shortest_route

#38
def get_active_stations():
  updated_metro = vc_metro
  #39
  for station_under_construction in stations_under_construction:
    #40
    for current_station, neighboring_station in vc_metro.items():
      if current_station != station_under_construction:
        #41
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        #42
        updated_metro[current_station] = set([])
  #43
  return updated_metro





#33
def goodbye():
  print("Thanks for using SkyRoute!")

#23
#print(get_route("Marine Building","Central Park"))

 #27
#
print(skyroute())
#43 print(get_active_stations())
#8,12
#print(set_start_and_end(None,None))

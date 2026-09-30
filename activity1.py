print("Welcome to ride builder!")
print()

print("Step 1 : Pick your vehicle")
print("1 - bike")
print("2 - car")
print()

choise = int(input("Enter 1 or 2:"))
print()

if choise == 1 :
    print("Step 2 : Pick your bike type")
    print("1 - scooty")
    print("2 - mountain bike")
    print()

    bike_type = int(input("Enter 1 or 2:"))

    if bike_type == 1:
      
      print("You picked : scooty")
      print("Top speed  : 80km/h")
      print("Best for   : city roads")
    else:
      print("You picked : mountain bike")
      print("Top speed  : 40km/h")
      print("Best for   : off road trails")

elif choise == 2:
   
   print("Step 2 : Pick your car type")
   print("1 - sedan")
   print("2 - suv")
   print()

   car_type = int(input("Enter 1 or 2:"))

   if car_type == 1:
      
      print("You picked : sedan")
      print("Seats      : 5 passengers")
      print("Best for   : family trips")
   else:
      print("You picked : suv")
      print("Seats      : 7 passengers")
      print("Best for   : off road adventures")

else:
   print("That was not a valid choice")
   print("Please enter 1 for Bike and 2 for Car")

print("Your costum ride is ready!")
print("Enjoy your journey!")